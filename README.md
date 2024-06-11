71220872/Nathanael Santoso 

71220856/Vincen Imanuel 

7122/Chika Venesa 

# AI untuk Prediksi Waktu dan Suhu AC 

AI unuk Prediksi Waktu dan Suhu AC menggunakan AI dan IoT untuk memperkirakan waktu dan suhu AC yang diperlukan untuk mencapai sebuah suhu dengan efisien. Algoritma yang digunakan adalah random forest karena mean errornya lebih rendah jika dibangkan dengan menggunakan linear regression (sekitar 56%), menurut kami hal tersebut terjadi dikarenakan data yang kami gunakan tidak sepenuhnya linear. Data diambil dengan device IoT dengan sensor DHT11.  

# Data Acquirement

Data yang digunakan merupakan data primer yang diambil dengan esp8266 dengan sensor DHT11. Input dari suhu AC masih di input secara manual. Data yang diambi dari device IoT dikirim ke broker yang kemudian diterima oleh Node-RED. Data yang diterima Node-RED dimasukkan ke database yang kemudian akan dipakai sebagai input ke AI.

# Code Python/Model Training

algoritma yang kita pakai adalah Linear Regression dan Random Forest. Untuk hasilnya, prediksi dari algoritma Linear Regression sedikit lebih masuk akal jika dibandingkan dengan Random Forest. Akan tetapi, untuk evaluasinya di saat kami menggunakan Mean Error, Mean Error dari Random Forest lebih rendah. Menurut kami ini terjadi karena data yang kami punya tidak sepenuhnya linear. Semakin rendah mean error maka semakin baik kinerja AI, maka kami memilih Random Forest.

# Pengolahan Data dan Interface

Terdapat dua metode yang dapat digunakan untuk mengolah data dengan AI yaitu sebagai berikut:

## Python HTML

![img1.1](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/app_img1.png)

![img1.2](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/app_img2.png)

app.py dapat di run secara langsung untuk menjalankan AI

## Node-RED

Untuk menjalankan dashboard Node-RED, diperlukan untuk menginstall node.js, Node-RED dan module 'node-red-node-mysql' untuk menjalankan dashboard.

Kemudian user perlu menjalankan xampp untuk database dan menjalankan Node-RED melalui node.js.

Setelah semua persiapan selesai, user dapat membuka dashboard di localhost dan memulai app2.py.

Data nantinya akan diambil dari database yang kemudian akan dikirim ke program Python yang dijalankan, yang kemudian akan dikembalikan lagi pada Node-RED.

Data diambil dari input user dan database yang kemudian di jadikan array. Data kemudian akan dikirim ke program app2.py dan di proses oleh AI.

Data kemudian dikirimkan kembali ke Node-RED untuk ditunjukkan.


### Tampilan UI Node-RED

![img2.2](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/node-red_ui2.png)
![img2.1](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/node-red_ui1.png)

### Tampilan Dashboard Pemrosesan Program Node-RED

![img2.3](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/node-red_dashboard.png)


### Tampilan app2.py

![img2.4](https://github.com/Nathasan1410/projek-AI-AC/blob/main/images/app2.png)
