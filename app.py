from flask import Flask
import nltk
from nltk.corpus import words

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def n_letter_words(words, length=5):
    buff = []
    for word in words:
        if len(word) == length:
            buff.append(word)
    return buff

def remove_by_letters(words: list, out_letters, in_letters, print_words=False):
    buff = []
    for word in words:
        has_out = not any([[i for i in list(out_letters) if i in word] for j in list(word) if j in word])
        has_in = sorted("".join([j for j in word if j in in_letters])) == sorted(in_letters)
        if print_words:
            print(f"Word: {word}, Out:{has_out}, In:{has_in}")
        if has_out and has_in:
            buff.append(word)
    return buff
word_list = n_letter_words(words.words(), length=5)
word_list = remove_by_letters(word_list,"gmfiestounpicky","arl",print_words=False)

for i in word_list: print(i, end=" ")