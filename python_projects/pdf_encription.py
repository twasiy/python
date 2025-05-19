import pikepdf
import os

# Set the folder where your PDFs are stored
pdf_folder = "/home/wasiy/Documents/document/"  # Change this to your actual folder path
password = ""  # Change this to your desired password

# Get all PDF files in the folder
file = os.listdir(pdf_folder)
pdf_files = [f for f in file if f.endswith(".pdf")] # Filter only PDF files from the list of files in the folder 

# Define permissions
permissions = pikepdf.Permissions(extract=False) # Disable extraction and printing
# Encrypt each PDF
for pdf_file in pdf_files:
    input_path = os.path.join(pdf_folder, pdf_file)
    output_path = input_path  # Save with the same name as input

    # Open the PDF with password (if it's password protected)
    try:
        pdf = pikepdf.Pdf.open(input_path, password='Tassok', allow_overwriting_input=True) # Open the PDF with the password
        pdf.save(output_path, encryption=pikepdf.Encryption(owner=password, user=password, allow=permissions, R=4)) # Encrypt with the desired password and permissions

        print(f"Encrypted: {pdf_file}")
    except pikepdf._core.PasswordError:
        print(f"Password error with {pdf_file}, skipping it.")

print("Encryption process completed.")
