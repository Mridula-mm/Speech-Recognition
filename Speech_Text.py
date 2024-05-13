# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr

def speech_recog():
    r=sr.Recognizer() #This line creates a Recognizer object from the speech_recognition library and stores it in the variable r
    #recognizer is responsible for recognizing speech from audio data.
    mic=sr.Microphone() #This line creates a Microphone object from the speech_recognition library and stores it in the variable mic.
    # microphone that will be used to capture audio.
    with mic as source: #access the microphone. This ensures that the microphone is properly opened and closed after use.
        print('pls speak...')
        r.energy_threshold=100 #energy_threshold helps filter out very low-level background noise that might not be relevant to speech.
        r.adjust_for_ambient_noise(source,duration=10) #method listens to the audio source for a short duration (10 seconds) and analyzes the 
        # typical noise levels in the environment. This information is then used by the recognizer to adjust its internal parameters for better 
        # speech recognition in that specific noise environment.
        # - both techniques, the recognizer becomes more effective at distinguishing actual speech from background noise,
        # leading to more accurate speech recognition results.
        audio=r.listen(source) #listen to the audio source (microphone) and record the spoken audio,stored in the audio variable.

        try:
            text=r.recognize_google(audio)
            print('you said:',text)

        except:
            print("Didn't hear anything.pls speak again..." )

speech_recog()