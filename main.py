from Texts import Text
from Hashing import HashTable
from LinkedList import LinkedList
from Indexing import Index
from Searching import Search
from Inverted_Index import InvertedIndex

path_1 = '/Users/picsartacademy/Downloads/1.txt'
path_2 = '/Users/picsartacademy/Downloads/2.txt'
text_instance1 = Text(path_1)
text_instance2 = Text(path_2)


indexing = Index()
word = "in"
print(f"Searching the word: '{word}' using normal index")
searching = Search()
searching.search(word)

print(f"Searching the word: '{word}' using inverted index")

inverted_indexing = InvertedIndex()
print(inverted_indexing.inverted_search(word))



