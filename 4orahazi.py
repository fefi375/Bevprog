def ckodolas():
    txt="kwwsv=22|rxwx1eh2gTz7z<Zj[fT" #z=122 a=97
    print(ord(txt[8]))
    dekod=""
    for i in range(0, len(txt)):
        dekod=dekod+chr(ord(txt[i])-3)
    
    print (dekod)
def valid(text, chars):
    b=""
    for i in range(len(text)):
        if text[i] in chars:
            b=b+(text[i])
    print (b)


def beszuro (elso, masodik):
    txt=input("Kerem a szöveget: ")
    index=txt.find(elso)
    fstring=txt[:index]+" "+masodik+" " +txt[index:]
    print(fstring)



def binaris():
    szam=int(input("Kerek egy pozitív tetszoleges termeszetes szamot: "))
    kettes=""
    hanyados=szam
    while(hanyados>0):
        kettes=kettes+str(hanyados%2)
        hanyados=hanyados//2
        
    print ("A szam binaris alakja: {0}".format(kettes[::-1]))


def main ():
    ckodolas()
    szo=input("Kerem az szot: ")
    chars=input("Kerem a betuket: ")
    valid(szo, chars)
    elso=input("Kerem az elso szot: ")
    masodik=input("Kerem a masodik szot: ")
    beszuro(elso, masodik)
    binaris()
    
if __name__=="__main__":
    main()