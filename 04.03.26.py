thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict["nimi"] = input("Sisesta nimi: ")
thisdict["panus"] = input("Sisesta panus: ")

print(thisdict)

# -------------------------------------------------

panustaja = input("Sisesta panustaja nimi: ")
panus = input("Sisesta panus: ")
panused_panusatajalt = {}
panused_panusatajalt[panustaja] = panus
print(panused_panusatajalt)

while True:
    kas_veel = input("Kas soovid veel panustajaid lisada? (jah/ei): ")
    if kas_veel.lower() == "jah" or kas_veel.lower() == "ja":
        panustaja = input("Sisesta panustaja nimi: ")
        panus = input("Sisesta panus: ")
        panused_panusatajalt[panustaja] = panus
        print(panused_panusatajalt)

    else:
        print("Panustamine lõppenud.")
        break
    
