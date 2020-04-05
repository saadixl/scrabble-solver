import json
import itertools

print("Insert the scrabble you want to solve: ")
scrabble = str(input()).lower()
possible_solutions = []

t=list(itertools.permutations(scrabble,len(scrabble)))
for i in range(0,len(t)):
    possible_solutions.append(''.join(t[i]))

with open('./en_dictionary.json') as dictionary_json:
	dictionary = json.load(dictionary_json)
	for ps in possible_solutions:
		if ps in dictionary.keys():
			print("{} is a valid word!".format(ps))