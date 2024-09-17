# Doughsy

Nama : Valiza Nadya Jatikansha

NPM : 2306240156

Kelas : PBP B

URL Doughsy : https://valiza-nadya-doughsy.pbp.cs.ui.ac.id 

- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)

## Tugas Individu 2 <a id="tugas-2"></a>

 1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    1. Membuat Repository dan Setup Environment
    - Membuat repository dan direktori baru sesuai dengan nama proyek
    - Menghubungkan direktori lokal ke repository menggunakan perintah `git add remote <url repository>`
    - Mengaktifkan Virtual Environment menggunakan `python3 -m venv env`
    - Membuat berkas requirements, menambahkan, dan menginstal dependencies yang dibutuhkan


    2. Membuat Proyek Django
    - Inisialisasi proyek baru menggunakan perintah `django-admin startproject projectname.`
    - Menambahkan host dari server yang diizinkan untuk mengakses aplikasi web pada `ALLOWED_HOSTS` pada `settings.py`
    - Buat aplikasi baru di dalam proyek menggunakan perintah `python manage.py startapp appname.`
    - Menambahkan aplikasi baru ke dalam daftar `INSTALLED_APPS` pada `settings.py`


    3. Konfigurasi Model Dasar Aplikasi (models.py)
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


    4. Mendefinisikan model pada `models.py` dan view pada `views.py`
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

    5. Konfigurasi URL aplikasi dan URL proyek 
    - Membuat berkas `urls.py` pada direktori aplikasi dan mengimplementasikan 
    - Memodifikasi berkas `urls.py` pada direktori proyek dengan menambahkan rute URL yang mengarah ke tampilan aplikasi


    6. Deployment and testing
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

## Tugas Individu 2 <a id="tugas-3"></a>

1. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

    Pentingnya data delivery dalam pengimplementasian sebuah platform antara lain:
    - **Pertukaran Informasi Efisien**: Memastikan komunikasi yang lancar antara server dan klien, sehingga aplikasi tetap responsif tanpa perlu memuat ulang halaman.
    - **Ketersediaan Informasi Real-Time**: Memberikan data yang selalu akurat, penting untuk platform seperti e-commerce atau sistem keuangan.
    - **Integrasi Sistem**: Menghubungkan berbagai komponen platform untuk bekerja secara sinergis.
    - **Pengambilan Keputusan Berbasis Data**: Mendukung analisis data dan pengambilan keputusan yang lebih baik.
    - **Skalabilitas dan Kestabilan**: Menjamin kinerja yang stabil meski jumlah pengguna meningkat.
    - **Keamanan dan Privasi Data**: Melindungi data melalui enkripsi dan protokol keamanan.
    - **Optimalisasi Sumber Daya**: Mengurangi biaya operasional dengan memanfaatkan sumber daya secara efisien.

2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
    JSON lebih sering dianggap lebih baik daripada XML karena lebih ringan, mudah dibaca, dan ditulis oleh manusia. JSON memiliki struktur sederhana berupa pasangan key-value, sehingga lebih mudah diproses oleh banyak bahasa pemrograman, terutama JavaScript. XML memang memiliki kelebihan dalam mendeskripsikan data kompleks dengan dukungan struktur hierarki dan atribut, serta menawarkan skema standar seperti XSD untuk validasi data. Namun, XML sering kali terasa lebih rumit dan verbose.

    Keuntungan utama JSON meliputi kesederhanaan, keterbacaan, integrasi erat dengan JavaScript, parsing yang lebih cepat, dan ukuran file yang lebih kecil. Hal ini membuat JSON lebih efisien untuk transmisi data di jaringan. Meskipun XML masih relevan untuk kebutuhan tertentu seperti validasi skema, JSON menjadi lebih populer dalam pengembangan web modern karena kesederhanaan dan kinerjanya yang lebih baik.

