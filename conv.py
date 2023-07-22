import os
import PyPDF2
from win32com import client

def convert_xlsx_to_pdf(input_file_path):
    # Convert the input file path to an absolute path.
    input_file_path = os.path.abspath(input_file_path)

    # Get the output file path by removing .xlsx extension and appending .pdf
    output_file_path = os.path.splitext(input_file_path)[0] + '.pdf'

    # Start an Excel instance.
    excel_app = client.Dispatch("Excel.Application")

    try:
        # Open the workbook.
        workbook = excel_app.Workbooks.Open(input_file_path)

        # Save the XLSX as PDF directly.
        workbook.ExportAsFixedFormat(0, output_file_path, Quality=0, IncludeDocProperties=True, IgnorePrintAreas=False)

        # Close the workbook and quit Excel.
        workbook.Close(False)
        excel_app.Quit()

        print("Conversion successful. PDF saved at:", output_file_path)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_docx_to_pdf(input_file_path):
    # Convert the input file path to an absolute path.
    input_file_path = os.path.abspath(input_file_path)

    # Get the output file path by removing .docx extension and appending .pdf
    output_file_path = os.path.splitext(input_file_path)[0] + '.pdf'

    # Start a Word instance.
    word_app = client.Dispatch("Word.Application")

    try:
        # Open the document.
        doc = word_app.Documents.Open(input_file_path)

        # Save the DOCX as PDF directly.
        doc.ExportAsFixedFormat(output_file_path, 17)  # 17 represents PDF format constant wdFormatPDF

        # Close the document and quit Word.
        doc.Close(False)
        word_app.Quit()

        print("Conversion successful. PDF saved at:", output_file_path)
    except Exception as e:
        print(f"Error during conversion: {e}")

# Function to process all XLSX and DOCX files in a directory and convert them to PDF.
def process_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith(".xlsx"):
            convert_xlsx_to_pdf(file_path)
        elif filename.endswith(".docx"):
            convert_docx_to_pdf(file_path)
"""
# Replace 'FVDB.xlsx' with the path to your actual XLSX file.
input_file_path = 'FVDB.xlsx'
# Convert individual XLSX file.
convert_xlsx_to_pdf(input_file_path)
"""


def merge_pdfs(input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in input_pdfs:
        with open(pdf, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_pdf, 'wb') as merged_file:
        pdf_merger.write(merged_file)






# Convert all XLSX and DOCX files in the current directory.
current_directory = os.getcwd()
process_files_in_directory(current_directory)
input_files = ["SP- .pdf", "usulan-.pdf", "usulan -hrg.pdf", "FVDB.pdf", "KAK.pdf"]
#input_pattern = "*.pdf"
#input_files = glob.glob(input_pattern)
output_file = "ContohPrint.pdf"
merge_pdfs(input_files, output_file)


for file in input_files:
    os.remove(file)