# Live Demo Link 🚀
[Home page 🏠](https://tugas2pbpirsyad.herokuapp.com/)

[Katalog page 📃](https://tugas2pbpirsyad.herokuapp.com/katalog/)

## Bagan request client
![alt text](./assets/bagan.JPG "bagan request client")

## Kenapa menggunakan virtual environtment?
- Alasan penggunaan  environment mental karena secara langsung melaksanakan instalasi packages dan dependencies yang mana kedua hal tersebut dibutuhkan dalam framework django yang sebelumnya tidak terinstalasi secara global di local.  Hal yang dapat dilakukan sebatas mengakses dari folder/direktori yang telah terinstal apabila virtual environtment tidak digunakan. Pembuatan enviroment kerja python yang terisolasi dapat dibuat melalui virtual environment yang mana apabila banyak project yang dimiliki user, hal tersebut tidak akan mengganggu.

## Apakah bisa membuat aplikasi web berbasis django tanpa menggunakan virtual environtment?
- Ya hal tersebut tetap dapat dilakukan dengan syarat tetap menginstall packages beserta dependencies yang diperlukan namun penginstalan dilakukan secara global. Hal tersebut memang dapat dilakukan namun memiliki kekurangan yakni apabila user melakukan project dalam skala besar serta banyak yang mana requirement yang dibutuhkan memiliki versi yang berbeda -beda contohnya sepert django, Pyform serta kivy dan lainnya akan menyebabkan masalah pada project-project tersebut. Oleh karena itu virtual enviroment dapat mencegah serta mengatasi hal-hal tersebut

## Cara mengimplementasikan poin 1 sampai poin 4
1. Pada views.py, syntax CatalogItem.objects.all() digunakan untuk mengambil semua data dari json dalam sebuah fungsi serta render() digunakan untuk pengembalian data tersebut ke dalam template html

2. Melalui perintah path(), pemasukkan path pada folder katalog file urls.py dilakukan demi pelaksanaan routing pada fungsi views.py serta tidak lupa penambahan path kedalam folder project django

3. Pemasukkan data melalui perintah loaddata json ke dalam database django lokal telah dilakukan selanjutnya fungsi akan terbentuk dan melalui perintah CatalogItem.objects.all(), fungsi akan mengambil data tersebut. Selanjutnya render akan dilakukan melalui perintah render (_____)

4. Melalui heroku, deployment dapat diatur dengan membuat file Procfile setelah itu pada Heroku _new app_ akan dibuat oleh user dan dilakukan import repo tugas 2 PBP ke Heroku dari github untuk dilakukan deploy. Tidak lupa untuk menambahkan api values serta api name yang terdapat pada settingan repository github tugas 2 

