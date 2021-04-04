import PyPDF2;

def pdf_merge():
    # Open the PDF file
    pdf1file = open('E:\\Stocks\\Apollo_3R-Feb04_2021.pdf','rb');
    pdf2file = open("E:\\Stocks\\GujGas-3R-Mar12_2021.pdf",'rb');

    # Read the PDF  from file
    pdf1reader = PyPDF2.PdfFileReader(pdf1file);
    pdf2reader = PyPDF2.PdfFileReader(pdf2file);

    # Create a PDF writer
    pdfwriter  = PyPDF2.PdfFileWriter();

    # loop the source PDFs
    for pageNum in range(pdf1reader.numPages):
        page = pdf1reader.getPage(pageNum);
        pdfwriter.addPage(page);

    for pageNum in range(pdf2reader.numPages):
        page = pdf2reader.getPage(pageNum);
        pdfwriter.addPage(page);

    pdfOutputFile = open('E:\\Stocks\\outputPDF.pdf','wb');
    pdfwriter.write(pdfOutputFile);

    pdfOutputFile.close();
    pdf1file.close();
    pdf2file.close();

if __name__ =='__main__':
    print('Helloooo.');
    pdf_merge();
    print('PDF merge is completed')