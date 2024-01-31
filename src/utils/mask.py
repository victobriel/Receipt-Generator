import re
class Mask:
	def __init__(self) -> None:
		pass
	def cpf(self, cpf: str) -> str:
		if not len(cpf): return ""
		if len(cpf) > 14: cpf = cpf[:14]
		cpf = re.sub(r'\D', '', cpf)
		if len(cpf) <= 3:
			return cpf
		elif len(cpf) <= 6:
			cpf = cpf[:3] + '.' + cpf[3:]
		elif len(cpf) <= 9:
			cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:]
		else:
			cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
		return cpf

	def cnpj(self, cnpj: str) -> str:
		if not len(cnpj): return ""
		if len(cnpj) > 18: cnpj = cnpj[:18]
		cnpj = re.sub(r'\D', '', cnpj)
		if len(cnpj) <= 2:
			return cnpj
		elif len(cnpj) <= 5:
			cnpj = cnpj[:2] + '.' + cnpj[2:]
		elif len(cnpj) <= 8:
			cnpj = cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:]
		elif len(cnpj) <= 12:
			cnpj = cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:]
		else:
			cnpj = cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:]
		return cnpj

	def cep(self, cep: str) -> str:
		if not len(cep): return ""
		if len(cep) > 9: cep = cep[:9]
		cep = re.sub(r'\D', '', cep)
		if len(cep) <= 5:
			return cep
		else:
			cep = cep[:5] + '-' + cep[5:]
		return cep

	def phone(self, phone: str) -> str:
		if not len(phone): return ""
		if len(phone) > 15: phone = phone[:15]
		phone = re.sub(r'\D', '', phone)
		if len(phone) <= 2:
			return phone
		elif len(phone) <= 7:
			phone = '(' + phone[:2] + ') ' + phone[2:]
		elif len(phone) <= 11:
			phone = '(' + phone[:2] + ') ' + phone[2:7] + '-' + phone[7:]
		else:
			phone = '(' + phone[:2] + ') ' + phone[2:7] + '-' + phone[7:11] + '-' + phone[11:]
		return phone

	def money(self, money: str) -> str:
		if not len(money): return "0.00"
		money = re.sub(r'\D', '', money)
		if money.startswith('0') and len(money) > 2:
			money = money[1:]
		if len(money) <= 2:
			if len(money) == 1:
				money = '0.0' + money
			elif not money.startswith('0.'):
				money = '0.' + money
		elif len(money) <= 5:
			money = money[:-2] + '.' + money[-2:]
		elif len(money) <= 8:
			money = money[:-5] + ',' + money[-5:-2] + '.' + money[-2:]
		elif len(money) <= 11:
			money = money[:-8] + ',' + money[-8:-5] + ',' + money[-5:-2] + '.' + money[-2:]
		else:
			money = money[:-11] + ',' + money[-11:-8] + ',' + money[-8:-5] + ',' + money[-5:-2] + '.' + money[-2:]
		return money
	
	def noDigit(self, text: str) -> str:
		if not len(text): return ""
		return re.sub(r'\d', '', text)
	
	def noLetter(self, text: str) -> str:
		if not len(text): return ""
		return re.sub(r'\D', '', text)
	
	def onlyNumber(self, text: str) -> str:
		if not len(text): return ""
		return re.sub(r'\W', '', text)
