#!python3

def AdderWithDouble():

    adder = Adder()

    def obj(cmd, *args):

        nonlocal adder

        if cmd == "double":
            adder("add", adder("get"))
        else:
            return adder(cmd, *args)

    return obj


def Adder():

    i = 0

    def obj(cmd, *args):

        nonlocal i

        if cmd == "reset":
            i = 0
        elif cmd == "add":
            i += args[0]
        elif cmd == "get":
            return i

    return obj

# adder = Adder()

# adder("add", 10)
# adder("add", 10)
# adder("add", adder("get"))

# print(adder("get"))

# adder("reset")

# print(adder("get"))

# adder1 = Adder()

# adder1("add", 10)
# adder1("add", 10)

# print(adder1("get"))

# adder2 = Adder()

# adder2("add", 10)
# adder2("add", 15)

# print(adder2("get"))

# Inheritance

adder3 = AdderWithDouble()

adder3("add", 5)

print(adder3("get"))

adder3("double")

print(adder3("get"))
