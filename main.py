import os
import getpass
import datetime as dt
hari_ini = dt.datetime.today()  
from colorama import Fore, Style

class Karyawan:
    list_kry = []
    id_kry = 0

    def __init__(self, id, nama, umur, alamat, email, no_hp):
        self.id = id
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.email = email
        self.no_hp = no_hp

        Karyawan.id_kry += 1

    def getId(self):
        return self.id

    def setNama(self,nama):
        self.nama = nama
    def getNama(self):
        return self.nama
    
    def setUmur(self,umur):
        self.umur = umur
    
    def setAlamat(self,alamat):
        self.alamat = alamat
    
    def setEmail(self,email): 
        self.email = email

    def setNohp(self,nohp):
        self.no_hp = nohp
        
    def info(self):
        print('ID \t\t:', self.id )
        print('Nama\t\t:', self.nama)
        print('Umur\t\t:', self.umur)
        print('Alamat\t\t:', self.alamat)
        print('Email\t\t:', self.email)
        print('No. Hp\t\t:', self.no_hp)

class Divisi(Karyawan):
    data_pengajuan = []
    obj_pengajuan = []

    def __init__(self, id, nama, umur, alamat, email, no_hp, divisi, gaji, status):
        super().__init__(id, nama, umur, alamat, email, no_hp)
        self.divisi = divisi
        self.__gaji = gaji
        self.status = status
    
    def setDivisi(self,divisi):
        self.divisi = divisi

    def setGaji(self,gaji):
        self.__gaji = gaji

    def setStatus(self,status):
        self.status = status
    def getStatus(self):
        return self.status
    
    def info(self):
        super().info()
        print('Divisi\t\t:',self.divisi)
        print('Gaji\t\t: Rp.',self.__gaji)
        print('Status\t\t:',self.status)

    def pengajuan(self):
        text = '===== Pengajuan =====\n'  
        print(text.center(66))
        ket = input('Keterangan\t\t: ')
        mTgl = input('Mulai Tgl [dd/mm/yy]\t: ')
        sTgl = input('sampai Tgl [dd/mm/yy]\t: ')

        f = open("pengajuan.txt", "a")
        f.write('\n')
        f.write(hari_ini.strftime('%a, %b %d %Y %X') + '\n')
        f.write('ID           : '+ self.id +'\n')
        f.write('Nama         : '+ self.nama +'\n')
        f.write('No Hp        : '+ self.no_hp +'\n')
        f.write('Divisi       : '+ self.divisi +'\n')
        f.write('Keterangan   : ' + ket +'\n')
        f.write('Mulai Tgl    : ' + mTgl +'\n')
        f.write('Sampai tgl   : ' + sTgl +'\n\n')
        f.close()

        for h in data_login:
            Divisi.data_pengajuan.append(ket)
            Divisi.obj_pengajuan.append(h)

        os.system('cls')
        print(Fore.GREEN +'Menunggu Verifikasi' + Style.RESET_ALL)

