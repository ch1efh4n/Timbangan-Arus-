#github
#welcome

print("Hello Young Einstein!")
print("Welcome to Timbangan Arus Analyzer")
print()

#input banyak tabel data pengamatan
Tabel = int(input("Banyak pengambilan data = "))
Interval = range(0,Tabel)
Array_I = []
Array_d = []
Array_U = []
Array_x = []


#inputan diketahui
print("\nPart 1 : Masukkan Data yang Diketahui")
NST_X = 0.0005
NST_I = 0.05
k = float(input("Nilai Konstanta Pegas Kawat lilitan (k) = "))
s = float(input("Nilai jarak antar lilitan (S) = "))
r = float(input("Jari-jari lilitan (r) = "))
N = int(input("Banyak lilitan (N)= "))

#inputan nilai x1 rata-rata
print("\nPart 2 : Masukkan Nilai Pemendekan rata-rata masing-masing arus")
for i in Interval:
    x = float(input(f"Nilai X{int(i+1)} Rata-rata = "))
    Array_x.append(x)
    i += 1
print()

## perulangan untuk arus
print("\nPart 3: DeltaXrat\n")
for ii in Interval:
    print(f"Perubahan Pemendekan Kumparan Untuk Arus",ii+1)
    I = float(input(f"I{int(ii+1)} = "))
    Array_I.append(I)
    dd = 0
    for iii in range(4):
        d = float(input(f"DeltaX{int(iii+1)} = "))
        Array_d.append(d)
        dd = dd + d
        iii += 1

    II = I**2
    DeltaXrat = dd/4
    round(DeltaXrat,3)
    round(DeltaXrat,3)
    print(f"I{ii+1} = ",I)
    print(f"I{ii+1}^2 = ",II)
    print(f"Pemendekan Rata-rata{ii+1} = ", DeltaXrat)
    print()
    ii += 1

for iv in Interval:
    U = (k*DeltaXrat*s)/(II*r*N)
    deltaU = float(((NST_X/Array_x[iv])+(2*NST_I/I)+(NST_X/s)+(NST_X/r))*U)
    ksr = (deltaU/U) * 100
    Useb_min = U - deltaU
    Useb_plus = U + deltaU
    print(f'u{iv+1}       = ', U)
    print(f'delta U{iv+1} = ',deltaU)
    print(f'ksr{iv+1}     = ',ksr)
    print(f'Useb(-){iv+1} = ',Useb_min)
    print(f'Useb(+){iv+1} = ',Useb_plus)
    iv += 1
    print()
