def normal(s):
   ns=""
   s=s.lower()
   for i in range(0, len(s)):
      if s[i] != " ":
         ns+=s[i]
   return ns

def anagramma1(s1, s2):
   benne=True
   s1=normal(s1)
   s2=normal(s2)
   for i in range(0, len(s1)):
      if s1[i] in s2:
         benne==True
      else:
         benne=False
      
         
   if benne==True:
      print("A második szó az első anagrammája")
   else:
      print("A két szó nem anagrammaja egymasnak")


def anagramma2(s1, s2):
   s1=normal(s1)
   s2=normal(s2)
   masodik=len(s2)
   elso=0
   vszamok=[]
   for i in range(0, len(s1)):
      for j in range(0, len(s2)):
         if s1[i]==s2[j] and s1[i] not in vszamok:
            elso+=1
            vszamok.append(s1[i])
   
   if elso==masodik:
      print("A második szó az első anagrammája")
   else:
      print("A két szó nem anagrammaja egymasnak")

def main():
   s1=input("Kerek egy szot: ")
   s2=input("Kerem a masodik szot ")
   anagramma1(s1, s2)
   anagramma2(s1, s2)
   
    
if __name__=="__main__":
    main()