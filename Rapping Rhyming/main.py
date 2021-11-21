import speech_recognition as sr
#from spleeter import separator

from google.cloud import speech

client = speech.SpeechClient()

# #spleeter.separator("audio.wav")
# r = sr.Recognizer()
# filename = "Danger Doom - Crosshairs.wav"

# with sr.AudioFile(filename) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)
