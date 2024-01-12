import os
from functools import reduce
import matplotlib.pyplot as plt

def is_prima(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

def is_palindrome(string):
            cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
            return cleaned_string == cleaned_string[::-1]

def switch_case_menu(option):
    if option == 1:
        os.system('cls')
        print("1. Sequence\n")
        data_tuple = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

        def separate_data(data):
            nama = []
            harga = []
            for i in range(0, len(data), 2):
                nama.append(data[i])
            for i in range(1, len(data), 2):
                harga.append(data[i])
            return nama, harga

        def create_dictionary(nama, harga):
            result_dict = {}
            for i in range(len(nama)):
                result_dict[nama[i]] = harga[i]
            return result_dict

        separated_data = separate_data (data_tuple)
        combined_dict = create_dictionary(separated_data[0], separated_data[1])

        print(f"\n1. Data tuple\t\t\t: {data_tuple}")
        print(f"2. Data yang telah dipisah\t:{separated_data}")
        print(f"3. Data Gabungan\t\t:{combined_dict}")
        input("\n\nTekan Enter untuk kembali ke menu...")
        os.system('cls')

    elif option == 2:
        

        while True:
            os.system('cls')
            print("Menu\t:")
            print("1. Cek Bilangan Prima")
            print("2. Cek Palindrome")
            print("0. Keluar")

            try:
                menu_option = int(input("Masukkan pilihan menu (0 - 2): "))
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                continue

            if menu_option == 0:
                os.system('cls')
                break

            elif menu_option == 1:
                angka = int(input("Masukkan angka: "))
                result = is_prima(angka)
                print(f"Hasil: {result}")
                input("\n\nTekan Enter untuk kembali ke menu...")
                os.system('cls')

            elif menu_option == 2:
                kata = input("Masukkan kata atau kalimat: ")
                result = is_palindrome(kata)
                print(f"Hasil: {result}")
                input("\n\nTekan Enter untuk kembali ke menu...")
                os.system('cls')

            else:
                print("Opsi tidak valid. Pilih 0, 1, atau 2.")

    elif option == 3:
        os.system('cls')
        print("3. Pure Function\n")
        def tambah_angka(angka, total=0):
            return total + angka

        while True:
            total = int(input("Masukkan nilai total awal\t: "))

            while True:
                angka = int(input("Masukkan angka yang ingin ditambahkan (0 untuk keluar, -1 untuk ulang)\t: "))
                os.system('cls')

                if angka == 0:
                    os.system('cls')
                    break
                elif angka == -1:
                    os.system('cls')
                    total = int(input("Masukkan nilai total awal untuk mengulang dari awal\t: "))
                else:
                    total = tambah_angka(angka, total)
                    print(f"Total sekarang: {total}")

            print("Yakin Ingin keluar ?")
            print("1. Tidak")
            print("0. Yakin")
            
            pilihan = input("Masukkan pilihan: ")
            if pilihan == '0':
                os.system('cls')
                break

    elif option == 4:

        while True:
            os.system('cls')
            print("4. Lambda\n")
            print("Menu\t:")
            print("1. Easy")
            print("2. Hard")
            print("0. Keluar")

            try:
                menu_option = int(input("Masukkan pilihan menu (0 - 2): "))
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                break

            if menu_option == 0:
                os.system('cls')
                break

            elif menu_option == 1:
                def tambah_angka(angka, total=0):
                    return total + angka

                while True:
                    total = int(input("Masukkan nilai total awal\t: "))

                    while True:
                        angka = int(input("Masukkan angka yang ingin ditambahkan (0 untuk keluar, -1 untuk ulang)\t: "))
                        os.system('cls')

                        if angka == 0:
                            os.system('cls')
                            break
                        elif angka == -1:
                            os.system('cls')
                            total = int(input("Masukkan nilai total awal untuk mengulang dari awal\t: "))
                        else:
                            total = tambah_angka(angka, total)
                            print(f"Total sekarang: {total}")

                    print("Yakin Ingin keluar ?")
                    print("1. Tidak")
                    print("0. Yakin")
                        
                    pilihan = input("Masukkan pilihan: ")
                    if pilihan == '0':
                        os.system('cls')
                        break

            elif menu_option == 2:
                    klasifikasi_angka = lambda x: "Positif" if x > 0 else ("Negatif" if x < 0 else "Nol")
                    pencarian_angka = lambda list_angka, find: "found" if find in list_angka else "not found"

                    while True:
                        os.system('cls')
                        print("Menu\t:")
                        print("1. Klasifikasi Angka")
                        print("2. Pencarian Angka")
                        print("0. Keluar")

                        try:
                            sub_menu_option = int(input("Masukkan pilihan menu (0 - 2): "))
                        except ValueError:
                            print("Input tidak valid. Masukkan angka.")
                            break

                        if sub_menu_option == 0:
                            os.system('cls')
                            break

                        elif sub_menu_option == 1:
                            angka = int(input("Masukkan angka: "))
                            result = klasifikasi_angka(angka)
                            print(f"Hasil: {result}")
                            input("\n\nTekan Enter untuk kembali ke menu...")
                            os.system('cls')

                        elif sub_menu_option == 2:
                            list_angka = input("Masukkan list angka (pisahkan dengan spasi): ").split()
                            find = input("Masukkan angka yang ingin dicari: ")
                            result = pencarian_angka(list_angka, find)
                            print(f"Hasil: {result}")
                            input("\n\nTekan Enter untuk kembali ke menu...")
                            os.system('cls')

                        else:
                            print("Opsi tidak valid. Pilih 0, 1, atau 2.")
            else:
                print("Opsi tidak valid. Pilih 0, 1, atau 2.")
                        
    elif option == 5:
        os.system('cls')
        print("5. List Comprehension\n")
        angka_list = []
        jenis_angka = input("Cari ganjil/genap\t: ").lower()
        start = int(input("Masukkan batas bawah\t: "))
        end = int(input("Masukkan batas atas\t: "))

        # List Comprehension
        if jenis_angka == "ganjil":
            angka_list = [x for x in range(start, end + 1) if x % 2 != 0]
        elif jenis_angka == "genap":
            angka_list = [x for x in range(start, end + 1) if x % 2 == 0]
        else:
            print("Jenis angka tidak valid. Pilih 'ganjil' atau 'genap'.")
            
        print("List angka", jenis_angka, "pada rentang ", start, "sampai", end, "adalah\t: ", angka_list )
        input("\n\nTekan Enter untuk kembali ke menu...")
        os.system('cls')
        
    elif option == 6:
        os.system('cls')
        print("6. Generator Expression")
        jenis_angka = input("Cari ganjil/genap: ").lower()
        start = int(input("Masukkan batas bawah: "))
        end = int(input("Masukkan batas atas: "))
        
        generator_angka = (x for x in range(start, end + 1) if (jenis_angka == "ganjil" and x % 2 != 0) or (jenis_angka == "genap" and x % 2 == 0))
        print("List angka", jenis_angka, "pada rentang ", start, "sampai", end, "adalah\t: ",", ".join(map(str, generator_angka)))
        input("\n\nTekan Enter untuk kembali ke menu...")
        os.system('cls')

    elif option == 7:
        os.system('cls')
        print("7. Higher Order Function\n")
        def sisagold(a, b, fungsi_kurang):
            return fungsi_kurang(a, b)

        def kurang(x, y):
            return x - y

        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))

        hasil = sisagold(a, b, kurang)
        print(f"Hasil sisagold dengan fungsi kurang\t= {hasil}")
        input("\n\nTekan Enter untuk kembali ke menu...")
        os.system('cls')

    elif option == 8:
        while True:
                print("8. Filtering\n")
                os.system('cls')
                print("1. Filter list angka kelipatan 3 (easy)")
                print("2. Filter angka prima (medium)")
                print("3. Filter angka palindrome (hard)")
                print("0. Kembali ke menu utama")

                try:
                    submenu_option = int(input("Masukkan pilihan menu (0 - 3): "))
                except ValueError:
                    print("Input tidak valid. Masukkan angka.")
                    continue

                if submenu_option == 1:
                    os.system('cls')
                    bawah = int(input("Masukkan batas bawah: "))
                    atas = int(input("Masukkan batas atas: "))
                    ganjil_genap = int(input("Angka ganjil (1) atau genap (0)?: "))
                    data = [i for i in range(bawah, atas + 1) if i % 2 == ganjil_genap]
                    kelipatan_tiga = list(filter(lambda x: x % 3 == 0, data))
                    print("Kelipatan 3:", kelipatan_tiga)
                    input("\n\nTekan Enter untuk kembali ke menu...")
                    os.system('cls')

                elif submenu_option == 2:
                    os.system('cls')
                    bawah = int(input("Masukkan batas bawah: "))
                    atas = int(input("Masukkan batas atas: "))
                    ganjil_genap = int(input("Angka ganjil (1) atau genap (0)?: "))
                    data = [i for i in range(bawah, atas + 1) if i % 2 == ganjil_genap]
                    prima = list(filter(is_prima, data))
                    print("Angka Prima:", prima)
                    input("\n\nTekan Enter untuk kembali ke menu...")
                    os.system('cls')

                elif submenu_option == 3:
                    os.system('cls')
                    kalimat = input("Masukkan kalimat: ")
                    kata = kalimat.split()
                    palindrome = list(filter(is_palindrome, kata))
                    non_palindrome = list(filter(lambda x: not is_palindrome(x), kata))
                    print("Palindrome:", palindrome)
                    print("Non-Palindrome:", non_palindrome)
                    input("\n\nTekan Enter untuk kembali ke menu...")
                    os.system('cls')

                elif submenu_option == 0:
                    os.system('cls')    
                    break

                else:
                    os.system('cls')
                    print("Opsi tidak valid.")

    elif option == 9:
        os.system('cls')
        print("9. Mapping\n")
        result = list(map(lambda y: y * 2, filter(lambda x: x % 2 == 1, range(10))))
        print(result)
        input("\n\nTekan Enter untuk kembali ke menu...")
        os.system('cls')

    elif option == 10:
        os.system('cls')
        print("10. Reduce\n")
    
        data_angka = [3, 9, 15, 21, 27, 33, 39, 45]  # hasil dari soal no.8.1
        hasil_penjumlahan = reduce(lambda x, y: x + y, data_angka)
        print(hasil_penjumlahan)

    elif option == 11:
        os.system('cls')
        print("11. Closure\n")
        def hitung_pangkat(x):
            def pangkat(y):
                return y ** x
            return pangkat

        while True:
            x_input = int(input("Masukkan nilai x: "))
            y_input = int(input("Masukkan nilai y: "))

            pangkat_user = hitung_pangkat(x_input)

            hasil_pangkat = pangkat_user(y_input)
            print(f"Hasil pangkat {x_input} dari {y_input} adalah {hasil_pangkat}")

            ulangi = input("Apakah Anda ingin menghitung lagi? (y/n): ").lower()
            os.system('cls')
            if ulangi != 'y':
                break

    elif option == 12:
        os.system('cls')
        print("12. Decorator\n")
        def decorator_ubah_output(func):
            def wrapper(*args, **kwargs):
                while True:
                    bilangan_input = int(input("Masukkan bilangan: "))
                    hasil = func(bilangan_input, *args, **kwargs)
                    if hasil:
                        print("Hasil benar!")
                    else:
                        print("Hasil salah!")

                    ulangi = input("Ingin mengulang? (y/n): ").lower()
                    os.system('cls')
                    if ulangi != 'y':
                        break
            return wrapper

        @decorator_ubah_output
        def is_prima(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        is_prima()
        input("\n\nTekan Enter untuk kembali ke menu...")
        os.system('cls')        

    elif option == 13:
        os.system('cls')
        print("13. Data visualization\n")
        # Data kendaraan
        data = [('Bus', 5, 200),
                ('Trem', 8, 150),
                ('Kereta', 12, 300),
                ('Minibus', 6, 180),
                ('Tram', 9, 220)]
        
        # Pisahkan data
        jenis_kendaraan, penggunaan_energi, biaya_operasional = zip(*data)

        # Visualisasi data penggunaan energi
        plt.figure(figsize=(15, 5))
        plt.subplot(1, 3, 1)
        plt.bar(jenis_kendaraan, penggunaan_energi, color='skyblue')
        plt.title('Penggunaan Energi')
        plt.xlabel('Jenis Kendaraan')
        plt.ylabel('Penggunaan Energi per Km')

        # Visualisasi data biaya operasional
        plt.subplot(1, 3, 2)
        plt.bar(jenis_kendaraan, biaya_operasional, color='lightgreen')
        plt.title('Biaya Operasional')
        plt.xlabel('Jenis Kendaraan')
        plt.ylabel('Biaya Operasional per Km')

        # Scatter plot hubungan antara penggunaan energi dan biaya operasional
        plt.subplot(1, 3, 3)
        plt.scatter(penggunaan_energi, biaya_operasional, color='coral', label='Kendaraan')
        plt.title('Hubungan Penggunaan Energi dan Biaya Operasional')
        plt.xlabel('Penggunaan Energi per Km')
        plt.ylabel('Biaya Operasional per Km')

        # Memberikan label pada tiap titik
        for i, jenis in enumerate(jenis_kendaraan):
            plt.annotate(jenis, (penggunaan_energi[i], biaya_operasional[i]))

        # Menambahkan legenda
        plt.legend()

        # Tampilkan plot
        plt.tight_layout()
        plt.show()

    else:
        print("Opsi tidak valid")
        
while True:
    print("\n\t\t\t\t~~~~~REMIDI UAP~~~~~\n")
    print("Nama\t: Rifqi Aflah Naufal Firmansyah")
    print("NIM\t: 202010370311404\n")
    print("1.\tSequence \t\t8.\tFiltering ")
    print("2.\tFunction \t\t9.\tMapping ")
    print("3.\tPure Function \t\t10.\tReduce")
    print("4.\tLambda \t\t\t11.\tClosure")
    print("5.\tList Comprehension \t12.\tDecorator")
    print("6.\tGenerator Expression \t13.\tData visualization")
    print("7.\tHigher Order Function ")

    try:
        menu_option = int(input("\nMasukkan pilihan hasil code kegiatan (1 - 13), atau 0 untuk keluar\t: "))
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        break
    
    if menu_option == 0:
        print("Program selesai.")
        break  # Keluar dari loop jika pengguna memilih 0
    else:
        switch_case_menu(menu_option)


