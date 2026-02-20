pomiary = [12.5, 14.2, 13.8, 11.0, 10.5, 9.8, 12.1, 15.6, 17.2, 18.0, 16.5, 14.0]

wynik1 = round(sum(pomiary) / len(pomiary), 2)
print(wynik1)

tempmax = max(pomiary)
tempmin = min(pomiary)
print(tempmax)
print(tempmin)
wynik2 = tempmax - tempmin
print("amplituda to " + str(wynik2) + " stopni")


zimno = 0
for i in pomiary:
    if i <12:
        zimno += 1
print(zimno)

zmiana = 0
for i in range(len(pomiary)-1):
    zmiana1 = pomiary[i+1] - pomiary[i]
    if zmiana1 > zmiana:
        zmiana = zmiana1
        godzina = i + 1
print(zmiana)
print(godzina)