import argparse, sys, os, variabelGlobal, dashboard, validasi, user
#Mengambil argumen yang diberikan melalui CLI
parser = argparse.ArgumentParser()
parser.add_argument("namaFolder")
args = parser.parse_args()
folderDir = args.namaFolder

os.chdir('saves')
if not os.path.isdir(folderDir) :
    print('Nama folder tidak valid')
    sys.exit()

#PROSEDUR UNTUK LOAD DATA
variabelGlobal.Load(folderDir)

#WAJIB LOGIN TERLEBIH DAHULU
while True: # Akan terus mengulang sampe username dan password yang dimasukkan sesuai
    print("======= Login =======")
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if validasi.isCredentialValid(username,password):
            print('Halo {}!, Selamat datang di Kantong Ajaib.'.format(username))
            role = user.checkRole(username)
            break
    print("Username atau password mungkin salah")
    
variabelGlobal.username = username
variabelGlobal.role = role
#Ketika berhasil login, username pengguna disimpan di variabel 'username' dan id pengguna yang bersangkutan
#disimpan di variabel 'id_user' (dideklarasi di dalam fungsi isUsernameValid)
dashboard.Show(role)

