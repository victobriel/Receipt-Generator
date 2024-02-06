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

  def getSize(self) -> dict:
    if self._path:
      image = Image.open(self._path)
      return {'width': image.width, 'height': image.height}
    else:
      return {'width': 0, 'height': 0}
