class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabets = alphabet
        self.alphabet_table = []
        self.corresponding_alphabet_indexes = {}
        for i in range(len(self.alphabets)):
            copy = self.alphabets[i:] + self.alphabets[:i]
            self.alphabet_table.append(copy)
            self.corresponding_alphabet_indexes[self.alphabets[i]] = i
    def encode(self, text):
        new_key = ''
        index = 0
        while len(new_key) < len(text):
            new_key += self.key[index]
            index += 1
            if index >= len(self.key):
                index = 0
        encoded_word = ''
        for i in range(len(text)):
            if text[i] in self.alphabets and new_key[i] in self.alphabets:
                text_index = self.corresponding_alphabet_indexes.get(text[i])
                key_index = self.corresponding_alphabet_indexes.get(new_key[i])
                encoded_word += self.alphabet_table[text_index][key_index]
            else:
                encoded_word += text[i]
        return encoded_word

    def decode(self, text):
        new_key = ''
        index = 0
        while len(new_key) < len(text):
            new_key += self.key[index]
            index += 1
            if index >= len(self.key):
                index = 0
        decoded_word = ''
        for i in range(len(text)):
            if text[i] in self.alphabets and new_key[i] in self.alphabets:
                key_index = self.corresponding_alphabet_indexes.get(new_key[i])
                word_index = self.alphabet_table[key_index].index(text[i])
                decoded_word += self.alphabets[word_index]
            else:
                decoded_word += text[i]
        return decoded_word