# Nama         : Ridwanul Bakhri
# NIM          : K3522068
# Prodi        : Pendidikan Teknik Informatika dan Komputer
# Fakultas     : Fakultas Keguruan dan Ilmu Pendidikan
# Universitas  : Universitas Sebelas Maret

# Minggu, 30 April 2023


# Method Recursif untuk menghitung mundur angka
def hitungMundur(angka):
    # Percabangan 'if', jika angka (sebagai parameter) bernilai '0', maka akan mencetak -> "Waktu Habis!"
    if (angka == 0):
        print("Waktu habis!")
    # Jika angka (sebagai parameter) tidak bernilai '0', maka akan mencetak -> "Angka : ((Angka + 1) - 1)
    # dan melakukan recursif/pemanggilan fungsi dirinya sendiri dengan parameter angka nilainya dikurangi 1 setiap putaran
    else:
        # Mencetak -> "Angka : ((Angka + 1) - 1)
        print("Angka : ", ((angka + 1) - 1))
        # Melakukan recursif/pemanggilan fungsi dirinya sendiri dengan nilai parameter 'angka' dikurangi 1 setiap pemanggilan
        hitungMundur(angka - 1)

# Uji Coba
hitungMundur(10)
"""
Output -> Angka :  10
          Angka :  9
          Angka :  8
          Angka :  7
          Angka :  6
          Angka :  5
          Angka :  4
          Angka :  3
          Angka :  2
          Angka :  1
          Waktu habis!
"""



















