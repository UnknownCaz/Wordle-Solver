testword = "sltricky"

def remove_by_letters(words: list, out_letters, in_letters, print_words=False):
    for word in words:
        has_out = not any([[i for i in list(out_letters) if i in word] for _ in list(word)])
        has_in = sorted("".join([j for j in word if j in in_letters])) == sorted(in_letters)
        print(f"Word: {word}, Out:{has_out}, In:{has_in}")

remove_by_letters([testword],"uo", "il")