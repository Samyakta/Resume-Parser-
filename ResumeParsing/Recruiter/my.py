import nltk
import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["pythonwithmongodb"]

mycollection=mydb["programmers"]

# myrecord={"Name":"Suraj Sahani","Language Known":"Java,Python"}
# x=mycollection.insert_one(myrecord)
# print(x.inserted_id)

mylist=[

{"Name":"Advait","Language Known":"Java,Python"},
{"Name":"Adarsh","Language Known":"Java,Python"},
{"Name":"Hritik","Language Known":"Java,Python"},
{"Name":"Amit","Language Known":"Java,Python"},
{"Name":"Rakesh","Language Known":"Java,Python"},
{"Name":"Shubham","Language Known":"Java,Python"},
{"Name":"Amkit","Language Known":"Java,Python"},
{"Name":"Aniket","Language Known":"Java,Python"},
{"Name":"Vikas","Language Known":"Java,Python"},
{"Name":"Jagdish","Language Known":"Java,Python"},


]

# y=mycollection.insert_many(mylist)
# print(y.inserted_ids)

x=mycollection.find_one()
# for y in mycollection.find():
#      print(y)
# x=y
print(x)


with open('C:\\Users\\Acer\\Visual Studio Projects\\ResumeParsing\\Recruiter\\output1.txt') as f:
    contents = f.read()


 
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
    print(names)

    

def name ():
    names = extract_names(text)
    value = names
    return value

var = name()
print(var[0])

import os
import nltk
from nltk import tokenize
import nltk.corpus
import re 



with open('C:\\Users\\Acer\\Visual Studio Projects\\ResumeParsing\\Recruiter\\output1.txt') as f:
    contents = f.read()
    

  
for i in re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",contents):   #US phone numbers
    print("Phone number:",i)
   
    
    

for i in re.findall(r".\d{2} \d{10}",contents):   
     print("Phone number:",i)


