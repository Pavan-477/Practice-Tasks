#Write a Python program that accepts a word from the user and reverse it.
seq=input("Enter a string to reverse :")
reversed_seq = ''
for i in seq:
    reversed_seq = i + reversed_seq
print(reversed_seq)