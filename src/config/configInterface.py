from ..config.config import Config

class ConfigInterface(Config):
  def __init__(self, path="config/config-interface.json") -> None:
    self._path: str = path
    super().__init__(self._path)
    self._config: dict = self._load_config()

  def _get_default_config(self) -> dict:
    return {
      "lastNumber": "0000",
      "saveData": True
    }
