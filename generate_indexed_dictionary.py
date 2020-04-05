import json

indexed_dict = {}

def lexi_sort(word):
	chars = [char for char in word]
	chars.sort()
	return ''.join(chars)

with open('./unindexed_dictionary_en.json') as dictionary_json:
	dictionary = json.load(dictionary_json)
	words = dictionary.keys()
	for word in words:
		sorted = lexi_sort(word)
		if sorted in indexed_dict.keys():
			indexed_dict[sorted].append(word)
		else:
			indexed_dict[sorted] = [word]
	with open('./indexed_dictionary_en.json', 'w') as outfile:
		json.dump(indexed_dict, outfile)
		print("All done")