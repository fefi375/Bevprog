def main():
    text="""
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb"""
    newtext=""""""
    for i in range(0, len(text)): #10 #: = 58
        if ord(text[i])+2 > 89 and ord(text[i])<97:
            newtext=newtext+chr(ord(text[i])-24)
        elif ord(text[i])>63 and ord(text[i])+2<=122:
           newtext=newtext+chr(ord(text[i])+2)
        elif ord(text[i])+2>122:
            newtext=newtext+chr(ord(text[i])-24)
        else:
            newtext=newtext+text[i]
            
        
    print(newtext)
        
    
if __name__=="__main__":
    main()