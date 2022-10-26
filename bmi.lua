function ulang()
  
  io.write("Masukkan berat badan anda (kg) : ")
  berat = tonumber(io.read())
  io.write("Masukkan tinggi badan anda (cm) : ")
  tinggiCM = tonumber(io.read())
  tinggiM = tinggiCM*0.01
  bmi = berat/(tinggiM*tinggiM)
  idealL = (tinggiCM - 100)-(tinggiCM - 100)*0.1
  idealP = (tinggiCM - 100)-(tinggiCM - 100)*0.15
  
  print("BMI anda adalah : "..tostring(bmi))
  
  if bmi > 23 then
    print("Anda kelebihan berat badan, berat badan yang ideal untuk anda adalah : ")
    print("Laki-laki : "..tostring(idealL).." kg")
    print("Perempuan : "..tostring(idealP).." kg")
  elseif bmi < 18.5 then
    print("Anda kekurangan berat badan, berat badan yang ideal untuk anda adalah : ")
    print("Laki-laki : "..tostring(idealL).." kg")
    print("Perempuan : "..tostring(idealP).." kg")
  else
     print("Berat badan anda normal")
  end
  
  io.write("Lakukan perhitungan lagi? ya / tidak : ")
  pengulangan = io.read()
      
  if pengulangan == "ya" then
    ulang()
  elseif pengulangan == "tidak" then
    print("Ok")
  else
    print("Saya tidak mengerti perintah anda, saya akan menganggap anda menjawab tidak.")
  end
end
ulang()
