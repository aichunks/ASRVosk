# # import speech_recognition as sr
# # import tkinter as tk

# # class SpeechTextSynchronizationApp:
# #     def __init__(self, master, paragraph):
# #         self.master = master
# #         self.paragraph = paragraph
# #         self.spoken_text_var = tk.StringVar()
# #         self.spoken_text_var.set("")

# #         self.create_widgets()

# #     def create_widgets(self):
# #         self.paragraph_label = tk.Label(self.master, text="Paragraph:")
# #         self.paragraph_label.pack()

# #         self.paragraph_text = tk.Text(self.master, height=5, width=40)
# #         self.paragraph_text.insert(tk.END, self.paragraph)
# #         self.paragraph_text.pack()

# #         self.speech_text_label = tk.Label(self.master, text="Spoken Text:")
# #         self.speech_text_label.pack()

# #         self.speech_text_entry = tk.Entry(self.master, textvariable=self.spoken_text_var, state=tk.DISABLED)
# #         self.speech_text_entry.pack()

# #         self.highlight_button = tk.Button(self.master, text="Highlight Match", command=self.highlight_match)
# #         self.highlight_button.pack()

# #         self.start_listening_button = tk.Button(self.master, text="Start Listening", command=self.start_listening)
# #         self.start_listening_button.pack()

# #     def start_listening(self):
# #         recognizer = sr.Recognizer()

# #         with sr.Microphone() as source:
# #             print("Speak the paragraph:")
# #             audio_input = recognizer.listen(source)

# #         spoken_text = recognizer.recognize_google(audio_input)
# #         self.spoken_text_var.set(spoken_text)

# #         self.highlight_match()

# #     def highlight_match(self):
# #         spoken_text = self.spoken_text_var.get()
# #         paragraph = self.paragraph_text.get("1.0", tk.END)

# #         # Simple matching: Highlight matching words in yellow
# #         for word in spoken_text.split():
# #             if word in paragraph:
# #                 start_index = paragraph.index(word)
# #                 end_index = start_index + len(word)
# #                 self.paragraph_text.tag_add("highlight", f"1.{start_index}", f"1.{end_index}")
# #                 self.paragraph_text.tag_config("highlight", background="yellow")

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     root.title("Speech Text Synchronization App")

# #     sample_paragraph = "This is a sample paragraph for synchronization."
# #     app = SpeechTextSynchronizationApp(root, sample_paragraph)

# #     root.mainloop()


# import speech_recognition as sr
# import tkinter as tk

# class SpeechTextSynchronizationApp:
#     def __init__(self, master, paragraph):
#         self.master = master
#         self.paragraph = paragraph
#         self.spoken_text_var = tk.StringVar()
#         self.spoken_text_var.set("")

#         self.create_widgets()

#     def create_widgets(self):
#         self.paragraph_label = tk.Label(self.master, text="Paragraph:")
#         self.paragraph_label.pack()

#         self.paragraph_text = tk.Text(self.master, height=5, width=40)
#         self.paragraph_text.insert(tk.END, self.paragraph)
#         self.paragraph_text.pack()

#         self.speech_text_label = tk.Label(self.master, text="Spoken Text:")
#         self.speech_text_label.pack()

#         self.speech_text_entry = tk.Entry(self.master, textvariable=self.spoken_text_var, state=tk.DISABLED)
#         self.speech_text_entry.pack()

#         self.highlight_button = tk.Button(self.master, text="Highlight Match", command=self.highlight_match)
#         self.highlight_button.pack()

#         self.start_listening_button = tk.Button(self.master, text="Start Listening", command=self.start_listening)
#         self.start_listening_button.pack()

#     def start_listening(self):
#         recognizer = sr.Recognizer()

#         with sr.Microphone() as source:
#             print("Speak the paragraph:")
#             audio_input = recognizer.listen(source)

#         spoken_text = recognizer.recognize_google(audio_input)
#         self.spoken_text_var.set(spoken_text)

#         self.highlight_match()

#     def highlight_match(self):
#         spoken_text = self.spoken_text_var.get()
#         paragraph = self.paragraph_text.get("1.0", tk.END)

#         # Reset tags to clear previous highlighting
#         self.paragraph_text.tag_delete("highlight")
#         self.paragraph_text.tag_config("highlight_match", background="yellow")
#         self.paragraph_text.tag_config("highlight_nomatch", background="red")

#         # Simple matching: Highlight matching words in yellow and non-matching words in red
#         for word in spoken_text.split():
#             if word in paragraph:
#                 start_index = paragraph.index(word)
#                 end_index = start_index + len(word)
#                 self.paragraph_text.tag_add("highlight_match", f"1.{start_index}", f"1.{end_index}")
#             else:
#                 self.paragraph_text.tag_add("highlight_nomatch", "1.0", "1.end")

#         # Apply the tags to the text widget
#         self.paragraph_text.tag_add("highlight_match", "1.0", "end")
#         self.paragraph_text.tag_add("highlight_nomatch", "1.0", "end")

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Speech Text Synchronization App")

#     sample_paragraph = "This is a sample paragraph for synchronization."
#     app = SpeechTextSynchronizationApp(root, sample_paragraph)

#     root.mainloop()


import speech_recognition as sr
import tkinter as tk

class SpeechTextSynchronizationApp:
    def __init__(self, master, paragraph):
        self.master = master
        self.paragraph = paragraph
        self.spoken_text_var = tk.StringVar()
        self.spoken_text_var.set("")

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
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak the paragraph:")
            audio_input = recognizer.listen(source)

        spoken_text = recognizer.recognize_google(audio_input)
        self.spoken_text_var.set(spoken_text)

        self.highlight_match()

    def highlight_match(self):
        spoken_text = self.spoken_text_var.get()
        paragraph = self.paragraph_text.get("1.0", tk.END)

        # Reset tags to clear previous highlighting
        self.paragraph_text.tag_delete("highlight")
        self.paragraph_text.tag_config("highlight_match", background="yellow")
        self.paragraph_text.tag_config("highlight_nomatch", background="red")

        # Simple matching: Highlight correct words in yellow and incorrect words in red
        start_index = "1.0"
        for word in spoken_text.split():
            if word in paragraph:
                end_index = f"1.{paragraph.index(word) + len(word)}"
                self.paragraph_text.tag_add("highlight_match", start_index, end_index)
                start_index = end_index
            else:
                end_index = f"{start_index}+{len(word)}c"
                self.paragraph_text.tag_add("highlight_nomatch", start_index, end_index)
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
