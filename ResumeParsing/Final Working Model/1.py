#identifies only organisation

import spacy
with open('output1.txt', 'r') as f:
    target = f.read()


nlp = spacy.load("en_core_web_sm")
doc = nlp(target)

for ent in doc.ents:
    if ent.label_ == 'ORG':
        print(ent.text)


