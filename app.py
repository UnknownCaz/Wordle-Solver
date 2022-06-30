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
#TODO add multiple letter compat
def remove_by_letters(words: list, out_letters, in_letters, print_words=False):
    buff = []
    for word in words:
        has_out = not any(list(out_letters) in _ for _ in list(word))
        has_in = any(in_letters in _ for _ in word)
        if has_out and has_in:
            buff.append(word)
        if print_words:
            print(f"Word: {word}, Out:{has_out}, In:{has_in}")
    print(buff)
    return buff
word_list = n_letter_words(words.words(), length=5)
word_list = remove_by_letters(word_list,"ur","y",print_words=True)

for i in word_list: print(i)