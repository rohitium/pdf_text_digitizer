import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pdf_text_digitizer.digitize import digitize_pdf

def main():
    # Define the path to the example PDF file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_file_path = os.path.join(current_dir, 'example1.pdf')
    
    # Ensure the PDF file exists
    if not os.path.isfile(pdf_file_path):
        print(f"Error: The file {pdf_file_path} does not exist.")
        return
    
    # Digitize the PDF and print the extracted text
    extracted_text = digitize_pdf(pdf_file_path)
    print("Extracted Text:\n", extracted_text)

if __name__ == "__main__":
    main()
