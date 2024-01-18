from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate fake data
name = fake.name()
address = fake.address()
phone_number = fake.phone_number()
birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
email = fake.email()

# Print the fake data
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Phone Number: {phone_number}")
print(f"Birthday: {birthday}")
print(f"Email: {email}")

def generate_phone_number(country):
    fake = Faker(country)
    return fake.phone_number()

def generate_address(country):
    fake = Faker(country)
    return fake.address()
def generate_name(country):
    fake = Faker(country)
    return fake.name()


print(generate_phone_number('nl_BE'))
print(generate_phone_number('pt_PT'))
print(generate_phone_number('en_US'))
print(generate_phone_number('en_UK'))

print("Nome")
print(generate_name('pt_PT'))
print("Address")
print(generate_address('pt_PT'))