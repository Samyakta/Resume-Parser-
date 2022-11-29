#identifies only organisation

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well.")

for ent in doc.ents:
    if ent.label_ == 'ORG':
        print(ent.text)


