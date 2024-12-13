# PathLinkGo Nasıl Kullanılır?

PathLinkGo'da iki ana seçenekten birini seçmelisin: **link** (bağlantı) ya da **path** (konum).

## 1. Seçim Yapmak
- Link seçmek için: `"link"` ya da kısaltması olan `"l"` komutunu kullanabilirsin.  
- Path seçmek için: `"path"` ya da kısaltması olan `"p"` komutunu kullanabilirsin.  

## 2. Hedef Belirlemek
Seçim yaptıktan sonra gitmek istediğin listede hangi eleman olduğunu belirtmen gerekiyor:  
- **İndeks numarasını yazabilirsin:**  
  Örnek: `>> 1`  

## 3. Hızlı Erişim
Hızlı erişim için şu yöntemi kullanabilirsin:  
- **Link için:** `link 0`  
- **Path için:** `path 0`  

## 4. Değer Ekleme (Append)
Listeye yeni bir değer eklemek için `"append"` ya da kısaltması olan `"a"` komutunu kullanabilirsin.
- İkinci parametrede, eklemek istediğin değerin türünü belirtmelisin:
    - Link eklemek için: `"link"` ya da kısaltması olan `"l"`
    - Path eklemek için: `"path"` ya da kısaltması olan `"p"`
- Üçüncü parametrede ise eklemek istediğin değeri yazmalısın.
    
### Örnekler:
- `>> append path "/root"`
- `>> append link "https://github.com"`