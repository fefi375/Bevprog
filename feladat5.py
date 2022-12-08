class Verem:
   def __init__(self, a=[]) -> None:
      self.a=a 
      
   def ures(self):
      if self.a==[]:
         return True

   def betesz(self, szam):
      self.a=self.a.append(szam)
   
   def kivesz(self):
      self.a.remove()
   
   def meret(self):
      return len(self.a)
   

def main():
   v=Verem()
   print(v.a)
   v.ures()
   n=int(input("Melyik szamot tegyem bele: "))
   v.betesz(n)
   print(v.a)
    
if __name__=="__main__":
    main()