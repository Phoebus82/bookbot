import sys
def get_book_text(file_path):
	with open(file_path) as fi:
		file_contents = fi.read()
	return file_contents

def main():
	print(get_book_text("books/frankenstein.txt"))
#main()
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
from stats import counter
from stats import letr_counter
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
counter(get_book_text(f"{sys.argv[1]}"))

letr_counter(get_book_text(f"{sys.argv[1]}"))
print("============= END ===============")

