import Texts
import Hashing
import LinkedList


class InvertedIndex:
    inverted_indexing = {}
    def __init__(self):
        path_1 = '/Users/picsartacademy/Downloads/1.txt'
        path_2 = '/Users/picsartacademy/Downloads/2.txt'
        text_instance1 = Texts.Text(path_1)
        text_instance2 = Texts.Text(path_2)

        for key in text_instance1.txt1.keys():
            hashed_key = Hashing.HashTable.hash_function(key)
            if hashed_key not in InvertedIndex.inverted_indexing:
                InvertedIndex.inverted_indexing[hashed_key] = LinkedList.LinkedList()
            sub_list = InvertedIndex.inverted_indexing[hashed_key]
            sub_list.append('1.txt')

        for key in text_instance2.txt2.keys():
            hashed_key = Hashing.HashTable.hash_function(key)
            if hashed_key not in InvertedIndex.inverted_indexing:
                InvertedIndex.inverted_indexing[hashed_key] = LinkedList.LinkedList()
            sub_list = InvertedIndex.inverted_indexing[hashed_key]
            sub_list.append('2.txt')

    def inverted_search(self, word):
        hashed_word = Hashing.HashTable.hash_function(word)
        if hashed_word in InvertedIndex.inverted_indexing:
            sub_list = InvertedIndex.inverted_indexing[hashed_word]
            return ', '.join(sub_list.get_filenames())
        else:
            return "Not found"
