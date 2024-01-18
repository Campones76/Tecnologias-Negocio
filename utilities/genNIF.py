from nifverifier import generate_dead_ass_valid_nif
# Generate a valid NIF
# Valid initial values are: "1, 2, 3, 5, 6, 8, 9"

print("Please choose an option:")
print("1: Start with a '1'")
print("2: Start with a '2'")
print("3: Start with a '3'")
print("4: Start with a '5'")
print("5: Start with a '6'")
print("6: Start with a '8'")
print("7: Start with a '9'")

option = int(input("Enter your option: "))
if option == 1:
    n="1"
elif option == 2:
    n="2"
elif option == 3:
    n="3"
elif option == 4:
    n="5"
elif option == 5:
    n="6"
elif option == 6:
    n="8"
elif option == 7:
    n="9"
else:
    print("Invalid option")


valid_nif = generate_dead_ass_valid_nif(initial_value=n)
print(valid_nif)