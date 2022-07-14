#Ran
#careless
#susu beruang
'''
Nama file : Kuis 
Nama      : FRANS BACHTIAR
Npm       : 2024240041
Jurusan   : Sistem Informasi
kelas     : SI 1B
tanggal   : 09-12-2020
Deskripsi : Menghitung besarnya uang kuliah
'''
#variable method
xNpm=xNama=xKelas=xSKS=xBeasiswa=0

#deklarasi method
def inputdata():
    global xNpm,xNama,xKelas,xSKS,xBeasiswa
    print("===============================================================================================================")
    xNpm = int(input('NPM               : '))
    xNama = str(input('Nama              : '))
    xKelas = input('Kelas(Pagi/Malam) : ')
    xSKS = int(input('Jumlah SKS        : '))
    xBeasiswa = int(input('Beasiswa          : '))
    print("===============================================================================================================")
#MENGHITUNG UANG MENGGUNAKAN METHOD
def hitunguang(xKelas):
    if xKelas== 'pagi' or xKelas == 'PAGI' :
        tarif = 100
    elif xKelas == 'malam' or xKelas == 'MALAM' :
        tarif = 150
#=====RUMUS ATAU KODE UNTUK MENGHITUNG RINCIAN UANG===========#    
    total = tarif * xSKS
    beasiswa = total * (xBeasiswa / 100)
    uang = total - beasiswa
#MEMBUAT RINCIAN UANG KULIAH
    print(xNpm,' Dengan Nama ',xNama,' Uang Kuliah Anda Sebesar ',uang)
    print('Dengan rincian : ')
    print("============================")
    print('Uang per SKS      : ',tarif)
    print('Sub Total         : ',total)
    print('Potongan Beasiswa : ',beasiswa)
    print("============================")
    return xKelas

#====UNTUK MEMBUAT TAMPILAN MENU UNTUK PROGRAM=======
def menu():
    print()
    print('    *Hitung uang kuliah*')
    print('===========================')
    print('| [1]. Input data         |')
    print('| [2]. Tampil Uang kuliah |')
    print('| [3]. Keluar             |')
    print("===========================")
    pilihan = input('Pilihan Anda : ')
#VARIABLE UNTUK TAMPILAN MENU
    if pilihan == '1':
        print()
        inputdata()
        menu()
    elif pilihan == '2':
        print()
        hitunguang(xKelas)
        menu()
        print()
    elif pilihan == '3':
        exit()
    else:
        print("                                      /----------/ ")
        print('$Keyword yang anda masukkan salah     |  +   +  |')
        print("                                     <|    -    |>")
        print("                                      |_________|")
        print("                                         |   |")
#PEMANGGILAN METHOD
menu()

#exit
#susu beruang
#pain today pride tomorrow
