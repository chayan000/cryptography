Name: Chayan Pathak    Roll: 12310630

There are two folders 1.Alice 2.Bob all the codes related to Alice is inside Alice folder and
all the codes related to Bob is inside Bob folder.

goal:
1)encrypt a file(F) present at Alice folder using DES algorithm(F').
2)encrypt the key(K) used in the upper step using RSA algorithm(K').
3)digitally sign the file(sig).
4)send the encrypted file(F'), encrypted key(K') and the signature(sig) to Bob.
5)decrypt the key(K') using RSA algorithm(K).
6)decrypt the encrypted file(F') using DES algorithm(F).
7)verify the digital signature(sig)

Instructions to execute:

1)run des.py in Alice folder
2)choose option 1
3)enter the file name(F): hello.txt
4)enter the encrypted file name(F'): helloe.txt
5)enter the key(K): iitbhilai
6)copy encrypted file(F') to Bob folder: helloe.txt
7)run RSA_encrypt.py in Alice folder
8)enter the key(K): iitbhilai
9)copy the encrypted key(K') written inside b" ".
10)paste the encrypted key(K') at specified space in Bob folder's RSA_decrypt.py
11)run RSA_decrypt.py and copy the key(K): iitbhilai
12)run des.py in Bob folder
13)choose option 2
14)enter the file name(F'): helloe.txt
15)enter the decrypted file name(F): hellod.txt
16)enter the key(K): iitbhilai
17)in Alice folder run sign.py
18)enter the file name(F): hello.txt
19)copy the signature(sig) inside b' '.
20)run verify.py in Bob folder
21)enter the filename(F): hellod.txt
22)result will be printed
