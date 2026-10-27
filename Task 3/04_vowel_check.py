character = input("Enter a character: ")

if len(character) == 1 and character.lower() in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")
