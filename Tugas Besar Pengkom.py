# Program <Simulasi Elevator>
# Berfungsi untuk mensimulasikan sebuah lift sederhana dalam Python.

# KAMUS
# lantai = jumlah lantai dalam sebuah gedung : int
# posisi = posisi lift dalam gedung : int
# maxkap = kapasitas maksimal lift : int
# sum_orang = banyak orang yang henda menaiki lift : int
# gedung = tinggi gedung (berapa banyak lantai dalam gedung) : array [1...lantai)] of int
# orang = orang yang hendak menggunakan lift : array [1...sum_orang] of int
# BB = berat badan masing-masing orang : array [...sum_orang] of float
# pos_awal = posisi awal : array [...sum_orang] of int
# tujuan = lantai tujuan : array [sum_orang] of int
# lift = orang yang berada di dalam lift : [] of int
# B_lift = berat orang yang beradad di dalaf lift: [] of float

def RemoveOrang(tujuan, orang, lift, posisi) :
    # Berfungsi untuk menurunkan orang pada lantai tujuan.
    # KAMUS LOKAL
    # remove_lift : array of int
    
    # ALGORITMA
    remove_lift=[]
    for i in range(len(tujuan)) :
        if tujuan[i]==posisi and orang[i] in lift :
            remove_lift.append(orang[i])
    if remove_lift :
        for i in range(len(remove_lift)) :
            BB.pop(orang.index(remove_lift[i]))
            tujuan.pop(orang.index(remove_lift[i]))
            pos_awal.pop(orang.index(remove_lift[i]))
            orang.remove(remove_lift[i])
            B_lift.pop(lift.index(remove_lift[i]))
            lift.remove(remove_lift[i])
    return lift, B_lift, orang, tujuan, BB, pos_awal

def AddOrang(orang, pos_awal, BB, berat) :
    # berfungsi untuk memasukkan orang ke dalam lift.
    # KAMUS LOKAL
    # 

    # ALGORITMA
    for i in range(len(orang)-1, -1, -1) :
        if orang[i] in lift:
            continue
        if pos_awal[i]==posisi and berat<=maxkap :
            lift.append(orang[i])
            B_lift.append(BB[i])
            berat+=BB[i]
    berat=0
    for i in range(len(B_lift)) :
        berat+=B_lift[i]
    return berat, lift, B_lift

def BeratLift(berat) :
    # Berfungsi untuk menghitung berat orang yang ada di dalam lift.
    # KAMUS LOKAL
    # berat : int

    # ALGORITMA
    berat=0
    for i in range(len(B_lift)) :
        berat+=B_lift[i]
    return berat

# ALGORITMA PROGRAM UTAMA
import time

# Data
# input
lantai = int(input("Masukkan banyak lantai pada gedung: "))
posisi = int(input("Masukkan posisi lift: "))
maxkap = int(input("Masukkan kapasitas maksimal lift [kg]: "))
sum_orang = int(input("Masukkan banyak orang yang hendak menggunakan lift: "))

# array kosong
gedung = [i+1 for i in range(lantai)]
orang = [i+1 for i in range(sum_orang)]
BB = [float(0) for i in range(sum_orang)]
pos_awal = [0 for i in range(sum_orang)]
tujuan = [0 for i in range(sum_orang)]
lift = []
B_lift = []
berat=0

# input data per-orang
for i in range(sum_orang) :
    BB[i]=float(input(f"Masukkan berat badan orang ke-{i+1} [kg]: "))
    pos_awal[i]=int(input(f"Masukkan lantai posisi orang ke-{i+1}: "))
    tujuan[i]=int(input(f"Masukkan lantai tujuan orang ke-{i+1}: "))

# menentukan ke atas atau bawah dulu
atas = True
if posisi==gedung[0] :
    atas = True
elif posisi==gedung[-1] :
    atas = False
elif posisi==min(pos_awal) :
    if posisi<min(tujuan) :
        atas = True
    elif posisi>max(tujuan) :
        atas = False
elif posisi<min(pos_awal) :
    atas = True
elif posisi>max(pos_awal) :
    atas = False

# display
if atas==True :
    arrow = "↑"
else :
    arrow = "↓"
print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')

# pergerakan lift
if atas==True :
    while len(orang)!=0 :
        #naik
        arrow = "↑"
        paling_atas=max(max(tujuan), max(pos_awal))
        while posisi!=paling_atas :
            time.sleep(1.5)
            lift, B_lift, orang, tujuan, BB, pos_awal = RemoveOrang(tujuan, orang, lift, posisi)
            berat = BeratLift(berat)
            print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
            time.sleep(1.5)
            berat, lift, B_lift = AddOrang(orang, pos_awal, BB, berat)
            berat = BeratLift(berat)
            print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
            time.sleep(1.5)
            posisi+=1
            print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
        if posisi==paling_atas :
            lift, B_lift, orang, tujuan, BB, pos_awal = RemoveOrang(tujuan, orang, lift, posisi)
            print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
        #turun
        arrow = "↓"
        if len(tujuan)!=0 :
            paling_bawah=min(min(tujuan), min(pos_awal))
            while posisi!=paling_bawah :
                time.sleep(1.5)
                lift, B_lift, orang, tujuan, BB, pos_awal = RemoveOrang(tujuan, orang, lift, posisi)
                berat = BeratLift(berat)
                print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
                time.sleep(1.5)
                berat, lift, B_lift = AddOrang(orang, pos_awal, BB, berat)
                berat = BeratLift(berat)
                print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
                time.sleep(1.5)
                posisi-=1
                print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
            if posisi==paling_bawah :
                time.sleep(1.5)
                lift, B_lift, orang, tujuan, BB, pos_awal = RemoveOrang(tujuan, orang, lift, posisi)
                berat = BeratLift(berat)
                print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
else :
    while len(orang)!=0 :
        #turun
        arrow = "↓"
        paling_bawah=min(min(tujuan), min(pos_awal))
        while posisi!=paling_bawah :
            time.sleep(1.5)
            lift, B_lift, orang, tujuan, BB, pos_awal = RemoveOrang(tujuan, orang, lift, posisi)
            berat = BeratLift(berat)
            print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
            time.sleep(1.5)
            berat, lift, B_lift = AddOrang(orang, pos_awal, BB, berat)
            berat = BeratLift(berat)
            print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
            time.sleep(1.5)
            posisi-=1
            print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
        if posisi==paling_bawah :
            time.sleep(1.5)
            lift, B_lift, orang, tujuan, BB, pos_awal = RemoveOrang(tujuan, orang, lift, posisi)
            berat = BeratLift(berat)
            print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
        #naik
        arrow = "↑"
        if len(tujuan)!=0 :
            paling_atas=max(max(tujuan), max(pos_awal))
            while posisi!=paling_atas :
                time.sleep(1.5)
                lift, B_lift, orang, tujuan, BB, pos_awal = RemoveOrang(tujuan, orang, lift, posisi)
                berat = BeratLift(berat)
                print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
                time.sleep(1.5)
                berat, lift, B_lift = AddOrang(orang, pos_awal, BB, berat)
                berat = BeratLift(berat)
                print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
                time.sleep(1.5)
                posisi+=1
                print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
            if posisi==paling_atas :
                lift, B_lift, orang, tujuan, BB, pos_awal = RemoveOrang(tujuan, orang, lift, posisi)
                berat = BeratLift(berat)
                print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
berat=0
time.sleep(1.5)
print()
print(f"[{arrow}][{posisi}] : {lift} [{berat}/{maxkap}] [kg]", end='\r')
print("Selesai")