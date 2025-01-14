from Negara import Negara
from Negara import Pemimpin
from Tatasurya import Planet
from Tatasurya import Bintang

Negara1 = Negara("indonesia", "Asia", "Republik", "1,905 juta km²", "273,8 juta (per 2021)")
Negara2 = Negara("Rusia", "Eropa dan Asia (Transkontinental)", "Republik Federasi", "17,1 juta km²", "143,4 juta (per 2021)")

Pemimpin1 = Pemimpin("Republik Presidensial", "Joko Widodo (per 2021)", "tanggal 21 Juni 1961", "singkat, ringkas, tapi tendangannya lumayan,")
Pemimpin2 = Pemimpin("Republik Federasi", "Vladimir Putin (per 2021)", "7 Oktober 1952", "gaya kepemimpinan yang kuat dan tegas")

Planet1 = Planet("Bumi", "Bima Sakti", "Ketiga dari Matahari", "Bulan", "Sekitar 24 jam", "Sekitar 365 hari")
Planet2 = Planet("Mars", "Bima Sakti", "Keempat dari Matahari", "Dua satelit utama (Phobos dan Deimos)", "Sekitar 24,6 jam", "Sekitar 687 hari")

Bintang1 = Bintang("Matahari", "Tidak ada (terletak di Lingkaran Matahari)", "Sekitar 149,6 juta kilometer dari Bumi", "Bintang tipe G dengan suhu permukaan sekitar 5.500 derajat Celsius", "Diameter sekitar 1,4 juta kilometer")
Bintang2 = Bintang("Sirius", "Canis Major (Anjing Besar)", "Sekitar 8,6 tahun cahaya dari Bumi", "Bintang ganda yang terdiri dari Sirius A (bintang utama) dan Sirius B (bintang katai putih)", "Sirius A memiliki diameter sekitar 1,7 juta kilometer")

print(":::NEGARA 1:::")
print("Nama Negara        : " + Negara1.Nama_Negara)
print("Luas Negara		   : " + Negara1.Luas_Negara)
print("Benua 			   : " + Negara1.Benua)
print("Nama Pemimpin	   : " + Pemimpin1.Nama_pemimpin)
print("Jumlah Penduduk    : " + Negara1.Jumlah_Penduduk)
print("Jenis Pemerintahan : " + Negara1.Jenis_Pemerintahan)
print("Jenis Pemimpin 	   : " + Pemimpin1.Jenis_pemimpin)
print("TTL Pemimpin	   : " + Pemimpin1.Tanggal_Lahir_Pemimpin)
print("ciri Khas Pemimpin : " + Pemimpin1.Ciri_Khas_Pemimpin)
print("==========================================================================================")
print(":::NEGARA 2:::")
print("Nama Negara        : " + Negara2.Nama_Negara)
print("Luas Negara		   : " + Negara2.Luas_Negara)
print("Benua 			   : " + Negara2.Benua)
print("Nama Pemimpin	   : " + Pemimpin2.Nama_pemimpin)
print("Jumlah Penduduk    : " + Negara2.Jumlah_Penduduk)
print("Jenis Pemerintahan : " + Negara2.Jenis_Pemerintahan)
print("Jenis Pemimpin 	   : " + Pemimpin2.Jenis_pemimpin)
print("TTL Pemimpin	   : " + Pemimpin2.Tanggal_Lahir_Pemimpin)
print("ciri Khas Pemimpin : " + Pemimpin2.Ciri_Khas_Pemimpin)
print("==========================================================================================")
print(":::PLANET dan BINTANG 1:::")
print("Galaksi               : " + Planet1.Galaksi)
print("Nama Planet           : " + Planet1.Nama_Planet)
print("Nama Bintang          : " + Bintang1.Nama_Bintang)
print("Satelit Planet        : " + Planet1.Satelit_Planet)
print("Rasi Bintang          : " + Bintang1.Rasi_Bintang)
print("Jarak Bintang         : " + Bintang1.Jarak_Bintang)
print("Rotasi Planet         : " + Planet1.Rotasi_Planet)
print("Revolusi Planet       : " + Planet1.Revolusi_Planet)
print("Ukuran Bintang        : " + Bintang1.Ukuran_Bintang)
print("Karakteristik bintang : " + Bintang1.Karakteristik_Bintang)
print("Posisi Planet         : " + Planet1.Posisi_Planet)
print("==========================================================================================")
print(":::PLANET dan BINTANG 2:::")
print("Galaksi               : " + Planet2.Galaksi)
print("Nama Planet           : " + Planet2.Nama_Planet)
print("Nama Bintang          : " + Bintang2.Nama_Bintang)
print("Satelit Planet        : " + Planet2.Satelit_Planet)
print("Rasi Bintang          : " + Bintang2.Rasi_Bintang)
print("Jarak Bintang         : " + Bintang2.Jarak_Bintang)
print("Rotasi Planet         : " + Planet2.Rotasi_Planet)
print("Revolusi Planet       : " + Planet2.Revolusi_Planet)
print("Ukuran Bintang        : " + Bintang2.Ukuran_Bintang)
print("Karakteristik bintang : " + Bintang2.Karakteristik_Bintang)
print("Posisi Planet         : " + Planet2.Posisi_Planet)
print("==========================================================================================")