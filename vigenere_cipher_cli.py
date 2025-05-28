class EncryptionDecryption:
    def __init__(self):
        self.all_ascii_characters = ''.join([chr(i) for i in range(32, 127)])

        self.all_ascii_characters_table = []
        self.corresponding_ascii_indexes = {}
        for i in range(len(self.all_ascii_characters)):
            copy = self.all_ascii_characters[i:] + self.all_ascii_characters[:i]
            self.all_ascii_characters_table.append(copy)
            self.corresponding_ascii_indexes[self.all_ascii_characters[i]] = i

    def encryption_function(self, text, key):
        new_key = ''
        index = 0
        while len(new_key) < len(text):
            new_key += key[index]
            index += 1
            if index >= len(key):
                index = 0
        encoded_word = ''
        for i in range(len(text)):
            if text[i] in self.all_ascii_characters and new_key[i] in self.all_ascii_characters:
                key_index = self.corresponding_ascii_indexes[new_key[i]]
                text_index = self.corresponding_ascii_indexes[text[i]]
                encoded_word += self.all_ascii_characters_table[key_index][text_index]
            else:
                encoded_word += text[i]
        return encoded_word

    def decryption_function(self, text, key):
        new_key = ''
        index = 0
        while len(new_key) < len(text):
            new_key += key[index]
            index += 1
            if index >= len(key):
                index = 0
        decoded_word = ''
        for i in range(len(text)):
            if text[i] in self.all_ascii_characters and new_key[i] in self.all_ascii_characters:
                key_index = self.corresponding_ascii_indexes[new_key[i]]
                row = self.all_ascii_characters_table[key_index]
                col_index = row.index(text[i])
                decoded_word += self.all_ascii_characters[col_index]
            else:
                decoded_word += text[i]
        return decoded_word


    def main(self):
        while True:
            choice = input('Enter do you want to quit? (yes/no): ').strip().lower()
            if choice == 'yes':
                break
            elif choice == 'no':
                choose = input('"e" for encryption and "d" for decryption: ').strip().lower()

                
                if choose == 'e':
                    plain_text = input('Enter messege you want to encrypt: ')

                    key = input('Enter the key: ')
                    print(f"Your encrypted messege is :{self.encryption_function(plain_text,key)}")

                elif choose == 'd':
                    encrypted_word = input('Enter Encrypted word: ')
                    key = input('Enter the key: ')
                    print(f'Your plain text messege is : {self.decryption_function(encrypted_word,key)}')
                else:
                    print('Invalid option')
            else:
                print('Invalid option')

if __name__ == "__main__":
    ed = EncryptionDecryption()
    ed.main()