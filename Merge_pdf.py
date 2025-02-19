# WAP to manipulate PDF files using Pypdf. your program should be able to merge mutiple pdf files into one pdf file. you are welcome to add more functionality to your program.
# pypdf is a free and open source pure python pdf library capable of spliting merging cropping and transforming the pages of pdf files. it can also add custom data viewing options and passwords to pdf files.pypdf can retrieve text and metadata from pdfs as well as merge entire files together.

# importing required modules
from pypdf import PdfReader
from pypdf import PdfWriter

# creating a pdf reader object
reader = PdfReader("PNGfiles/Book2.pdf")

# printing no. pages in pdf 
print("length is :",len(reader.pages))
print("\nThe text in the pdf file is:")
page = reader.pages[0]
# extracting text from page
print(page.extract_text())

def merge_pdfs(pdfs, output):
    pdfWriter=PdfWriter()
    
    for pdf in pdfs:
        pdfWriter.append(pdf)
    
    with open(output,'wb') as f:
        pdfWriter.write(f)
    print("pdfs merged successfully")

def main():
    pdfs=['PNGfiles/Book2.pdf','PNGfiles/class diagram.pdf']
    output = 'PNGfiles/merged.pdf'
    
    merge_pdfs(pdfs=pdfs,output=output)
    
if __name__ == "__main__":
    main()