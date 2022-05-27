import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


''' Importar as bibliotecas necessárias para se trabalhar;
	abrir o arquivo que será realizada a validação;
	criar o dataframe no Pandas;
	passar as funções que irão realizar as validações;
	ajustar as funções para lerem como imput as colunas corretas dentro do dataframe;
	ajustar as funções para o que resultado seja gravado em uma nova coluna no dataframe;
	salvar o arquivo com novas colunas de validação criadas.'''


filename = filedialog.askopenfilename(initialdir="/",
                                      title="Select a File to be validated",
                                      filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))


#inserir o arquivo aberto como DataFrame.

df = pd.read_excel(filename)

resistence = ["R0", "R1-", "R1+", "R2-", "R2+", "R3", "R4", "R5"]
weathering = ["W6", "W5", "W4", "W3", "W2", "W1"]


def resistence_weathering (r, w):
    #Essa função lê os parâmetros r e w (resistência e alteração) e avalia a coerência das entradas.

    if (r in resistence[0:4] and w in weathering[0:3]) or (r in resistence[4:6] and w in weathering[3:5]):
        validacao = "ok"
    elif r in resistence[6:] and w in weathering[0:3]:
        validacao = "Descrição inconsistente"
    else:
        validacao = "Descrição incompleta" #Possibilidade de inserir outras combinações inconsistentes.
    return validacao

df["VALIDACAO"] = df.apply(lambda x: resistence_weathering(x["RESISTENCIA"], x["ALTERACAO"]), axis = 1)
#passando a função através de uma lambda e chamando como parâmetros as colunas de entrada;

df.to_excel('descricao_validada.xlsx')