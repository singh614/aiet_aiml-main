import speech_recognition as sr
import pyttsx3

spk = pyttsx3.init()
spk.setProperty('rate', 140)    # words per minute
spk.setProperty('volume', 1.0)  # 100% volume

rec = sr.Recognizer()

with sr.Microphone() as mic:
    print('Speak:')
    spk.say('Speak Now')
    spk.runAndWait()
    audio = rec.listen(mic, timeout=1, phrase_time_limit=4)
    
    try:
        text = rec.recognize_google(audio)        
        print('You said:', text, end='\n\n')
        spk.say('You might have said, ' + text)
        spk.runAndWait()
    except Exception as err:
        print('Error:', err, end = '\n\n')

