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


def play_round(secret_word, guesses, new_guess, remaining_turns):
    if "-" not in mask_word(secret_word, guesses+[new_guess]):
        return remaining_turns, False, True
    if new_guess in guesses:
        return remaining_turns, True, False
    if new_guess in secret_word:
        guesses.append(new_guess)
        return remaining_turns, False, False
    if new_guess not in secret_word:
        guesses.append(new_guess)
        return remaining_turns-1, False, False
