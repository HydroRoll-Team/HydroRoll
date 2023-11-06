"""余弦相似度比较"""


import joblib
import jieba
import numpy as np

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class cosSim:
    def __init__(self, simple: list = [], test_data: list = []):
        self.simple = simple
        self.inputs = test_data
        self.texts = self.simple
        self.texts.extend(self.inputs)

    @property
    def corpuss(self):
        return [" ".join(jieba.cut(text)) for text in self.simple]
    
    @property
    def vocabulary(self):
        return self.getVocabulary(self.corpuss)

    @property
    def vectors(self):
        return self.getVectors(self.corpuss, self.vocabulary)
    
    @property
    def input_corpuss(self):
        return [" ".join(jieba.cut(text)) for text in self.inputs]
    
    @property
    def input_vocabulary(self):
        return self.getVocabulary(self.input_corpuss)
    
    @property
    def input_vector(self):
        return  self.getVectors(self.input_corpuss, self.input_vocabulary)
    
    def append(self, add_test_data: list = []):
        self.inputs.extend(add_test_data)
        
    @property
    def similarities(self):
        similarities = []
        corpuss = [" ".join(jieba.cut(text)) for text in self.texts]
        vocabulary = self.getVocabulary(corpuss)
        vector = self.getVectors(corpuss, vocabulary)
        for v in vector[len(self.texts)-1:]:
            sim = []
            for v1 in vector[:len(self.simple)+1]:
                sim.append(self.cos_sim(v1, v))
                print('sim', sim)
            similarities.append(max(sim))

        return similarities
    
    @staticmethod
    def cos_sim(vector_a, vector_b):
        """
        计算两个向量之间的余弦相似度
        :param vector_a: 向量 a 
        :param vector_b: 向量 b
        :return: sim
        """
        vector_a = np.array(vector_a).reshape(1, -1)
        vector_b = np.array(vector_b).reshape(1, -1)
        return cosine_similarity(vector_a, vector_b)[0][0]

    @staticmethod
    def getVocabulary(corpuss):
        vectorizer = CountVectorizer(max_features=500)
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(vectorizer.fit_transform(corpuss))
        words = vectorizer.get_feature_names_out()
        return words

    @staticmethod
    def getVectors(corpus, vocabulary):
        vectorizer = CountVectorizer(vocabulary=vocabulary)
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
        vectors = tfidf.toarray()
        return vectors

    def save(self, filename):
        joblib.dump(self, filename)

    @staticmethod
    def load(filename):
        return joblib.load(filename)
    
    def reload(self):
        self.texts = self.simple
        self.texts.extend(self.inputs)
        self.similarities