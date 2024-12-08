textbooks = {
'math' : 150,
'biology' : 100,
'chemistry' : 100,
'physics': 150,
'geography' : 150,
'history' : 150,
'economics' : 100,
'politics' : 100
}
textbooks['physics']=200
# print(textbooks)

textbooks['english literature'] = 100
textbooks['english grammar'] = 100

# print(textbooks)
math_price = textbooks['math']
biology_price = textbooks['biology']
chemistry_price= textbooks['chemistry']
physics_price = textbooks['physics']
geography_price = textbooks['geography']
history_price = textbooks['history']
economics_price = textbooks['economics']
politics_price = textbooks['politics']
english_literature_price = textbooks['english literature']
english_grammar_price = textbooks['english grammar']

book = input("Which textbook would you like to buy? ")

if book == 'math':
  print(math_price)
elif book == 'biology':
  print(biology_price)
elif book == 'chemistry':  
  print(chemistry_price)
elif book == 'physics':
  print(physics_price)
elif book == 'geography':
  print(geography_price)
elif book == 'history':
  print(history_price)
elif book == 'economics':
  print(economics_price)
elif book == 'politics':
  print(politics_price)
elif book == 'english literature':
  print(english_literature_price)
elif book == 'english_grammar':
  print(english_grammar_price)
else: 
  print("Textbook not available")