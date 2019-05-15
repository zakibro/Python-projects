#! python3

import sys
import os
import PyPDF2

password = sys.argv[1]
#Dodaj ściężkę do walk.os



for folderName, subfolders, filenames in os.walk('XXXX'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfReader = PyPDF2.PdfFileReader(open(os.path.join(folderName, filename), 'rb'))
            print(pdfReader)
            #print(pdfReader.isEncrypted)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            pdfWriter.encrypt(password)
            filename = filename.strip('.pdf')
            print(filename)
            resultPdf = open(filename + '_encrypted.pdf', 'wb')
            pdfWriter.write(resultPdf)





