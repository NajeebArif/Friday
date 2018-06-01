
#First of all lets import all the things which we need

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

#Now lets initialize friday to speek up.
#She will say the below lines on start up.
fridayGreeting = 'Hi I am Friday! How can i help you boss? You can ask me any question.'
fridayGivingAGoToSpeak = 'Please ask now'
fridayCantUnderstandYou = 'Sorry Boss!! I did not get you on that..'
fridayAnswers = "Sir Najeeb Arif is my boss"
fridaySaysBy = "Ok Boss Bye bye have a great day ahead"
#lets set the language
language = 'en'
#Text which i will say
myText = "who is your boss"

#now lets create the speech using gTTS
fridaySpeech = gTTS(text=fridayGreeting, lang=language, slow=False)
fridaySpeech.save("fridayGreetsYou.mp3")

#fridays go speech creation
fridaySpeech2 = gTTS(text=fridayGivingAGoToSpeak, lang=language, slow=False)
fridaySpeech2.save("fridayGivesAGo.mp3")

#friday's not able to understand what you said
fridaySpeech3 = gTTS(text=fridayCantUnderstandYou, lang=language, slow=False)
fridaySpeech3.save("fridayCantUnderstandYou.mp3")

#fridays obvious anwser
fridaySpeech4 = gTTS(text=fridayAnswers, lang=language, slow=False)
fridaySpeech4.save("fridayAnswers.mp3")

#fridays says bye
fridaySpeechBye = gTTS(text=fridaySaysBy, lang=language, slow=False)
fridaySpeechBye.save("fridaySaysBy.mp3")

playsound("fridayGreetsYou.mp3")

#now lets ask friday a question

#Name of my mic
mic_name = "Microphone (Realtek High Defini"

#sample rate is how often values are recorded
sample_rate = 48000

#Chunk size is the buffer to hold the data
chunk_size = 2048

#initialize the recognizer
r = sr.Recognizer()

#lets get all the mics in our system
mic_list = sr.Microphone.list_microphone_names()

#Lets set the suitable device ID from the above list
for i,microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i

#Lets use the microphone now. we will also specify the device id to specifically
#look for incase microphone is not working an error will thrown
with sr.Microphone(device_index=device_id,sample_rate=sample_rate,chunk_size=chunk_size) as source:
    #lets wait for a second for recognizer to adjust the energy level threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    playsound("fridayGivesAGo.mp3")
    audio = r.listen(source)

    try:
        myQuestion = r.recognize_google(audio)
    #error occurs when google is not able to recog what you said
    except sr.UnknownValueError:
        playsound("fridayCantUnderstandYou.mp3")
        myQuestion= ""
    except sr.RequestError as e:
        #formattedError = format(e)
        requestError = "Sorry Boss!! i was not able to contact Dr. Google coz i got "+e+" as error"
        fridaySpeech5 = gTTS(text=requestError, lang=language, slow=False)
        fridaySpeech5.save("requestError.mp3")
        playsound("requestError.mp3")

#now lets see what did i say
if myQuestion == myText:
    playsound("fridayAnswers.mp3")
else:
    print(myQuestion)
playsound("fridaySaysBy.mp3")
