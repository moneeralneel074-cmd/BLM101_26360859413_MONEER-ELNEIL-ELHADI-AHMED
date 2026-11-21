ak = None #Akmülatör 
pc = 1  # program sayacı 
# komutları sürekli alıp işlmek için sonsuz döngü başlatılır.
while True:
    komut = input("Bir komut gir: ").lower() #kulanıcıdan komut alınır ve küçük harfe çevilir. 

    if komut == "halt":
        print("Dur!")
        break # programı sonlandırır ve dögüden çıkar.

    elif komut in ["load", "add", "sub", "mul"]:
        sayi = int(input("Bir sayi gir: "))  # işlem yapılacak tam sayıyı alınır. 

        if komut == "load":
            ak = sayi    # girilen sayıyı akmülatöre yükler.

        elif komut == "add":
            ak += sayi   # akmülatördeki değere sayıyı ekler.

        elif komut == "sub":
            ak -= sayi   # akmülatördeki değerden sayıyı çıkarır.

        elif komut == "mul":
            ak *= sayi   # akmülatördeki değeri sayı ile çarpar.

    else:
        print("Geçersiz komut!")
        continue # geçersiz komutta pc artırılmadan döngünün başına dönülür.
    # geçerli komut girdiğinde program sayacı 1 artırılır ve durum yazdırılır.
    pc += 1
    print(f"pc = {pc} | ak = {ak}")
    