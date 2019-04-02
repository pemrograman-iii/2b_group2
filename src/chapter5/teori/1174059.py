# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:31:29 2019

@author: Ah elah
"""

#1
Device Manager : device manager berfungsi untuk menampilkan dan mengelola 
semua hardware yang sudah dinstall ataupun dapat di instalasi ke dalam 
perangkat windows.

folder /dev pada linux: Di dalam sistem operasinya, perangkat yang tehubung 
akan dianggap sebagai file. Di dalam folder /dev file-file tersebut ada 

#2
Langkah - langkah instalasi driver arduino :
    -download file driver arduino terlebih dahulu dan masukkan ke dalam 
    directory yang diinginkan
    -hubungkan arduinio uno anda ke pc anda dengan kabel USB yang tersedia
    -lalu windows akan memunculkan pop up yang memberitahu bahwa ingin 
    menginstall dirver, tapi nanti tidak akan menemukan drivernya
    -buka Device Manager
    -cari unknown device di dalam Device Manager di dalam tab other device
    -klik kanan pada unknown device tersebut lalu pilih update driver software
    -pilih browse my computer for driver software lalu masukkan directory 
    dimana anda menyimpan driver arduino yang telah anda download tadi
    -setelah itu klik install dan tunggu hingga proses selesai
    
#3
Untuk melihat atau membaca BAUDRATE dan PORT kita hanya perlu menginstal 
Arduino IDE, setelah itu buka menu serial monitor yang berada di tab TOOLS.
Dari sana akan terlihat baik BAUDRATE dan PORT yang sedang digunakan oleh 
arduino anda.

#4
PySerial merupakan sebuah library yang digunakan untuk komunikasi ke port 
serial terutama untuk MICROCONTROLLER. PySerial melakukan debut pertamanya 
pada tahun 2002 yang semakin berkembang dalam setiap versinya hingga tahun 
2017 lalu.

#5
-stop() untuk menghentikan pembacaan program
-serial.to_bytes(sequence): berfungsi untuk mengubah sequence ke dalam bytes 
agar dapat diupload ke arduino.
-close(): untuk menutup port dan menghentikan pembacaan program

#6
Dengan menggunakan pengulangan kita dapat mengambil data berkali-kali tanpa 
harus mengeksekusi file python tersebut berulang-ulang. Tanpa perulangan 
juga penting karena dapat digunakan di saat tertentu seperti jika ingin 
mengukur suhu ruangan yang hanya dilakukan pada saat tertentu tidak terus 
menerus.

#7
Untuk membuat fungsi yang menggunakan Pyserial kita hanya perlu untuk 
menginisialisasi pembubatan funsi dengan menggunakan 
def namafungsi() : lalu masukkan pyserial tersebut dengan indentasi. 
Atau cukup dengan menggunakan fungsi while loop degan menggunakan while true: