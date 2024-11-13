def angka_posisi(daftar_angka):
    angka_pertama = daftar_angka[1]
    if angka_pertama >= (len(daftar_angka)):
        return -1

    return daftar_angka[angka_pertama]

def hitung_luas(alas, tinggi):
   return (alas*tinggi)/2

def hitung_keliling(alas, tinggi, sisi_miring):
   return sum([alas, tinggi, sisi_miring])