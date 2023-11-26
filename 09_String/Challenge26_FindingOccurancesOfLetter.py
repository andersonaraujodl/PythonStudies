'''
Write a program that receives a sentence and then a letter and finds:
1. How many times this letter appears in the phrase.
2. What's the position of its first occurrence.
3. What's the position of its last occurrence.
'''

sentence = str(input("Type a sentence: ")).strip()
characterToFind = str(input("Type a character to count: ")).strip()

print("The character \'{}\' appeared {} times in the sentence.".format(characterToFind, sentence.lower().count(characterToFind.lower())))
print("The character \'{}\' first appeared on index {}.".format(characterToFind, sentence.lower().find(characterToFind.lower())))
print("The character \'{}\' last appeared on index {}.".format(characterToFind, sentence.lower().rfind(characterToFind.lower())))