from numpy import array
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from tensorflow import keras
import numpy as np
import pickle

model = keras.models.load_model('english_keras_prediction.h5')
tokenizer = pickle.load(open("tokenizer_english.pickle", 'rb'))

def generate_seq(seed_text, n_words):
	max_length = 5
	in_text = seed_text
    # generate a fixed number of words
	for _ in range(n_words):
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		# pre-pad sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=max_length, padding='pre')
		preds = model.predict(encoded)
		yhat = np.argmax(preds, axis = -1)
		# print(preds, yhat)
		# map predicted word index to word
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		# append to input
		in_text += ' ' + out_word
	return [in_text]