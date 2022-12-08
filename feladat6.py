import math
def mkul(n):
   m=[]
   osszeg=0
   for i in range(0, n):
      a=int(input("Add meg a magassagot: "))
      m.append(a)
   for i in range(1, len(m)):
      osszeg=osszeg+abs(m[i]-m[i-1])
      
   print("A szomszédos felhőkarcolók magasságkülönbsége : {0}".format(osszeg))
    



def main():

   n=int(input("Hany felhokarcolo legyen: "))
   mkul(n)
   # Vegyük a 2^1024 számot. Ha ezen szám számjegyeit felhőkarcolók magasságának tekintjük, akkor mennyi lesz a szomszédos felhőkarcolók magasságkülönbségének az összege?
   print("b feladat: ")
   szam=2**1024
   li=[]
   for i in str(szam):
      li.append(i)
   #print(li)
   osszeg=0
   for i in range(0, len(li)):
      osszeg=osszeg+abs(int(li[i])-int(li[i-1]))
      
   print(osszeg)
if __name__=="__main__":
    main()