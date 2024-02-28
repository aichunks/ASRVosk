from vosk import Model, KaldiRecognizer
import pyaudio
import re
from termcolor import colored

# Load the Vosk model
model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/1._January_2024/Date_20_01_2024/vosk-api-master/python/models/vosk-model-en-in-0.5/")

# Create a recognizer
recognizer = KaldiRecognizer(model, 16000)

def highlight_text(paragraph, spoken_text, correct=True):
    # Determine the color based on correctness
    color = 'yellow' if correct else 'red'

    # Highlight the spoken text in the paragraph
    highlighted_text = paragraph.replace(spoken_text, colored(spoken_text, color))

    return highlighted_text

def recognize_and_highlight(paragraph):
    # Open a microphone stream
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()

    keywords = []  # Initialize an empty list to store keywords

    try:
        # Read the provided paragraph
        print("Provided Paragraph:", paragraph)

        # Capture audio from the microphone
        print("Say something:")
        data = stream.read(1028)
        while len(data) > 0:
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print(result)
                # Extract the spoken text from the result
                spoken_text = result.strip()

                # Add spoken text to keywords list if it's not already present
                if spoken_text.lower() not in keywords:
                    keywords.append(spoken_text.lower())

                # Highlight the spoken text in the paragraph
                highlighted_paragraph = highlight_text(paragraph, spoken_text)
                print("Highlighted Paragraph:", highlighted_paragraph)

            data = stream.read(1028)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the microphone stream
        stream.stop_stream()
        stream.close()
        mic.terminate()

if __name__ == "__main__":
    # Provide the paragraph as user input
    print()
    print()
    print()
    print()

    user_paragraph = input("Paste the paragraph here: ")


    print()
    print()
    print()
    print()
    print()


    # Start speech recognition and highlighting
    recognize_and_highlight(user_paragraph)
