import tkinter as tk
import re

root = tk.Tk()
root.iconbitmap('img/body.ico')

class Application(tk.Frame):
	''' Classe base para criação de aplicativo '''
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('Calculador de IMC')
		self.master.geometry('400x200+700+200')
		self.master.resizable(width=False, height=False)
		self.pack()
		self.create_widgets()

	def create_widgets(self):

		self.imc = IMC()



class IMC(object):
	''' Classe para Calculo e Exibição da classificação do
	Índice de Massa Corporal.
	'''
	def __init__(self):
		''' Construção do widget '''

		self.l_altura = tk.Label(text='Digite a Altura em cm:')
		self.l_altura.pack()
		self.altura_cm = tk.Entry()
		self.altura_cm.pack()

		self.l_peso = tk.Label(text='Digite o Peso em Kg:')
		self.l_peso.pack()
		self.peso_kg = tk.Entry()
		self.peso_kg.pack()

		self.result = tk.Label(text='Resultado')
		self.result.pack()

		self.calcular = tk.Button(text='Calcular')
		self.calcular.pack()
		self.calcular['command'] = self.show_result


	def _get_imc(self):
		''' Calculo do IMC e obtenção da classificação. '''
		try:
			alt = self._format_number(self.altura_cm.get(), True)
			pes = self._format_number(self.peso_kg.get())
			imc = pes/((alt/100)**2)
			self.result['fg'] = '#33AFFF'
			return self._classificacao(imc)+self._peso_ideal(alt)
		except:
			self.result['fg'] = '#FF3333'
			return 'Erro, os campos devem ser preenchidos corretamente.'

	def _peso_ideal(self, alt):
		''' Calculo da faixa de peso ideal '''
		x_alt = (alt/100)**2
		return f'\n Sua faixa de peso ideal está entre:\n {x_alt*18.5:.2f}Kg e {x_alt*24.9:.2f}Kg.'

	def _format_number(self, num, is_alt=False):
		if is_alt:
			return float(re.sub(r'\.|,','',num))
		return float(re.sub(r',','.',num))

	def _classificacao(self, imc):
		''' Classificação '''
		if imc < 18.5:
			self.result['fg'] = '#FF7433'
			return 'Abaixo do Peso'
		if imc < 24.9:
			self.result['fg'] = '#28C478'
			return 'Peso Normal'
		if imc < 29.9:
			self.result['fg'] = '#C4B128'
			return 'Sobrepeso'
		if imc < 34.9:
			self.result['fg'] = '#C42892'
			return 'Obesidade Grau 1'
		if imc <= 39.9:
			self.result['fg'] = '#9928C4'
			return 'Obesidade Grau 2'
		self.result['fg'] = '#FF0064'
		return 'Obesidade Grau 3'

	def show_result(self):
		self.result['text'] = self._get_imc()
