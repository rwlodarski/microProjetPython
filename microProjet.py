from nltk.corpus import wordnet
from nltk import word_tokenize
from re import match, findall

# A function used to generate a list of standard words/phrases used to describe required skills and competencies
def gatherSkillsKeywords():
    keywords = []

    pattern = "\'(.*?)\'"
    hardcodedKeywords = ['Skill', 'Qualification', 'Requirement']
    
    for w in hardcodedKeywords:
        #for every keyword we look up its possible meanings - synsets in NLTK
        for s in wordnet.synsets(w):
            #for each synset we enrich the keywords list with its synonyms
            keywords.extend(s.lemma_names())
    #function returns a set with unique keywords
    return set(keywords)

def fileOpen():
    f = open('ad.txt')
    for line in f:
        print(line.strip())
    return f

def tokenize(file):
    raw = file.read()
    tokens = word_tokenize(raw)
    print(tokens)

def main():
    print(gatherSkillsKeywords())

    
main()
