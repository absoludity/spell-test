#!/usr/bin/python
import argparse
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


def test_words(sentences, stats, num_words=0):
    print("Type the missing word for each sentence, or 'exit' when "
        "you've had enough:")

    wrong_words = []

    count = 0
    for word in order_words(sentences.keys(), stats):
        if num_words and count == num_words:
            return wrong_words

        sentence = sentences[word]
        print(sentence)
        typed_word = raw_input()

        if typed_word == "exit":
            return wrong_words

        word_stat = stats.get(word, dict(DEFAULT_STATISTIC))
        word_stat["total_count"] += 1

        if typed_word == word:
            print("Correct!")
            word_stat["right_count"] += 1
        else:
            print("Needs practise, the correct spelling is '{}'.".format(word))
            wrong_words.append(word)

        stats[word] = word_stat
        count += 1
        print("You've spelled '{}' correctly {} times out of {}.".format(
            word, word_stat["right_count"], word_stat["total_count"]))


        print("")

    return wrong_words


sentences = read_sentences("words.txt")

stats = read_stats()

parser = argparse.ArgumentParser(description="Test your spelling!")
parser.add_argument('num_words', type=int, default=10)

args = parser.parse_args()

wrong_words = []

try:
    wrong_words = test_words(sentences, stats, num_words=args.num_words)
finally:
    write_stats(stats)
    if wrong_words:
        print("Here are the words you need to work on from this game:")
        for word in wrong_words:
            print("{word}: {sentence}".format(word=word, sentence=sentences[word]))
    else:
        print("Wow - no mistakes! Well done :D\n")

    print("Thanks for playing!")
