import speech_recognition as sr




r = sr.Recognizer()


mic = sr.Microphone()



def listen():
    with mic as source:
        print("listining...")
        audio = r.listen(source)
        print(audio)
        text = (r.recognize_google(audio))
        return text
    