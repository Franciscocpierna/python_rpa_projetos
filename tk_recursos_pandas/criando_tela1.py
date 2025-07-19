#Importando a biblioteca para tratalhar com a Interface Gráfica
import tkinter as tk
from tkinter import *

#Importanda classes do Tkinter
from tkinter import filedialog, messagebox, simpledialog

#Importa a classe pandas como pd e a numpy como np
import pandas as pd
import numpy as np

#importando a classe Table
from pandastable import Table

# Cria uma janela principal com o título "Editor de Excel", 
#cria um objeto da classe "ExcelEditor" passando a janela como parâmetro, 
#e inicia o loop principal do tkinter
janela = Tk()
janela.title("Editor de Excel com Pandas")
janela.attributes("-fullscreen", False)

class ExcelEditor:
    
    #__init__ é um método especial chamado construtor, 
    #que é usado para inicializar um novo objeto. 
    #Definindo um construtor para uma classe chamada self, com um parâmetro janela_principal. 
    #Esse janela_principal pode ser qualquer objeto que será passado como argumento
    #janela_principal - Master
    def _init_(self, janela_principal):
    
        print("Testando...")
    
    

editor = ExcelEditor()


janela.mainloop()