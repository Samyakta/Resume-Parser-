from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate

from Recruiter.forms import ParserForm, RecruiterForm
from Recruiter.models import Parser
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



with open('C:\\Users\\Admin\\OneDrive\\Desktop\\Programming\\mydirectory\\Suraj working model\\ResumeParsing\\output.txt') as f:
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

    

# def name ():
   
   
#     value = names
#     return value

# var = name()
# print(var[0])

import os
import nltk
from nltk import tokenize
import nltk.corpus
import re 


pnumber=9321
with open('C:\\Users\\Admin\\OneDrive\\Desktop\\Programming\\mydirectory\\Suraj working model\\ResumeParsing\\output.txt') as f:
    contents = f.read()
    

  
for i in re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",contents):   #US phone numbers
    print("Phone number:",i)
   
    
    

for i in re.findall(r".\d{2} \d{10}",contents):   
     print("Phone number:",i)
     pnumber=i

text = contents
names = extract_names(text)

# Create your views here.
def home(request):
    form=RecruiterForm
    return render(request,'Recruiter/home.html',{'form':form})
def filter(request):
    
    return render(request,'Recruiter/filter.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmPassword']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        form=RecruiterForm(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                form=RecruiterForm
        
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! ")
        
       
        
        return redirect('login')
    else:
        form=RecruiterForm
      
    return render(request, "Recruiter/home.html",{'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
        #     login(request)
            
            return render(request, "Recruiter/upload.html",{"user":user})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    
    return render(request, "Recruiter/login.html")

def upload(request):
    
    if request.method=='POST':
        form=ParserForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
          
            form=ParserForm
           

    else:
        form=ParserForm

    return render(request,'Recruiter/upload.html',{'form':form})



#name-phone-email-skill-org

import docx2txt

# # Passing docx file to process function
# text = docx2txt.process("Ami Jape.docx")

# # Saving content inside docx file into output.txt file
# with open("output.txt", "w") as text_file:
# 	print(text, file=text_file)


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
 
    return person_names[0]
 
 
# if __name__ == '__main__':
#     text = extract_text_from_docx('Ami Jape.docx')
#     names = extract_names(text)
 
  
#     print(names[0])  # noqa: T001

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
def getphone():
    num=('551.227.6212')
    for i in re.findall(r".\d{2} \d{10}",contents):   
      print("Phone number:",i)
    
    # num=i
    return num

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


def resumedata(request):
    
    return render(request,'Recruiter/resumedata.html',{'x':extract_names(text),'p':  getphone(),'email':pattern,'skill':skills} )

