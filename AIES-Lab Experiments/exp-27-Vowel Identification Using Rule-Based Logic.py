sentence=input("Enter a sentence: ")

vowels="AEIOUaeiou"

for ch in sentence:

    if ch.isalpha():

        if ch in vowels:
            print(ch,"-> Vowel")
        else:
            print(ch,"-> Consonant")
