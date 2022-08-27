try:
    print('The answer is:',eval(input('Please enter in the question: ')))
except NameError:
    print('Please enter in a question with count, not a letter!')
except SyntaxError:
    print('Please enter in a question with count, not a symbol!')