import PyPDF2



def check_pdf_structure(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfFileReader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Get document information
        print("Document Information:")
        document_info = pdf_reader.metadata()
        print(document_info)

        # Get the number of pages
        num_pages = pdf_reader.getNumPages()
        print("\nNumber of Pages:", num_pages)

        # Iterate through each page
        for page_number in range(num_pages):
            page = pdf_reader.getPage(page_number)
            # Extract text from the page
            page_text = page.extractText()
            print("\nPage", page_number + 1, "Text:")
            print(page_text[:200])  # Print a portion of the text for inspection

        # Get trailer
        trailer = pdf_reader.trailer
        print("\nTrailer:")
        print(trailer)

        # Get the cross-reference table
        xref = pdf_reader.xref
        print("\nCross-Reference Table:")
        print(xref)

# Replace 'your_pdf_file.pdf' with the path to your PDF file
check_pdf_structure('PROGRESSREPORT.pdf')
