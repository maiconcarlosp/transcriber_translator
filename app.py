from googletrans import Translator
import speech_recognition as sr
count = 0
lista = []

# adicionar idiomas aqui
idiomas = {'Português':'pt', 'Inglês':'en', 'Espanhol':'es', 'Francês':'fr'}

for idioma, valor in idiomas.items():
    count += 1
    lista.append(str(count) +' - ' + idioma)

# atribuição do valor para entrada
print('\nIdioma do áudio:')
for idioma in lista:
    print(idioma)
entrada = input()
entrada = list(idiomas.values())[int(entrada)-1]

# atribuição de valor para a saída
print('\nIdioma de tradução:')
for idioma in lista:
    print(idioma)
saida = input()
saida = list(idiomas.values())[int(saida)-1]


arquivo = "pt.wav"
r = sr.Recognizer()
tradutor = Translator()

with sr.AudioFile(arquivo) as audio:
    audio_data = r.record(audio)
    texto = r.recognize_google(audio_data, language=entrada)
    print('\nTexto original = ' + texto.upper())
    src = tradutor.detect(texto).lang
    print('\nTexto traduzido = ' + tradutor.translate(texto.upper(), src=src, dest=saida).text)