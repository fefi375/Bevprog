def main():
   o=input("Kerem az oldalakat: ")
   li=o.split(',')
   szamok=[]
   nli=[]
   for i in li:
      if "-" in i:
         a=i.split('-')
         for j in range(int(a[0]), int(a[1])+1):
            nli.append(j)
      else:
         nli.append(int(i))
   print(nli)
    
if __name__=="__main__":
    main()