

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
