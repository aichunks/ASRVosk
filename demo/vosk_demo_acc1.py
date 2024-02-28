## checking accuracy and testing

import re
import pyaudio
from vosk import Model, KaldiRecognizer

# Load the Vosk model
# model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/2._February_2024/Date_28_02_2024/Speech_Project/vosk-api-master/python/models/vosk-model-en-in-0.5/")

# model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/2._February_2024/Date_28_02_2024/Speech_Project/vosk-api-master/python/models/vosk-model-en-us-0.22/")

model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/2._February_2024/Date_28_02_2024/Speech_Project/vosk-api-master/python/models/vosk-model-small-en-us-0.15")

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
            spoken_words.remove(word)  # Remove matched words from spoken_words

    return matched_words


## check the word error rate / checking the accracy of the model

def calculate_wer(paragraph, recognized_words):
    # Tokenize the ground truth paragraph and recognized words
    ref_words = re.findall(r'\b\w+\b', paragraph.lower())
    rec_words = recognized_words.lower().split()

    # Initialize variables to count errors
    substitutions = 0
    deletions = len(ref_words)
    insertions = 0

    # Find and count substitutions, deletions, and insertions
    for word in rec_words:
        if word in ref_words:
            substitutions += 1
            deletions -= 1
            ref_words.remove(word)
        else:
            insertions += 1

    wer = (substitutions + deletions + insertions) / max(1, len(ref_words))
    return wer

def recognize_and_highlight(paragraph):
    # Open a microphone stream
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()

    try:
        # Read the provided paragraph
        print("Provided Paragraph:", paragraph)

        print()

        # Capture audio from the microphone
        print("Say something:")


        print()

        data = stream.read(1028)
        while len(data) > 0:
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print()
                print(result)
                # Extract the recognized text from the result
                recognized_text = result.strip()
                print('recognized text',recognized_text)

                # Find matching words in order
                matched_words = find_matching_words(paragraph, recognized_text)

                # Print matched words in order
                if matched_words:
                    print("Matched words:", " ".join(matched_words))

                # Calculate WER
                wer = calculate_wer(paragraph, recognized_text)
                print("Word Error Rate:", wer)

            data = stream.read(1028)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the microphone stream
        stream.stop_stream()
        stream.close()
        mic.terminate()

if __name__ == "__main__":

    print()
    print()
    # Provide the paragraph as user input
    user_paragraph = input("Paste the paragraph here: ")
    print()
    print()

    # Start speech recognition and highlighting
    recognize_and_highlight(user_paragraph)

