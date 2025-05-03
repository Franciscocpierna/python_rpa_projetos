#Alterando Cor Fonte e Fundo e Mesclando as Cores

import xlsxwriter as opcoesDoXlsxWriter
import os

#nomeCaminhoArquivo = 'C:\\Users\\Aluno\\Desktop\\Curso RPA\\xlsxwriter\\PintaFundoEFonteExemplo.xlsx'
nomeCaminhoArquivo = 'C:\\python_projetos\\python_rpa_projetos\\python_excel\\PintaFundoEFonteExemplo.xlsx'
minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)

sheetDados = minhaPlanilha.add_worksheet("Dados")


#Preto = black
#Branco = white
#Amarelo = yellow
#Laranja = orange
#Vermelho = red
#Azul = blue
#Verde = green
#Cinza = gray
#Rosa = pink
#Roxo = purple
#Marinho = navy
#Prata = silver

#Altera a cor do fundo da célula
#corFundo = minhaPlanilha.add_format({'fg_color':'yellow'})

#Altera a cor da fonte
corFonte = minhaPlanilha.add_format()
corFonte.set_font_color('blue')

#Mesclando cores na celula
corFonteFundo = minhaPlanilha.add_format({'align': 'center',
                                        'font_color': 'white',
                                        'bold': True,
                                        'bg_color': 'gray'})

#Adicionando dados na Sheet
sheetDados.write("A1", "Nome", corFonteFundo)
sheetDados.write("B1", "Idade", corFonteFundo)
sheetDados.write("A2", "Amanda", corFonte)
sheetDados.write("B2", 21, corFonte)
sheetDados.write("A3", "Allan", corFonte)
sheetDados.write("B3", 28, corFonte)


#Fechando o arquivo
minhaPlanilha.close()


#Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)