3. **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
    Method `is_valid()` pada Django digunakan untuk memeriksa apakah data yang dimasukkan melalui form sudah sesuai dengan aturan yang telah ditentukan, seperti memastikan bahwa semua kolom wajib telah diisi dan sesuai dengan tipe data atau format yang diharapkan. Fungsi utama `is_valid()` adalah melakukan validasi data yang dikirim melalui form, memeriksa apakah semua field memenuhi aturan validasi yang ditentukan dalam model form atau melalui validasi khusus. Jika data valid, method ini akan mengembalikan nilai `True`; jika tidak, akan mengembalikan `False` dan menyimpan pesan kesalahan terkait field yang tidak valid dalam atribut `form.errors`. Ini memungkinkan pengembang untuk dengan mudah menampilkan pesan kesalahan kembali kepada pengguna. Selain itu, `is_valid()` juga memicu metode `clean()`, yang membersihkan dan menormalkan data form, memastikan bahwa data berada dalam format yang dapat digunakan sebelum diproses atau disimpan ke database. 

    `is_valid()` sangat penting karena beberapa alasan. Pertama, ini menjaga integritas data dalam aplikasi dengan memastikan hanya data yang valid dan bersih yang akan diproses, mencegah kesalahan, kerentanan keamanan, atau gangguan fungsi yang disebabkan oleh data yang tidak valid atau rusak. Kedua, `is_valid()` memungkinkan pengembang untuk memberikan umpan balik kepada pengguna ketika mereka mengirimkan data yang salah atau tidak lengkap. Dengan menyediakan pesan kesalahan, pengguna dapat mengidentifikasi dan memperbaiki masalah sebelum mengirim ulang data. Ketiga, method ini mencegah penyimpanan data yang tidak valid ke dalam database, menjaga konsistensi dan keandalan data dengan memastikan hanya data yang benar yang disimpan. Terakhir, Django menyediakan validasi form bawaan, seperti pemeriksaan field wajib dan tipe data, membuat `is_valid()` menjadi alat yang efisien dan otomatis untuk menangani validasi, sehingga memudahkan pengembang dalam memastikan bahwa aplikasi bekerja sesuai dengan yang diharapkan.

4. **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
    `csrf_token` diperlukan saat membuat form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang mengeksploitasi akses pengguna untuk melakukan aksi yang tidak diinginkan tanpa sepengetahuan mereka. Tanpa `csrf_token`, aplikasi menjadi rentan karena penyerang dapat membuat permintaan berbahaya yang tampak sah dari pengguna yang sedang login. 

    Jika kita tidak menambahkan `csrf_token` pada form Django, penyerang dapat membuat situs web atau skrip yang mengirimkan permintaan HTTP ke server aplikasi atas nama pengguna yang sedang login. Contohnya, penyerang dapat mengarahkan pengguna ke halaman jahat yang secara otomatis mengirimkan formulir tanpa sepengetahuan pengguna, memanfaatkan cookie sesi pengguna untuk mengelabui server agar percaya bahwa permintaan tersebut sah. Hal ini dapat mengakibatkan berbagai tindakan berbahaya, seperti pengubahan data sensitif, pelaksanaan transaksi, atau pencurian data pribadi.

    `csrf_token` bekerja dengan menambahkan token unik ke setiap form yang dikirim ke server. Token ini kemudian diverifikasi oleh server untuk memastikan bahwa permintaan tersebut berasal dari sumber yang sah, yaitu dari form yang dihasilkan oleh aplikasi itu sendiri. Dengan cara ini, `csrf_token` mencegah penyerang membuat permintaan palsu atas nama pengguna yang sedang login, karena mereka tidak akan memiliki token yang valid untuk disertakan dalam permintaan.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    1. **Membuat Direktori Templates**: Membuat directory `templates` di dalam direktori aplikasi Django yang berisi file `base.html``
    2. **Membuat Form:** Pertama, membuat `ProductForm` pada file `forms.py` di direktori proyek. Form ini akan digunakan untuk menambahkan data produk baru.
    3. **Menambahkan View untuk Form:** Membuat function `create_product_entry` pada `views.py`. Function ini menangani input dari form dan menyimpan data ke database jika form valid.
    4. **Menambahkan Template:** Membuat atau perbarui file HTML (`create_product_entry.html`) yang berisi form input sehingga pengguna dapat memasukkan data produk.
    5. **Membuat 4 View Data Delivery:** Menambahkan 4 fungsi view di `views.py` untuk menampilkan data produk dalam format XML dan JSON, baik secara keseluruhan maupun berdasarkan ID.
    6. **Menambahkan URL Routing:** Menambahkan URL routing di `urls.py` untuk menghubungkan setiap view yang telah dibuat sehingga dapat diakses melalui URL tertentu.

**Hasil Akses URL pada Postman**

Referensi: https://portswigger.net/web-security/csrf
