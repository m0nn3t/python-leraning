liczby = [120, 200, 150, 110, 180, 130, 210, 140, 220, 160, 170, 200, 190, 250, 120, 180, 260, 230, 150, 240, 200, 110, 170, 130, 150, 300, 270, 120, 160, 210, 220, 140, 230, 110, 110, 250, 190, 260, 150, 270, 200, 120, 180, 300, 140, 160, 230, 230, 250, 130]

ilosc_gorek = 0
miejsce_gorki = []
takie_same = 0
for i in range(1, len(liczby)-1):

    if liczby[i-1] < liczby[i] > liczby[i + 1]:
        ilosc_gorek +=1
        miejsce_gorki.append(i)

for i in range(1,len(liczby)):
    if liczby[i-1] == liczby[i]:
        takie_same += 1

print(ilosc_gorek)

print(miejsce_gorki)

print(takie_same)