#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyPDF2 as pdf
from PyPDF2.pdf import ContentStream
from PyPDF2.generic import TextStringObject, NameObject
from PyPDF2.utils import b_

class PDFConverter:
    def __init__(self, fileName):
        self.pdfObj = pdf.PdfFileReader(fileName)

    def removeWatermark(self):
        #for pageNum in range(self.pdfObj.getNumPages()):
        print(self.pdfObj.getDocumentInfo())
        for pageNum in range(399, 400):
            page = self.pdfObj.getPage(pageNum)
            print(page.extractText().encode('latin-1'))
            contentObj = page["/Contents"].getObject()
            content = ContentStream(contentObj, self.pdfObj)
            for opr, opt in content.operations:
                if opt == b_("TJ"):
                    txt = opr[0][0]
                    if isinstance(txt, TextStringObject):
                        pass
            page.__setitem__(NameObject('/Contents'), content)
            print("\n\n")


    def save(self, outFileName):
        pass

def PrintUsage():
    print("usage: ./pdfconverter.py option")
    print("option:")
    print("option:")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        PrintUsage()
        sys.exit(0)
    cmd = sys.argv[1]
    fileName = sys.argv[2]
    outFileName = sys.argv[3]
    convert = PDFConverter(fileName)
    convert.removeWatermark()
    convert.save(outFileName)
