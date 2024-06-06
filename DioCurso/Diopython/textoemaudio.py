
import pyttsx3


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


with open('Lext.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
        speak_text(linha)
