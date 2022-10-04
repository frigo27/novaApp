from cotacao import pegar_cotacoes
import PySimpleGUI as sg

layout = [
    [sg.Text("Pegar Cotação da moeda")],
    [sg.InputText(key="nome_cotacao")],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text("",key="texto_cotacao")],
]

janela = sg.Window("Sistema de Cotações", layout)

while True:

    event, values = janela.read()

    if event == sg.WIN_CLOSED or event == "Cancelar" :
        break
    if event == "Pegar Cotação":
        codigo_cotacao = values["nome_cotacao"]
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela["texto_cotacao"].update(f"Pegando cotação {codigo_cotacao} a cotação em Reais: R$ {cotacao}")
        print(f"Pegando cotação {codigo_cotacao}")

janela.close()