class Admin(Divisi):
    def __init__(self, id, nama, umur, alamat, email, no_hp, divisi, gaji, status):
        super().__init__(id, nama, umur, alamat, email, no_hp, divisi, gaji, status)
    
    def cekId(self,id):
        for e in Karyawan.list_kry:
            if e.getId() == id:
                return e

    def tambahData(self):
        os.system('cls')
        text = '===== INPUT DATA BARU ======\n'
        print(text.center(66))
        id = str(Karyawan.id_kry)
        nama = input("Nama\t\t: ")
        umur = input("Umur\t\t: ")
        alamat = input("Alamat\t\t: ")
        email = input("Email\t\t: ")
        no_hp = input("No. HP\t\t: ")
        divisi = input("Divisi\t\t: ")
        gaji = input("Gaji\t\t: Rp.")
        status = input("Status\t\t: ")
        obj = Divisi(id,nama,umur,alamat,email,no_hp,divisi,gaji,status)
        Karyawan.list_kry.append(obj)  

        lagi = input('\n\nInput Data lagi [y/n] > ')
        if lagi != 'y':
            os.system('cls')
            print(Fore.GREEN + 'Data Berhasil Ditambah' + Style.RESET_ALL)
            menu_utama_hrd()

    def ubahData(self):
        text = '====== UBAH DATA =====\n'
        print(text.center(66))
        id_cari = input('\nMasukan ID\t: ')
        e = obj.cekId(id_cari)
        if e == None:
            os.system('cls')
            print()
            print(Fore.RED +'ID TIDAK DITEMUKAN' + Style.RESET_ALL)
        else:
                print(f'''
            +==========================================+
            |   [1] Nama                               |
            |   [2] Umur                               |
            |   [3] Alamat                             |
            |   [4] Email                              |
            |   [5] No. Hp                             |
            |   [6] Divisi                             |
            |   [7] Gaji                               |
            |   [8] Status                             |
            +==========================================+
            ''')
                try: 
                    pilihan = int(input('\nPiihan\t\t: '))
                    if pilihan == 1:
                        data_baru = input('Nama Baru\t: ')
                        e.setNama(data_baru)
                        os.system('cls')
                        print(Fore.GREEN +'Nama Berhasil Diubah' + Style.RESET_ALL)
                    elif pilihan == 2:
                        data_baru = input('Umur Baru\t: ')
                        e.setUmur(data_baru) 
                        os.system('cls')
                        print(Fore.GREEN +'Umur Berhasil Diubah' + Style.RESET_ALL)
                    elif pilihan == 3:
                        data_baru = input('Alamat Baru\t: ')
                        e.setAlamat(data_baru) 
                        os.system('cls')
                        print(Fore.GREEN +'Alamat Berhasil Diubah' + Style.RESET_ALL)
                    elif pilihan == 4:
                        data_baru = input('Email Baru\t: ')
                        e.setEmail(data_baru) 
                        os.system('cls')
                        print(Fore.GREEN +'Email Berhasil Diubah' + Style.RESET_ALL)
                    elif pilihan == 5:
                        data_baru = input('No.Hp Baru\t: ')
                        e.setNohp(data_baru) 
                        os.system('cls')
                        print(Fore.GREEN +'No. Hp Berhasil Diubah' + Style.RESET_ALL)
                    elif pilihan == 6:
                        data_baru = input('Divisi Baru\t: ')
                        e.setDivisi(data_baru) 
                        os.system('cls')
                        print(Fore.GREEN +'Divisi Berhasil Diubah' + Style.RESET_ALL)
                    elif pilihan == 7:
                        data_baru = input('Gaji Baru\t: ')
                        e.setGaji(data_baru) 
                        os.system('cls')
                        print(Fore.GREEN +'Gaji Berhasil Diubah' + Style.RESET_ALL)
                    elif pilihan == 8:
                        data_baru = input('Status Baru\t: ')
                        e.setStatus(data_baru) 
                        os.system('cls')
                        print(Fore.GREEN +'Status Berhasil Diubah' + Style.RESET_ALL)
                    else:
                        os.system('cls')
                        print(Fore.RED + 'Pilihan Salah!' + Style.RESET_ALL)
                except ValueError:
                    os.system('cls')
                    print(Fore.RED + 'Masukan Angka' + Style.RESET_ALL)

                os.system('cls')
                print(Fore.GREEN +'Data Berhasil Dihapus '+ Style.RESET_ALL)
                menu_utama_hrd()

    def hapusData(self):
        text = '===== HAPUS DATA =====\n'
        print(text.center(66))
        id_cari = input('\nMasukan ID\t: ')
        e = obj.cekId(id_cari)

        if e == None:
            os.system('cls')
            print()
            print(Fore.RED +'ID TIDAK DITEMUKAN' + Style.RESET_ALL)
        else:
            print()
            Karyawan.list_kry.remove(e)
            os.system('cls')
            print(Fore.GREEN +'Data Berhasil Dihapus '+ Style.RESET_ALL)
        menu_utama_hrd()
        
    def tampilData(self):
        text = '===== INFORMASI KARYAWAN =====\n'
        print(text.center(66))

        if len(data_login) != 0:
            for h in data_login:
                h.info()
            input('\nMenu [Enter] > ')
            os.system('cls')
            menu_utama_karyawan()
        else:
            print('Jumlah\t\t: ', len(Karyawan.list_kry))
            print()
            for i in Karyawan.list_kry:
                i.info()
                print()
            input('Menu [Enter] > ')
            os.system('cls')
            menu_utama_hrd()

    def cariData(self):
        text = '====== PENCARIAN DATA =====\n'
        print(text.center(66))
        id_cari = input('\nMasukan ID\t: ')
        e = obj.cekId(id_cari)
        if e == None:
            os.system('cls')
            print()
            print(Fore.RED +'ID TIDAK DITEMUKAN' + Style.RESET_ALL)
            menu_utama_hrd()
        else:
            print()
            e.info()

            input('\n\nMenu [Enter] > ')
            os.system('cls')
            menu_utama_hrd()

    def verifikasi(self):
        f = open("pengajuan.txt", "r")
        print(f.read())
        if len(Divisi.data_pengajuan) != 0:
            for i in Divisi.obj_pengajuan:
                acc = input('Verivikasi ID {} [y/n] > '.format(i.getId()))
                if acc == 'y':
                    f = open("pengajuan.txt", "a")
                    f.write('Status ID {}  : Terverifikasi\n'.format(i.getId()))
                    f.close()
                    str = ''.join(Divisi.data_pengajuan[0])
                    i.setStatus(str)
                    Divisi.data_pengajuan.pop(0)
                else:
                    f = open("Pengajuan.txt", "a")
                    f.write('Status ID {}  : Tidak Terverifikasi\n'.format(i.getId()))
                    f.close()
                    Divisi.data_pengajuan.pop(0)
            Divisi.obj_pengajuan.clear()
            
        else:
            os.system('cls')
            print(Fore.YELLOW +'Tidak Ada Data Yang Perlu Diverifikasi!' + Style.RESET_ALL)
            menu_utama_hrd()
            
        input('Menu [Enter] > ')
        os.system('cls')
        menu_utama_hrd()
    
    def infoPengajuan(self):
        f = open("pengajuan.txt", "r")
        print(f.read())

        input('Menu [Enter] > ')
        os.system('cls')
        menu_utama_hrd()

