from vosk import Model, KaldiRecognizer
import pyaudio
import tkinter as tk

class SpeechRecognitionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Speech Recognition GUI")

        self.model = Model("/media/taranjeet/Drive/Taran.aic.WorkSpace/Year_2024/1._January_2024/Date_20_01_2024/vosk-api-master/python/models/vosk-model-en-in-0.5/")


        self.recognizer = KaldiRecognizer(self.model, 16000)

        self.input_label = tk.Label(master, text="Enter a paragraph:")
        self.input_label.pack()

        self.input_text = tk.Text(master, height=5, width=50)
        self.input_text.pack()

        self.recognition_result_label = tk.Label(master, text="Recognition Result:")
        self.recognition_result_label.pack()

        self.result_text = tk.Text(master, height=5, width=50, state=tk.DISABLED)
        self.result_text.pack()

        self.recognize_button = tk.Button(master, text="Recognize", command=self.recognize)
        self.recognize_button.pack()

        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
        self.stream.start_stream()

    def recognize(self):
        paragraph = self.input_text.get("1.0", tk.END)
        data = self.stream.read(1028)

        if self.recognizer.AcceptWaveform(data):
            result = self.recognizer.Result()
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)
            self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechRecognitionGUI(root)
    root.mainloop()
