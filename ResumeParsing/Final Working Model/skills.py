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

