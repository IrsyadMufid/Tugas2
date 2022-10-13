[Link Heroku](https://tugas2pbpirsyad.herokuapp.com/todolist/)

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
- Cross Site Request Forgery atau biasa disebut sebagai CSRF merupakan suatu kerentanan dalam situs yang memungkinkan terjadinya suatu exploit yang mana sebuah domain yang berbeda meminta request maupun perintah dengan mengatasnamakan pengguna yang terdaftar di situs target tersebut. Oleh karena itu diperlukan {% csrf_token %} untuk menangkal serangan CSRF yang dilakukan oleh penyerang. {% csrf_token %} akan menghasilkan token ketika rendering pada situs dilakukan serta menyaring request yang masuk pada situs tersebut. Pada kasus elemen <form>,  apabila {% csrf_token %} tidak disertai maka akan terjadi kerentanan dalam situs tersebut yang akan mengancam keamanan post request yang berguna untuk mengirim data dari user menuju server. 
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
- Ya hal tersebut masih bisa untuk dilakukan. Kita tetap bisa membuat <form> secara manual tanpa bantuan generator form.as_table. Hal yang pertama harus lakukan adalah membuat form pada sebuah template yang berbentuk html yang nantinya akan mengirim request post yang berada dalam method post serta csrf_token didalamnya. Setelah itu pelengkapan tag input beserta nama sebagai tanda pengenal setelah itu dilakukan pemasukkan ke dalam form dengan cara request.POST.get()

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Pembacaan request dari client oleh views ketika user menekan tombol tambah task
2. Penerimaan parameter dan value dari form setelah itu data diambil menggunakan request.POST.get() 
3. Pembuatan objek baru dengan menggunakan Task.objects.create(title = title, description = description, date = datetime.datetime.now(), user = request.user) yang berisi title serta deskripsi yang disubmit user serta tanggal user membuat task tersebut dan nantinya database akan menyimpan hal tersebut untuk dilakukan CRUD (Create, Read, Update, Delete)
4. Pengaksesan data yang sudah tersimpan di database menggunakan Task.objects.filter(user= request.user) dan menampilkannya data untuk halaman todolist  tersebut menggunakan for loop yang terletak pada html
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Pembuatan aplikasi baru pada direktori Tugas2 dengan py -m manage startapp todolist
2. Penambahan path('todolist/', include('todolist.urls')) pada urls.py yang terletak pada project django
3. Pembuatan class di models.py yang terletak pada todolist dan membuat field sesuai dengan kriteria yang dibutuhkan
4. Lakukan migrate model dengan field tersebut dengan melakukan py -m manage makemigrations lalu py -m manage migrate.
5. Membuat class CreateForm dalam file baru yang bernama forms.py yang berfungsi untuk menampilkan form serta mensubmit data yang nantinya akan dipakai untuk  fungsi-fungsi yang akan dibuat dalam  views.py yang berguna untuk menampilkan todolist,login, logout, register dan hal lainnya. Fungsi-fungsi tersebut akan dihubungkan ke create_task.html, login.html, register.html, dan todolist.html
- Tidak lupa untuk melakukan commit serta push menuju github agar dapat deploy ke dalam heroku dan membuat dummy sesuai perintah soal 

## Akun Heroku
- Username: pc1 ; password: heroku123456
- Username: pc2 ; password: heroku123456

## README TUGAS 5
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
    Internal : Ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. digunakan untuk Membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
    Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik, pada setiap halaman website.

    External : Ditulis terpisah dengan kode HTML Eksternal CSS serta ditulis di sebuah file khusus yang berekstensi .css. Diletakkan setelah bagian <head> pada halaman.
    Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin diatur tampilannya. 

    Inline : Ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, Inline CSS ditulis.
    Sulit dalam mengatur website jika hanya menggunakan inline style CSS karena Inline CSS digunakan hanya untuk mengubah satu elemen saja.

## Jelaskan tag HTML5 yang kamu ketahui
	 
    <!DOCTYPE>	Menentukan tipe dokumen
    <html>	Create sebuah dokumen HTML
    <title>	Create judul dari sebuah halaman
    <body>	Create body dari sebuah halaman
    <h1> to <h6>	Create heading
    <p>	Create paragraf
    <br>	Insert satu baris putus
    <hr>	Create perubahan dasar kata didalam isi
    <!--...-->	komentar
    <form>	Create form HTML untuk input pengguna
    <input>	Create sebuah kontrol input
    <textarea>	Create sebuah kontrol input multibaris (text area)



## Tipe-Tipe CSS Selector
    Universal Selector : Memilih semua elemen html. Syntax: *

    Type Selector : Memilih semua elemen node namenya sesuai

    Class Selector : Memilih semua elemen yang punya attribut class yang sesuai

    ID Selector : Memilih sebuah elemen berdasarkan nilai attribut idnya

    Attribut selector : Memilih semua elemen yang punya attribut

## Implementasi checklist
1. Menambahkan tag `<link>` pada  setiap html yang membutuhkan untuk menggunakan CDN dari bootstrap css
2. Memasukan elemen-elem yang dibutuhkan ke dalam class container yang ada
3. Peimplemntasian login dari https://mdbootstrap.com/docs/standard/extended/login/
4. Pengakplikasian todolist dari https://getbootstrap.com/docs/4.0/components/card/

## README Tugas 6

## Perbedaan antara asynchronous programming dengan synchronous programming.
- Synchronus: click, wait, refresh. Jadi saat user click atau mengirim request, user harus menunggu server menampilkan semuanya dulu, baru bisa berinteraksi lagi. Contoh: saat kita klik ketik sesuatu di kolom pencarian google dan enter, kita harus menunggu google menampilkan semua informasi yang ada, baru bisa berinteraksi lagi
- Asynchronus: user bisa terus berinteraksi saat nunggu respons dari server, jadi tidak nunggu halamannya selesai. Contoh: chat dan email. Biasanya terjadi di belakang layar.

## Paradigma Event-Driven Programming
- Merupakan paradigma dimana event menentukan sebuah alur program yang bisa terdiri atas tindakan pengguna, luaran dari sebuah tindakan maupun pesan dari progam lainnya serta lainnya. Seperti contoh pada modal, ketika menekan tambah task akan memunculkan modal yang bersangkutan untuk mengisi judul serta deskripsi yang diinginkan. Setekah mengisi, user menekan tombol submit, maka objek Task baru akan terbentuk yang nanti akan dimasukkan ke database dan ditampilkan pada halaman todolist 

## Penerapan asynchronous programming pada AJAX
- User tidak perlu reload secara menyeluruh pada web dikarenakan pembaharuan dilakukan saat submit form yang ada di modal yang mana AJAX digunakan untuk pemberian informasi dari serta menuju server serta asynchronous programming menyebabkan halaman terus diproses dan penanganan reply mungkin dilakukan.

## Pengimplemntasian checklist
1. Penambahan tag script pada todolist_ajax untuk menggunakan JavaScript untuk jquery dan bootstrap
2. Pembuatan fungsi loadData untuk menghapus card serta table yang ada pada elemen div dengan id task_card dan table_Card. Selanjutnya menggunakan method AJAX GET untuk mengambil data dari objek task yang sudah dirender menjadi json. Setelah itu, membuat card serta table untuk masing-masing objek dan menambahkannya ke dalam div dengan id task_card serta table_card
3. Pembuatan fungsi $(document).ready() untuk melakukan fungsi loadData pada todolist ketika pertamakalidibuka
4. Pembuatan fungsi $(document).on() untuk menghandle submisi form pada modal
5. Pembuatan tombol tambah task pada navbar dengan id yang ada pada modal
6. Menghapus for loop pada task dan menggantinya dengan class serta id pada loadData
7. Pembuatan modal yang berisi judul serta deskripsi serta sumbit untuk mengsubmit form
8. Membuat fungsi show_json untk mengambilkan data dalam bentuk json
9. Membuat fungsi add_todolist_ajax untuk menerima request POST dari web dalam bentuk objek dan menambahkan path ajax/submit dalam url.py
10. Membuat fungsi show_totolist_ajax untuk menampilakan data dalam todolist_ajax.html sehingga dapat berpindah dari todolist.html ke todolist_ajax.html mauapun sebaliknya serta menambhakan url ajax/ pada url.py