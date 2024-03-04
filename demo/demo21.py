### One by one + symbols not get + working actual 1



from vosk import Model, KaldiRecognizer
import pyaudio
import re
import json
# import nltk
# from nltk.tokenize import word_tokenize

# nltk.download('punkt')  # Ensure punkt tokenizer is downloaded

# Load the Vosk model
model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/2._February_2024/Date_28_02_2024/Speech_Project/vosk-api-master/python/models/vosk-model-small-en-us-0.15")

# Create a recognizer
recognizer = KaldiRecognizer(model, 16000)



def find_matching_words(provided_paragraph, spoken_paragraph):
    provided_words = provided_paragraph.split()
    spoken_words = spoken_paragraph.split()

    # text = ' '.join(spoken_words)
    # pattern = re.compile(r'\b[a-zA-Z]+\b|\bi\b')

    # spoken_words = pattern.findall(text)


    # import pdb;pdb.set_trace()

    matched_words = [word for word in provided_words if word in spoken_words]
    missing_words = [word for word in provided_words if word not in spoken_words]
    extra_words = [word for word in spoken_words if word not in provided_words]

    print('matched_words from fn: ', matched_words)
    print('extra_words words from fn: ',extra_words)
    print('missing words from fn: ', missing_words)

    return matched_words, missing_words, extra_words



def recognize_and_highlight(paragraph, starting_index=0):
    # Open a microphone stream
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()


    spoken_text = ""  # Variable to store spoken text

    try:
        print()
        print("Provided Paragraph:", paragraph)
        print()

        print("Say something:")
        print()
        
        data = stream.read(1028)

        while len(data) > 0:
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                # spoken_text += result.strip() + " "  # Concatenate spoken text
                result_json = json.loads(result)
                spoken_text += result_json["text"].strip() + " "  

                print('spoken_text: ', spoken_text)

                matched_words, missed_words, additional_spoken_words = find_matching_words(paragraph, spoken_text)

                # # Print each word individually
                # for word in matched_words:
                #     print("Matched words:", word)
                # for word in missed_words:
                #     print("Missing words:", word)
                # for word in additional_spoken_words:
                #     print("Extra words:", word)

                # Print each category of words on separate lines
                print("Matched words:")
                for word in matched_words:
                    print(f"\t- {word}")

                if missed_words:
                    print("Missing words:")
                    for word in missed_words:
                        print(f"\t- {word}")

                if additional_spoken_words:
                    print("Extra words:")
                    for word in additional_spoken_words:
                        print(f"\t- {word}")


                print()

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
