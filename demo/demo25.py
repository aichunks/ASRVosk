# ### One by one + symbols not get + working actual 1 + colourized + fix

## white colour for spoked words, red for unspoken or missde words, yellow for addtional spoken words

from vosk import Model, KaldiRecognizer
import pyaudio
import re
import json
from colorama import Fore, Style

# Load the Vosk model
model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/2._February_2024/Date_28_02_2024/Speech_Project/vosk-api-master/python/models/vosk-model-small-en-us-0.15")

# Create a recognizer
recognizer = KaldiRecognizer(model, 16000)

provided_paragraph = ""  # Global variable to store the provided paragraph
missed_words = set()    # Store missed words globally

def find_matching_words(spoken_paragraph):
    global provided_paragraph
    global missed_words

    provided_words = provided_paragraph.split()
    spoken_words = spoken_paragraph.split()

    matched_words = [word if word in spoken_words else Fore.RED + word + Style.RESET_ALL for word in provided_words]
    extra_words = [Fore.YELLOW + word + Style.RESET_ALL for word in spoken_words if word not in provided_words]

    # Add newly missed words to the global set
    missed_words.update([word for word in provided_words if word not in spoken_words])

    # Keep missed words red even after speaking again
    for word in missed_words:
        if word in provided_words:
            matched_words[provided_words.index(word)] = Fore.RED + word + Style.RESET_ALL

    # Remove spoken words from the provided paragraph
    for word in spoken_words:
        if word in provided_words:
            provided_words.remove(word)

    provided_paragraph = ' '.join(provided_words)

    return matched_words, extra_words

def recognize_and_highlight(starting_index=0):
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()

    spoken_text = ""  

    try:
        print()
        print("Provided Paragraph:", provided_paragraph)
        print()

        print("Say something:")
        print()
        
        data = stream.read(1028)

        while len(data) > 0:
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                result_json = json.loads(result)
                spoken_text += result_json["text"].strip() + " "  

                matched_words, extra_words = find_matching_words(spoken_text)

                print(' '.join(matched_words))
                print(' '.join(extra_words))

            data = stream.read(1028)

    except KeyboardInterrupt:
        pass
    
    finally:
        stream.stop_stream()
        stream.close()
        mic.terminate()

if __name__ == "__main__":
    user_paragraph = input("Paste the paragraph here: ")
    provided_paragraph = user_paragraph  # Set the provided paragraph
    recognize_and_highlight()
