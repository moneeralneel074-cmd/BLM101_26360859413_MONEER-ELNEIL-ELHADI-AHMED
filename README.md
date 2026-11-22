#  BLM101_26360859413_MONEER-ELNEIL-ELHADI-AHMED
# Öğrenci Bilgileri:
 öğrenci adı : MONEER ELNEIL ELHADI AHMED.
 öğrenci numarası : 26360859413. 
 # Proje Konusu : 
  Makine Döngüsü ve Akümülatör (Accumulator) CPU Simülatörü.
 # Kurulum ve çalıştırma :
* Bu projeyi çalıştırmak için bilgisayarınızda python kurulu olmalıdır.
* Gerekli python sürümü : python3.x(örneğin: python 3.14).
* Projeyi Github üzerinde indirin ve ´src´ klasörüne girin.
* Yöntem 1(Visual Studio Code):Dosyayı Visual Studio code ile açıp çalıştırabilirsiniz:  
* Yöntem 2(Terminal) : Terminal veya komut istemcisini bilgisayarınızdan açıp şu komutu yazarak programı çalıştırın:
* python "pyton projesi.py" 
# Algoritma ve çalışma mantığı : 
* 1 . Program başlanıcında akümülatör ('ak') ve program sayacı ('pc') tanımlanır.
* 2 . Sonsuz döngü ('while True ') içinde kullanıcıdan bir komut alınır ve 'lower()' ile küçük harfe çevilir.
* 3 . Komut 'halt' ise '"dur!"' mesajı yazdırılır ve döngü sonlandırır.
* 4 . Komut 'load','add','sub' veya 'mul' ise kullanıcıda bir tam sayı alınır ve ilgili işlem 'ak' üzerinde uygulanır.
* 'load': 'ak' değerini girilen sayı ile günceller.
* 'add' : 'ak' değerine girilen sayıyı ekler.
* 'sub' : 'ak' değeriniden girilen sayıyı çıkarır.
* 'mul' : 'ak' değerini girilen sayı ile çarpar.
* 5 . İşlem tamamlandığında 'pc' değeri 1 artırılır ve güncel 'pc' ile 'ak' değerleri ekrana yazdırılır.
* 6 . Geçersiz bir komut girilirse '"Geçersiz komut!"' yazdırılır ve 'pc' artırılmadan bir sonraki döngü adımına geçilir.
```  ## Örnek çalıştırma
  ´´´text
bir komut gir : load
bir sayı gir : 10
  pc = 2 | ak = 10 
```
 


