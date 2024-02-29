# from vosk import Model, KaldiRecognizer
# import pyaudio

# # Load the Vosk model
# model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/1._January_2024/Date_20_01_2024/vosk-api-master/python/models/vosk-model-en-in-0.5/")

# # Create a recognizer
# recognizer = KaldiRecognizer(model, 16000)

# def find_matching_words(paragraph, spoken_text):
#     # Split paragraph and spoken text into words
#     paragraph_words = paragraph.lower().split()
#     spoken_words = spoken_text.lower().split()

#     # Initialize variables to track missing and additional words
#     missing_words = []
#     additional_words = []

#     # Find matching words and their indices
#     matched_words = []
#     for word in paragraph_words:
#         if word in spoken_words:
#             matched_words.append(word)
#             spoken_words.remove(word)  # Remove matched words from spoken_words
#         else:
#             missing_words.append(word)

#     # Any remaining words in spoken_text are additional words
#     additional_words = spoken_words

#     return matched_words, missing_words, additional_words

# def recognize_and_highlight(paragraph):
#     # Open a microphone stream
#     mic = pyaudio.PyAudio()
#     stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
#     stream.start_stream()

#     try:
#         # Read the provided paragraph
#         print("Provided Paragraph:", paragraph)
#         print()

#         # Capture audio from the microphone
#         print("Say something:")
#         print()
        
#         data = stream.read(1028)
#         while len(data) > 0:
#             if recognizer.AcceptWaveform(data):
#                 result = recognizer.Result()
#                 print(result)
#                 # Extract the spoken text from the result
#                 spoken_text = result.strip()

#                 # Find matching words, missing words, and additional words
#                 matched_words, missing_words, additional_words = find_matching_words(paragraph, spoken_text)

#                 # Check each word individually
#                 paragraph_words = paragraph.lower().split()
#                 spoken_words = spoken_text.lower().split()
#                 for word in paragraph_words:
#                     if word in matched_words:
#                         print(f"Matched word: {word}")
#                     elif word in spoken_words:
#                         print(f"Additional spoken word: {word}")
#                     else:
#                         print(f"Missing word: {word}")

#             data = stream.read(1028)

#     except KeyboardInterrupt:
#         pass
#     finally:
#         # Close the microphone stream
#         stream.stop_stream()
#         stream.close()
#         mic.terminate()

# if __name__ == "__main__":

#     print()
#     print()
#     # Provide the paragraph as user input
#     user_paragraph = input("Paste the paragraph here: ")

#     print()
#     print()

#     # Start speech recognition and highlighting
#     recognize_and_highlight(user_paragraph)



from vosk import Model, KaldiRecognizer
import pyaudio

# Load the Vosk model
model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/1._January_2024/Date_20_01_2024/vosk-api-master/python/models/vosk-model-en-in-0.5/")

# Create a recognizer
recognizer = KaldiRecognizer(model, 16000)

def find_matching_words(paragraph, spoken_text):
    # Split paragraph and spoken text into words
    paragraph_words = paragraph.lower().split()
    spoken_words = spoken_text.lower().split()

    # Initialize variables to track missing and additional words
    missing_words = []
    additional_words = []

    # Find matching words and their indices
    matched_words = []
    for word in paragraph_words:
        if word in spoken_words:
            matched_words.append(word)
            spoken_words.remove(word)  # Remove matched words from spoken_words
        else:
            missing_words.append(word)

    # Any remaining words in spoken_text are additional words
    additional_words = spoken_words

    return matched_words, missing_words, additional_words

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
                print(result)
                # Extract the spoken text from the result
                spoken_text = result.strip()

                # Find matching words, missing words, and additional words
                matched_words, missing_words, additional_words = find_matching_words(paragraph, spoken_text)

                # Print matched words, missing words, and additional words joined together
                print("Matched words: ", " ".join(matched_words))
                print("Missing words: ", " ".join(missing_words))
                print("Additional spoken words: ", " ".join(additional_words))

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

