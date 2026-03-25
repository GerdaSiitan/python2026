# --------------- map vol 3 -----------------------

tervitused = ['Tere', 'Tere', 'Tere']
print(list(map(str.upper, tervitused)))

def f(x):
    return x%10
a = [34, 5, 789, 24134]
print(list(map(f, a)))

# --------------- reduce -----------------------
#Misha puudub krt, aga Alina näide
#NVM MISHA TULI, NVMMMM DIMA SÜÜDI
#Ehk Alina näide here we come:

from functools import reduce

number = [1, 2, 3, 4]
tulemus = reduce(lambda x, y: x + y, number)
print(tulemus)

# --------------- lambda -----------------------

liida = lambda x, y: x + y
print(liida(5, 6))

# --------------- thisdict -----------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict["nimi"] = input("Sisesta nimi: ")
thisdict["panus"] = input("Sisesta panus: ")

print(thisdict)