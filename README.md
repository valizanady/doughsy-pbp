# Tugas Individu 2 

Nama : Valiza Nadya Jatikansha

NPM : 2306240156

Kelas : PBP B

URL Doughsy : https://valiza-nadya-doughsy.pbp.cs.ui.ac.id 

 1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    1) Membuat Repository dan Setup Environment
    - Membuat repository dan direktori baru sesuai dengan nama proyek
    - Menghubungkan direktori lokal ke repository menggunakan perintah `git add remote <url repository>`
    - Mengaktifkan Virtual Environment menggunakan `python3 -m venv env`
    - Membuat berkas requirements, menambahkan, dan menginstal dependencies yang dibutuhkan

    2) Membuat Proyek Django
    - Inisialisasi proyek baru menggunakan perintah `django-admin startproject projectname.`
    - Menambahkan host dari server yang diizinkan untuk mengakses aplikasi web pada `ALLOWED_HOSTS` pada `settings.py`
    - Buat aplikasi baru di dalam proyek menggunakan perintah `python manage.py startapp appname.`
    - Menambahkan aplikasi baru ke dalam daftar `INSTALLED_APPS` pada `settings.py`

    3) Konfigurasi Model Dasar Aplikasi (models.py)
    - Membuat model pada `models.py` di direktori aplikasi dengan mengidentifikasi kebutuhan aplikasi. Aplikasi Doughsy menggunakan model seperti berikut ini, 
    ```
    from django.db import models

    class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Donut(models.Model):
    flavor = models.CharField(max_length=50) 
    size = models.CharField(max_length=10)   
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.flavor} ({self.size})"
    ```
    - Melakukan migrasi model setiap ada perubahan data menggunakan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk migrasi ke database lokal 

    4) Mendefinisikan model pada `models.py` dan view pada `views.py`
    - Implementasikan function view pada `views.py` sesuai dengan kebutuhan fitur aplikasi
    - Buat berkas template (HTML) untuk menampilkan data dari views menggunakan struktur kode Django. Berikut kode yang saya implementasikan pada aplikasi Doughsy,
    ```
    <h1>{{ appName }}</h1>

    <h5>NPM: </h5>
    <p>{{ npm }}<p>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```

    5) Konfigurasi URL aplikasi dan URL proyek 
    - Membuat berkas `urls.py` pada direktori aplikasi dan mengimplementasikan 
    - Memodifikasi berkas `urls.py` pada direktori proyek dengan menambahkan rute URL yang mengarah ke tampilan aplikasi

    6) Deployment and testing
    - Menjalankan proyek Django menggunakan perintah `python manage.py runserver`
    - Melakukan deploy aplikasi ke platform hosting (Pacil Web Service (PWS))
    - Melakukan testing dengan memodifikasi `tests.py` dan menjalankan perintah `python manage.py test`

2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.** 
``` mermaid 
flowchart LR
   A[Client] --> B[urls.py]
   B --> C[views.py]
   C --> D[models.py]
   C --> E[Template HTML]
   D --> C
   E --> F[Response HTML]
   F --> A[Client]
  
   subgraph Django Request-Response Flow
     C[views.py] --> |"Process and pass data to the HTML template"| E
     E[Template HTML] --> |"Return a view with the processed data"| F
   end
```

- **Client**: Pengguna atau klien mengirimkan permintaan dari browser mereka, yang kemudian diterima oleh aplikasi Django.
- **urls.py**: Berfungsi untuk mencocokkan URL yang diminta dengan view yang relevan di views.py. Dengan kata lain, setiap URL yang diminta diarahkan ke logika tertentu di aplikasi.
- **views.py**: Mengelola logika utama dari aplikasi yang apat melibatkan pengambilan data dari models.py (jika ada interaksi dengan database) dan kemudian memproses data tersebut untuk diserahkan ke template.
- **models.py**: Jika diperlukan, views.py mengambil data dari database melalui models.py, yang merupakan representasi dari tabel-tabel dalam database
- **Template HTML**: Setelah views.py menyelesaikan pemrosesan data, data tersebut diberikan kepada template HTML yang menghasilkan halaman web dinamis berdasarkan informasi yang dikumpulkan.
- **Response HTML**: Template HTML yang sudah dirender dikirim kembali sebagai respon ke klien untuk ditampilkan di browser.

3. **Jelaskan fungsi git dalam pengembangan perangkat lunak!**

Git adalah sistem kontrol versi yang digunakan untuk melacak semua perubahan yang telah dibuat pada kode dalam sebuah proyek, sehingga kita dapat melihat perubahan apa saja yang sudah dilakukan pada kode dari waktu ke waktu. Git juga mendukung kolaborasi, yang memungkinkan banyak pengembang bekerja secara bersamaan pada proyek yang sama tanpa risiko merusak kode satu sama lain. Selain itu, Git juga menyediakan fitur branching dan merging, di mana pengembang dapat membuat cabang terpisah untuk bekerja pada fitur baru atau memperbaiki bug, dan kemudian menggabungkannya kembali ke cabang utama setelah pekerjaan selesai.

4. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Django sering digunakan sebagai framework awal untuk belajar pengembangan perangkat lunak karena beberapa hal berikut,
- **Open sources**: Django adalah framework open source, artinya dapat digunakan dan dimodifikasi oleh siapa saja tanpa biaya.
- **Skalabilitas**: Django dapat digunakan untuk proyek skala kecil maupun skala besar, sehingga framework ini masih relevan untuk proyek yang lebih besar di masa depan, tanpa perlu beralih ke framework lain yang lebih kompleks.
- **Keamanan**: Django memiliki fitur keamanan yang kuat secara bawaan, seperti perlindungan dari serangan umum (SQL injection, XSS, CSRF). 
- **Fitur Bawaan yang Lengkap**: Django menyediakan berbagai fitur bawaan seperti ORM (Object-Relational Mapping), manajemen pengguna, autentikasi, dan sistem template. 
- **Komunitas**: Django memiliki komunitas besar yang aktif, hal ini membuat proses pembelajaran lebih mudah karena pengembang pemula dapat menemukan tutorial, panduan, serta solusi untuk masalah yang mereka hadapi dengan cepat.

5. **Mengapa model pada Django disebut sebagai ORM?**

Model pada Django disebut ORM (Object-Relational Mapping) karena Django menggunakan ORM untuk memetakan objek Python ke dalam tabel database. Dengan ORM, pengembang  tidak perlu menulis query SQL manual untuk mengakses atau menyimpan data di database. Cukup dengan menggunakan gunakan objek Python untuk mengelola data.

Referensi : https://medium.com/@yc.yugesh/django-web-development-framework-3a9edcd6e4a