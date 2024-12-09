import os
import webbrowser

Arg = input()

Args = Arg.split()

def Open():
    PathList = [ "C:\\Users\\Doğukan\\Desktop\\2" ]
    LinkList = [ "https://hackthebox.com", "https://tryhackme.com" ]
    
    AddArg3 = False
    Arg3 = -1

    if len(Args) == 1:
            
            if Args[0] == 'link' or Args[0] == 'l':
                print ("\nLinkler\n")

                for Link in LinkList:
                    print(str(LinkList.index(Link) + 1) + ") " + Link)
                
            elif Args[0] == 'path' or Args[0] == 'p':
                print ("\nDosya Konumları\n")

                for Path in PathList:
                    print(str(PathList.index(Path) + 1) + ") " + Path)

            print ("\n>> ")
            SelectPathLinkIndex = input()

            if SelectPathLinkIndex == "exit":
                print ("Araçtan çıkış sağlandı")
            else:
                try:
                    Arg3 = int(SelectPathLinkIndex)
                    AddArg3 = True
                except:
                    print("Komut algılanamadı")
            


    if len(Args) == 2 or AddArg3:

        PathLinkIndex = -1

        if AddArg3:
            PathLinkIndex = Arg3
        else:
            try:
                PathLinkIndex = int(Args[1])
            except:
                print ("Argüman olarak indeks girmeniz gerekmekte")

        if type(PathLinkIndex) == int and PathLinkIndex != -1:
            
            if (Arg[0] == "link" or Arg[0] == "l") and (PathLinkIndex >= 0 and PathLinkIndex < len(LinkList)):
                webbrowser.open(LinkList[PathLinkIndex])
            elif (Arg[0] == "path" or Arg[0] == "p") and (PathLinkIndex >= 0 and PathLinkIndex < len(PathList)):
                if os.path.exists(PathList[PathLinkIndex]):
                    os.startfile(PathList[PathLinkIndex])
                else:
                    print ("Dosya bulunamadı")
            else:
                print ("Indeks aşımı")

if Args[0] == 'help' or Args[0] == 'h':
    print("""
PathLinkGo Nasıl Kullanılır?

PathLinkGo'da iki ana seçenekten birini seçmelisin: link (bağlantı) ya da path (konum)

1. Seçim Yapmak:
    - Link seçmek için: "link" ya da kısaltması olan "l" komutunu kullanabilirsin
    - Path seçmek için: "path" ya da kısaltması olan "p" komutunu kullanabilirsin

2. Hedef Belirlemek:
    Seçim yaptıktan sonra gitmek istediğin listede hangi eleman olduğunu belirtmen gerekiyor:
    - İndeks numarasını yazabilirsin:
    Örnek: >> 1

3. Hızlı Erişim:
    Hızlı erişim için ise şu yöntemi kullanabilirsin:
    - Link için: link 0
    - Path için: path 0
""")


elif Args[0] == 'link' or Args[0] == 'l' or Args[0] == 'path' or Args[0] == 'p':
    Open()