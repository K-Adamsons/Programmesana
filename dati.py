def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8") # w - write; 
    fails.write(teksts+"\n")
    fails.close()
    return

# ierakstit("Mani sauc Krišjānis")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()
    return
# pierakstit_klat("Mani sauc Krišjānis")

def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

# print(nolasit_visu())

def dabut_rindinas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()
    return rindas

saraksts = dabut_rindinas()
for i in range(len(saraksts)):
    saraksts[i] = saraksts[i].strip()
    
print(saraksts)