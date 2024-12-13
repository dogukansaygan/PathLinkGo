import os
import webbrowser
import re

Arg = input()
Args = ""

if '"' in Arg:
    Args = re.findall(r'"([^"]+)"|\S+', Arg)
else:
    Args = Arg.split()

def Open():

    FileName = ""

    if Args[0] in ['path', 'p']:
        FileName = "Paths.txt"
    
    elif Args[0] in ['link', 'l']:
        FileName = "Links.txt"

    FilePath = os.path.abspath(__file__)[0:-13] + FileName

    with open(FilePath, "r", encoding="utf-8") as LinkFile:
        List = LinkFile.readlines()
    
    AddArg3 = False
    Arg3 = -1

    if len(Args) == 1:
            
            if Args[0] in ['path', 'p']:
                print ("\nDosya Konumları\n")
            
            elif Args[0] in ['link', 'l']:
                print ("\nLinkler\n")

            for ListItem in List:
                print(str(List.index(ListItem) + 1) + ") " + ListItem)

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
            
            if (Arg[0] == "link" or Arg[0] == "l") and (PathLinkIndex >= 0 and PathLinkIndex < len(List)):
                webbrowser.open(List[PathLinkIndex])
            elif (Arg[0] == "path" or Arg[0] == "p") and (PathLinkIndex >= 0 and PathLinkIndex < len(List)):
                if os.path.exists(List[PathLinkIndex]):
                    os.startfile(List[PathLinkIndex])
                else:
                    print ("Dosya bulunamadı")
            else:
                print ("Indeks aşımı")

def Append():
    if len(Args) == 3:

        FileName = ""

        if Args[1] in ['path', 'p']:
            FileName = "Paths.txt"
        elif Args[1] in ['link', 'l']:
            FileName = "Links.txt"


        if FileName:
            FilePath = os.path.abspath(__file__)[0:-13] + FileName

            with open(FilePath, "r", encoding="utf-8") as File:
                FileContent = File.read()

            with open(FilePath, "a", encoding="utf-8") as File:
                if FileContent.strip():
                    File.write("\n" + str(Args[2]))
                else:
                    File.write(str(Args[2]))
    

if Args[0] == 'help' or Args[0] == 'h':
    print("""
PathLinkGo Nasıl Kullanılır?

PathLinkGo'da iki ana seçenekten birini seçmelisin: link (bağlantı) ya da path (konum)

1. Seçim Yapmak:
    - Link seçmek için: "link" ya da kısaltması olan "l" komutunu kullanabilirsin
    - Path seçmek için: "path" ya da kısaltması olan "p" komutunu kullanabilirsin

2. Hedef Belirlemek:
    Seçim yaptıktan sonra gitmek istediğin listede hangi elemanı seçmek istediğini belirtmen gerekiyor:
    - İndeks numarasını yazabilirsin.
    Örnek: >> 1

3. Hızlı Erişim:
    Hızlı erişim için şu komutları kullanabilirsin:
    - Link için: link 0
    - Path için: path 0

4. Değer Ekleme (Append):
    Listeye yeni bir değer eklemek için "append" ya da kısaltması olan "a" komutunu kullanabilirsin.
    - İkinci parametrede, eklemek istediğin değerin türünü belirtmelisin:
        - Link eklemek için: "link" ya da kısaltması olan "l"
        - Path eklemek için: "path" ya da kısaltması olan "p"
    - Üçüncü parametrede ise eklemek istediğin değeri yazmalısın.
    
    Örnekler:
    >> append path "/root"
    >> append link "https://github.com"
""")



elif Args[0] == 'link' or Args[0] == 'l' or Args[0] == 'path' or Args[0] == 'p':
    Open()

elif Args[0] == 'append' or Args[0] == 'a':
    Append()