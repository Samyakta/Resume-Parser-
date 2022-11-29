#read text file 


with open('output1.txt') as f:
    contents = f.read()

import nltk
import docx2txt
 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_text_from_docx(docx_path):
    txt = text.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
def read_text():
    read = contents.read



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
    text = contents
    names = extract_names(text)

    # print(names[0])

def name ():
    value = names
    return value

var = name()
print(var[0])

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

