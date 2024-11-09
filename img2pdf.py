import os
import glob
from natsort import natsorted
from PIL import Image
import PyPDF2

# Function to convert image files to PDFs
def convert_image_to_pdf(image_file, output_pdf):
    img = Image.open(image_file)
    img.save(output_pdf, "PDF")

# Function to merge PDFs
def merge_pdfs(input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()
    for pdf in input_pdfs:
        with open(pdf, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_pdf, 'wb') as merged_file:
        pdf_merger.write(merged_file)

# Function to process image files in the directory
def process_files_in_directory(input_files):
    pdf_files = []

    for image_file in input_files:
        pdf_output = image_file + ".pdf"
        convert_image_to_pdf(image_file, pdf_output)
        pdf_files.append(pdf_output)

    # Merge all the generated PDF files into one
    merged_pdf_output = "merged_output.pdf"
    merge_pdfs(pdf_files, merged_pdf_output)

    print(f"Merged PDF saved as {merged_pdf_output}")

# Get the current directory and find all image files (e.g., jpg, png)
current_directory = os.getcwd()
image_files = natsorted(glob.glob(os.path.join(current_directory, "*.jpg")) + glob.glob(os.path.join(current_directory, "*.png")))

# Process the sorted image files
process_files_in_directory(image_files)
