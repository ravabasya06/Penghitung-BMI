def ulang():

    berat = int(input("Masukkan berat badan anda (kg) : "))
    tinggiCM = int(input("Masukkan tinggi badan anda (cm) : "))
    tinggiM = tinggiCM*0.01
    bmi = berat/(tinggiM*tinggiM)
    idealL = (tinggiCM - 100)-(tinggiCM - 100)*0.1
    idealP = (tinggiCM - 100)-(tinggiCM - 100)*0.15
    bmiR = round(bmi, 2)
    print("BMI anda adalah : "+str(bmiR))
    if bmiR > 23:
        print("Anda kelebihan berat badan, berat badan yang ideal untuk anda adalah : ")
        print("Laki-laki : "+str(idealL)+" kg")
        print("Perempuan : "+str(idealP)+" kg")
    elif bmiR < 18.5:
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
