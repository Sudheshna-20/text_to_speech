from cgitb import text
from gtts import gTTS
from playsound import playsound
language="en"
audio="speech.mp3"
sp=gTTS(text="hello gopal"*10,slow=False)
sp.save(audio)
playsound(audio)