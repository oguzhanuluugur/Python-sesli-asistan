
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import time
from datetime import datetime
import webbrowser


r=sr.Recognizer()

def konustur(yazı):
    tts=gTTS(text=yazı,lang="tr")
    file="yazı.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def kayıt():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio,language="tr")
        except sr.UnknownValueError:
            konustur("Anlayamadım")
        return voice
def cevapla(voice):
    if "Oğuzhan" in voice:
        konustur("hoşgeldin oğuzhan")
    if "nasılsın" in voice:
        konustur("iyidir sen nasılsın")
    if  "saat kaç" in voice:
        konustur(datetime.now().strftime("%H:%M:%S"))
    if "arama yap" in voice:
        konustur("ne arama yapmak istiyorsun")
        search=kayıt()
        url="https://www.google.com/search?q="+search
        webbrowser.get().open(url)
        konustur(search+"için bulduklarım")
    if "kapat" in voice:
        konustur("görüşürüz")
        exit()

konustur("Ben oğuzhan'ın asistanıyım siz kimsiniz")
time.sleep(1)
while(1):
    ses=kayıt()
    print(ses)
    cevapla(ses)