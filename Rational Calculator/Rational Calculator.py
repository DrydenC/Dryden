def gcd(a, b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a 

def second(c,d):
    c = int(input("Second Numerator: "))
    d = int(input("Second Denominator: "))
    return(c,d)
    
print("Welcome to my rational number calculator!")
print("Please input a rational number")

repeat = True
a = int(input("Numerator: "))
b = int(input("Denominator: "))
c = 0
d = 0

while(repeat):
    print(f"The current result is {a} / {b}")

    print("1. Subtract a rational number from the current result")
    print("2. Add a rational number to the current result")
    print("3. Multiply the current result by a rational number")
    print("4. Divide the current result by a rational number")
    print("5. Take the reciprocal of the current result")
    print("6. Quit")

    answer = int(input("Please enter a selection: "))

    if answer >= 1 and answer < 5:
        c,d = second(c,d)

        if answer == 1:
            finalnum = ((a*d) - (b*c))
            finalden = (b*d)
    
        elif answer == 2:
            finalnum = ((a*d) + (b*c))
            finalden = (b*d)
    
        elif answer == 3:
            finalnum = a*c
            finalden = b*d
    
        elif answer == 4:
            finalnum = a*d
            finalden = b*d
        
        elif answer == 5:
            finalnum = b
            finalden = a
    
        a = finalnum
        b = finalden

        if (a/b) == a:
            print(a)

    elif answer == 6:
        exit()