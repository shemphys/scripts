Hi, this is a little script to cypher the archives of a given folder.

# Security concerns
Having access to this code is not really a security problem.
This script uses a process called Password-Base Key Derivation Function (PBKDF) to generate the cyphering key.
This process needs the salt and the password to decypher. Knowing one but not the other will result in a lot of work to get to the files.
The PBKDF process is deliberately slow to difficult brute force attacks.

## About salt.txt
The term "salt" comes from the analogy of real-life salt, which is added to food to enhance or alter taste. In criptography, it alters the hash of a password or message.
It's not meant to be secret, unlike a password or a cryptographyc key.
Its main purpose is to prevent attacks that use precomputed tables of hash values, like rainbow table attacks, by ensuring that each user's password is hashed in a unique way.

In this case it is generated using ```os.urandom(16)``` which generates (n) random bytes (16 bytes, 128 bits, 256 combinations).
Having a previously generated salt won't lead you to future salts.
Even if the attacker would have the password and a previous salt, the total of possible salts is 256^16, or about 3.4 x 10^38. To put it in perspective, even if an attacker could generate a billion (10^9) salts per second, it would take them over a billion billion billion (10^27) years to generate all possible salts (much longer than the current age of the universe xD)
The attacker would also need to know the exact time when each salt was generated to associate it with a particular has or encrypted data, wich is typically not feasible.
So, creating a dictionary is not practical or feasible to do so.

### Sensitive material
- salt.txt
- password

# Steps
## Cyphering:
1. go into cypher.py and change ```folder_path``` and ```output_folder``` to your folder's path.
Remember: python does not allow the use of single '\', so you have these three options:
- double backslash: ```\\```
- single slash: ```/```
- use raw string (just add 'r' before): ```r"path\to\folder"```

2. go into cypher folder in the terminal or shell:
```
py cypher.py
```
Then type the password (no restrictions, up to you).

After this step, you should see the output_folder where you wanted it to be if it didnt exist yet.
Also, ```salt.txt``` should appear next to cypher.py

## Decyphering
1. go into decypher.py and change ```folder_path``` and ```output_folder``` to your folder's path.
(same rules as before with slashes)
Also, if output_folder doesn't exist it'll be created.

Aaaaaaaaaaaaaaand that it's pretty much all, cuz salt.txt will be automatically taken by the script so, enjoy.
