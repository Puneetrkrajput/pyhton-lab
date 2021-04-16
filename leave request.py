letter='''Dear sir, <name> here .
i am sick so i am taking leave today dated <date> .
please consider my request. '''
# print(letter)

name= input("enter your name\n ")
date= input("enter date\n ")
letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)