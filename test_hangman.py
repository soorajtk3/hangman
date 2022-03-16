import os

import hangman


def test_get_word_no_punctuation():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_get_word_no_proper_nouns():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("Noufal\n")
        f.write("John\n")
        f.write("Simon\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_get_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_mask_word_single():
    secret_word = "elephant"
    guessed = ["l"]
    ret = hangman.mask_word(secret_word, guessed)
    assert ret == "-l------"


def test_mask_bad_guess():
    secret_word = "elephant"
    guessed = ["x"]
    ret = hangman.mask_word(secret_word, guessed)
    assert ret == "--------"


def test_mask_good_guess():
    secret_word = "hangman"
    guesses = ["m"]
    ret = hangman.mask_word(secret_word, guesses)
    assert ret == "----m--"


def test_mask_guess_multiple():
    secret_word = "hangman"
    guesses = ["n"]
    ret = hangman.mask_word(secret_word, guesses)
    assert ret == "--n---n"


def test_mask_good_guess_mix():
    secret_word = "hangman"
    guesses = ["g", "q", "m"]
    ret = hangman.mask_word(secret_word, guesses)
    assert ret == "---gm--"


def test_create_status_normal():
    secret_word = "hospital"
    guesses = ["n", "x", "h"]
    remaining_turns = 6
    assert hangman.create_status(secret_word, guesses, remaining_turns) == """Word: h-------
    Guesses: n x h
    Remaining turns : 6
    """


def test_create_status_not_guessed():
    secret_word = "hospital"
    guesses = []
    remaining_turns = 8
    status = hangman.create_status(secret_word, guesses, remaining_turns)
    assert status == """Word: --------
    Guesses: 
    Remaining turns : 8
    """


def test_play_round_correct_guess():
    secret_word = "hospital"
    guesses = []
    remaining_turns = 8
    new_guess = "a"
    remaining_turns, repeat, finished = hangman.play_round(
        secret_word, guesses, new_guess, remaining_turns)
    assert guesses == ["a"]
    assert remaining_turns == 8
    assert repeat == False
    assert finished == False


def test_play_round_correct_wrong():
    secret_word = "hospital"
    guesses = ["a"]
    remaining_turns = 7
    new_guess = "q"
    remaining_turns, repeat, finished = hangman.play_round(
        secret_word, guesses, new_guess, remaining_turns)
    assert guesses == ["a", "q"]
    assert remaining_turns == 6
    assert repeat == False
    assert finished == False


def test_play_round_correct_repeat():
    secret_word = "hospital"
    guesses = ["a"]
    remaining_turns = 8
    guess = "a"
    remaining_turns, repeat, finished = hangman.play_round(
        secret_word, guesses, guess, remaining_turns)
    assert guesses == ["a"]
    assert remaining_turns == 8
    assert repeat == True
    assert finished == False


def test_play_round_correct_complete():
    secret_word = "hospital"
    guesses = ["h", "o", "s", "p", "i", "t", "a"]
    remaining_turns = 8
    new_guess = "l"
    remaining_turns, repeat, finished = hangman.play_round(
        secret_word, guesses, new_guess, remaining_turns)

    assert finished == True
