def counter(file_contents):
        count_list = file_contents.split()
        num_words = len(count_list)
        print(f"Found {num_words} total words")

def sort_on(items):
    return items["value"]	
def letr_counter(txt):
	lowered = txt.lower()
	all_eyes = 0
	letter_counter = {}
	for i in lowered:
		if i in letter_counter.keys():
			letter_counter[i] += 1
		else:
			letter_counter[i] = 1
	count_kv = []
	for k, v in letter_counter.items():
		my_dict= {}
		my_dict["key"] = k
		my_dict["value"] = v
		count_kv.append(my_dict)
	count_kv.sort(reverse=True, key=sort_on)
	for i in count_kv:
		if i["key"].isalpha() == True:
			print(f"{i["key"]}: {i["value"]}")
