#-*- coding: latin-1 -*-


import PySimpleGUI as sg

layout = [
    [sg.Input()],

    [
        sg.Button("ac", border_width=0, button_color="#A5A5A5", font="Arial 20", size=3, pad=2, key="-AC-"),
        sg.Button("±", border_width=0, button_color="#A5A5A5", font="Arial 20", size=3, pad=2, key="-MAISMENOS-"),
        sg.Button("%", border_width=0, button_color="#A5A5A5", font="Arial 20", size=3, pad=2, key="-PORCENTAGEM-"),
        sg.Button("÷", border_width=0, button_color="#FE9504", font="Arial 20", size=3, pad=2, key="-DIVISAO-")
    ],


    [
        sg.Button("7", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-SETE-"),
        sg.Button("8", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-OITO-"),
        sg.Button("9", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-NOVE-"),
        sg.Button("x", border_width=0, button_color="#FE9504", font="Arial 20", size=3, pad=2, key="-MULTIPLICACAO-")
    ],


    [
        sg.Button("4", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-QUATRO-"),
        sg.Button("5", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-CINCO-"),
        sg.Button("6", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-SEIS-"),
        sg.Button("-", border_width=0, button_color="#FE9504", font="Arial 20", size=3, pad=2, key="-MENOS-")
    ],

    [
        sg.Button("1", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-UM-"),
        sg.Button("2", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-DOIS-"),
        sg.Button("3", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-TRES-"),
        sg.Button("+", border_width=0, button_color="#FE9504", font="Arial 20", size=3, pad=2, key="-MAIS-")
    ],

    [
        sg.Button(border_width=0, button_color="#000000", font="Arial 20", size=3, pad=2, key="-NADA-"),
        sg.Button("0", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-ZERO-"),
        sg.Button(",", border_width=0, button_color="#333333", font="Arial 20", size=3, pad=2, key="-VIRGULA-"),
        sg.Button("=", border_width=0, button_color="#FE9504", font="Arial 20", size=3, pad=2, key="-IGUAL-"),
    ]

]

window = sg.Window("teste", layout, background_color="#000000").read()
