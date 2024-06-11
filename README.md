71220872/Nathanael Santoso 

7122/Vincen Imanuel 

7122/Chika Venesa 

# AI unuk Prediksi Waktu dan Suhu AC 

AI unuk Prediksi Waktu dan Suhu AC menggunakan AI dan IoT untuk memperkirakan waktu dan suhu AC yang diperlukan untuk mencapai sebuah suhu dengan efisien. Algoritma yang digunakan adalah ____ karena _____. Data diambil dengan device IoT dengan sensor DHT11.  

# Data Acquirement (jelasin  tentang IoT and gmn data di ambil)

Data yang digunakan merupakan data primer yang diambil dengan esp8266 dengan sensor DHT11. Input dari suhu AC masih di input secara manual. Data yang diambi dari device IoT dikirim ke broker yang kemudian diterima oleh Node-RED. Data yang diterima Node-RED dimasukkan ke database yang kemudian akan dipakai sebagai input ke AI.

# Code Python/Model Training

algoritma yang kita pakai adalah
(jelasin model & algoritma)

# Pengolahan data dan interface

Terdapat dua metode yang dapat digunakan untuk mengolah data dengan AI

## Python HTML (punya Vincent)

![img1.1](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/app_img1.png)

![img1.2](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/app_img2.png)

app.py dapat di run secara langsung untuk menjalankan AI

## Node-RED

Untuk menjalankan dashboard Node-RED, diperlukan untuk menginstall node.js, Node-RED dan module 'node-red-node-mysql' untuk menjalankan dashboard.

Kemudian user perlu menjalankan xampp untuk database dan menjalankan Node-RED melalui node.js

Setelah semua persiapan selesai, user dapat membuka dashboard di localhost dan memulai app2.py

Data nanti akan diambiil dari database yang kemudian akan dikirim ke program Python yang dijalankan yang kemudian akan dikembalikan lagi pada Node-RED.

Data diambil dari input user dan database yang kemudian di jadikan array. Data kemudian akan dikirim ke program app2.py dan di proses oleh AI.

Data kemudian dikirimkan kembali ke Node-RED untuk ditunjukkan.


### penampakan ui node red

![img2.2](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/node-red_ui2.png)
![img2.1](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/node-red_ui1.png)

### penampakan dashboard pemrosesan program node red

![img2.3](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/node-red_dashboard.png)


### penampakan app2.py

![img2.4](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/app2.png)
