word=input("give the word to count vowels and consonants:").lower().strip().replace(" ","")
if word.isalpha():
    vowels=word.count('a')+word.count('e')+word.count('i')+word.count('o')+word.count('u')
    consonants=len(word)-vowels
    print(f"THERE ARE {vowels} VOWELS")
    print(f"THERE ARE {consonants} consonants")

elif word=="":
    print("ENTER SOMETHING TO GIVE VALUES")

else:
    print("pls give word only")