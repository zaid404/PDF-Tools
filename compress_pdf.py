import PyPDF2

# Open the original PDF file
with open('as.pdf', 'rb') as original_pdf:
    pdf_reader = PyPDF2.PdfReader(original_pdf)
    
    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Add pages from the original PDF to the new PDF
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    # Specify the compression level (0 to 9, where 0 is no compression and 9 is maximum compression)
    pdf_writer.set_page_layout(pdf_reader.pages[9].mediabox)
    
    # Save the compressed PDF to a new file
    with open('compressed.pdf', 'wb') as compressed_pdf:
        pdf_writer.write(compressed_pdf)
