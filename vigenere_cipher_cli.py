class EncryptionDecryption:
    def __init__(self):
        self.ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.SHIFTED = ''
        for i in range(26):
            self.SHIFTED += self.ALPHABET[i:] + self.ALPHABET[:i] + "\n"
        self.SHIFTED = self.SHIFTED.split()
        
    def encryption_function(self,plain_text,key):
        new_key = ''
        index = 0
        plain_text = plain_text.replace(" ",'')

        while len(new_key) < len(plain_text):
            new_key += key[index]
            index += 1
            if index >= len(key):
                index = 0

        encrypted_word = ''
        index_char = []
        index_key = []

        for char in plain_text:
            index_char.append(ord(char) - 65)

        for char in new_key:
            index_key.append(ord(char) - 65)

        for i in range(len(plain_text)):
            encrypted_word += self.SHIFTED[index_char[i]][index_key[i]]

        return encrypted_word

    def decryption_function(self,enword,key):
        new_key = ''

        index = 0

        while len(new_key) < len(enword):
            new_key += key[index]
            index += 1
            if index >= len(key):
                index = 0

        plain_text = ''

        index_key = []


        for char in new_key:
            index_key.append(ord(char) - 65)

        for i in range(len(enword)):
                row = index_key[i]
                col = self.SHIFTED[row].index(enword[i])
                plain_text += chr(col + 65)                
                

        return plain_text

    def main(self):
        while True:
            choice = input('Enter do you want to quit? (yes/no): ').lower().replace(' ','')
            if choice == 'yes':
                break
            elif choice == 'no':
                choose = input('"e" for encryption and "d" for decryption: ').lower().replace(' ','')

                
                if choose == 'e':
                    plain_text = input('Enter messege you want to encrypt: ').upper().replace(' ','')

                    key = input('Enter the key: ').upper().replace(' ','')
                    print(f"Your encrypted word {self.encryption_function(plain_text,key)}.")

                elif choose == 'd':
                    encrypted_word = input('Enter Encrypted word: ').upper().replace(' ','')
                    key = input('Enter the key: ').upper().replace(' ','')
                    print(f'Your plain text messege is : {self.decryption_function(encrypted_word,key)}')
                else:
                    print('Invalid option')
            else:
                print('Invalid option')

if __name__ == "__main__":
    ed = EncryptionDecryption()
    ed.main()