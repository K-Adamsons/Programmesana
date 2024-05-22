def rezultats(sk1,sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2 
    return rez

for skaitlis in range(1,11,2):
    for otrs in range(1,11):
        print("pirmais skaitlis:", skaitlis, "otrais  skaitlis:", otrs, "rezutāts:", rezultats(skaitlis, otrs))

skaitlis1 = 4
skaitlis2 = 3

print("pirmais skaitlis:", skaitlis1)
print("otrais skaitlis:", skaitlis2)
print("rezultats:", rezultats(skaitlis1,skaitlis2))

rezultats(5, 7)

pirmais ="6"

print (pirmais)

vārds2 ="nine"

print (pirmais + vārds2)

def zvaigznes(skaits):
    for rindasNR in range(1, skaits+1):
        print("*"*rindasNR)

zvaigznes(100)        