testword = "young"

def remove_by_letters(words: list, out_letters, in_letters, print_words=False):
    for word in words:
        has_out = [[i for i in list(out_letters) if i in word] for j in list(word) if j in word]
        has_in = any(in_letters in _ for _ in word)
        print(f"Word: {word}, Out:{has_out}, In:{has_in}")

remove_by_letters([testword],"uo", "y")