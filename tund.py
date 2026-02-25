# --------------- sorted, sort, filter -----------------------

from matplotlib.pylab import number


words=['10','2','1']
words.sort()
print(words)

print(sorted('alina'))

nums = [0,1,2]
list(filter(lambda x: x, nums))


# --------------- map -----------------------

numbrid = [0,1,2]
def liitmine(x):
    return x + 56

print(type(numbrid), numbrid)

numbrid = map(liitmine, numbrid)
print(type(numbrid), numbrid)

numbrid = list(numbrid)
print(type(numbrid), numbrid)

# --------------- enumerate -----------------------

arvud = [10, 20, 30]
for i, arv in enumerate(arvud):
    if i == 9:
        print(arv)

# --------------- map vol 2 -----------------------

tahed = ['a', "b", 'c', "d"]
numbrid = ['1', '2', '3', '4']

def tahtnumber (taht, number):
    return taht + number

kood = map(tahtnumber, tahed, numbrid)
print(list (kood))

# --------------- zip -----------------------

a=["a", "b", "c", "d"]
b=["1", "2", "3", "4"]

for i, j in zip(a, b):
    print(i, j)

# --------------- lambda -----------------------+