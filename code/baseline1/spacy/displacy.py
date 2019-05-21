import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Autonomous cars shift insurance liability toward manufacturers")
# Since this is an interactive Jupyter environment, we can use displacy.render here
displacy.serve(doc, style='dep')