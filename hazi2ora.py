import math
def feladat1():
    e=int(input("Kerlek add meg az eletkorod: "))
    if e>=21:
        print("Fogyaszthat Amerikaban legalisan alkoholt.")
    elif e <21:
        print("Nem fogyaszthat Amerikaban alkoholt.")
    if e>=18:
        print("Vasarolhat dohanytermeket Magyarorszagon.")
    elif e<18:
        print("Nem vasarolhat dohanytermeket Magyarorszagon")
    if e>=16:
        print("Szerezhet jogositvanyt.")
    elif e<16:
        print("Nem szerezhet hogositvanyt.")
    if e>=12:
        print("Megnezheti egyedul a Shrek 2-ot.")
    elif e<12:
        print("Nem nezheti meg egyedul a Shrek 2-ot")
def feladat2():
    print("II.Feladat: ")
    print ("1. Pitagorasz tetel: ")
    a=int(input("Kerlek add meg a derekszogu haromszog egyik oldalát: "))
    b=int(input("Kerlek add meg a derekszogu haromszog masik oldalát: "))
    c=a**2+b**2
    print("A derekszogu haromszog atfogoja: ", c)
    print("Sin kiszamolasa haromszogben: ")
    s_1=float(input("kerlek add meg a derekszogu haromszog szoggel szembeni oldalát: "))
    s_2=float(input("Kerlek add meg a derekszogu haromszog atfogojat: "))
    s=float(s_2/2_1)
    print("a szog szinusza : ",s)
    print("A masodfoku egyenlet megoldokeplete: ")
    a=int(input("Kerem az a erteket: "))
    b=int(input("Kerem a b erteket: "))
    c=int(input("Kerem a c erteket: "))
    x_1=(+b+math.sqrt(4*a*c))/2*2
    x_2=(-b+math.sqrt(4*a*c))/2*2
    print("Az x1 erteke: ", x_1)
    print("Az x2 erteke: ", x_2)
    
def feladat3():
    print("III.Feladat: ")
    na=int(input("Natrium: "))
    cl=int(input("Klor: "))
    nacl=0
    mna=0
    mcl=0
    if cl==2*na:
        nacl=2*na
        
    elif 2*na>cl:
        nacl=2*na
        mna=(2*na-cl)*2
        
    elif 2*na<cl:
        nacl=na
        mcl=(cl-na*2)
    print("Létrejött NaCL: {0} \nMaradék Nátrium atom: {1} \nmaradék Klór atom: {2}" .format(nacl, mna, mcl))
    
def main():
    feladat1()
    feladat2()
    feladat3()
    
if __name__=="__main__":
    main()