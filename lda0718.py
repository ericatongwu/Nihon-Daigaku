
#generate term matrix
import gensim
from gensim import corpora
matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# doc_clean is the noun file

lda = gensim.models.ldamodel.LdaModel
# creating the object for LDA model using gensim libaray

ldamodel = Lda(matrix, num_topics = 3,id2word = dictionary, passes=50)
# run the LDA model on matrix, parameters could be changed

print(ldamodel.print_topics(num_topics=3, num_words=3))

