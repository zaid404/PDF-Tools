# File Conversion and PDF Merging Script

Description:
This Python script is designed to perform various file conversion tasks and merge the resulting PDFs into a single PDF file. The script utilizes the `os`, `PyPDF2`, and `win32com` modules to handle file operations, PDF manipulation, and Microsoft Office file conversions.

Features:
1. File Conversion Functions:
   - `convert_xlsx_to_pdf(input_file_path)`: Converts XLSX files to PDF format using Microsoft Excel's COM interface.
   - `convert_docx_to_pdf(input_file_path)`: Converts DOCX files to PDF format using Microsoft Word's COM interface.

2. Directory Processing:
   - `process_files_in_directory(directory_path)`: Processes all XLSX and DOCX files within the specified directory and converts them to PDFs using the respective conversion functions.

3. PDF Merging:
   - `merge_pdfs(input_pdfs, output_pdf)`: Merges multiple input PDFs into a single PDF using PyPDF2's PdfMerger.

Usage:
1. File Conversion:
   - Ensure Microsoft Excel and Microsoft Word are installed on the system to perform XLSX and DOCX conversions.
   - Call `convert_xlsx_to_pdf(input_file_path)` or `convert_docx_to_pdf(input_file_path)` with the path to the specific XLSX or DOCX file for individual conversions.

2. Directory Processing:
   - Set the current working directory or provide a specific directory path to `process_files_in_directory(directory_path)`.
   - The function will process all XLSX and DOCX files in the specified directory and convert them to PDFs.

3. PDF Merging:
   - List the individual PDF files to merge in the `input_files` list.
   - Call `merge_pdfs(input_files, output_pdf)` with the list of input files and the desired output PDF file name.
   - The merged PDF will be saved as "ContohPrint.pdf" (replace with desired name).

Important Note:
- Always be cautious when performing file operations and ensure you have backups of the original files.
- Review and customize the script to fit your specific requirements.
- Provide necessary file paths and dependencies for the code to work correctly.
- Consider adding error handling and validation for better robustness.

This script can be useful for anyone who needs to convert XLSX and DOCX files to PDF format and then merge multiple PDFs into a single file. It provides a straightforward way to automate these tasks, saving time and effort.
