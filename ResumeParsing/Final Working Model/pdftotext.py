#pdf to text
#not working 
import PyPDF2
a=PyPDF2.PdfFileReader("Resume 1.pdf")
str=''
for i in range(1,11):
   str += a.getPage(i).extractText()
with open("text1.txt","w", encoding='utf-8')  as f:
    f.write(str)


# b=PyPDF2.PdfFileReader('Pramod.pdf')
# str=''
# for p in range(0,1):
#    str += b.getPage(p).extractText()
# with open("text2.txt","w", encoding='utf-8')  as f:
#     f.write(str)

# c=PyPDF2.PdfFileReader('Prac 5.pdf')
# str=''
# for j in range(0,1):
#    str += c.getPage(j).extractText()
# with open("text3.txt","w", encoding='utf-8')  as f:
#     f.write(str)





    