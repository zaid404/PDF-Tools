import PyPDF2
import os

def pdf_to_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            text = ""
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            return text
    except PyPDF2.utils.PdfReadError as e:
        print(f"Error processing {pdf_path}: {e}")
        return None  # Return None to indicate an error

# Read the list of PDF file names from input.txt
input_file = 'input.txt'
with open(input_file, 'r', encoding='utf-8') as file:
    pdf_files = [line.strip() for line in file if line.strip().endswith('.pdf')]

# Specify the output directory (relative to the current working directory)
output_directory = 'output'

# Create the output directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Create a list to store the names of successfully processed files
success_files = []

# Process each PDF file
for pdf_file in pdf_files:
    pdf_path = os.path.join(os.getcwd(), pdf_file)
    
    # Attempt to process the PDF file
    text_result = pdf_to_text(pdf_path)

    # If an error occurred, skip to the next file
    if text_result is None:
        continue

    # Create an output file name based on the input file name
    output_file_path = os.path.join(output_directory, f'{os.path.basename(pdf_file).replace(".pdf", "_out.txt")}')
    with open('berhasil.txt', 'w', encoding='utf-8') as success_file:
        success_file.write('\n'.join(success_files))

    # Save the text to the specified file
    with open(output_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text_result)

    # Add the name of the successfully processed file to the list
    success_files.append(pdf_file)

    # Print the converted text
    print(f"Processed {pdf_file} and saved the result to {output_file_path}")

# Write the names of successfully processed files to berhasil.txt

