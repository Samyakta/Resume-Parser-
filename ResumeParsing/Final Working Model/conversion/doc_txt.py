import docx2txt
Text=docx2txt.process("Derik.docx")
with open("output1.txt","w")as text_file:
   print(Text, file=text_file)
