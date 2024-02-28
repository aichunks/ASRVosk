import tkinter as tk
import pyaudio
from vosk import Model, KaldiRecognizer
import json

class SpeechTextSynchronizationApp:
    def __init__(self, master, paragraph):
        self.master = master
        self.paragraph = paragraph
        self.spoken_text_var = tk.StringVar()
        self.spoken_text_var.set("")

        # self.model = Model("path/to/your/vosk/model")
        self.model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/1._January_2024/Date_20_01_2024/vosk-api-master/python/models/vosk-model-en-in-0.5/")

        self.recognizer = KaldiRecognizer(self.model, 16000)

        self.create_widgets()

    def create_widgets(self):
        self.paragraph_label = tk.Label(self.master, text="Paragraph:")
        self.paragraph_label.pack()

        self.paragraph_text = tk.Text(self.master, height=5, width=40)
        self.paragraph_text.insert(tk.END, self.paragraph)
        self.paragraph_text.pack()

        self.speech_text_label = tk.Label(self.master, text="Spoken Text:")
        self.speech_text_label.pack()

        self.speech_text_entry = tk.Entry(self.master, textvariable=self.spoken_text_var, state=tk.DISABLED)
        self.speech_text_entry.pack()

        self.highlight_button = tk.Button(self.master, text="Highlight Match", command=self.highlight_match)
        self.highlight_button.pack()

        self.start_listening_button = tk.Button(self.master, text="Start Listening", command=self.start_listening)
        self.start_listening_button.pack()

    def start_listening(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()

        print("Speak the paragraph:")
        buffer = bytearray(8000)
        while True:
            buffer = stream.read(8000)
            if len(buffer) == 0:
                break
            if self.recognizer.AcceptWaveform(buffer):
                result = self.recognizer.Result()
                result_dict = json.loads(result)
                spoken_text = result_dict.get("text", "")
                self.spoken_text_var.set(spoken_text)
                break

        stream.stop_stream()
        stream.close()
        p.terminate()

        self.highlight_match()

    def highlight_match(self):
        spoken_text = self.spoken_text_var.get()
        paragraph = self.paragraph_text.get("1.0", tk.END).strip()

        # Reset tags to clear previous highlighting
        self.paragraph_text.tag_delete("highlight")
        self.paragraph_text.tag_config("highlight_match", background="yellow")
        self.paragraph_text.tag_config("highlight_nomatch", background="red")

        # Simple matching: Highlight correct words in yellow and incorrect words in red
        start_index = "1.0"
        for word, paragraph_word in zip(spoken_text.split(), paragraph.split()):
            if word.lower() == paragraph_word.lower():
                end_index = f"{start_index}+{len(paragraph_word)}c"
                self.paragraph_text.tag_add("highlight_match", start_index, end_index)
            else:
                end_index = f"{start_index}+{len(paragraph_word)}c"
                self.paragraph_text.tag_add("highlight_nomatch", start_index, end_index)
                # Only highlight the incorrect word in red
                self.paragraph_text.tag_config("highlight_nomatch", background="red")
            start_index = end_index

        # Apply the tags to the text widget
        self.paragraph_text.tag_add("highlight_match", "1.0", "end")
        self.paragraph_text.tag_add("highlight_nomatch", "1.0", "end")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Speech Text Synchronization App")

    sample_paragraph = "This is a sample paragraph for synchronization."
    app = SpeechTextSynchronizationApp(root, sample_paragraph)

    root.mainloop()
