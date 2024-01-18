from gubbins import Gubbins

def generate_and_validate(prefix, i):
    serial = Gubbins.generate(prefix, i)
    prefix, id = Gubbins.validate(serial)
    assert prefix.lower() == prefix.lower()
    assert id == i
    print(i, serial)

print("Please choose an option:")
print("1: Use prefix 'AX'")
print("2: Use prefix 'G'")
print("3: Use prefix 'C'")

option = int(input("Enter your option: "))

for i in range(10):
    if option == 1:
        generate_and_validate("AX", i)
    elif option == 2:
        generate_and_validate("G", i)
    elif option == 3:
        generate_and_validate("C", i)
    else:
        print("Invalid option")
