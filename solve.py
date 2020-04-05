import json
import itertools

def lexi_sort(word):
	chars = [char for char in word]
	chars.sort()
	return ''.join(chars)

print("Insert the scrabble you want to solve: ")
scrabble = str(input()).lower()
# Sorting the inserted word lexicographically
sorted = lexi_sort(scrabble)

# Opening the indexed dictionary
with open('./indexed_dictionary_en.json') as dictionary_json:
	dictionary = json.load(dictionary_json)
	# If the sorted word is available as a key
	if sorted in dictionary.keys():
		# There is possible solution
		possible_solutions = dictionary[sorted]
		len = len(possible_solutions)
		# Print the possible solutions
		print("I've found {} possible solutions!".format(len))
		for i in range(len):
			print("{}) {}".format(i + 1, possible_solutions[i]))
	else:
		print("It's impossible to make a word with {}!".format(scrabble))