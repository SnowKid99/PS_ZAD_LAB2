#zad1
filmy=["Iron-man","Back to the future","Lock and Key","Star Wars","The Lord of the Rings"]
print(filmy)
filmy.reverse()
print(filmy)
filmy.insert(5,"Avangers")
filmy.insert(6,"Spider-man")
filmy.insert(7,"Resident Evil")
filmy.insert(8,"Justice league")
filmy.insert(9,"Deadpool")
print(filmy)

#zad3
przedmioty={
	"Wizualizacja danych":"WD",
	"CAD komputerowe wspomaganie programowania":"CAD-kwp",
	"Przedmiot humanizujący":"human",
	"Język angielski":"ENG",
	"Rachunek różniczkowy i całkowy":"RRiC",
	"Elementy matematyki dyskretnej":"EMD",
	"Programowanie strukturalne":"PS"
}
print(przedmioty)
print(len(przedmioty))

#zad6
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
if a%2==0 and b>c:
	print("a parzysta i b wieksze od c")
elif a%2==0:
	print("a parzysta ale b mniejsze od c")
elif a%2!=0 and b>c:
	print("a nieparzysta ale b wieksze od c")
elif a%2!=0:
	print("a nieparzysta i b mniejsze od c")

#zad7
lista=[1,1.3,2.5,2.8,3,3.5,4,4.4,5,5.5]
for i in range(1,len(lista),1):
	print(lista[i]+lista[i-1])

#zad5
import sys as system
ciag_znakow=system.stdin.readline()
system.stdout.write(str(ciag_znakow.count("a")))