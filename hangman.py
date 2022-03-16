import random


def get_word(wordfile="/usr/share/dict/words"):
    good_words = []
    with open(wordfile) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) >= 5:
                good_words.append(i)
    return random.choice(good_words)


def mask_word(secret_word, guesses):
    word = []
    for i in secret_word:
        if i in guesses:
            word.append(i)
        else:
            word.append("-")
    return "".join(word)


def create_status(secret_word, guesses, remaining_turns):
    masked_word = mask_word(secret_word, guesses)
    guesses = " ".join(guesses)
    return f"""Word: {masked_word}
    Guesses: {guesses}
    Remaining turns : {remaining_turns}
    """
