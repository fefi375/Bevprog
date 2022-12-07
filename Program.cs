using System;
using System.IO;

class Program
{   static public void Main(String[] args)
    {
        StreamWriter sw = new StreamWriter("kozos.txt");
        sw.WriteLine("Ez a közös fájl (C#)");
        sw.Close();
    }
}