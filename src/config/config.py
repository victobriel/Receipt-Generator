import json,os

class Config:
  def __init__(self, path = "config.json") -> None:
    self._path: str = path
    if not os.path.exists("config"):
      os.makedirs("config")
    self._config: dict = self._load_config()

  def _load_config(self) -> dict:
    try:
      with open(self._path, "r") as file:
        data = json.load(file)
        return data
    except FileNotFoundError:
      return self._create_config()

  def get(self, key) -> str:
    return self._config[key]

  def set(self, key, value) -> None:
    self._config[key] = value
    self._save_config()

  def _save_config(self) -> None:
    with open(self._path, "w") as file:
      json.dump(self._config, file, indent=2)
      file.close()

  def _create_config(self) -> dict:
    with open(self._path, "w") as file:
      json.dump(self._get_default_config(), file, indent=2)
    return self._load_config()
  
  def clear(self) -> None:
    with open(self._path, "w") as file:
      json.dump(self._get_default_config(), file, indent=2)
      file.close()
