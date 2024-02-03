from PySide6.QtCore import (QObject,Signal)
import os,requests
from ..version import version

class Updater(QObject):

  addMessage = Signal(str)
  setTotalProgress = Signal(int)
  setCurrentProgress = Signal(int, bool)

  def __init__(self, parent=None) -> None:
    super().__init__()
    self._parent = parent
    self._file: str = None
    self._data: dict = None

  def check(self) -> bool:
    __version__ = version # program version

    self.addMessage.emit("Procurando por atualizações...")
    self.addMessage.emit(f'Versão atual: {__version__}')

    fileVersion: str = os.path.join(os.getcwd(), 'version.txt')
    dataFileVersion: str = None
    if os.path.exists(fileVersion):
      with open('update.txt', 'r') as file:
        dataFileVersion = file.read()
      if dataFileVersion == __version__:
        self.addMessage.emit('Já está na versão mais recente')
        try:
          os.remove('update.txt')
        except FileNotFoundError:
          pass
        return False

    url: str = 'https://api.github.com/repos/victobriel/receipt-generator/releases/latest'
    try:
      self._data: dict = requests.get(url).json()
    except requests.exceptions.RequestException as e:
        self.addMessage.emit(f'Erro ao buscar atualizações: {e}')
        return False
    githubVersion: str = self._data['tag_name'].replace('v', '')
    self.addMessage.emit(f'Versão mais recente: {githubVersion}')
    self.setCurrentProgress.emit(0, True)
    if __version__ != githubVersion:
        return True
    else:
        return False

  def download(self) -> bool:
    url: str = self._data['assets'][0]['browser_download_url']
    try:
      request = requests.get(url, stream=True)
      request.raise_for_status()
    except requests.exceptions.RequestException as e:
      self.addMessage.emit(f'Erro ao baixar atualização: {e}')
      return False

    fileName: str = url.split('/')[-1]
    readBytes: int = 0
    chunkSize: int = 1024
    currentPath: str = os.getcwd()
    tempFolder: str = os.path.join(currentPath, 'temp')

    if not os.path.exists(tempFolder):
        os.makedirs(tempFolder)

    self._file = os.path.join(tempFolder, fileName)

    with request as r:
      self.setTotalProgress.emit(int(r.headers['Content-Length']))
      with open(self._file, 'wb') as f:
        while True:
          chunk = r.raw.read(chunkSize)
          if not chunk:
            break
          f.write(chunk)
          readBytes += chunkSize
          self.setCurrentProgress.emit(readBytes, False)
    return True
