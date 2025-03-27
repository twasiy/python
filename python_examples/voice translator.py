import pyttsx3
import speech_recognition as sr
from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed
engine.setProperty('volume', 1)  # Set volume

# Function to translate text
def change(text='Type', src='english', dest='bengali'):
    try:
        translated_text = GoogleTranslator(source=src, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle translation
def data():
    s = comb_sour.get().lower()
    d = comb_dest.get().lower()
    masg = sour_textbox.get("1.0", END).strip()

    if not masg:
        des_textbox.delete("1.0", END)
        des_textbox.insert(END, "⚠️ Please enter text to translate!")
        return

    textget = change(text=masg, src=s, dest=d)
    des_textbox.delete("1.0", END)
    des_textbox.insert(END, textget)

# Function for Speech-to-Text (Voice Input)
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        sour_textbox.delete("1.0", END)
        sour_textbox.insert(END, "🎤 Listening... Please speak!")
        root.update()  # Update UI

        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            sour_textbox.delete("1.0", END)
            sour_textbox.insert(END, text)
        except sr.UnknownValueError:
            sour_textbox.delete("1.0", END)
            sour_textbox.insert(END, "❌ Couldn't understand. Try again!")
        except sr.RequestError:
            sour_textbox.delete("1.0", END)
            sour_textbox.insert(END, "❌ No internet connection!")

#Function for Text-to-Speech (Voice Output)
def voice_output():
    text = des_textbox.get("1.0", END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

#GUI Setup
root = Tk()
root.title('Voice Translator')
root.geometry("500x700")
root.config(bg='#121212')

# Label
lab_text = Label(root, text='Voice Translator', font=('Arial', 18, 'bold'), fg='yellow', bg='#121212')
lab_text.pack(pady=10)

# Source Text Box
sour_textbox = Text(root, font=('Arial', 12), wrap=WORD)
sour_textbox.pack(pady=10, padx=10, fill=X)

# Language Selection
list_text = ['english', 'bengali', 'hindi', 'french', 'spanish']

comb_sour = ttk.Combobox(root, values=list_text)
comb_sour.pack()
comb_sour.set('english')

comb_dest = ttk.Combobox(root, values=list_text)
comb_dest.pack()
comb_dest.set('bengali')

# Buttons
btn_frame = Frame(root, bg='#121212')
btn_frame.pack(pady=10)

Button(btn_frame, text='🎤 Speak', command=voice_input, font=('Arial', 12, 'bold'), bg='#00a86b', fg='white').pack(side=LEFT, padx=5)
Button(btn_frame, text='Translate', command=data, font=('Arial', 12, 'bold'), bg='#ff8c00', fg='white').pack(side=LEFT, padx=5)
Button(btn_frame, text='🔊 Listen', command=voice_output, font=('Arial', 12, 'bold'), bg='#008CBA', fg='white').pack(side=LEFT, padx=5)

# Destination Text Box
des_textbox = Text(root, font=('Arial', 12), wrap=WORD)
des_textbox.pack(pady=10, padx=10, fill=X)

root.mainloop()
