import math

def kor(sugar):
    tkor=sugar**2*math.pi
    return tkor

def teglalap(a, b):
    tterulet=a*b
    return tterulet

def fibonacci():
    n=int(input("Hanyadik elemet szamoljam ki a Fibonacci sorozatnak?"))
    szam1=0
    szam2=0
    osszeg=0
    for j in range (0, n):
        osszeg=szam1+szam2
        szam2=szam1
        szam1=osszeg
        if szam2==0:
            szam1+=1
        
    print("A Fibonacci sorozat {0}. tagja: {1}".format(n ,osszeg))
    
    
def tukorszamok():
    tszam=input("Kerek egy szamot es megmondom hogy tukorszam-e ")
    egyenlo=True
    szlist=list(tszam)
    if szlist==szlist[::-1]:
        print("A szam tukorszam. :)")  
    else: print("A szam nem tukorszam.") 
                
def distance(p1, p2):
    a=(p1[0]+p2[0])**2
    b=(p1[1]+p2[1])**2
    d=math.sqrt(a+b)
    return d
            
def main ():
    r=int(input("Kerlek add meg a sugarat: "))
    print("A kor terulete: {0}".format(kor(r)))
    a=int(input("Kerlek add meg a teglalap egyik oldalat: "))
    b=int(input("Kerlek add meg a teglalap masik oldalat: "))
    print("A teglalap terulete: {0}".format(teglalap(a, b)))
    gulakup=input("Mit szamoljak ki? (gula/kup)")
    if gulakup=="gula":
        a2=int(input("Kerem az alap egyik oldalat: "))
        b2=int(input("Kerem az alap masik oldalat: "))
        m=int(input("Milyen magas legyen? "))
        vgula=(teglalap(a2, b2)*m)/3
        print("A gula terfogata: {0}".format(vgula))
        
    else:
        r2=int(input("Kerem a kor sugarat: "))
        m=int(input("Milyen magas legyen?"))
        vkup=(kor(r2)*m)/3
        print("A kup terfogata: {0}".format(vkup))
        
    fibonacci()
    tukorszamok()
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))
if __name__=="__main__":
    main()