def catAndMouse(x, y, z):
    input_number=int(input())
    input_string = input()
    for i in input_string:
        if i == input_string[0]:
            x = int(i)
        elif i == input_string[2]:
            y = int(i)
        elif i == input_string[4]:
            z = int(i)
    for i in range (input_number):
        if abs(x - z) < abs(y - z):
            return "Cat A"
        elif abs(x-z)==abs(y-z):
            return "Cat A"
        else:
            return "Cat A"


catAndMouse(1, 3, 2)
