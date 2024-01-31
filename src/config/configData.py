from ..config.config import Config

class ConfigData(Config):
  def __init__(self, path="config-data.json") -> None:
    self._path: str = path
    super().__init__(self._path)
    self._config: dict = self._load_config()

  def _get_default_config(self) -> dict:
    return {
      "company": "",
      "beneficiary": {
      "name": "",
      "cpf/cnpj": "",
      "address": {
      "cep": "",
      "district": "",
      "city": "",
      "street": "",
      "number": "",
      "neighborhood": "",
      "country": ""
      },
      "phone": ""
      },
      "logo": False,
      "currency": "R$"
    }
