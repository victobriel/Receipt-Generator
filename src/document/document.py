from PySide6.QtCore import QDate,QDir,QObject,QIODevice,QFile
from PySide6.QtGui import QPainter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from ..logo.logo import Logo
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtPdf import QPdfDocument

class Document(QObject):
  def __init__(self, parent=None):
    super().__init__()
    self._parent = parent
    self._number: str = self._parent.lastNumber()
    self._fileName: str = ""
    self._company: str = ""
    self._date: QDate = None
    self._payer = {
      "name": "",
      "cpf/cnpj": "",
      "phone": ""
    }
    self._beneficiary = {
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
    }
    self._products = []
    self._currency: str = ""
    self._logo = None
    self._obs: str = ""
    self._value: float = 0.0

  @property
  def number(self) -> str:
    return self._number

  @number.setter
  def number(self, number: str) -> None:
    self._number = number

  @property
  def fileName(self) -> str:
    return self._fileName

  @fileName.setter
  def fileName(self, fileName: str) -> None:
    self._fileName = fileName

  @property
  def company(self) -> str:
    return self._company

  @company.setter
  def company(self, company: str) -> None:
    self._company = company

  @property
  def date(self) -> QDate:
    return self._date

  @date.setter
  def date(self, date: QDate) -> None:
    self._date = date

  @property
  def payer(self) -> dict:
    return self._payer

  @payer.setter
  def payer(self, payer: dict) -> None:
    self._payer = payer

  @property
  def beneficiary(self) -> dict:
    return self._beneficiary

  @beneficiary.setter
  def beneficiary(self, beneficiary: dict) -> None:
    self._beneficiary = beneficiary

  @property
  def products(self) -> list:
    return self._products

  @products.setter
  def products(self, products: list) -> None:
    self._products = products

  @property
  def currency(self) -> str:
    return self._currency

  @currency.setter
  def currency(self, currency: str) -> None:
    self._currency = currency

  @property
  def obs(self) -> str:
    return self._obs

  @obs.setter
  def obs(self, obs: str) -> None:
    self._obs = obs

  @property
  def value(self) -> float:
    return self._value

  @value.setter
  def value(self, value: float) -> None:
    self._value = value

  @property
  def logo(self) -> Logo:
    return self._logo

  @logo.setter
  def logo(self, logo: Logo) -> None:
    self._logo = logo

  def createLogo(self, path: str) -> None:
    self._logo = Logo(path)

  def print(self, printer: QPrinter) -> None:
    painter = QPainter()
    painter.begin(printer)
    pageRect = printer.pageRect(QPrinter.Unit.DevicePixel).toRect()
    pageSize = pageRect.size()

    self.__document = QPdfDocument(self)
    self.__file: QFile = QFile(self._fileName)

    if self.__file.open(QIODevice.ReadOnly):
      self.__document.load(self._fileName)

    for i in range(0, self.__document.pageCount()):
      if i > 0:
          printer.newPage()
      page = self.__document.render(i, pageSize)
      painter.drawImage(pageRect, page)
    painter.end()

  def _inPx(self, point: float) -> float:
    return point/0.75

  def render(self) -> None:
    if self._payer["name"] == "":
      dir = f'{QDir().currentPath()}/backup/temp'
    else:
      payerName: str = self._payer["name"].replace(" ", "_")
      dir = f'{QDir().currentPath()}/backup/{payerName}'
    if not QDir(dir).exists():
      QDir().mkdir(dir)

    number: str = self._number.replace(" ", "_").replace("/", "-")
    dir = f'{dir}/{number}.pdf'

    inPx = self._inPx

    pdfmetrics.registerFont(TTFont('Roboto-Bold', 'src/fonts/Roboto-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Roboto-Italic', 'src/fonts/Roboto-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Roboto-Light', 'src/fonts/Roboto-Light.ttf'))
    pdfmetrics.registerFont(TTFont('Roboto', 'src/fonts/Roboto-Regular.ttf'))

    c: canvas.Canvas = canvas.Canvas(dir, pagesize=A4, bottomup=0)

    c.translate(10, 40)
    c.scale(1, -1)

    # Logo
    if self.hasLogo():
      c.drawImage(self._logo.path, inPx(30), inPx(-80), width=inPx(80), height=inPx(80))

    c.scale(1, -1)
    c.translate(-10, -40)

    y: int = 70
    c.setFont("Roboto-Bold", 30)

    c.drawCentredString(inPx(350), inPx(y), "RECIBO")
    y += 60

    # Company
    c.setFont("Roboto", 18)
    companyName: str = self._company
    if companyName != "":
      c.drawString(inPx(35), inPx(y), companyName)
      y += 15

    # Beneficiary
    c.setFont("Roboto", 12)
    benefName: str = self._beneficiary["name"]
    if benefName == "":
      c.setFont("Roboto-Italic", 12)
      c.drawString(inPx(35), inPx(y), "Beneficiário: Não informado")
      c.setFont("Roboto", 12)
    else:
      c.drawString(inPx(35), inPx(y), "Beneficiário: {0}".format(benefName))
    y += 15

    benefStreet: str = self._beneficiary["address"]["street"]
    benefCep: str = self._beneficiary["address"]["cep"]
    benefNumber: str = self._beneficiary["address"]["number"]
    benefNeighborhood: str = self._beneficiary["address"]["neighborhood"]

    if (benefStreet == ""
          or benefCep == ""
            or benefNumber == ""
              or benefNeighborhood == ""):
      c.setFont("Roboto-Italic", 12)
      c.drawString(inPx(35), inPx(y), "Endereço: Não informado")
      c.setFont("Roboto", 12)
    else:
      c.drawString(inPx(35), inPx(y), f'Endereço: {benefStreet}, {benefNumber} - bairro {benefNeighborhood} - {benefCep}')
    y += 15

    benefDistrict: str = self._beneficiary["address"]["district"]
    benefCity: str = self._beneficiary["address"]["city"]
    benefCountry: str = self._beneficiary["address"]["country"]

    if (benefDistrict != ""
          and benefCity != ""
            and benefCountry != ""):
      c.drawString(inPx(35), inPx(y), f'{benefCity} - {benefDistrict} - {benefCountry}')
      y += 15

    benefPhone: str = self._beneficiary["phone"]
    if benefPhone == "":
      c.setFont("Roboto-Italic", 12)
      c.drawString(inPx(35), inPx(y), "Fone: Não informado")
      c.setFont("Roboto", 12)
    else:
      c.drawString(inPx(35), inPx(y), f'Fone: {benefPhone}')
    y += 10

    c.line(inPx(35), inPx(y), inPx(410), inPx(y))
    y += 15

    # Client
    c.setFont("Roboto", 14)
    c.drawString(inPx(35), inPx(y), "Cliente:")
    y += 15

    c.setFont("Roboto", 12)
    payerName: str = self._payer["name"]
    if payerName == "":
      c.setFont("Roboto-Italic", 12)
      c.drawString(inPx(35), inPx(y), "Nome: Não informado")
      c.setFont("Roboto", 12)
    else:
      c.drawString(inPx(35), inPx(y), payerName)
    y += 15

    payerCpfCnpj: str = self._payer["cpf/cnpj"]
    if payerCpfCnpj != "":
      c.drawString(inPx(35), inPx(y), "CPF/CNPJ: {0}".format(payerCpfCnpj))
    else:
      c.setFont("Roboto-Italic", 12)
      c.drawString(inPx(35), inPx(y), "CPF/CNPJ: Não informado")
      c.setFont("Roboto", 12)
    y += 15

    payerPhone: str = self._payer["phone"]
    if payerPhone == "":
      c.setFont("Roboto-Italic", 12)
      c.drawString(inPx(35), inPx(y), "Telefone: Não informado")
      c.setFont("Roboto", 12)
    else:
      c.drawString(inPx(35), inPx(y), "Telefone: {0}".format(payerPhone))
    y += 10

    c.line(inPx(35), inPx(y), inPx(410), inPx(y))
    y += 15

    c.setFont("Roboto", 14)
    c.drawString(inPx(35), inPx(y), "Recibo #{0}".format(self._number))
    y += 15

    c.rect(inPx(35), inPx(y), inPx(375), inPx(20), fill=1)
    y += 12
    c.setFont("Roboto-Bold", 11)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(inPx(40), inPx(y), "Descrição")
    c.drawString(inPx(310),inPx(y), "Quant.")
    c.drawString(inPx(370),inPx(y), "Valor")
    y += 22

    c.setFont("Roboto", 11)
    c.setFillColorRGB(0, 0, 0)
    if self._products == []:
      c.drawString(inPx(38), inPx(y), "Não há produtos")
      y += 10
      c.line(inPx(35), inPx(y), inPx(410), inPx(y))
      y += 15
    else:
      for product in self._products:
        c.drawString(inPx(40), inPx(y), product["description"])
        c.drawString(inPx(310),inPx(y), product["quantity"])
        c.drawString(inPx(370),inPx(y), self._parent.applyMask(product["price"], 'money'))
        y += 5
        c.line(inPx(35), inPx(y), inPx(410), inPx(y))
        y += 15

    c.setFont("Roboto-Bold", 11)
    c.drawRightString(inPx(400), inPx(y), "TOTAL: {0} {1}".format(self._currency, self._parent.applyMask(str(self._value), 'money')))
    y += 15

    c.setFont("Roboto", 11)
    c.drawString(inPx(35), inPx(y), "Observações:")
    y += 15

    c.setFont("Roboto-Italic", 11)
    c.drawString(inPx(35), inPx(y), self._obs)
    y += 10

    c.line(inPx(35), inPx(y), inPx(410), inPx(y))
    y += 15

    c.setFont("Roboto", 11)
    if (benefDistrict != ""
          and benefCity != ""):
      c.drawCentredString(inPx(225), inPx(y), "{0}-{1}, {2}".format(benefCity, benefDistrict, self._date.toString("dd/MM/yyyy")))
    else:
      c.setFont("Roboto-Italic", 11)
      c.drawCentredString(inPx(225), inPx(y), "Endereço não informado, {0}".format(self._date.toString("dd/MM/yyyy")))
      c.setFont("Roboto", 11)
    y += 30

    c.line(inPx(150), inPx(y), inPx(300), inPx(y))
    y += 10

    c.setFont("Roboto", 11)
    if benefName == "":
      c.setFont("Roboto-Italic", 11)
      c.drawCentredString(inPx(225), inPx(y), "Beneficiário não informado")
      c.setFont("Roboto", 11)
    else:
      c.drawCentredString(inPx(225), inPx(y), self._beneficiary["name"])
    y += 10

    c.setFont("Roboto-Italic", 11)
    c.drawCentredString(inPx(225), inPx(y), self._beneficiary["cpf/cnpj"])

    y = inPx(20)
    c.setFont("Roboto", 11)
    c.drawString(inPx(35), inPx(y), "Recibo #{0}".format(self._number))

    y = inPx(470)
    c.setFont("Roboto-Light", 9)
    c.drawRightString(inPx(440), inPx(y), "Esta folha é parte integrante do recibo #{0}".format(self._number))

    # if not self._parent.ui.actionRemoveMessage.isChecked():
    #   MESSAGE = "Gerado por software livre desenvolvido por {1}".format(QDate.currentDate().toString("dd/MM/yyyy"), "https://github.com/victobriel")
    #   c.setFont("Roboto", 7)
    #   c.drawString(inPx(10), inPx(y), MESSAGE)

    c.showPage()
    c.save()

    self._fileName = dir
    self._parent.saveNumber(self._number)

  def hasLogo(self) -> bool:
    return self._logo != None
