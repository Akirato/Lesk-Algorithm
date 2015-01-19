#Author: Nurendra Choudhary.
#Algorithm Reference: http://en.wikipedia.org/wiki/Lesk_algorithm

from nltk.corpus import wordnet 
from nltk.tokenize.punkt import PunktWordTokenizer
import sys


functionwords = ['about', 'across', 'against', 'along', 'around', 'at',
                 'behind', 'beside', 'besides', 'by', 'despite', 'down',
                 'during', 'for', 'from', 'in', 'inside', 'into', 'near', 'of',
                 'off', 'on', 'onto', 'over', 'through', 'to', 'toward',
                 'with', 'within', 'without', 'anything', 'everything',
                 'anyone', 'everyone', 'ones', 'such', 'it', 'itself',
                 'something', 'nothing', 'someone', 'the', 'some', 'this',
                 'that', 'every', 'all', 'both', 'one', 'first', 'other',
                 'next', 'many', 'much', 'more', 'most', 'several', 'no', 'a',
                 'an', 'any', 'each', 'no', 'half', 'twice', 'two', 'second',
                 'another', 'last', 'few', 'little', 'less', 'least', 'own',
                 'and', 'but', 'after', 'when', 'as', 'because', 'if', 'what',
                 'where', 'which', 'how', 'than', 'or', 'so', 'before', 'since',
                 'while', 'although', 'though', 'who', 'whose', 'can', 'may',
                 'will', 'shall', 'could', 'be', 'do', 'have', 'might', 'would',
                 'should', 'must', 'here', 'there', 'now', 'then', 'always',
                 'never', 'sometimes', 'usually', 'often', 'therefore',
                 'however', 'besides', 'moreover', 'though', 'otherwise',
                 'else', 'instead', 'anyway', 'incidentally', 'meanwhile']

def overlapcontext( synset, sentence ):
    gloss = set(PunktWordTokenizer().tokenize(synset.definition()))
    print "n"
    print synset.definition()
    print gloss
    print synset.definition().split()
    gloss = gloss.difference( functionwords )
    if isinstance(sentence, str):
        sentence = set(sentence.split(" "))
    elif isinstance(sentence, list):
        sentence = set(sentence)
    elif isinstance(sentence, set):
        pass
    else:
        return
    sentence = sentence.difference( functionwords )
    return len( gloss.intersection(sentence) )

def lesk( word, sentence ):
    bestsense = None
    maxoverlap = 0
    for sense in wordnet.synsets(word):
        overlap = overlapcontext(sense,sentence)
        for h in sense.hyponyms():
            overlap += overlapcontext( h, sentence )
        if overlap > maxoverlap:
                maxoverlap = overlap
                bestsense = sense
    return bestsense


print lesk("owl","owl is a bird")