obj = Admin('','','','','','','','','')
a = Admin(str(Karyawan.id_kry),'Andi','20','Wonogiri','andi77@gmail.com','082123456789','IT','5.400.000','Aktif')
b = Admin(str(Karyawan.id_kry),'Budi','18','Sumatra Utara','budi@gmail.com','08210023028','IT','5.250.000','Aktif')
c = Admin(str(Karyawan.id_kry),'Caca','21','Yogyakarta','caca@gmail.com','08221267432','IT','5.000.000','Aktif')
data_obj = [a,b,c]
for i in data_obj:
    Karyawan.list_kry.append(i) 

data_username = [a.nama,b.nama,c.nama]
data_passw = ['1','2','3']
data_login = []

def menu_login():
    os.system('cls')
    while True:
        try:
            print(f'''
                                HRDQ
            +==========================================+
            |               [1] Masuk                  |
            +==========================================+
            |               [0] Keluar                 |
            +==========================================+
            ''')
            pilihan = int(input('\nPilihan > '))
            os.system('cls')
            if pilihan == 1:
                login()
            elif pilihan == 0:
                print(Fore.GREEN + 'Terima Kasih' + Style.RESET_ALL)
                exit()
            else:
                print(Fore.RED + 'Pilihan Salah' + Style.RESET_ALL)
        except ValueError:
            os.system('cls')
            print(Fore.RED + 'Masukan Angka' + Style.RESET_ALL)

def login():
    u = 0
    while u < 3:
        print('===== Login ====='.center(60))
        username = input('\nUsername\t: ')
        pw = getpass.getpass('Password\t: ')
        os.system('cls')
        if u == 2:
            print(Fore.RED + '3x Salah!' + Style.RESET_ALL)
            break
        if username == 'admin' and pw == 'admin':
            if len(Divisi.data_pengajuan) != 0:
                print(Fore.YELLOW +'Pengajuan {}'.format(len(Divisi.data_pengajuan)) + Style.RESET_ALL)
                menu_utama_hrd()
            else:
                menu_utama_hrd()
        elif username in data_username and pw in data_passw:
            for i in Karyawan.list_kry:
                if i.getNama() == username:
                    print('Selamat Datang,',username)
                    data_login.append(i)
                    menu_utama_karyawan()
        elif username in data_username and pw not in data_passw:
            os.system('cls')
            print(Fore.RED + 'Password Salah!' + Style.RESET_ALL)
            lagi = input('Coba Lagi? [y/n]> ')
        elif username not in data_username and pw in data_passw:
            os.system('cls')
            print(Fore.RED + 'Username Salah!' + Style.RESET_ALL)
            lagi = input('Coba Lagi? [y/n]> ')
        else:
            os.system('cls')
            print(Fore.RED + 'Akun tidak terdaftar!' + Style.RESET_ALL)
            break
    
        os.system('cls')
        if lagi == 'n':
            break
        u += 1

def menu_utama_hrd():
    while True:
        try: 
            print(f'''
                                HRDQ

            +==========================================+
            |   [1] Tambah Data                        |
            |   [2] Tampil Data                        |
            |   [3] Hapus Data                         |
            |   [4] Cari Data                          |
            |   [5] Ubah Data                          |
            |   [6] Verifikasi                         |
            |   [7] Info Pengajuan                     |
            |   [0] Keluar                             |
            +==========================================+
            ''')
            input_menu = int(input('\nPilihan > '))
            os.system('cls')
            for i in Karyawan.list_kry:
                if input_menu == 1:
                        i.tambahData()
                elif input_menu == 2:
                        i.tampilData()
                elif input_menu == 3:
                        i.hapusData()
                elif input_menu == 4:
                        i.cariData()
                elif input_menu == 5:
                        i.ubahData()
                elif input_menu == 6:
                        i.verifikasi()
                elif input_menu == 7:
                        i.infoPengajuan()
                elif input_menu == 0:
                    menu_login()
                else:
                    print(Fore.RED + 'Pilihan Salah!' + Style.RESET_ALL)
        except ValueError:
            os.system('cls')
            print(Fore.RED + 'Masukan Angka' + Style.RESET_ALL)

def menu_utama_karyawan():
    while True:
        try:
            print(f'''
                                HRDQ

            +==========================================+
            |   [1] Profil                             |
            |   [2] Pengajuan                          |
            |   [0] Keluar                             |
            +==========================================+
            ''')
            inp_menu = int(input('\nPilihan > '))
            os.system('cls')
            if inp_menu == 1:
                for i in Karyawan.list_kry:
                    i.tampilData()
            elif inp_menu == 2:
                for i in data_login:
                    i.pengajuan()
            elif inp_menu == 0:
                data_login.pop(0)
                menu_login()
            else:
                print(Fore.RED + 'Pilihan Salah!' + Style.RESET_ALL)
        except ValueError:
            os.system('cls')
            print(Fore.RED + 'Masukan Angka' + Style.RESET_ALL)

menu_login()