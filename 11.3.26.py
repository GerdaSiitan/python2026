punkt1 = (13, 123)
sisestatud_kordinaadid = [234, 2]
mingi_sonastik = {"meeskond": (23, -222)}

kordinaadid = tuple(sisestatud_kordinaadid)
x1 = 2.3345
y1 = 3.4567
kordinaadid = (x1, y1)

while True:
    meeskond = input("Sisesta meeskonna nimi: ")
    if meeskond.lower().strip() == "stop":
        break
    if meeskond != "":
        try:    
            sisestatud_kordinaadid = input("Sisesta meeskonna kordinaadid (x, y): ").split(",")

        except ValueError:
            print("Viga: Palun sisesta kordinaadid õigesti (x, y).")
            continue
    print(sisestatud_kordinaadid)

kaugus = round(((x1-x)**2 + (y1-y)) ** (1/2), 6)