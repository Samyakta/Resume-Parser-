#name-phone-email-skill-org

import docx2txt

# Passing docx file to process function
text = docx2txt.process("Ami Jape.docx")

# Saving content inside docx file into output.txt file
with open("output.txt", "w") as text_file:
	print(text, file=text_file)


#name --> phone, email, skills

#Extracting Indian names Perfectly!
 
import docx2txt
import nltk
 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
 

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
 
 
def extract_names(txt):
    person_names = []
 
    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )
 
    return person_names
 
 
if __name__ == '__main__':
    text = extract_text_from_docx('Ami Jape.docx')
    names = extract_names(text)
 
  
    print(names[0])  # noqa: T001

#take file from path --> phone number--> email--> PERFECTLY WORKING!!!!

import os
import nltk
from nltk import tokenize
import nltk.corpus
import re 


with open('output.txt') as f:
    contents = f.read()
    
for i in re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",contents):   #US phone numbers
    print("Phone number:",i)

for i in re.findall(r".\d{2} \d{10}",contents):   
     print("Phone number:",i)

def data():
    value = "mail"
    return value

data = data()

pattern = r'[\w]@[\w]+.\w{3}'
pattern = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',contents)
#re.findall(data)}

print("Email ID:",pattern)

with open('output.txt', 'r', encoding="cp437") as f:
    target = f.read()

   
with open('skillset.txt', 'r', encoding="utf-8") as f:
    skills = f.readlines()

extracted = []
for i in skills:
    if i.lower() in target.lower():
        extracted.append(i.removesuffix('\n'))

extracted = [i for i in extracted if i != '' or i!= ' ']  

print("Skills:")

for i in extracted:       
    print(f'{i}')
        
