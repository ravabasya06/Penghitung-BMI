def ulang():

    bb = int(input("Masukkan berat badan anda (kg) : "))
    tinggi = int(input("Masukkan tinggi badan anda (cm) : "))
    tinggiM = tinggi*0.01
    bmi = bb/(tinggiM*tinggiM)
    idealL = (tinggi - 100)-(tinggi - 100)*0.1
    idealP = (tinggi - 100)-(tinggi - 100)*0.15
    print("BMI anda adalah : "+str(bmi))
    if bmi > 23:
        print("Anda kelebihan berat badan, berat badan yang ideal untuk anda adalah : ")
        print("Laki-laki : "+str(idealL)+" kg")
        print("Perempuan : "+str(idealP)+" kg")
    elif bmi < 18.5:
        print("Anda kekurangan berat badan, berat badan yang ideal untuk anda adalah : ")
        print("Laki-laki : "+str(idealL)+" kg")
        print("Perempuan : "+str(idealP)+" kg")
    else:
        print("Berat badan anda normal")
    pengulangan = input("Lakukan perhitungan lagi? ya / tidak : ")
    
    if pengulangan == "ya":
        ulang()
    elif pengulangan == "tidak":
        print("Ok")
    else:
        print("Saya tidak mengerti perintah anda, saya akan menganggap anda menjawab tidak.")
ulang()