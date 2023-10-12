print("GENERATION GENERATOR")
print()
birth_year = int(input("what year were your born:  "))
if birth_year <= 1925:
    print("You are a Traditionalist")
elif birth_year >= 1947 and birth_year <= 1965:
    print("You are Baby Boomers")
elif birth_year >=1865 and birth_year <= 1982:
    print("Hey there Mellinial")
elif birth_year >= 1996:
    print("Hell0 gen Z")
else:
    print("Error!")