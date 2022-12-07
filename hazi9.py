def kommunikacio():
    w=open("C:/Gyakorlás python/9hazi/9hazi/bin/Debug/net6.0/kozos.txt", 'w')
    print("Ez a közös fájl (Python)", file=w)
    w.close()

def pivers():
    fi = open("C:/Gyakorlás python/pivers.txt", 'r')
    sorok=fi.read()
    szavak=sorok.split(" ")
    hossz=[]
    for i in szavak:
        hossz.append(len(i))
    print(hossz[0], end=',')
    for i in range(1, len(hossz)):
        print(hossz[i], end='')
    fi.close()


def fajlkezeles():
    f = open("C:/Gyakorlás python/string1.py", 'r', encoding="utf-8") 
    sorok=f.readlines()
    #print(sorok)
    with open("C:/Gyakorlás python/string1_clean.py", 'w', encoding="utf8") as f2:
        for i in sorok:
            if "#" not in i:
                print(i, file=f2)
        
    f.close()
def main():
    kommunikacio()
    pivers()
    fajlkezeles()
    
if __name__=="__main__":
    main()