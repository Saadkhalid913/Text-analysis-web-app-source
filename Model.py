import pickle 
import tensorflow as tf 

print(tf.__version__)
from tensorflow.keras.models import Sequential 
import re
import numpy as np 
import nltk
from nltk.stem import wordnet, WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download("wordnet")
nltk.download("stopwords")

emotions = ["anger", "fear", "joy", "love", "sadness", "surprise"]


def GetStopwords():
  words = stopwords.words("english")
  words.remove("not")
  return words

EnglishStopwords = GetStopwords()
tokenizer = None 

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.loads(f.read())

num_words = len(tokenizer.index_word) + 1

def CleanFeatures(features):
  '''
    takes 2D numpy array of text data and 
    removes stopwords, non-alphanumeric characters,
    trailing whitespaces, and applies lemmatization 
  '''

  lemma = WordNetLemmatizer()
  sentences = features.flatten()
  cleaned = []
  for sentence in sentences:
      sentence = re.sub("[^a-zA-Z]", " ", sentence)
      sentence = sentence.lower()
      sentence = sentence.split()
      sentence = [lemma.lemmatize(word) for word in sentence if word not in set(EnglishStopwords)]
      sentence = " ".join(sentence)
      cleaned.append(sentence)

  
  return cleaned 

def TokenizeTestData(testData, tokenizerObject):
  '''
    testData: 1D array of sentences
    returns 2D array of
  '''
  sequences = tokenizerObject.texts_to_sequences(testData)
  return tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen = 150, dtype='int32')


@tf.autograph.experimental.do_not_convert
def CreateModel():
  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Embedding(num_words, 480, input_length=150))
  model.add(tf.keras.layers.Flatten())
  model.add(tf.keras.layers.Dense(units = 128, activation="relu"))
  model.add(tf.keras.layers.Dropout(rate = 0.15))
  model.add(tf.keras.layers.Dense(units = 64, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 6, activation="softmax"))
  model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])
  return model


@tf.autograph.experimental.do_not_convert
def CreateMinifiedModel():
  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Embedding(num_words, 240, input_length=150))
  model.add(tf.keras.layers.Flatten())
  model.add(tf.keras.layers.Dense(units = 64, activation="relu"))
  model.add(tf.keras.layers.Dropout(rate = 0.15))
  model.add(tf.keras.layers.Dense(units = 48, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 6, activation="softmax"))
  model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])
  return model

model = CreateMinifiedModel()
model.load_weights("test/test")
  




def replace_not_alphabetical_chars(s: str):
  return re.sub("[^a-zA-Z]", " ", s)
def SplitSentence(s: str):
  s = s.lower()
  s = s.split()
  return s 

def softmax(x):

    y = np.exp(x - np.max(x))
    f_x = y / np.sum(np.exp(x))
    return f_x

def MakePred(s):
  s = CleanFeatures(np.array([[s]]))
  s = TokenizeTestData(s, tokenizer)
  all_sentence_preds = model.predict(s)[0]
  result = list(map(float, all_sentence_preds))
  final = [{"name": emotions[i], "percentage": result[i]} for i in range(6)]
  return final

if __name__ == "__main__":
  for sent in MakePred("this was a pretty bad model. i felt that this wont help me make a good replicate"):
    print(sent)





