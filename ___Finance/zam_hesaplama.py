#coded by oguzkaba

# MAAŞ Zam Hesaplama

eski_Banka=input("'Eski'- Bankaya yatan(AGİ dahil) :")
yeni_Banka=input("'Yeni'- Bankaya yatan(AGİ dahil) :")

elden_eski=input("'Eski'- Nakit alınan :")
elden_yeni=input("'Yeni'- Nakit alınan :")

eski_maas=float(eski_Banka)+float(elden_eski)
yeni_maas=float(yeni_Banka)+float(elden_yeni)

sonuc_tl=yeni_maas-eski_maas
sonuc_yuzde=(sonuc_tl/eski_maas)*100

print("Yapılan zam: %" +str(round(sonuc_yuzde,1))+"  ,  "+ str(sonuc_tl)+"TL" )
print("'Yeni' maaş: "+str(yeni_maas)+" TL")
print("'Eski' maaş: "+str(eski_maas)+" TL")