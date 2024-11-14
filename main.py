# from gtts import gTTS
# import pyglet
# audio = "audio.mp3"
# language = "ru"
#
#
# f = open(R"C:\Intel\1.txt", 'r')
# theText = f.read()
# f.close()
# sp = gTTS(text=theText, lang=language, slow=False)
# sp.save(audio)

import pyttsx3

engine = pyttsx3.init() # Создание объекта engine
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
f = open(R"C:\Intel\1.txt", 'r')
theText = f.read()
audio_file = "output.mp3"
#engine.say(theText) # Преобразование текста в речь
#engine.runAndWait() # Проигрывание звука
engine.save_to_file(theText, audio_file)
engine.runAndWait()
f.close()





# song = pyglet.media.load("audio.mp3")
# song.play()
# pyglet.app.run()


# import pyttsx3
#
# language = "ru"
# engine = pyttsx3.init(driverName='sapi5')
# f = open(R"C:\Intel\1.txt", 'r')
# theText = f.read()
# f.close()
# engine.say(theText)
# engine.runAndWait()