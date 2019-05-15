#! python3

""" "sister" file for encrypter.py - tries to decrypt the file """"

import sys
import os
import PyPDF2

password = sys.argv[1]


for folderName, subfolders, filenames in os.walk('C://Users//PabloD//Desktop//python_projects'):
    for filename in filenames:
        if filename.endswith('_encrypted.pdf'):
            pdfReader = PyPDF2.PdfFileReader(open(os.path.join(folderName, filename), 'rb'))
            try:
                pdfReader.decrypt(password)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                filename = filename.strip('_encrypted.pdf')
                resultPdf = open(filename + 'new' + '.pdf', 'wb')
                pdfWriter.write(resultPdf)
            except:
                print('Złe hasło')
                continue



