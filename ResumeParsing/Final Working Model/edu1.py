
# with open('output1.txt') as f:
#     contents = f.read()


# def get_education(document):
#     education_terms = []
#     with open('edu1.txt', 'r') as file:
#         education_terms = file.readlines()
    
#     education_terms = [term.strip('\n') for term in education_terms]
#     education = []
#     for line in document:
#         for word in line.split(' '):
#             if len(word) > 2 and word in education_terms:
#                 if line not in education:
#                     education.append(line)
#         print(education[0])
#     return (education)
   

with open('output.txt', 'r', encoding="cp437") as f:
    target = f.read()

   
with open('edu1.txt', 'r', encoding="utf-8") as f:
    skills = f.readlines()

extracted = []
for i in skills:
    if i.lower() in target.lower():
        extracted.append(i.removesuffix('\n'))

extracted = [i for i in extracted if i != '' or i!= ' ']  

print("edu:")

for i in extracted:       
    print(f'{i}')

