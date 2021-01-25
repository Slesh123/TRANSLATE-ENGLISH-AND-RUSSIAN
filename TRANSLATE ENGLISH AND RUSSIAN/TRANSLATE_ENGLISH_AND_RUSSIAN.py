
def addfile(f):
    ENGLISH=open('file.txt','a')
    RUSSIAN=open('file.txt','a')
    eng_sona=input("ENGLISH WORD ")
    rus_sona=input("РУССКОЕ СЛОВО ")
def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

rus_list=loe_failist("RUSSIAN.txt")
eng_list=loe_failist("ENGLISH.txt")
print(rus_list)
print(eng_list)


def translateE(e):
    english=input("WORD: ")
    english.open('ENGLISH.txt','a',encoding="utf-8-sig")
    english.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas


def tolkimine():
    pass
    
def translateR():
    russian=input("Слово: ")
    russian.open('RUSSIAN.txt','a',encoding="utf-8-sig")
    russian.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas




print(rus_list)
print(eng_list)

while True:
    v=input("1-ПЕРЕВОД,2-НОВОЕС СЛОВО,3-ИСПРАВИТЬ ОШИБКУ,4-ПРОВЕРКА ЗНАНИЙ")
    if v=="1":
        tolkimine()
    elif v=="2":
        rus_sona=input("Русское Слово ")
        eng_sona=input("English Word")
        rus=translateR()('RUSSIAN.txt',rus_sona)
        eng=translateE(e)('ENGLISH.txt',eng_sona)