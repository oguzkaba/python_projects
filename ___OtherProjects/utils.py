# bulunduğu klasör
# print(os.getcwd())

# farklı klasöre geçiş
# os.chdir("C:/Users/Oğuz KABA/Desktop/Diğer Dosyalar")

# klasörde bulunan dosyalar
# print(os.listdir())

# klasör oluşturma
# os.mkdir("aa")

# kasör ismi değştirme
# os.rename("aa","yeniKlasor")

# klasör mü?
# os.path.isdir("/home/sinan")

# dosya ismi ver -> olmayandosya.py
# os.path.split("/home/sinan/pythonProject/adventureGame/olmayandosya.py")

# dosyanın adını ve uzantısını ayrı ayrı ver -> ('olmayandosya', '.py')
# os.path.splitext("/home/sinan/pythonProject/adventureGame/olmayandosya.py")

# dosya mı?
# os.path.isfile("/home/sinan/pythonProject/adventureGame/index.py")

# dosya yada klasör var mı?
# os.path.exists("/home")

# dosyayı ilgili program ile açma
# os.startfile('deneme.txt')

# uzantı ismi ile dosya listeleme
# uzanti=input('Uzantı ismi (.txt, .xlsx gibi) giriniz ?  :')
# sayac=0
# os.chdir('C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar')
# dosyalar = os.listdir('C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar')
# for dosya in dosyalar:
#      if dosya.endswith(uzanti):
#             sayac=sayac+1 
#             os.rename(dosya,str(sayac)+uzanti)
# print(str(sayac) + ' Adet dosya ismi değiştirildi')
# import time

# print(str(time.ctime()))

s="GV-VT-00027_1-1"
s=s.split("_")
print(s[0])