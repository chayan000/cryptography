from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def read_from_file(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data

input_file=input("enter the file name you want to verify\n")
message = read_from_file(input_file)
digest = SHA256.new()
digest.update(message)

# Read shared key from file
public_key = False
with open ("alice_pubkey.txt", "r") as myfile:
    public_key = RSA.importKey(myfile.read())

#enter the signature here that alice has given
sig = b''


verifier = PKCS1_v1_5.new(public_key)
verified = verifier.verify(digest, sig)
if(verified):
    print("file is verified and found same")
else:
    print("file is not same")    