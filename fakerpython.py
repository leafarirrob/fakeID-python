import random
from faker import Faker

country = input("Italy___English___Japan\nSelect: ")

if country == "Italy":
    fake = Faker("it_IT")
elif country == "English":
    fake = Faker("en_US")
elif country == "Japan":
    fake = Faker("ja_JP")
else:
    print("!!!")
    
for i in range(10):
    print("Name: ", fake.name())
    print("Age: ", random.randint(25, 65))
    print("Phone number: ", fake.phone_number())
    print("Address: ", fake.address())
    print("IP: ", fake.ipv4_private())
    print("Text: ", fake.text())
    print("")
    print("")