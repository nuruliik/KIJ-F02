import process_oop

proses = process_oop.process_oop()

pilihan = 0
while pilihan!='1' and pilihan!='2':
    print "Pilih metode :\n" \
          "1.Enkripsi\n" \
          "2.Dekripsi\n"
    pilihan = raw_input()

if pilihan=='1':
    print "Masukan text yang mau di enkripsi : \n"
    plaintext = raw_input()
    key = ""
    while(len(key)<8 or len(key)>8):
        print "Masukan key nya (HARUS DELAPAN KARAKTER) :\n"
        key = raw_input()
    proses.ofb_enkripsi(plaintext,key)

elif pilihan=='2':
    print "Masukan chipertext yang mau di enkripsi (DALAM BENTUK HEX) : \n"
    chipertext = raw_input()
    key = ""
    while (len(key) < 8 or len(key) > 8):
        print "Masukan key nya (HARUS DELAPAN KARAKTER) :\n"
        key = raw_input()
    proses.ofb_dekripsi(chipertext,key)
