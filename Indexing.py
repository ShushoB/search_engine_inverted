import Texts

class Index:
    normal_words = []
    indexed_words = list(Texts.Text.txt1.keys())
    indexed_words.append(Texts.Text.txt2.keys())
    with open('/Users/picsartacademy/Downloads/words_alpha.txt', 'r') as file:
        for line in file:
            for word in line.split():
                normal_words.append(word)

    def search_normalize(self):
        low = 0
        high = len(Index.normal_words) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_val = Index.normal_words[mid]
            for target in Index.indexed_words:
                if mid_val == target:
                    return target
                elif mid_val < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return "Not found"






