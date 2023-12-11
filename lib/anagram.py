class Anagram:
    def __init__(self, word):
        self.anagram = word

    def match(self, word_list):
        anagram_matches = [name for name in word_list if sorted(self.anagram) == sorted(name)]
        return anagram_matches
