from gtts import gTTS
from playsound import playsound
import pypdf
import os  # Import the os module for file existence checks

def text_to_speech(pdf_path, output_mp3="output.mp3"):
    """Converts text from a PDF to speech and saves it as an MP3 file.

    Args:
        pdf_path: The path to the PDF file.
        output_mp3: The name of the output MP3 file.
    """
    try:
        if not os.path.exists(pdf_path):  # Check if the PDF file exists
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        with open(pdf_path, 'rb') as book:  # Use 'with' to ensure file closing
            reader = pypdf.PdfReader(book)
            all_text = ""

            for page in reader.pages:
                text = page.extract_text()
                if text:  # Check if text was extracted from the page
                    all_text += text + " "  # Add a space between pages

            if not all_text.strip():  # Check for empty or whitespace-only text
                print("Warning: No extractable text found in the PDF.")
                return  # Exit early if no text

            print(f"Extracted {len(all_text)} characters from PDF.") # Helpful debug print

            speech = gTTS(text=all_text, lang="en",slow=False)
            speech.save(output_mp3)
            print(f"Saved speech to {output_mp3}")  # Helpful debug print

            playsound(output_mp3)  # Play the generated audio
            print("Playing audio...") # Helpful debug print

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except pypdf.errors.PdfReadError as e: # Catch PDF read errors
        print(f"Error reading PDF: {e}")
    except Exception as e:  # Catch other potential errors
        print(f"An unexpected error occurred: {e}")


# Example usage:
pdf_file = "/home/wasiy/Downloads/wasiy.pdf"  # Replace with the actual path to your PDF
text_to_speech(pdf_file) # Call the function
# Or specify a different output filename:
# text_to_speech(pdf_file, "my_audio.mp3")