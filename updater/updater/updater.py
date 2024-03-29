from PySide6.QtCore import (QObject,Signal)
import requests,json,logging,subprocess,time,sys,zipfile,os,shutil
from pathlib import Path

class Updater(QObject):

  addMessage = Signal(str)
  setTotalProgress = Signal(int)
  setCurrentProgress = Signal(int, bool)

  def __init__(self, parent=None) -> None:
    super().__init__()
    self._parent = parent
    self._data: dict = None
    self._filePath: str = None
    self._mainPath: str = str(Path().absolute())
    self._tempFolder: str = Path(self._mainPath).joinpath('temp')
    self._appJsonPath: str = Path(self._mainPath).joinpath('app.json')
    logging.basicConfig(filename='log.log', level=logging.INFO)
    logging.info(f'controll --PID {self._parent._pid}, --FREEZE {self._parent._freeze}')

  def check(self) -> bool:
    logging.info('Checking for updates')
    self.addMessage.emit("Procurando por atualizações...")
    try:
      if not Path.exists(self._appJsonPath):
        self._mainPath = str(Path().absolute().parents[0])
        self._appJsonPath = Path(self._mainPath).joinpath('app.json')
        if not Path.exists(self._appJsonPath):
          logging.error(f'App.json not found')
          return False
      with open(self._appJsonPath, 'r') as file:
        data = json.load(file)
      __version__ = data['version']
    except Exception as e:
      logging.error(f'Error reading app.json: {e}')
      self.addMessage.emit(f'Erro ao ler app.json: {e}')
      return False

    logging.info(f'Current version: {__version__}')
    self.addMessage.emit(f'Versão atual: {__version__}')

    url: str = 'https://api.github.com/repos/victobriel/receipt-generator/releases/latest'
    try:
      self._data: dict = requests.get(url).json()
    except requests.exceptions.RequestException as e:
      logging.error(f'Error fetching updates: {e}')
      self.addMessage.emit(f'Erro ao buscar atualizações: {e}')
      return False
    githubVersion: str = self._data['tag_name'].replace('v', '')
    logging.info(f'Latest version: {githubVersion}')
    self.addMessage.emit(f'Versão mais recente: {githubVersion}')
    self.setCurrentProgress.emit(0, True)
    if __version__ != githubVersion:
      return True
    else:
      return False

  def download(self) -> bool:
    url: str = self._data['assets'][0]['browser_download_url'] # Asset without updater
    try:
      request = requests.get(url, stream=True)
      request.raise_for_status()
      logging.info(f'Downloading update from {url}')
    except requests.exceptions.RequestException as e:
      logging.error(f'Error fetching updates: {e}')
      self.addMessage.emit(f'Erro ao baixar atualização: {e}')
      return False

    fileName: str = self._data['assets'][0]['name']
    readBytes: int = 0
    chunkSize: int = 1024

    if not Path.exists(self._tempFolder):
      Path.mkdir(self._tempFolder)

    self._filePath = Path(self._tempFolder).joinpath(fileName)
    logging.info(f'Saving downloaded update in {self._filePath}')

    with request as r:
      self.setTotalProgress.emit(int(r.headers['Content-Length']))
      with open(self._filePath, 'wb') as f:
        while True:
          chunk = r.raw.read(chunkSize)
          if not chunk:
            break
          f.write(chunk)
          readBytes += chunkSize
          self.setCurrentProgress.emit(readBytes, False)

    self.setCurrentProgress.emit(0, True)
    return True

  def install(self) -> bool:
    extract: bool = self.extract()
    if not extract:
      return False
    copy: bool = self.copy()
    if not copy:
      return False
    return True

  def extract(self) -> bool:
    logging.info('Installing update')
    self.addMessage.emit('Instalando atualização...')
    logging.info(f'Extracting {self._filePath} to {self._tempFolder}')
    try:
      with zipfile.ZipFile(self._filePath, 'r') as z:
        z.extractall(self._tempFolder)
      os.remove(self._filePath)
      logging.info(f'Deleted {self._filePath}')
      updaterFolder: str = Path(self._tempFolder).joinpath('updater')
      if os.path.exists(updaterFolder):
        shutil.rmtree(updaterFolder)
    except Exception as e:
      self.addMessage.emit(f'Erro ao instalar atualização: {e}')
      logging.error(f'Error installing update: {e}')
      return False
    return True

  def copy(self) -> bool:
    logging.info('Copying files')
    self.addMessage.emit('Copiando arquivos...')
    try:
      shutil.copytree(self._tempFolder, self._mainPath, dirs_exist_ok=True)
      logging.info(f'Files copied to {self._mainPath}')
      shutil.rmtree(self._tempFolder)
    except Exception as e:
      self.addMessage.emit(f'Erro ao copiar arquivos: {e}')
      logging.error(f'Error copying files: {e}')
      return False
    return True

  def runApp(self) -> None:
    logging.info('Starting application')
    self.addMessage.emit('Iniciando aplicativo...')
    try:
      appName: str = 'receipt-generator.exe'
      with open(self._appJsonPath, 'r') as file:
        data = json.load(file)
      appName = data['app']
      logging.info(f'Starting {appName}')
      command: list = [appName]
      time.sleep(4) # Wait for the application to close
      subprocess.Popen(command,
                      stdin=subprocess.PIPE,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.STDOUT,
                      close_fds=True)
    except Exception as e:
      self.addMessage.emit(f'Erro ao iniciar aplicativo: {e}')
      logging.error(f'Error starting application: {e}')
    sys.exit()
