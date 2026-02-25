töötajad = ["Alice", "Bob", "Charlie", "Diana"]
palgad = [3000, 2500, 4000, 3500]

# n = input(int("Sisesta kelle palka tahad näha: "))
# print("töötajad", Töötajad[n], "palgad", palgad[n])

def peaprogramm():
    valik = input("Vali tegevus: 1) palga päring 2) keskmine palk 3) uue töötaja lisamine ")
    if valik == "1":
        palga_päring()
    elif valik == "2":
        print("töötajate keskmine palk on", keskmine())
    elif valik == "3":
        uue_töötaja_lisamine()
    else:
        print("vale valik")
peaprogramm()

def palga_päring():
     otsitav_nimi = input("Sisesta kelle palka tahad näha: ")
     töötajate_arv = len(töötajad)
     for jk_nr in range(töötajate_arv):
         if töötajad[jk_nr] == otsitav_nimi:
             print("töötajad", töötajad[jk_nr], "palgad", palgad[jk_nr])
         else:
             print("ei leitud")

         töötaja_asukoht  = töötajad.index(otsitav_nimi) #ylemine rida pikem versioon
         print("leitud, ta palk on", töötaja_asukoht)
palga_päring()

def keskmine():
    palkade_summa = len(palgad)
    kogupalk = 0
    for i in range(palkade_summa):
        kogupalk = sum(palgad)
        keskmine_palk = kogupalk / palkade_summa
    return keskmine_palk
print("töötajate keskmine palk on", keskmine())

# if Töötajad[1] == otsitav_nimi:
#     print("leitud, ta asukoht on", 1)
# if Töötajad[2] == otsitav_nimi:
#     print("leitud, ta asukoht on", 2)
# if Töötajad[3] == otsitav_nimi:
#     print("leitud, ta asukoht on", 3)
# if Töötajad[4] == otsitav_nimi:
#     print("leitud, ta asukoht on", 4)

def uue_töötaja_lisamine():
    töötajate_arv = len(töötajad)
    olemasolevad_nimed = ""
    for i in range(töötajate_arv):
        olemasolevad_nimed = (olemasolevad_nimed + töötajad[i])
    print("Olemasolevad töötajad on:", olemasolevad_nimed)
    uus_töötaja = input("Sisesta uue töötaja nimi: ")
    töötajad.append(uus_töötaja)
    uus_palk = int(input("Sisesta uue töötaja palk: "))
    palgad.append(uus_palk)
    print("Uus töötaja lisatud:", uus_töötaja, "palgaga", uus_palk)
    print(palgad, töötajad)
uue_töötaja_lisamine()  