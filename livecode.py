regular=40000
VIP=75000
VVIP=100000
pelanggan=0

total=regular+VIP+VVIP

for tiket in range (1,3):
    pelanggan=regular+10000
if VIP ==0:
    if VVIP ==0:
         print("Mendapat minuman gratis!")
else:
    ("tidak dapat")

print("total:",total)

#program menggunakan 3 jenis tiket, kemudian pelanggan bisa memilih lebih dari 1 tiket.jika yang mendapatkan
#khusus tiket vip dan vvip maka mereka mendapat minuman gratis.jika pelanggan memiliki member card maka 
#tidak akan mendapatkan member card lagi.
