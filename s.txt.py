import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print ('say something!')
	audio = r.listen(source)

try: 
	print ('google thinlks :\n' + r.recognize_google(audio))

except:
	pass
