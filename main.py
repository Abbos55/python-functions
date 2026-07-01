def salom(ism):
    print(f"Salom, {ism}!")


def qoshish(a, b):
    return a + b


def kopaytirish(a, b):
    return a * b


salom("Abbos")
print("Yig'indi:", qoshish(10, 5))
print("Ko'paytma:", kopaytirish(4, 6))

def kvadrat(x):
    return x * x

print(kvadrat(9))

def katta_son(a, b):
    if a > b:
        return a
    return b

print(katta_son(25, 18))