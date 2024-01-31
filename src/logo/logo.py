from PIL import Image

class Logo:
  def __init__(self, path: str) -> None:
    self._path: str = path
    self._width: float = None
    self._height: float = None

  @property
  def path(self) -> str:
    return self._path
  
  @path.setter
  def path(self, path: str) -> None:
    self._path = path

  def getSize(self) -> tuple:
    if self._path:
      image = Image.open(self._path)
      return image.size
    else:
      return (0, 0)
