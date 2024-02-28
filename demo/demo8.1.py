## Working 1 
## matched words

from vosk import Model, KaldiRecognizer
import pyaudio
import re

# Load the Vosk model
model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/1._January_2024/Date_20_01_2024/vosk-api-master/python/models/vosk-model-en-in-0.5/")

# Create a recognizer
recognizer = KaldiRecognizer(model, 16000)

def find_matching_words(paragraph, spoken_text):
    # Split paragraph and spoken text into words
    paragraph_words = paragraph.lower().split()
    spoken_words = spoken_text.lower().split()

    # Find matching words and their indices
    matched_words = []
    for word in paragraph_words:
        if word in spoken_words:
            matched_words.append(word)

    return matched_words

def recognize_and_highlight(paragraph):
    # Open a microphone stream
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()

    try:
        # Read the provided paragraph
        print("Provided Paragraph:", paragraph)

        print()
        print()
        # Capture audio from the microphone
        print("Say something:")

        print()
        print()
        
        data = stream.read(1028)
        while len(data) > 0:
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print(result)
                # Extract the spoken text from the result
                spoken_text = result.strip()

                # Find matching words in order
                matched_words = find_matching_words(paragraph, spoken_text)

                # Print matched words in order
                if matched_words:
                    print("Matched words:", " ".join(matched_words))

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