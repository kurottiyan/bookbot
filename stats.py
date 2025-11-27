import sys

def get_num_words(text):
        number_of_words = len(text.split())
        return number_of_words

def count_chars(text):
	characters = list(text.lower())
	char_count = {" ": 0 }
	for char in characters:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def book_report(book_path, word_count, char_counts):
	print(book_path)
	print(word_count)
	sorted_by_value_desc = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
	if isinstance(sorted_by_value_desc, dict):
    		for key, value in sorted_by_value_desc.items():
        		print(f"{key}: {value}")
	else:
    		print("Error: Provided data is not a dictionary.")


