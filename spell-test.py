#!/usr/bin/python
import json
import os

from utils import (
    order_words,
    DEFAULT_STATISTIC,
)


def read_sentences(filepath):
    sentences = {}

    with open(filepath, "r") as file_handle:
        for line in file_handle.readlines():
            word, _, sentence = line.partition(" ")
            sentences[word] = sentence.strip()

    return sentences


def write_stats(stats, filepath="my_spelling_stats.json"):
    with open(filepath, "w+") as file_handle:
        json.dump(stats, file_handle)


def read_stats(filepath="my_spelling_stats.json"):
    if not os.path.exists(filepath):
        return {}

    with open(filepath, 'r') as file_handle:
        return json.load(file_handle)


def test_words(sentences, stats):
    print("Type the missing word for each sentence, or 'exit' when "
        "you've had enough:")


    for word in order_words(sentences.keys(), stats):
        sentence = sentences[word]
        print(sentence)
        typed_word = raw_input()

        if typed_word == "exit":
            exit(0)

        word_stat = stats.get(word, dict(DEFAULT_STATISTIC))
        word_stat["total_count"] += 1

        if typed_word == word:
            print("Correct!")
            word_stat["right_count"] += 1
        else:
            print("Needs practise, the correct spelling is '{}'.".format(word))

        stats[word] = word_stat
        print("You've spelled '{}' correctly {} times out of {}.".format(
            word, word_stat["right_count"], word_stat["total_count"]))


        print("")


sentences = read_sentences("words.txt")

stats = read_stats()


try:
    test_words(sentences, stats)
finally:
    print("Saving your spelling statistics... thanks for playing!")
    write_stats(stats)
