from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def read_from_file(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data

input_file=input("enter the file name you want to sign\n")
message = read_from_file(input_file)
digest = SHA256.new()
digest.update(message)


private_key = False
with open ("alice_privkey.txt", "r") as myfile:
    private_key = RSA.importKey(myfile.read())

# Load private key and sign message
signer = PKCS1_v1_5.new(private_key)
sig = signer.sign(digest)
print("This is the signature\n")
print(sig)