import random
from test import Welcome_message


Welcome_message("Selamat Datang Di BEE Games")

nama_user = input("masukan nama: ")
while nama_user == "":
    nama_user= input("woyy isi nama lu dulu:")


while True:
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4 #ini tete kosong
    bee_position = random.randint(1, 4)

    goa = goa_kosong.copy() # ini tmpt si bee
    goa[bee_position - 1] = "|0_0|"

    goa_kosong = ' '.join(goa_kosong)
    goa = ' '.join(goa)

    print(f'''
    Halo {nama_user}! Coba perhatikan goa dibawah ini
    {goa_kosong}
    ''')

    pilihan_user = int(input("menurut kamu di goa nomor berapa BEE berada? [1 / 2 / 3 / 4] "))

    confirm_answer = input(f"apakah kamu yakin adalah {pilihan_user}? [y/n]: ")

    if confirm_answer == "n":
        print("program dihentikan!")
        exit()
    elif confirm_answer == "y":
        if pilihan_user == bee_position:
            print(f"{goa} \n Selamat kamu menang 🏆.")
        else:
            print(f"{goa} \n kamu kalah 🙊")
    else:
        print("silahkan ulangi programnya")
        exit()
    
    play_again = input("\n\nApakah ingin melanjutkan gamenya lagi? [y/n]")
    if play_again == "n":
        break
print("program selesai")
