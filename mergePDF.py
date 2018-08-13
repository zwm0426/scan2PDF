import os
from PyPDF2 import PdfFileWriter, PdfFileReader

# define input files' name
inputName1 = "高体资料_正.pdf"
inputName2 = "高体资料_反.pdf"

# define output and 2 input stream:
output = PdfFileWriter()
input1 = PdfFileReader(open(inputName1, "rb"))
input2 = PdfFileReader(open(inputName2, "rb"))
 
# get and print how many pages input1/2 has:
pageNumFile1 = input1.getNumPages()
pageNumFile2 = input2.getNumPages()


if (pageNumFile1 == pageNumFile2):
	pageNumString = "Each PDF file has " + str(input1.getNumPages()) + " pages."
	print(pageNumString)

	pageNum = pageNumFile1
	# read 2 files in positive order and reverse order:
	for page in range(pageNum): #[0, pageNum - 1]
		print("Adding page #" + str(page) + " and page #" + str(pageNum - 1 - page) + " to output")
		# add page from input1 - positive order 
		output.addPage(input1.getPage(page))
		# add page from input2 - reverse order 
		output.addPage(input2.getPage(pageNum - 1 - page))


	outputStream = open("output.pdf", "wb")
	output.write(outputStream)
else:
	print("The page numbers don't match, please check the source documents.")
	pageNumString = " '" + inputName1 + "'has " + str(input1.getNumPages()) + " pages, "\
					+"while '" + inputName2 + "' has " + str(input2.getNumPages()) + " pages.\n"
	print(pageNumString)









