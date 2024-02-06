from PySide6.QtWidgets import QTableWidget,QTableWidgetItem
from PySide6.QtCore import Slot

class ProductsList(QTableWidget):
  def __init__(self, parent=None) -> None:
    super().__init__()
    self._parent = parent
    self.cellChanged.connect(self._onCellChangedEmitted)

  def add(self, description: str, quantity: str, price: str) -> None:
    if len(description) == 0:
      return self._parent.statusBar().showMessage('Nome é obrigatório', timeout=3000)
    if int(quantity) <= 0:
      return self._parent.statusBar().showMessage('Quantity must be greater than 0', timeout=3000)
    if len(price) <= 0:
      return self._parent.statusBar().showMessage('Price is required', timeout=3000)
    row: int = self.rowCount()
    self.insertRow(row)
    self.setItem(row, 0, QTableWidgetItem(description))
    self.setItem(row, 1, QTableWidgetItem(quantity))
    self.setItem(row, 2, QTableWidgetItem(price))

  def remove(self, row: int) -> None:
    if not self.rowCount():
      return self._parent.statusBar().showMessage('Não há itens para remover', timeout=3000)
    if row > self.rowCount():
      return self._parent.statusBar().showMessage('Item não encontrado', timeout=3000)
    self.removeRow(row)
    self._parent.updateTotalValue()

  @Slot(int, int)
  def _onCellChangedEmitted(self, row: int, column: int) -> None:
    if column != 2:
      return
    if self.item(row, 2) is None:
      return
    priceText: str = self.item(row, 2).text()
    priceTextMasked: str = self._parent.applyMask(priceText, 'money')
    if priceText != priceTextMasked:
      self.setItem(row, 2, QTableWidgetItem(priceTextMasked))
      self._parent.updateTotalValue()

  def getProducts(self) -> list:
    products = []
    for row in range(self.rowCount()):
      description: str = self.item(row, 0).text()
      quantity: int = int(self.item(row, 1).text())
      price: float = float(self.item(row, 2).text())
      products.append({
        'description': description,
        'quantity': quantity,
        'price': price
      })
    return products
