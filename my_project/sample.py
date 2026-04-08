from faker import Faker
fake = Faker()  # Create a Faker generator
print(f"Fake Name: {fake.name()}")
print(f"Fake Address: {fake.address()}")
print(f"Fake Text: {fake.text()}")
for _ in range(5):
    print(f"Fake Email: {fake.email()}")
    print