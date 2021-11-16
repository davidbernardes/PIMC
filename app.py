'''
    Aplicativo Para Cálculo de IMC com interface gráfica.
'''
from imc import Application, root, IMC

app = IMC(master=root, title='Cálculo do IMC - Índice de Massa Corporal')

if __name__ =='__main__':
    app.mainloop()