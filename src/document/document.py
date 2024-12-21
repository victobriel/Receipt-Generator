from PySide6.QtCore import QDate,QDir,QObject,QIODevice,QFile,Signal
from PySide6.QtGui import QPainter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle,getSampleStyleSheet
from ..logo.logo import Logo
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtPdf import QPdfDocument
from ..utils.mask import Mask

class Document(QObject):

  saveReceiptNumber = Signal()

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
    currentPath: str = QDir().currentPath()
    dataPath: str = currentPath + "/data"
    tempPath: str = currentPath + "/data/temp"
    if not QDir(dataPath).exists():
      QDir().mkdir(dataPath)
    if not QDir(tempPath).exists():
      QDir().mkdir(tempPath)

    payerName: str = self._payer["name"]
    if payerName == "":
      dir = tempPath
    else:
      dir = dataPath + "/" + payerName.replace(" ", "_")

    if not QDir(dir).exists():
      QDir().mkdir(dir)

    number: str = self._number.replace(" ", "_").replace("/", "-")
    dir = f"{dir}/{number}.pdf"

    self._parent.statusBar().showMessage(f"Salvando recibo em {dir}")

    m = self._inPx
    try:
      pdfmetrics.registerFont(TTFont('Roboto-Bold', currentPath + "/fonts/Roboto-Bold.ttf"))
      pdfmetrics.registerFont(TTFont('Roboto-Italic', currentPath + "/fonts/Roboto-Italic.ttf"))
      pdfmetrics.registerFont(TTFont('Roboto-Light', currentPath + "/fonts/Roboto-Light.ttf"))
      pdfmetrics.registerFont(TTFont('Roboto', currentPath + "/fonts/Roboto-Regular.ttf"))

      c: canvas.Canvas = canvas.Canvas(dir, pagesize=A4, bottomup=0) # widthMin=0point, widthMax=595point, heightMin=0point, heightMax=842point

      c.translate(10, 40)
      c.scale(1, -1)

      # Logo
      if self.hasLogo():
        # c.drawImage(self._logo.path, m(28), m(-80), width=m(80), height=m(80)) # 80x80
        width, height = self._logo.getSize().values()
        if width > height:
          width = width * 80 / height
          height = 80
        else:
          height = height * 80 / width
          width = 80
        c.drawImage(self._logo.path, m(28), m(-height), width=m(width), height=m(height))

        c.scale(1, -1)
        c.translate(-10, -40)

        c.setFont("Roboto-Bold", 30)
        c.drawCentredString(m(350), m(height/2 + 40), "RECIBO")
        y: int = int(height)
      else:
        c.scale(1, -1)
        c.translate(-10, -40)
        y: int = 70
        c.setFont("Roboto-Bold", 30)
        c.drawCentredString(m(350), m(y), "RECIBO")

      y += 60

      # Company
      c.setFont("Roboto", 18)
      companyName: str = self._company
      if companyName != "":
        c.drawString(m(35), m(y), companyName)
        y += 15

      # Beneficiary
      c.setFont("Roboto", 12)
      benefName: str = self._beneficiary["name"]
      if benefName == "":
        c.setFont("Roboto-Italic", 12)
        c.drawString(m(35), m(y), "Emitente: Não informado")
        c.setFont("Roboto", 12)
      else:
        c.drawString(m(35), m(y), "Emitente: {0}".format(benefName))
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
        c.drawString(m(35), m(y), "Endereço: Não informado")
        c.setFont("Roboto", 12)
      else:
        c.drawString(m(35), m(y), f'Endereço: {benefStreet}, {benefNumber} - bairro {benefNeighborhood} - {benefCep}')
      y += 15

      benefDistrict: str = self._beneficiary["address"]["district"]
      benefCity: str = self._beneficiary["address"]["city"]
      benefCountry: str = self._beneficiary["address"]["country"]

      if (benefDistrict != ""
            and benefCity != ""
              and benefCountry != ""):
        c.drawString(m(35), m(y), f'{benefCity} - {benefDistrict} - {benefCountry}')
        y += 15

      benefPhone: str = self._beneficiary["phone"]
      if benefPhone == "":
        c.setFont("Roboto-Italic", 12)
        c.drawString(m(35), m(y), "Fone: Não informado")
        c.setFont("Roboto", 12)
      else:
        c.drawString(m(35), m(y), f'Fone: {benefPhone}')
      y += 10

      c.line(m(35), m(y), m(410), m(y))
      y += 15

      # Client
      c.setFont("Roboto", 14)
      c.drawString(m(35), m(y), "Cliente:")
      y += 15

      c.setFont("Roboto", 12)
      payerName: str = self._payer["name"]
      if payerName == "":
        c.setFont("Roboto-Italic", 12)
        c.drawString(m(35), m(y), "Nome: Não informado")
        c.setFont("Roboto", 12)
      else:
        c.drawString(m(35), m(y), payerName)
      y += 15

      payerCpfCnpj: str = self._payer["cpf/cnpj"]
      if payerCpfCnpj != "":
        c.drawString(m(35), m(y), "CPF/CNPJ: {0}".format(payerCpfCnpj))
      else:
        c.setFont("Roboto-Italic", 12)
        c.drawString(m(35), m(y), "CPF/CNPJ: Não informado")
        c.setFont("Roboto", 12)
      y += 15

      payerPhone: str = self._payer["phone"]
      if payerPhone == "":
        c.setFont("Roboto-Italic", 12)
        c.drawString(m(35), m(y), "Telefone: Não informado")
        c.setFont("Roboto", 12)
      else:
        c.drawString(m(35), m(y), "Telefone: {0}".format(payerPhone))
      y += 10

      c.line(m(35), m(y), m(410), m(y))
      y += 15

      c.setFont("Roboto", 14)
      c.drawString(m(35), m(y), "Recibo #{0}".format(self._number))
      y += 15

      c.rect(m(35), m(y), m(375), m(20), fill=1)
      y += 12
      c.setFont("Roboto-Bold", 11)
      c.setFillColorRGB(1, 1, 1)
      c.drawString(m(40), m(y), "Descrição")
      c.drawString(m(310),m(y), "Quant.")
      c.drawString(m(370),m(y), "Valor")
      y += 22

      c.setFont("Roboto", 11)
      c.setFillColorRGB(0, 0, 0)
      if self._products == []:
        c.drawString(m(38), m(y), "Não há produtos")
        y += 10
        c.line(m(35), m(y), m(410), m(y))
        y += 15
      else:
        for product in self._products:
          c.drawString(m(40), m(y), product["description"])
          c.drawString(m(310),m(y), product["quantity"])
          c.drawString(m(370),m(y), self._parent.applyMask(product["price"], 'money'))
          y += 5
          c.line(m(35), m(y), m(410), m(y))
          y += 15

      total: str = self._parent.applyMask(str(self._value), 'money')
      
      c.setFont("Roboto-Bold", 11)
      c.drawRightString(m(400), m(y), "TOTAL: {0} {1}".format(self._currency, total))
      y += 15


      c.setFont("Roboto", 11)
      c.drawRightString(m(400), m(y), "({0})".format(self._parent.applyMask(total, 'money2words')))
      y += 15

      c.drawString(m(35), m(y), "Observações:")
      y += 15

      c.setFont("Roboto-Italic", 11)
      # wrap line if it's too long
      text = self._obs
      for i in range(0, len(text), 100):
        c.drawString(m(35), m(y), text[i:i+100])
        y += 10
      y += 10

      c.line(m(35), m(y), m(410), m(y))
      y += 15

      c.setFont("Roboto", 11)
      if (benefDistrict != ""
            and benefCity != ""):
        c.drawCentredString(m(225), m(y), "{0}-{1}, {2}".format(benefCity, benefDistrict, self._date.toString("dd/MM/yyyy")))
      else:
        c.setFont("Roboto-Italic", 11)
        c.drawCentredString(m(225), m(y), "Endereço não informado, {0}".format(self._date.toString("dd/MM/yyyy")))
        c.setFont("Roboto", 11)
      y += 30

      c.line(m(150), m(y), m(300), m(y))
      y += 10

      c.setFont("Roboto", 11)
      if benefName == "":
        c.setFont("Roboto-Italic", 11)
        c.drawCentredString(m(225), m(y), "Emitente não informado")
        c.setFont("Roboto", 11)
      else:
        c.drawCentredString(m(225), m(y), self._beneficiary["name"])
      y += 10

      c.setFont("Roboto-Italic", 11)
      c.drawCentredString(m(225), m(y), self._beneficiary["cpf/cnpj"])

      y = m(20)
      c.setFont("Roboto", 11)
      c.drawString(m(35), m(y), "Recibo #{0}".format(self._number))

      y = m(470)
      c.setFont("Roboto-Light", 9)
      c.drawRightString(m(440), m(y), "Esta folha é parte integrante do recibo #{0}".format(self._number))

      c.showPage()
      c.save()
    except Exception as e:
      self._parent.statusBar().showMessage(f"Erro ao renderizar recibo: {e}")

    self._fileName = dir
    self.saveReceiptNumber.emit()

  def hasLogo(self) -> bool:
    return self._logo != None
