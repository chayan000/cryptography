import rsa
import codecs

with open("bob_pubkey.txt","rb") as f:
    public_key=rsa.PublicKey.load_pkcs1(f.read())
data= input("enter the key\n")
message = codecs.encode(data)
encrypted_message=rsa.encrypt(message,public_key)
print("This is the encrypted message, copy the message written inside quotes \n")
print(encrypted_message)