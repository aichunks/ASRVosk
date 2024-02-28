## working 1

from vosk import Model, KaldiRecognizer
import pyaudio
import re
from termcolor import colored

# Load the Vosk model
model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/1._January_2024/Date_20_01_2024/vosk-api-master/python/models/vosk-model-en-in-0.5/")


# Create a recognizer
recognizer = KaldiRecognizer(model, 16000)

def highlight_text(paragraph, spoken_text, correct=True):
    # Split the paragraph and spoken text into words
    paragraph_words = set(paragraph.lower().split())
    spoken_words = set(spoken_text.lower().split())

    # Determine the color based on correctness
    color = 'yellow' if correct else 'red'

    # Highlight the words in the paragraph
    highlighted_text = ' '.join(
        colored(word, color) if word.lower() in spoken_words else word
        for word in paragraph.split()
    )

    return highlighted_text

def recognize_and_highlight(paragraph, keywords):
    # Open a microphone stream
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()

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

                # Check if any keyword is present in the spoken text
                correct = any(keyword.lower() in spoken_text.lower() for keyword in keywords)

                # Highlight the words in the paragraph
                highlighted_paragraph = highlight_text(paragraph, spoken_text, correct)
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
    user_paragraph = input("Paste the paragraph here: ")

    # Define a list of keywords to spot
    keywords = ['keyword1', 'keyword2', 'keyword3']

    # Start speech recognition and highlighting
    recognize_and_highlight(user_paragraph, keywords)