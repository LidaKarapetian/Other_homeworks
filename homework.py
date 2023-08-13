#!/usr/bin/python

import os.path

def check_file_existence(filename):
    if not os.path.isfile(filename):
        print("Your files does not exists: %s. Please check" %filename)
        return False
    return True

def get_data(filename):
    with open(filename, "r") as file:
        return file.read()

def get_symbols_count(data):
    dict = {}
    for el in data:
        if el in dict:
            dict[el] += 1
        else:
            dict[el] = 1
    return dict

def get_logest_word(data):
    data = data.split()
    longest = max(data, key = len)
    return longest

def get_text_with_words_reversed(data):
    ml = data.split()
    for i in range(len(ml)):
        ml[i] = ml[i][::-1]
    return " ".join(ml)

def get_sentences_count(data):
    sentence_endings = ['.', '?', '!']
    sentence_count = 0
    for i in data:
        if i in sentence_endings:
            sentence_count += 1
    return sentence_count

def write_into_file(filename, result):
    with open(filename, "w") as file:
        for i in result:
            file.write(i + '\n')

def create_file(filename):
	f = open(filename, "w")
	f.close()

def main():
    filename = "data.txt"
    if not check_file_existence(filename):
        exit()
    data = get_data(filename)
    symbols_count = "Symbols count: " + str(get_symbols_count(data))
    longest_word = "The longest word: " + get_logest_word(data)
    sentences_count  = "Sentences count: " + str(get_sentences_count(data))
    reversed_data = "Text with words reversed: " + get_text_with_words_reversed(data)
    result = [
        longest_word,
        symbols_count,
        sentences_count,
        reversed_data
    ]
    if not check_file_existence(filename):
        create_file("result.txt")
    write_into_file("result.txt", result)
    
main()
    