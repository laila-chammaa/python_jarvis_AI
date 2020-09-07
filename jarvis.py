import wolframalpha
client = wolframalpha.Client("52Y926-3LQGPLGP4J")

import PySimpleGUI as sg
import wikipedia

import pyttsx3
engine = pyttsx3.init()

sg.theme('DarkPurple1')
layout = [  [sg.Text('My name is Jarvis, and I can answer most questions.')],
            [sg.Text('Type your question:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Jarvis', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    input = values[0]

    wolfram = True
    wiki = True

    try:
        wolfram_res = client.query(input)
        wolfram_res = next(wolfram_res.results).text
    except:
        wolfram = False
    try:
        wiki_res = wikipedia.summary(input, sentences=1)
    except:
        wiki = False

    if (wolfram and wiki):
        sg.PopupNonBlocking("WolframAlpha result: " + wolfram_res + "\nWikipedia result: " + wiki_res, title="Answer")
        engine.say("WolframAlpha result: " + wolfram_res)
    elif (wolfram):
        sg.PopupNonBlocking("WolframAlpha result: " + wolfram_res, title="Answer")
        engine.say("WolframAlpha result: " + wolfram_res)
    elif (wiki):
        sg.PopupNonBlocking("Wikipedia result: " + wiki_res, title="Answer")
        engine.say("Wikipedia result")
    else:
        sg.PopupNonBlocking("error")
        engine.say("error")
    
    engine.runAndWait()


window.close()