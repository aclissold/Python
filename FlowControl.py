def if_else():
    print("Executing if_else().")
    x = int(input("Enter your age: "))
    if x < 0:
            print("You're lying!")
    elif x < 21:
            print("You're younger than me.")
    elif x == 21:
	    print("We're the same age!")
    else:
	    print("You're older than me.")

def for_test():
    print("Executing for_test().")
    list = ['a', 'b', 'c', 'd']
    for letter in list:
        print(letter, end=' ')
    print()
    for i in range(len(list)):
        print(list[i], end=' ')

def break_test():
    print("Executing break_test().")
    letters = ['a', 'b', 'c']
    print("Now using a break statement to print the first two letters of the \
first three\nletters of the alphabet.")
    for i in range(len(letters)):
        if i == 2:
            break
        else:
            print(letters[i], end=' ')

def continue_test():
    print("Executing continue_test().")
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)

continue_test()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
