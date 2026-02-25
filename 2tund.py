for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print()


# -----------------------------------------------------

inimesed = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
palgad = [1200, 650, 990, 1500, 3000, 2500, 1600]


input("Mida arvutada? keskmine - k ; minimum - m ; rikkad - r ; päring - p ; sort - s")

def keskmine(k):
        k = sum(palgad) / len(palgad)
        return k
    
def minimum():
        return min(palgad)
    
if input == 'k':
    print("Keskmine palk on", keskmine())
elif input == 'm':
    print("Minimaalne palk on", minimum())
elif input == 'r':
    for i in range(len(palgad)):
        if palgad[i] > 2000:
            print(inimesed[i], "on rikas")
elif input == 'p':
    nimi = input("Täht ['A', 'B', 'C', 'D', 'E', 'F', 'G'] : ")
    if nimi in inimesed:
        index = inimesed.index(nimi)
        print(nimi, "palk on", palgad[index])
    else:
        print("Nimekirjas pole sellist inimest")

