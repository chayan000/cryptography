from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import hashlib

def pad_key(input_key):
    # Using SHA-256 to derive a fixed-length key
    hashed_key = hashlib.sha256(input_key.encode('utf-8')).digest()
    
    # Take the first 8 bytes of the hashed key
    truncated_key = hashed_key[:8]
    
    return truncated_key

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext,DES.block_size))
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_text.decode('utf-8')

def write_to_fileencrypted(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)
def write_to_filedecrypted(filename, data):
    with open(filename, 'w') as file:
        file.write(data)        

def read_from_file(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data

def menu():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        input_file = input("Enter the name of the file to encrypt: ")
        output_file = input("Enter the name of the encrypted file: ")
        input_key = input("Enter the encryption key: ")

        key = pad_key(input_key)
        plaintext = read_from_file(input_file)
        ciphertext = des_encrypt(plaintext, key)
        write_to_fileencrypted(output_file, ciphertext)

        print(f'File encrypted using DES and saved to {output_file}')

    elif choice == '2':
        input_file = input("Enter the name of the file to decrypt: ")
        output_file = input("Enter the name of the decrypted file: ")
        input_key = input("Enter the decryption key: ")

        key = pad_key(input_key)
        encrypted_data = read_from_file(input_file)
        decrypted_text = des_decrypt(encrypted_data, key)
        write_to_filedecrypted(output_file, decrypted_text)

        print(f'Decrypted file saved to {output_file}')

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
