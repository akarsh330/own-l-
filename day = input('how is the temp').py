name = input('whats your name : ')
if len(name) < 3 :
    print('name must be at lest 3 alphabets')
elif len(name) > 50 :
    print('name should be under 50 alphabets')
else :
    print('the name is fine')