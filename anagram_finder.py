#!/usr/local/bin/python

'''

anagram_finder.py

USAGE: python anagram_finder.py
OUTPUT: prints anagrams to console eg. abut, tabu, tuba, tuba

A program to find all of the anagrams in a dictionary file which there are at 
least 4 letters in the word and at least as many anagrams as there are letters.
Dictionary file is assumed to be at /usr/share/dict/words, modify
DICTIONARY_FILE to specify another location.

'''

from collections import defaultdict


# specify dictionary file here
DICTIONARY_FILE = '/usr/share/dict/words'


def main(dictionary_words=DICTIONARY_FILE):		
	with open(dictionary_words) as f:
		words = f.read().splitlines()
		
	# prepare to build defaultdict for each word and its anagrams
	anagram_word_list = defaultdict(list)

	# wordletters (keys) are sorted letters of each word
	# values are words with the same sorted letters
	for word in words:
		word = word.lower()
		wordletters = "".join(sorted(word))
		anagram_word_list[wordletters].append(word)

	# constraints for each word to be at least 4 letters
	# needs as many anagrams as there are letters as a minimum
	anagrams_list = []
	for wordletters, anagrams in anagram_word_list.items():
		if len(wordletters) >= 4:
			if len(anagrams) >= len(wordletters):
				anagrams_list.append(', '. join(anagrams))

	return anagrams_list

if __name__ == "__main__":
	output = main()
	for entries in output: 
		print entries