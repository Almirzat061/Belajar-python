 # fungsi sewa lapangan
def lapangan():
     print("""
              selamat datang di lapangan futsal nosepa !
              berikut daftar lapangan yang tersedia :
              1. Lapangan matras besar Rp. 80.000/ jam
              2. Lapangan matras kecil Rp. 70.000/ jam
              3. Lapangan semen  besar Rp. 50.000/ jam
              4. lapangan semen  kecil Rp. 45.000/ jam

              apakah anda ingin sewa lapangan? 
              tekan (1) jika ingin sewa tekan (2) jika ingin keluar !
              """)
     pilih_lapangan   = int(input("masukan pulihan : "))
     if pilih_lapangan == 1 :
        pilihku = int(input("masukan lapangan pilihan anda : "))
        jam = int(input("berapa jam? : "))
        print ("terima kasih !")
        cetak_struk = int(input("apakahanda ingin mencetak struk ? tekan (1) jika ya tekan (2) jika tidak "))
        if (cetak_struk == 1):
          data = open("data.txt","w")
          data_sewa = open("pesan.txt","a")
          if pilihku == 1:
            # di cetak untuk penyewa 
             data.write("Lapangan =  " + str(pilihku) + "\n")
             data.write("Jam = " + str(jam) + " jam \n")
             totalpesan = 80000 * jam 
             data.write("total = " + "Rp. " + str(totalpesan)+ "\n")
            # dicetak untuk di lihat pemilik lapangan
             data_sewa.write("Lapangan =  " + str(pilihku) + "\n")
             data_sewa.write("Jam = " + str(jam) + " jam \n")
             totalpesan = 80000 * jam 
             data_sewa.write("total = " + "Rp. " + str(totalpesan)+ "\n")
             data.close()
             data_sewa.close()
          if pilihku == 2:
            # mencetak sruk untuk penyewa
             data.write("Lapangan =  " + str(pilihku) + "\n")
             data.write("Jam = " + str(jam) + " jam \n")
             totalpesan = 70000 * jam 
             data.write("total = " + "Rp. " + str(totalpesan)+ "\n")
             # mencetak struk untuk pemilik 
             data_sewa.write("Lapangan =  " + str(pilihku) + "\n")
             data_sewa.write("Jam = " + str(jam) + " jam \n")
             totalpesan = 70000 * jam 
             data_sewa.write("total = " + "Rp. " + str(totalpesan)+ "\n")
             data.close()
             data_sewa.close()
          if pilihku ==3:
            # mencetak struk untuk penyewa
             data.write("Lapangan =  " + str(pilihku) + "\n")
             data.write("Jam = " + str(jam) + " jam \n")
             totalpesan = 50000 * jam 
             data.write("total = " + "Rp. " + str(totalpesan)+ "\n")
             data.close()
            # mencetakstruk untuk pemilik
             data_sewa.write("Lapangan =  " + str(pilihku) + "\n")
             data_sewa.write("Jam = " + str(jam) + " jam \n")
             totalpesan = 50000 * jam 
             data_sewa.write("total = " + "Rp. " + str(totalpesan)+ "\n")
             data_sewa.close()
          if pilihku ==4:
            # mencetak struk untuk penyewa
             data.write("Lapangan =  " + str(pilihku) + "\n")
             data.write("Jam = " + str(jam) + " jam \n")
             totalpesan = 45000 * jam 
             data.write("total = " + "Rp. " + str(totalpesan)+ "\n")
             data.close()
             # mencetakstruk untuk pemilik
             data_sewa.write("Lapangan =  " + str(pilihku) + "\n")
             data_sewa.write("Jam = " + str(jam) + " jam \n")
             totalpesan = 45000 * jam 
             data_sewa.write("total = " + "Rp. " + str(totalpesan)+ "\n")
             data_sewa.close()
          if pilihku > 4 :
             print("inputan yang anda masukan salah")
          else :
            print("Terima kasih sudah menyewa lapangn kami :) ")
        if (cetak_struk == 2):
          print("Terima kasih sudah menyewa lapangan kami :) ")
     else :
       print(" Terima kasih ") 

# fungsi melihat daftar lapangan
def pilihanlapangan():
    print("""
              selamat datang di lapangan futsal nosepa !
              berikut daftar lapangan yang tersedia :
              1. Lapangan matras besar Rp. 80.000/ jam
              2. Lapangan matras kecil Rp. 70.000/ jam
              3. Lapangan semen  besar Rp. 50.000/ jam
              4. lapangan semen  kecil Rp. 45.000/ jam

              """)
  i = True
while (i == True):
    print("""
    Lapangan Futsal NOSEPA 
      1. Sewa Lapangan 
      2. Lihat daftar Lapangan  
     """)
    pilih = int(input("pilih : "))
    if (pilih ==  1):    
        lapangan() # memangil fungsi sewa lapangan 
    
    if (pilih == 2): 
        pilihanlapangan() # memanggil fungsi melihat daftar lapangan
    if (pilih > 2):
       print ("pilihan yang anda masukan salah !")   
i = False
   
