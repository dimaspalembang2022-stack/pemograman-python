#=================================================
#PROGRAM FUNGSI DAN MODULARASI PYTHON 
# Pertemuan 6 - Pemograman Python 
#Studi Kasus Perhitungan Nilai Mahasiswa 
#=================================================

# FUNGSI 1 input data Mahasiswa
def input data ():
    print("=== INPUT DATA MAHASISWA===")
    nama =input("Masukkan nama mahasiswa:")
    tugas=float(input("Masukkan nilai tugas:"))
    uts=float(input("Masukkan nilai UTS:"))
    uas=float(input("Masukkan nilai UAS:"))

return nama,tugas,uts,uas

# FUNGSI 2:Menghitung nilai akhir
def hitung nilai(tugas,uts,uas)
nilai akhir=(tugas*0.30)+(uts*0.30)+(uas*0.40)
return nilai akhir

#FUNGSI 3:Menentukan grade
def tentukan grade(nilai):
    if nilai>=85:
        return"A"
        elif nilai>=75:
            return"B"
            elif>=65:
                return"C"
elif nilai>=50:
    rwturn"D"
    FUNGSI 4 Menentukan status hasil 
    def status kelulusan (nilai):
        if nilai>=60:
            return"LULUS"
            else:
                return "TIDAK LULUS"
                #fungsi 5: Menampilkan hasil
                def tampilkan hasil(nama,nilai,grade,status):
                    print("\n=================================")
                    print("  HASIL NILAI MAHASISWA            ")
                    print("=================================")
                    print("Nama mahasiswa      :",nama)
                    print("Nilai akhir         :",round(nilai,2))
                    print("Grade               :",grade)
                    print("status              :",status)                
                    print("======================================")
# PROGRAM UTAMA
def main():
    nama,tugas,uts,uas=input data()

    nilai=hitung nilai(tugas,uts,uas)
    grade=tentukan grade (nilai)
    status=status kelulusan(nilai)
    tampilkan hasil(nama,nilai,grade,status)

    # Menjalakan program utama
    main()
    
