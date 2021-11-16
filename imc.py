import tkinter as tk
import re

root = tk.Tk()


class Application(tk.Frame):
	''' Classe base para criação de aplicativo '''
	def __init__(self, title, master=None):
		super().__init__(master)
		self.master = master
		self.master.title(title)
		self.master.geometry('700x250+700+200')
		self.master.resizable(width=True, height=True)
		self.master.iconbitmap('img/body.ico')
		self.create_widgets()

	def create_widgets(self):
		pass

	def sair(self):
		self.master.destroy()


class WedLabel():

	def __init__(self, label, frame=None):
		width = frame.winfo_width()
		self.frame = tk.Frame(frame, width=width)

		self.frame_r = tk.Frame(self.frame, width=width*30/100)
		self.frame_r.grid(row=0, column=0, columnspan=2, sticky='e')

		self.frame_l = tk.Frame(self.frame, width=width*70/100)
		self.frame_l.grid(row=0, column=2, columnspan=3, sticky='w')
		self.frame_l.update()

		self.label = tk.Label(self.frame_r, text=label, width=20, anchor='w')
		self.label.grid(row=0, column=0, padx=5, pady=5,sticky='n,e,s,w')

		self.input = tk.Entry(self.frame_l, width=int(width*12/100))
		self.input.grid(row=0, column=0, padx=5, pady=5, sticky='n,e,s,w')
		
	@property
	def get(self):
		return self.input.get()
	
	def reset(self):
		self.input.delete(0, 'end')
	

class IMC(Application):
	''' Classe para Calculo e Exibição da classificação do
	Índice de Massa Corporal.
	'''
	def create_widgets(self):
		''' Construção do widget '''
		self.header = tk.Frame(self.master, width=690, height=100)
		self.header.grid(row=0, column=0, padx=5, pady=10, columnspan=5, sticky='n,e,s,w')
		self.header.update()

		self.content_left = tk.Frame(self.master, width=300, height=100)
		self.content_left.grid(row=1, column=0, padx=5, pady=5, columnspan=3,  rowspan=2, sticky='n,e,s,w')

		self.content_right = tk.Frame(self.master, width=180, height=120)
		self.content_right.grid(row=1, column=3, padx=5, pady=5, columnspan=2, rowspan=3, sticky='n,e,s,w')
		
		self.footer = tk.Frame(self.master, width=690, height=45, relief="ridge")
		self.footer.grid(row=4, column=0, padx=5, pady=5, columnspan=5, sticky='n,e,s,w')
		self.footer.update()

		self.pasciente = WedLabel(
			label='Nome do pasciente:',
			frame=self.header
			)
		self.pasciente.frame.grid(row=0, column=0, columnspan=5, sticky='n,e,s,w')
		self.pasciente.input.focus()

		self.endereco = WedLabel(
			label='Endereço Completo:',
			frame=self.header
			)
		self.endereco.frame.grid(row=1, column=0, columnspan=5, sticky='n,e,s,w')

		self.altura = WedLabel(
			label='Altura (cm):',
			frame=self.content_left
			)
		self.altura.frame.grid(row=0, column=0, sticky='n,e,s,w')

		self.peso = WedLabel(
			label='Peso (Kg)',
			frame=self.content_left
			)
		self.peso.frame.grid(row=1, column=0, sticky='n,e,s,w')
				

		self.result = tk.Label(
			self.content_right,
			text='----',
			anchor='center',
			borderwidth=2,
			relief='ridge'
			)
		self.result.place(width=180, height=120)


		self.f_calc = tk.Frame(self.footer, width=138, height=18)
		self.f_calc.grid(row=0, column=0)

		self.calcular = tk.Button(self.footer, text='Calcular', width=18)
		self.calcular.grid(row=0, column=1)

		self.reiniciar = tk.Button(self.footer, text='Reiniciar', width=18)
		self.reiniciar.grid(row=0, column=2)

		self.f_rein = tk.Frame(self.footer, width=138, height=18)
		self.f_rein.grid(row=0, column=3)

		self.sair = tk.Button(self.footer, text='Sair', width=18)
		self.sair.grid(row=0, column=4)

		self.calcular['command'] = self.show_result
		self.reiniciar['command'] = self.reset
		self.sair['command'] = super().sair

	def _get_imc(self):
		''' Calculo do IMC e obtenção da classificação. '''
		try:
			alt = self._format_number(self.altura.get, True)
			pes = self._format_number(self.peso.get)
			imc = pes/((alt/100)**2)
			self.result['fg'] = '#33AFFF'
			return self._classificacao(imc)+self._peso_ideal(alt)
		except:
			self.result['fg'] = '#FF3333'
			return 'Erro!\nOs campos devem\n ser preenchidos corretamente.'

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

	def reset(self):
		self.result['text'] = '---'
		self.endereco.reset()
		self.peso.reset()
		self.altura.reset()
		self.pasciente.reset()
		self.pasciente.input.focus()
		