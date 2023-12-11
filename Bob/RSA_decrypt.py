import rsa

with open("bob_privkey.txt","rb") as f:
    private_key=rsa.PrivateKey.load_pkcs1(f.read())

#enter the encrypted key here inside ""
message = b""

decrypted_message=rsa.decrypt(message,private_key)
print("copy the decrypted key\n")
print(decrypted_message)