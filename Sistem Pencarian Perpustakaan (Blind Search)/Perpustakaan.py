judulBuku = {
    'HBTT':['DTM','NSI'],
    'DTM':['PMW','PBO'],
    'NSI':['DBL','AND'],
    'PMW':['SDG','BDD'],
    'PBO':['MLI','BDL'],
    'DBL':[],
    'AND':[],
    'SDG':[],
    'BDD':[],
    'MLI':[],
    'BDL':[]
}
#------------------------------------------------------------------
def menu ():
    import os
    os.system ("CLS")
    print("     SELAMAT DATANG DI PROGRAM PEPUSTAKAAN")
    print("Pilih daftar menu untuk mengakses program :\n")
    print("[1] Lihat Daftar Buku")
    print("[2] Cari Buku")
    print("[3] Keluar")

    code = int(input("\n Masukkan Pilihan Anda : "))
    pilihmenu(code)
#--------------------------------------------------------------------
def pilihmenu(p):
    if p == 1 :
        daftarBuku()
    elif p == 2 :
        mainDLS()
    elif p == 3 :
        keluar()
    else :
        print("\n Pilihan Yang Anda Masukkan Tidak Tersedia!!")
#--------------------------------------------------------------------
def daftarBuku():
    import os
    os.system("CLS")
    print("\n Daftar Buku Yang Tersedia : ")
    print(
        "Berikut Keterangan Singkatan yang Tersedia\n",
        "HBTT : Habis Gelap Terbitlah Terang\n",
        "DTM : Detective Conan Movie\n",
        "NSI : Nashoihul Ibad\n",
        "PMW : Pemrograman Website\n",
        "PBO : Pemrograman Berorientasi Objek\n",
        "DBL : Database Learning\n",
        "AND : Android Developer\n",
        "SDG : Sistem Digital\n",
        "BDD : Basis Data Dasar\n",
        "MLI : Machine Learning\n",
        "BDL : Basis Data Lanjut\n"
    )
    print("Press Enter to Back Main Menu!")
    input()
    menu()
#--------------------------------------------------------------------
def DLS(start, goal, path, level, maxD):
    print('Level Node Sekarang-',level)
    print('Node Tujuan Pengetesan-',start)
    path.append(start)
    if start == goal:
        print("Test Node Tujuan Sukses!!!")
        return path
    print('Test Node Tujuan Gagal!!!')
    if level == maxD:
        return False;
    print('\nMencari Node Saat ini', start)
    for child in judulBuku[start]:
        if DLS(child, goal, path, level+1, maxD):
            return path
        path.pop()
    return False
#--------------------------------------------------------------------
def mainDLS():
    import os
    os.system("CLS")
    start = 'HBTT'
    goal = input('Masukkan Node Tujuan-')
    maxD = int(input("Masukkan Limit Nilai Maksimal Kedalaman-"))
    print()
    path = list()
    res = DLS(start, goal, path, 0, maxD)
    if(res):
        print("Path ke Node Tujuan Tersedia!")
        print("Path",path)
    else:
        print("Tidak ada Path yang tersedia untuk Node Tujuan Yang Telah Diberikan Depth Limit")
    print("Press Enter to Back Main Menu!")
    input()
    menu()
#--------------------------------------------------------------------
def keluar():
    import os
    print("Bye-Bye NADIA Beach")
    os.system("PAUSE")
    exit()