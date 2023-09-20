#-*- coding: latin-1 -*-

import PySimpleGUI as sg

layout = [
    [sg.Push(background_color="#31656E"), sg.Text("CADASTRO", background_color="#31656E", font="Roboto 20"), sg.Push(background_color="#31656E")],
    [sg.Push(background_color="#31656E"), sg. Image("SunshineBoy.png", background_color="#31656E"), sg.Push(background_color="#31656E")],
    [sg.Text("NOME", size=6, background_color="#31656E", font="Arial 10"), sg.Input(key="-NOME-", background_color="#E3F2EB", font="Arial 12", size=40, border_width=2, pad=6), sg.Push(background_color="#31656E")],
    [sg.Text("CPF", size=6, background_color="#31656E", font="Arial 10"), sg.Input(key="-CPF-", background_color="#E3F2EB", font="Arial 12", size=40, border_width=2, pad=6)],
    [sg.Text("TEL", size=6, background_color="#31656E", font="Arial 10"), sg.Input(key="-TEL-", background_color="#E3F2EB", font="Arial 12", size=40, border_width=2, pad=6)],
    [sg.Text("LOGIN", size=6, background_color="#31656E", font="Arial 10"), sg.Input(key="-LOGIN-", background_color="#E3F2EB", font="Arial 12", size=40, border_width=2, pad=6)],
    [sg.Text("SENHA", size=6, background_color="#31656E", font="Arial 10"), sg.Input(key="-SENHA-", password_char="*", background_color="#E3F2EB", font="Arial 12", size=40, border_width=2, pad=6)],
    [sg.Push(background_color="#31656E"), sg. Button("CADASTRAR", button_color="#2B5A59", size=15, font="Arial 15", border_width=3, pad=10), sg.Push(background_color="#31656E")]
]

window = sg.Window("Tela Login", layout, background_color="#31656E").read()
