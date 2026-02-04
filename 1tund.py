kasvud = [175,169,170,170,181,168,173,159,182]
minu_kasv = 175

kasvud = sorted(kasvud, reverse=True)
print(kasvud)

koht = 0
for k in kasvud:
    if k >= minu_kasv:
        koht += 1

print("Minu koht on", koht)

# ----------------------------------------------

sona = input("Sisesta sõna: ")
print(sona[::-1])

# -------------------------------------------------

from os import replace
import re
nimed = ['An6na', 'Anne', 'A1lek6san6dr', 'Os8kar', 'E55va']

pattern = r'[0-9]'

puhastatud_nimed = [re.sub(pattern, '', nimi) for nimi in nimed]

print(puhastatud_nimed)

# -------------------------------------------------

palgad = ['1500 €', '2850 €', '4200 €', '5775 €', '2500 €', '1200 €', '2000 €', '3500 €']
uued_palgad = []

for palk in palgad:
    palk = palk.replace('€', '')
    palk = palk.strip()
    uued_palgad.append(int(palk))

print(uued_palgad)
