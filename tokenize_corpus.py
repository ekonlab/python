__author__ = 'albertogonzalez'

# http://www.lucypark.kr/courses/2015-ba/text-mining.html


from nltk.corpus import gutenberg
from nltk import regexp_tokenize
import nltk


# donwload corpus (just the first time!!)
nltk.download('gutenberg')
nltk.download('maxent_treebank_pos_tagger')
nltk.download("reuters")

# View
files_en = gutenberg.fileids()
doc_en = gutenberg.open('austen-emma.txt').read()

# Tokenize
pattern = r'''(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\. | [][.,;"'?():-_`]'''
tokens_en = regexp_tokenize(doc_en, pattern)
en = nltk.Text(tokens_en)

print(len(en.tokens))
print(len(set(en.tokens)))

en.vocab()
en.plot(50)


# Count
en.count('Emma')
en.dispersion_plot(['Emma', 'Frank', 'Jane'])

# Concordance
en.concordance('Emma', lines=5)

# Find similar words
en.similar('Emma')
en.similar('Frank')

# Collocations (not working!!!)
en.collocations()


# POS tagging
tokens = "The little yellow dog barked at the Persian cat".split()
tags_en = nltk.pos_tag(tokens)
print tags_en

# Noun Phrase chunking
parser_en = nltk.RegexpParser("NP: {<DT>?<JJ>?<NN.*>*}")
chunks_en = parser_en.parse(tags_en)
chunks_en.draw()


#############################################################

# TOPIC MODELING

# 1.- PREPROCESSING

# LOAD DOCUMENTS
from nltk.corpus import reuters
docs_en = [reuters.words(i) for i in reuters.fileids()]

# TOKENIZE
texts_en = docs_en
print(texts_en[0])

# ENCODE TOKENS TO INTEGERS
from gensim import corpora
dictionary_en = corpora.Dictionary(texts_en)
dictionary_en.save('en.dict')  # save dictionary to file for future use

# CALCULATE TF-IDF
from gensim import models
tf_en = [dictionary_en.doc2bow(text) for text in texts_en]
tfidf_model_en = models.TfidfModel(tf_en)
tfidf_en = tfidf_model_en[tf_en]
corpora.MmCorpus.serialize('en.mm', tfidf_en) # save corpus to file for future use

# print first 10 elements of first document's tf-idf vector
print(tfidf_en.corpus[0][:10])
# print top 10 elements of first document's tf-idf vector
print(sorted(tfidf_en.corpus[0], key=lambda x: x[1], reverse=True)[:10])
# print token of most frequent element
print(dictionary_en.get(9))

# 2.- TRAIN TOPIC MODELS

# LSI
ntopics, nwords = 3, 5
lsi_en = models.lsimodel.LsiModel(tfidf_en, id2word=dictionary_en, num_topics=ntopics)
print(lsi_en.print_topics(num_topics=ntopics, num_words=nwords))


# LDA
import numpy as np; np.random.seed(42)  # optional
lda_en = models.ldamodel.LdaModel(tfidf_en, id2word=dictionary_en, num_topics=ntopics)
print(lda_en.print_topics(num_topics=ntopics, num_words=nwords))


# HDP
import numpy as np; np.random.seed(42)  # optional
hdp_en = models.hdpmodel.HdpModel(tfidf_en, id2word=dictionary_en)
print(hdp_en.print_topics(topics=ntopics, topn=nwords))


# 3.- SCORING DOCUMENTS

bow = tfidf_model_en[dictionary_en.doc2bow(texts_en[0])]
sorted(lsi_en[bow], key=lambda x: x[1], reverse=True)
sorted(lda_en[bow], key=lambda x: x[1], reverse=True)
sorted(hdp_en[bow], key=lambda x: x[1], reverse=True)

bow = tfidf_model_en[dictionary_en.doc2bow(texts_en[1])]
sorted(lsi_en[bow], key=lambda x: x[1], reverse=True)
sorted(lda_en[bow], key=lambda x: x[1], reverse=True)
sorted(hdp_en[bow], key=lambda x: x[1], reverse=True)


# WORD EMBEDDING
# word2vec toy problem
from nltk.corpus import reuters
docs_en = [reuters.words(i) for i in reuters.fileids()]
texts_en = docs_en # because we loaded tokenized documents in step 1

from gensim.models import word2vec
wv_model_en = word2vec.Word2Vec(texts_en)
wv_model_en.init_sims(replace=True)
wv_model_en.save('en_word2vec.model')

wv_model_en.most_similar('president')
wv_model_en.most_similar('secretary')
wv_model_en.most_similar('country')


#############################################################




