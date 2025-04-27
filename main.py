def is_pangram(sentence):
  alphabet = set('abcdefghijklmnopqrstuvwxyz')
  sentence = set(sentence.lower())
  sentence_letters = set()

  for letters in sentence:
      if 'a' <= letters <= 'z':
          sentence_letters.add(letters)
  return len(sentence_letters) == 26



user_input = input("Enter a sentence: ")

if is_pangram(user_input):
  print("It's a pangram!")
else:
  print("It's not a pangram.")