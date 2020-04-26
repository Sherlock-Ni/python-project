spam = []
while True:
    print('Please,input what you want :')
    something = input()
    if something == ' ':
        break
    spam = spam + [something]
print(spam)

