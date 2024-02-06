from PySide6.QtWidgets import (QMainWindow,QTableWidgetItem,QFileDialog,
                               QDialog,QSizePolicy,QAbstractItemView)
from PySide6.QtGui import (QIcon,QResizeEvent)
from PySide6.QtCore import (QDate,QDir,QFile,Qt,QCoreApplication,QSize,Slot,QObject)
from PySide6.QtPrintSupport import (QPrinter, QPrintDialog)

from shutil import copyfile
import webbrowser as wb,requests,os,ctypes
from subprocess import (Popen,CalledProcessError,PIPE,DETACHED_PROCESS,CREATE_NEW_PROCESS_GROUP)

from ..ui.mainwindow.ui_mainwindow import Ui_MainWindow
from ..productslist.productslist import ProductsList
from ..documentviewer.documentviewer import DocumentViewer
from ..document.document import Document
from ..utils.mask import Mask
from ..config.configData import ConfigData
from ..config.configInterface import ConfigInterface

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Config
        self._config: ConfigData = ConfigData()
        self._configApp: ConfigInterface = ConfigInterface()
        # Document
        self._document: Document = Document(self)
        # UI
        self.__uiInit()
        # Check for updates
        self._openUpdater(True)
        # Config
        if self.ui.save_data_ckb.isChecked():
            self._loadConfig()
        self.ui.recei_num_edit.setText(self._document.number)
        self._updateCountryComboBox()
        # Signals
        self.ui.comp_edit.textChanged.connect(self._onCompEditTextChanged)
        self.ui.date_edit.dateChanged.connect(self._onDateEditDateChanged)
        self.ui.recei_num_edit.textChanged.connect(self._onReceivedNumEditTextChanged)
        self.ui.payer_nam_edit.textChanged.connect(self._onPayerNamEditTextChanged)
        self.ui.payer_cpf_edit.textChanged.connect(self._onPayerCPFEditTextChanged)
        self.ui.payer_pho_edit.textChanged.connect(self._onPhoneEditTextChanged)
        self.ui.benef_nam_edit.textChanged.connect(self._onBenefNamEditTextChanged)
        self.ui.benef_cpf_edit.textChanged.connect(self._onBenefCPFEditTextChanged)
        self.ui.benef_cep_edit.textChanged.connect(self._onBenefCEPEditTextChanged)
        self.ui.benef_sta_edit.textChanged.connect(self._onBenfStateEditTextChanged)
        self.ui.benef_cit_edit.textChanged.connect(self._onBenefCityEditTextChanged)
        self.ui.benef_str_edit.textChanged.connect(self._onBenefStreetEditTextChanged)
        self.ui.benef_num_edit.textChanged.connect(self._onBenefNumberEditTextChanged)
        self.ui.benef_nei_edit.textChanged.connect(self._onBenefNeighborhoodEditTextChanged)
        self.ui.benef_pho_edit.textChanged.connect(self._onBenefPhoneEditTextChanged)
        self.ui.country_combo.currentIndexChanged.connect(self._onCountryComboBoxIndexChanged)
        self.ui.prod_valu_edit.textChanged.connect(self._productValueChanged)
        self.ui.receipt_obs_edit.textChanged.connect(self._onReceiptObsEditTextChanged)
        self.ui.currency_btn.clicked.connect(self._onCurrencyBtnClicked)
        self.ui.currency_line_edit.returnPressed.connect(self._onCurrencyLineEditReturnPressed)
        self.ui.prod_valu_scro.actionTriggered.connect(self._onValueScrollActionTriggered)
        self.ui.add_serv_btn.clicked.connect(self._onAddBtnClicked)
        self.ui.logo_btn.clicked.connect(self._openLogoDialog)
        self.ui.logo_load_btn.clicked.connect(self._onLogoLoadBtnClicked)
        self.ui.rem_serv_btn.clicked.connect(self._onRemoveBtnClicked)
        self.ui.print_btn.clicked.connect(self.ui.actionPrint.trigger)
        self.ui.preview_btn.clicked.connect(self.ui.actionPreview.trigger)
        self.ui.save_data_ckb.clicked.connect(self._onSaveDataCkbClicked)
        # Actions
        self.ui.actionPreview.triggered.connect(self._onPreviewActionTriggered)
        self.ui.actionPrint.triggered.connect(self._onPrintActionTriggered)
        self.ui.actionCheckForUpdates.triggered.connect(self._openUpdater)
        self.ui.actionDocumentation.triggered.connect(self._onDocumentationTriggered)
        self.ui.country_combo.setCurrentIndex(0)
        self._document.saveReceiptNumber.connect(self._onSaveReceiptNumberEmitted)

    def resizeEvent(self, event: QResizeEvent) -> None:
        size = self.ui.prod_list.width()
        if size == 640:
            return
        self.ui.prod_list.setColumnWidth(0, size - 130)
        event.accept()

    def closeEvent(self, event) -> None:
        if self.ui.save_data_ckb.isChecked():
            self._updateConfig()
        event.accept()

    def __uiInit(self) -> None:
        # Set date
        currentDate: QDate = QDate.currentDate()
        self._document.date = currentDate
        self.ui.date_edit.setDate(currentDate)

        # Hide currency line edit
        self.ui.currency_line_edit.hide()

        self.ui.prod_list: ProductsList = ProductsList(self)
        if (self.ui.prod_list.columnCount() < 3):
            self.ui.prod_list.setColumnCount(3)
        __qtablewidgetitem0 = QTableWidgetItem()
        self.ui.prod_list.setHorizontalHeaderItem(0, __qtablewidgetitem0)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ui.prod_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ui.prod_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.ui.prod_list.setObjectName(u"prod_list")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ui.prod_list.sizePolicy().hasHeightForWidth())
        self.ui.prod_list.setSizePolicy(sizePolicy4)
        self.ui.prod_list.setSizePolicy(sizePolicy4)
        self.ui.prod_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.prod_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.prod_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.prod_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.prod_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.prod_list.horizontalHeader().setVisible(True)
        self.ui.prod_list.horizontalHeader().setHighlightSections(False)
        self.ui.prod_list.verticalHeader().setVisible(False)
        self.ui.prod_list.verticalHeader().setHighlightSections(False)
        self.ui.qTableViewLayout.addWidget(self.ui.prod_list)
        ___qtablewidgetitem0 = self.ui.prod_list.horizontalHeaderItem(0)
        ___qtablewidgetitem0.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        ___qtablewidgetitem1 = self.ui.prod_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quant.", None))
        ___qtablewidgetitem2 = self.ui.prod_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor", None))

        self.ui.prod_list.setColumnWidth(0, 293)
        self.ui.prod_list.setColumnWidth(1, 50)
        self.ui.prod_list.setColumnWidth(2, 80)

        self.ui.save_data_ckb.setChecked(self._configApp.get('saveData'))

    def isAdmin(self) -> bool:
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except AttributeError:
            return False

    def applyMask(self, text: str, type: str) -> str:
        mask: Mask = Mask()
        maskedText: str = text
        if type == 'cpf':
            maskedText = mask.cpf(text)
        if type == 'cnpj':
            maskedText = mask.cnpj(text)
        if type == 'cep':
            maskedText = mask.cep(text)
        if type == 'phone':
            maskedText = mask.phone(text)
        if type == 'money':
            maskedText = mask.money(text)
        if type == 'noDigit':
            maskedText = mask.noDigit(text)
        if type == 'noLetter':
            maskedText = mask.noLetter(text)
        if type == 'onlyNumber':
            maskedText = mask.onlyNumber(text)
        del mask
        return maskedText

    def _reqCep(self, cep: str) -> dict:
        if len(cep) < 9:
            return {}
        cepMasked: str = self.applyMask(cep, 'onlyNumber')
        cepMaskedInt: int = int(cepMasked)
        url = f'https://viacep.com.br/ws/{cepMaskedInt}/json/'
        self.ui.benef_cep_edit.clearFocus()
        try:
            data: dict = requests.get(url, timeout=5).json()
            return data
        except:
            return {}

    def _openLogo(self, fileName) -> bool:
        file: QFile = QFile(fileName)
        if not file.exists():
            nf: str = QDir.toNativeSeparators(fileName)
            self.statusBar().showMessage(f"Arquivo {nf} não pode ser aberto.", timeout=3000)
            return False

        currentPath: str = QDir().currentPath()
        dest: str = currentPath + "/images/logo.png"

        if not QDir(currentPath + "/images").exists():
            QDir().mkdir(currentPath + "/images")

        if (fileName != dest):
            try:
                copyfile(fileName, dest)
            except:
                nf: str = QDir.toNativeSeparators(fileName)
                self.statusBar().showMessage(f"Problema ao copiar arquivo {nf}. Consulte um adminitrador.", timeout=3000)
                return False

        if not self._document.hasLogo():
            self._document.createLogo(dest)
        else:
            self._document.logo.path = dest

        toolTipText: str = "Remover logo"
        self.ui.logo_btn.setIcon(QIcon(dest))
        self.ui.logo_btn.setIconSize(QSize(110, 110))
        self.ui.verticalGroupBox_0_0_0_0.setToolTip(toolTipText)
        self.ui.logo_load_btn.setText(toolTipText)
        return True

    def updateTotalValue(self) -> None:
        rowCount: int = self.ui.prod_list.rowCount()
        if not rowCount:
            return self.ui.total_value_lbl.setText('0.00')
        totalValue: int = 0
        for r in range(rowCount):
            rText = self.ui.prod_list.item(r, 2).text()
            rTextMasked = self.applyMask(rText, 'onlyNumber')
            rQuant = self.ui.prod_list.item(r, 1).text()
            totalValue += (int(rTextMasked) * int(rQuant))
        totalValueMasked: str = self.applyMask(str(totalValue), 'money')
        self.ui.total_value_lbl.setText(totalValueMasked)
        self._document.value = totalValue

    def _loadConfig(self) -> None:
        if self._config.get('logo'):
            self._openLogo(QDir().currentPath() + '/images/logo.png')

        self.ui.comp_edit.setText(self._config.get('company'))
        self._document.company = self.ui.comp_edit.text()

        self.ui.benef_nam_edit.setText(self._config.get('beneficiary')['name'])
        self._document.beneficiary["name"] = self.ui.benef_nam_edit.text()

        self.ui.benef_cpf_edit.setText(self._config.get('beneficiary')['cpf/cnpj'])
        self._document.beneficiary["cpf/cnpj"] = self.ui.benef_cpf_edit.text()

        self.ui.benef_cep_edit.setText(self._config.get('beneficiary')['address']['cep'])
        self._document.beneficiary["address"]["cep"] = self.ui.benef_cep_edit.text()

        self.ui.benef_sta_edit.setText(self._config.get('beneficiary')['address']['district'])
        self._document.beneficiary["address"]["district"] = self.ui.benef_sta_edit.text()

        self.ui.benef_cit_edit.setText(self._config.get('beneficiary')['address']['city'])
        self._document.beneficiary["address"]["city"] = self.ui.benef_cit_edit.text()

        self.ui.benef_str_edit.setText(self._config.get('beneficiary')['address']['street'])
        self._document.beneficiary["address"]["street"] = self.ui.benef_str_edit.text()

        self.ui.benef_num_edit.setText(self._config.get('beneficiary')['address']['number'])
        self._document.beneficiary["address"]["number"] = self.ui.benef_num_edit.text()

        self.ui.benef_nei_edit.setText(self._config.get('beneficiary')['address']['neighborhood'])
        self._document.beneficiary["address"]["neighborhood"] = self.ui.benef_nei_edit.text()

        country: str = self._config.get('beneficiary')['address']['country']
        self.ui.country_combo.setCurrentIndex(self.ui.country_combo.findText(country))

        self.ui.benef_pho_edit.setText(self._config.get('beneficiary')['phone'])
        self._document.beneficiary["phone"] = self.ui.benef_pho_edit.text()

        self.ui.currency_btn.setText(self._config.get('currency'))
        self._document.currency = self.ui.currency_btn.text()

    def lastNumber(self) -> str:
        return str(int(self._configApp.get('lastNumber')) + 1).zfill(4)

    def _updateCountryComboBox(self) -> None:
        self.ui.country_combo.addItem('Brasil')

    def _updateConfig(self) -> None:
        self._config.set('logo', self._document.hasLogo())
        self._config.set('company', self._document.company)
        self._config.set('currency', self._document.currency)
        self._config.set('beneficiary', self._document.beneficiary)

    @Slot()
    def _onSaveDataCkbClicked(self) -> None:
        status: bool = self.ui.save_data_ckb.isChecked()
        self._configApp.set('saveData', status)
        if status:
            self._updateConfig()
        else:
            self._config.clear()

    @Slot()
    def _productValueChanged(self) -> None:
        self.ui.prod_valu_edit.setText(self.applyMask(self.ui.prod_valu_edit.text(), 'money'))

    @Slot()
    def _onAddBtnClicked(self) -> None:
        if not len(self.ui.prod_desc_edit.text()):
            return
        if self.ui.prod_quant_spin.value() <= 0:
            return
        if not len(self.ui.prod_valu_edit.text()) or self.ui.prod_valu_edit.text() == '0.00':
            return
        valueTextMasked: str = self.applyMask(self.ui.prod_valu_edit.text(), 'onlyNumber')
        self.ui.prod_list.add(self.ui.prod_desc_edit.text(), self.ui.prod_quant_spin.text(), valueTextMasked)
        self._document.products.append({
            'description': self.ui.prod_desc_edit.text(),
            'quantity': self.ui.prod_quant_spin.text(),
            'price': valueTextMasked
        })
        self.ui.prod_desc_edit.clear()
        self.ui.prod_quant_spin.setValue(1)
        self.ui.prod_valu_edit.setText('0.00')

    @Slot()
    def _onRemoveBtnClicked(self) -> None:
        SELECTED_ITEMS: list[QTableWidgetItem] = self.ui.prod_list.selectedItems()
        if not len(SELECTED_ITEMS):
            return self.statusBar().showMessage('Selecione um item para remover', timeout=3000)
        self._document.products.pop(SELECTED_ITEMS[0].row())
        self.ui.prod_list.remove(SELECTED_ITEMS[0].row())

    @Slot()
    def _onPreviewActionTriggered(self) -> None:
        self._document.render()
        if not hasattr(self, '_dw'):
            self._dw: DocumentViewer = DocumentViewer()
        self._dw.show()
        self._dw.openFile(self._document.fileName)

    @Slot()
    def _onPrintActionTriggered(self) -> None:
        self._document.render()

        printer = QPrinter(QPrinter.HighResolution)
        dlg = QPrintDialog(printer, self)
        dlg.setWindowTitle("Print Document")
        if dlg.exec() == QDialog.Accepted:
            self._document.print(printer)
        else:
            self.statusBar().showMessage("Impressão cancelada.", timeout=3000)
            return
        state = printer.printerState()
        message = self._document.fileName + " : "
        if   state == QPrinter.PrinterState.Aborted:
            message += "Impressão abortada."
        elif state == QPrinter.PrinterState.Active:
            message += "Impressão ativa."
        elif state == QPrinter.PrinterState.Idle:
            message += "Impressão concluída."
        elif state == QPrinter.PrinterState.Error:
            message += "Erro na impressão."
        self.statusBar().showMessage(message, timeout=3000)

    @Slot()
    def _onCountryComboBoxIndexChanged(self) -> None:
        self._document.beneficiary["address"]["country"] = self.ui.country_combo.currentText()
    
    @Slot()
    def _onLogoLoadBtnClicked(self) -> None:
        if not self._document.hasLogo():
            self._openLogoDialog()
        else:
            if not self._document.hasLogo():
                return
            self._document.logo = None
            toolTipText: str = 'Carregar logo'
            default_logo = u":/logo/assets/photo.png"
            self.ui.logo_btn.setIcon(QIcon(default_logo))
            self.ui.logo_btn.setIconSize(QSize(60, 60))
            self.ui.verticalGroupBox_0_0_0_0.setToolTip(toolTipText)
            self.ui.logo_load_btn.setText(toolTipText)

    @Slot()
    def _openLogoDialog(self) -> None:
        dir: QDir = QDir().current()
        fileDialog: QFileDialog = QFileDialog(self, "Abrir logo",
                                                dir.absolutePath(), 'Imagens (*.png *.jpg *.jpeg)')
        while (fileDialog.exec() == QDialog.Accepted and
                not self._openLogo(fileDialog.selectedFiles()[0])):
            pass

    @Slot()
    def _onCurrencyBtnClicked(self) -> None:
        self.ui.currency_line_edit.show()
        self.ui.currency_btn.hide()
        self.ui.currency_line_edit.setFocus()
        self.ui.currency_line_edit.setText(self.ui.currency_btn.text())

    @Slot()
    def _onCurrencyLineEditReturnPressed(self) -> None:
        self.ui.currency_btn.setText(self.ui.currency_line_edit.text())
        self.ui.currency_line_edit.hide()
        self.ui.currency_btn.show()
        self.ui.currency_line_edit.clearFocus()
        self._document.currency = self.ui.currency_line_edit.text()

    @Slot(int)
    def _onValueScrollActionTriggered(self, action: int) -> None:
        productValueText: str = self.ui.prod_valu_edit.text()
        if not len(productValueText):
            self.ui.prod_valu_scro.setValue(0)
            self.ui.prod_valu_edit.setText('0')
            return
        productValueInt: int = int(self.applyMask(productValueText, 'onlyNumber')) # 0
        scrollSteps: int = 1000
        recipe: int = int(-abs(productValueInt / scrollSteps)) # 0
        scrollValue: int = self.ui.prod_valu_scro.value() # -1
        if action == 1:
            if productValueInt == 0:
                return
            if productValueInt < scrollSteps:
                return self.ui.prod_valu_edit.setText('0')
            productValueInt -= scrollSteps
        else:
            productValueInt += scrollSteps
        self.ui.prod_valu_edit.setText((str(productValueInt)))
        if scrollValue != recipe:
            self.ui.prod_valu_scro.setValue(recipe)

    @Slot(bool)
    def _openUpdater(self, notFreeze: bool) -> None:
        current: str = os.path.abspath(os.getcwd())
        updater: str = os.path.join(current, 'updater', 'updater.exe')
        rfreeze: str = '--not-freeze' if notFreeze else ''
        try:
            PID: str = str(os.getpid())
            command: list[str] = []
            command = [updater, PID, rfreeze, 'runas', '/user:Administrator'] if not self.isAdmin() else [updater, PID, rfreeze]
            Popen(command,
                  creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
                  stdout=PIPE,
                  stderr=PIPE,
                  stdin=PIPE,
                  close_fds=True)
        except CalledProcessError as e:
            print(e)
            self.statusBar().showMessage(f'Erro ao abrir o atualizador: {e}', timeout=3000)
        except:
            self.statusBar().showMessage('Erro ao abrir o atualizador', timeout=3000)

    @Slot(str)
    def _onCompEditTextChanged(self, text) -> None:
        self._document.company = text

    @Slot(QDate)
    def _onDateEditDateChanged(self, date: QDate) -> None:
        self._document.date = date

    @Slot(str)
    def _onReceivedNumEditTextChanged(self, text: str) -> None:
        self._document.number = text

    @Slot(str)
    def _onPayerNamEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'noDigit')
        self.ui.payer_nam_edit.setText(maskedText)
        self._document.payer["name"] = maskedText

    @Slot(str)
    def _onPayerCPFEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'cpf')
        self.ui.payer_cpf_edit.setText(maskedText)
        self._document.payer["cpf/cnpj"] = maskedText

    @Slot(str)
    def _onPhoneEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'phone')
        self.ui.payer_pho_edit.setText(maskedText)
        self._document.payer["phone"] = maskedText

    @Slot(str)
    def _onBenefNamEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'noDigit')
        self.ui.benef_nam_edit.setText(maskedText)
        self._document.beneficiary["name"] = maskedText

    @Slot(str)
    def _onBenefCPFEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'cpf')
        self.ui.benef_cpf_edit.setText(maskedText)
        self._document.beneficiary["cpf/cnpj"] = maskedText

    @Slot(str)
    def _onBenefCEPEditTextChanged(self, text: str) -> None:
        cepMasked: str = self.applyMask(text, 'cep')
        self.ui.benef_cep_edit.setText(cepMasked)
        self._document.beneficiary["address"]["cep"] = cepMasked
        if len(cepMasked) >= 9:
            data = self._reqCep(cepMasked)
            if data == {} or 'erro' in data:
                self.ui.benef_sta_edit.clear()
                self._document.beneficiary["address"]["district"] = ""
                self.ui.benef_cit_edit.clear()
                self._document.beneficiary["address"]["city"] = ""
                self.ui.benef_str_edit.clear()
                self._document.beneficiary["address"]["street"] = ""
                self.ui.benef_nei_edit.clear()
                self._document.beneficiary["address"]["neighborhood"] = ""
                self.statusBar().showMessage('CEP não encontrado', timeout=3000)
            else:
                self.ui.benef_sta_edit.setText(data['uf'])
                self._document.beneficiary["address"]["district"] = self.ui.benef_sta_edit.text()
                self.ui.benef_cit_edit.setText(data['localidade'])
                self._document.beneficiary["address"]["city"] = self.ui.benef_cit_edit.text()
                self.ui.benef_str_edit.setText(data['logradouro'])
                self._document.beneficiary["address"]["street"] = self.ui.benef_str_edit.text()
                self.ui.benef_nei_edit.setText(data['bairro'])
                self._document.beneficiary["address"]["neighborhood"] = self.ui.benef_nei_edit.text()

    @Slot(str)
    def _onBenfStateEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'noDigit')
        self.ui.benef_sta_edit.setText(maskedText)
        self._document.beneficiary["address"]["district"] = maskedText

    @Slot(str)
    def _onBenefCityEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'noDigit')
        self.ui.benef_cit_edit.setText(maskedText)
        self._document.beneficiary["address"]["city"] = maskedText

    @Slot(str)
    def _onBenefStreetEditTextChanged(self, text: str) -> None:
        self._document.beneficiary["address"]["street"] = text

    @Slot(str)
    def _onBenefNumberEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'noLetter')
        self.ui.benef_num_edit.setText(maskedText)
        self._document.beneficiary["address"]["number"] = maskedText

    @Slot(str)
    def _onBenefNeighborhoodEditTextChanged(self, text: str) -> None:
        self._document.beneficiary["address"]["neighborhood"] = text

    @Slot(str)
    def _onBenefPhoneEditTextChanged(self, text: str) -> None:
        maskedText: str = self.applyMask(text, 'phone')
        self.ui.benef_pho_edit.setText(maskedText)
        self._document.beneficiary["phone"] = maskedText

    @Slot(str)
    def _onReceiptObsEditTextChanged(self, text: str) -> None:
        self._document.obs = text

    @Slot()
    def _onDocumentationTriggered(self) -> None:
        wb.open_new_tab('https://github.com/victobriel/receipt-generator')

    @Slot(int)
    def _onSaveReceiptNumberEmitted(self) -> None:
        self._configApp.set('lastNumber', self._document.number)
