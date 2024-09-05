import streamlit as st

st.set_page_config(
    page_title="Apllication System",
    page_icon=":brain:"
)

st.title("About Mental Health")
st.caption("Menjelaskan tentang beberapa penyakit mental yang dipilih, dikarenakan cakupan penyakit mental cukup luas kami memilih beberapa penyakit mental yang lumayan umum diderita oleh masyarakat. Dan kami merangkum dari berbagai sumber terkait untuk mendapatkan data dan informasi yang terpercaya.")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Anxiety", "Bipolar", "Depresi", "Eating Disorder", "OCD", "PTSD", "Skizophrenia"])

with tab1:
   st.header("	:one: Anxiety")
   st.write("Gangguan kecemasan atau _Anxiety Disorder_ adalah perasaan khawatir atau cemas yang tidak terkendali dan berlebihan akan banyak hal. Kekhawatiran dan rasa takut yang intens dan terus - menerus sehubungan dengan situasi sehari - hari. Dapat terjadi hal - hal seperti jantung berdenyut kencang, napas tersengal - sengal, berkeringat, dan merasa lelah.")
   st.subheader("Berbagai Gejala Anxiety (Gangguan Kecemasan)")
   st.markdown("""
      - Merasa gugup, gelisah, atau tegang
      - Memiliki rasa bahaya, kepanikan, atau malapetaka yang akan datang
      - Detak jantung yang meningkat
      - Bernapas dengan cepat (hiperventilasi)
      - Berkeringat berlebihan / berkeringat dingin
      - Gemetaran
      - Merasa lemah atau lelah
      - Kesulitan berkonsentrasi
      - Mengalami kesulitan tidur
      - Gangguan pencernaan
      - Sulit mengendalikan rasa khawatir / kecemasan
      - Memiliki dorongan untuk menghindari hal-hal yang memicu kecemasan
      - Memikirkan dan melakukan perenungan tiada henti
      - Tangan dan kaki kesemutan
      - Rasa sakit dan nyeri pada tubuh
      - Mudah marah dan terpancing emosi
      - Menarik diri dari lingkungan social
      - Mudah marah dan terpancing emosi
      - Mudah terkejut
      - Sesak napas
      - Sering melamun
      - Merasa tak punya harapan
      - Merasa tak berharga
   """)

   st.subheader("Cara Mencegah atau Mengatasi Anxiety Disorder")
   st.markdown("""
      - Mencukupi waktu tidur dan istirahat
      - Membatasi rokok,  konsumsi kafein dan minuman beralkohol
      - Mengurangi stress dan mengendalikan emosi dengan mencoba teknik relaksasi, misalnya meditasi, tai chi dan yoga
      - Melakukan aktivitas fisik atau berolahraga secara teratur
      - Mencoba bertukar pikiran atau curhat dengan teman
      - Cari bantuan sesegera mungkin. Penanganan gangguan kecemasan, seperti banyak kondisi kesehatan mental lainnya, dapat menjadi lebih sulit jika pengidap menunda mencari bantuan. 
      - Buat jurnal. Memahami kehidupan pribadi dapat membantu seseorang dan profesional kesehatan mental untuk mengidentifikasi apa penyebab kecemasan dan apa yang tampaknya membantu orang tersebut merasa lebih baik.
      - Prioritaskan masalah dalam hidup. Kamu dapat mengurangi kecemasan dengan mengatur waktu dan energi secara hati-hati.
      - Melakukan hobi atau kegiatan menenangkan. Contohnya bermain musik, berkebun, merajut, ataupun melukis.
      - Mengatur pola makan sehat.
      - Bergabung ke komunitas dengan kegiatan yang disukai. Selain melakukan hobi, Anda juga bisa bersosialisasi.
      - Melakukan sesi konseling jika perlu kepada psikolog. Jika lebih parah dan membutuhkan pengobatan, sesi konseling diarahkan melalui psikiater.
      - Berlatih Pernapasan yang Menenangkan
               """)

   st.subheader("Penyebab Anxiety Disorder")
   st.markdown("""
   Berikut adalah beberapa penyebab atau pemicu yang memungkinkan timbulnya Anxiety :

      - Faktor genetik, riwayat keluarga juga dapat meningkatkan risiko gangguan 
      - Hormon yang terlepas dalam otak, sehingga meningkatkan denyut nadi dan pernapasan.
      - Lingkungan yang memicu stres dan membuat ketakutan, seperti lokasi dimana terjadi pelecehan, kekerasan, kematian.
      - Penyalahgunaan obat-obatan.
      - Mengkonsumsi kafein yang berdampak pada kerja jantung.
      - Beberapa kondisi medis seperti gangguan tiroid, gangguan kardiovaskular, atau gangguan hormonal dapat berkontribusi pada kecemasan.
      - Aktivitas berlebihan pada area otak yang terlibat dalam pengaturan emosi dan perilaku.
      - Ketidakseimbangan zat kimia otak, yaitu serotonin dan noradrenalin, yang terlibat dalam pengendalian dan pengaturan suasana hati. 
      - Memiliki riwayat mengalami kejadian traumatis atau menimbulkan stres, seperti kekerasan dalam rumah tangga (KDRT) atau penganiayaan anak.
      - Mengalami kondisi sakit dalam jangka panjang, seperti artritis.
      - Konsumsi berlebihan kafein, alkohol, atau obat-obatan terlarang dapat memicu atau memperburuk kecemasan. 
      - Beban stres yang terlalu berat, baik dari pekerjaan, hubungan, atau masalah keuangan, dapat memicu kecemasan.
      - Perubahan seperti pindah rumah, pergantian pekerjaan, atau peristiwa penting dalam hidup bisa menyebabkan kecemasan karena adanya ketidakpastian.
      - Pengalaman traumatis seperti kecelakaan, kehilangan orang terdekat, atau tindakan kekerasan bisa meningkatkan risiko kecemasan.
      - Kurang tidur atau kualitas tidur yang buruk dapat membuat seseorang lebih rentan terhadap kecemasan.
      - Pengalaman serangan panik sebelumnya dapat membuat seseorang cemas tentang kemungkinan serangan berulang.
      - Lingkungan yang tidak mendukung, diskriminasi, atau merasa tidak diterima oleh lingkungan sosial bisa memicu kecemasan.
      - Pola pikir yang cenderung negatif atau mengkhawatirkan tentang masa depan bisa memperburuk kecemasan.
      - Pertemuan sosial atau situasi di mana seseorang merasa dinilai oleh orang lain dapat memicu kecemasan sosial.
      - Tekanan untuk tampil baik di tempat kerja atau dalam lingkungan akademik dapat memicu kecemasan performa.
      - Ketakutan terhadap situasi atau objek tertentu, seperti rasa takut terbang atau ruang tertutup (klaustrofobia), dapat memicu kecemasan.
      - Penggunaan berlebihan media sosial atau terpapar berita yang menekankan kekhawatiran dapat memicu kecemasan.
      - Tuntutan sosial yang berlebihan, tetapi individu tersebut belum mampu memenuhinya.
      - Standar prestasi yang terlalu tinggi daripada kemampuan yang dimiliki oleh individu.
      - Memiliki perasaan rendah diri.
      - Kecenderungan individu dalam bersikap perfeksionis.
      - Kurang siapnya individu dalam menghadapi situasi yang sulit.
      - Pola pikir yang terbentuk secara negatif.
      - Persepsi negatif individu terhadap diri sendiri maupun situasi yang tengah dihadapi.
               """)

   st.subheader("Pengobatan Anxiety Disorder")
   st.markdown("""
      - Psikoterapi
      - Terapi perilaku kognitif (CBT)
      - Pengobatan medis
               """)

   st.divider()
   c = st.container()
   c.write("_Referensi :_")
   c.write("""Alodokter.com.(2022, 16 April)._Mengenal Anxiety yang 
            mengganggu dan Berbagai Jenisnya_. Diakses pada 17 Juni 2024,
            dari https://www.alodokter.com/mengenal-anxiety-yang-mengganggu-dan-berbagai-jenisnya 
         """)

   c.write("""Halodoc.com.(2023, 20 Agustus). _Apa Itu Gangguan Kecemasan (Anxiety Disorder)?_. Diakses pada 17 Juni 2024,
            dari https://www.halodoc.com/kesehatan/gangguan-kecemasan-umum 
         """)

   c.write("""Siloamhospitals.com.(2024, 20 Mei). _Anxiety Disorder - Penyebab, Gejala, Jenis, dan Pengobatannya_. Diakses pada 17 Juni 2024,
            dari https://www.siloamhospitals.com/informasi-siloam/artikel/anxiety-disorder  
         """)

   c.write("""Mitrakeluarga.com.(2022, 04 October). _Apa Itu Anxiety Disorder? Kenali Gejala dan Pengobatannya_. Diakses pada 17 Juni 2024,
            dari https://www.mitrakeluarga.com/artikel/apa-itu-anxiety-disorder 
         """)

   c.write("""Detik.com.(2024, 17 April). _Apa Itu Anxiety? Ini Tanda, Penyebab dan Cara Mengatasinya_. Diakses pada 17 Juni 2024,
            dari https://www.detik.com/jateng/berita/d-7296343/apa-itu-anxiety-ini-tanda-penyebab-dan-cara-mengatasinya 
         """)
   
   c.write("""National Institute Of Mental Health.(2024, April). _Anxiety Disorders_. Diakses pada 17 Juni 2024,
            dari https://www.nimh.nih.gov/health/topics/anxiety-disorders 
         """)

with tab2:
   st.header(" :two: Bipolar")
   st.write("Gangguan _Bipolar_ adalah suatu gangguan kesehatan mental yang berhubungan dengan perubahan suasana hati mulai dari posisi terendah depresif/tertekan ke tertinggi/manik. Pengidap yang sebelumnya merasa sangat gembira bisa tiba-tiba berubah menjadi sangat sedih dan putus asa.")
   st.subheader("Berbagai Gejala Bipolar")
   st.write("Terdapat dua fase dalam gejala gangguan bipolar, yaitu fase mania (naik) dan depresi (turun). Ketika periode mania terjadi, pengidap akan terlihat sangat bersemangat, enerjik, dan bicara cepat. Sementara itu, pada periode depresi, mereka akan terlihat sedih, lesu, dan kehilangan minat terhadap aktivitas sehari-hari. ")
   st.markdown("#### Mania")
   st.markdown("""
      - Sangat Bahagia / antusias
      - Terlalu bersemangat 
      - Berbicara sangat cepat
      - Memiliki rasa percaya diri yang berlebihan
      - Harga diri yang melambung
      - Kebutuhan tidur berkurang
      - Lebih banyak bicara daripada biasanya / bicara cepat dan semangat
      - Perhatian mudah teralihkan 
      - Membeli barang yg tidak diperlukaan dan menghamburkan uang secara tidak terkendali
      - Melakukan hubungan seks yang sembrono / Hasrat seksual meningkat 
      - Mudah tersinggung / sensitif
      - Kehilangan nafsu makan
      - Merasa sangat percaya diri, penting, berbakat, atau kuat
      - Berpikir bisa melakukan banyak hal sekaligus pada satu waktu
   """)

   st.markdown("#### Depresi")
   st.markdown("""
      - Merasa sangat sedih dan putus asa
      - Mudah Lelah
      - Kesulitan untuk menjaga focus dan konsentrasi
      - Tidak bersemangat untuk elakukan aktifitas apapun
      - Gangguan tidur,seperti insomnia atau bangun terlalu dini
      - Pesimis
      - Muncul keinginan untuk self harm / bunuh diri
      - Merasa diri sendiri tidak berharga / merasa bersalah yg berlebihan
      - Nafsu makan berkurang dan / atau penurunan berat badan, atau makan berlebihan dan penambahan berat badan  
      - Berbicara dengan sangat lambat, merasa tidak ada yang ingin mereka katakan, atau banyak lupa.
      - Merasa tidak mampu melakukan bahkan hal-hal sederhana
      - Tidak berminat untuk melakukan semua aktivitas, dorongan seks yang menurun atau bahkan tidak ada sama sekali, atau ketidakmampuan untuk merasakan kesenangan (anhedonia) 
      """)
   
   st.subheader("Cara Mencegah atau Mengatasi Bipolar Disorder")
   st.markdown("""
      - Rutin mengonsumsi obat sesuai resep dokter dan menjalani psikoterapi
      - Tidak mengonsumsi minuman beralkohol atau menyalahgunakan NAPZA
      - Berolahraga secara rutin
      - Mengelola stres dengan baik
      - Beristirahat dan tidur yang cukup
      - Menjalin hubungan baik dengan keluarga dan teman
      - Mengkonsumsi obat mood stabilizer untuk meredakan episode manik maupun depresif sesuai anjuran Dokter Spesialis Kedokteran Jiwa 
      - Mengkonsumsi obat yang berfungsi untuk mencegah penyebab utama depresi dan manik.
      - Mengenali berbagai hal yang dapat memicu manik dan depresif.
      - Pemulihan secara psikologis, bisa dengan konsultasi dengan psikolog. Tidak jarang pasien yang sudah menemui psikiater masih dalam pendampingan oleh psikolog.
      - Menerapkan gaya hidup sehat jiwa dan raga, seperti olahraga rutin, mengkonsumsi makanan sehat dan bergizi, tidur cukup, dan membuat segala aktivitas dengan terencana.
               """)

   st.subheader("Penyebab Bipolar")
   st.markdown("""
   Berikut adalah beberapa penyebab atau pemicu yang memungkinkan timbulnya Bipolar :
      - Genetik, yang diturunkan oleh salah satu anggota keluarga yang mengalami bipolar.
      - Ketidakseimbangan zat kimia di dalam otak (neurotransmitter) yang terkait dengan suasana hati, seperti serotonin, noradrenalin, dan dopamin.
      - Lingkungan sosial keluarga memicu gangguan bipolar.
      - Perubahan hormonal
      - Kemampuan menangani stress
      - Konsumsi zat-zat psikoaktif
      - Mengidap gangguan mental 
      - Perubahan siklus tidur
      - Pernah mengalami kejadian traumatis, seperti kekerasan fisik, bencana alam, ataupun kecelakaan lalu lintas.
      - Stres berat yang bisa dipicu oleh kehilangan orang yang dicintai atau karena masalah keuangan.
      - Gangguan tidur. 
      - Menderita kondisi medis tertentu yang tidak kunjung sembuh.
      - Penyalahgunaan NAPZA.
      - Kecanduan minuman beralkohol dan obat-obatan.
      - Trauma masa kecil yang sulit dilupakan, seperti kekerasan fisik, kekerasan seksual, dan tragedi lainnya.
      - Kejadian yang menyebabkan stres sehari-hari, seperti kesepian, patah hati, pemutusan kerja, tekanan dari orang dan lingkungan sekitar, bahkan pernikahan.
               """)

   st.subheader("Pengobatan Bipolar Disorder")
   st.markdown("""
      - Obat-obatan medis
      - Psikoterapi
      - Electroconvulsive Therapy (ECT)
      - Transcranial magnetic stimulation (TMS)
      - Rehabilitasi
      - Perawatan di Rumah Sakit
               """)

   st.divider()
   c = st.container()
   c.write("_Referensi :_")
   c.write("""Halodoc.com.(2023)._Apa Itu Gangguan Bipolar?_. Diakses pada 17 Juni 2024,
            dari https://www.halodoc.com/kesehatan/gangguan-bipolar 
          """)

   c.write("""Alodokter.com.(2023, 21 Februari). _Gangguan Bipolar_. Diakses pada 17 Juni 2024,
            dari https://www.alodokter.com/gangguan-bipolar 
         """)

   c.write("""Siloamhospitals.com.(2023, 20 September). _Gangguan Bipolar - Penyebab, Gejala, dan Penanganannya_. Diakses pada 17 Juni 2024,
            dari https://www.siloamhospitals.com/informasi-siloam/artikel/apa-itu-gangguan-bipolar  
         """)

   c.write("""Mitrakeluarga.com.(2022, 07 November). _Apa Itu Bipolar Disorder? Kenali Ciri-ciri dan Penyebabnya!_. Diakses pada 17 Juni 2024,
            dari https://www.mitrakeluarga.com/artikel/apa-itu-bipolar-disorder
         """)

   c.write("""Yankes.kemkes.co.id.(2023, 12 januari). _Gangguan Bipolar_. Diakses pada 17 Juni 2024,
            dari https://yankes.kemkes.go.id/view_artikel/2081/gangguan-bipolar 
         """)
   
   c.write("""National Institute Of Mental Health.(2024, April). _Bipolar Disorders_. Diakses pada 17 Juni 2024,
            dari https://www.nimh.nih.gov/health/topics/bipolar-disorder
         """)

with tab3:
   st.header(" :three: Depresi")
   st.write("_Depresi_ adalah gangguan suasana hati (mood) yang ditandai dengan perasaan sedih yang mendalam dan kehilangan minat terhadap hal-hal yang disukai. Seseorang dinyatakan mengalami depresi jika sudah 2 minggu merasa sedih, putus harapan, atau tidak berharga.")
   st.subheader("Berbagai Gejala Depresi")
   st.markdown("""
      - Merasa rendah diri, putus asa, tidak berharga
      - Sangat sensitif, mudah marah, tersinggung atau sedih berkelanjutan
      - Kesulitan berfikir,berkonsentrasi dan mengambil keputusan
      - Cenderung menutup diri dari lingkungan social
      - Tidak ada ketertarikan,minat atau motivasi untuk melakukan apapun
      - Selalu merasa bersalah dan sering menyalahkan diri sendiri
      - Selalu merasa cemas dan khawatir yang berlebihan
      - Suasana hati yang buruk
      - Menjadi apatis terhadap lingkungan sekitarnya
      - Timbul ide untuk menyakiti diri sendiri atau percobaan bunuh diri
      - Terlalu banyak tidur atau bahkan insomnia
      - Peningkatan / bahkan penurunan nafsu makan secara drastis
      - Mudah Lelah dan tidak bertenaga
      - Berat badan turun ataupun naik secara drastis
      - Nyeri pada bagian tubuh tertentu tanpa diketahui penyebab pastinya
      - Pusing atau nyeri yang tidak jelas penyebabnya
      - Gerak tubuh dan cara bicara lebih lambat dari biasanya
      - Tidak ada gairah seksual
      """)
   
   st.subheader("Cara Mencegah atau Mengatasi Depresi")
   st.markdown("""
      - Jaga kesehatan fisik
      - Mengelola dan mengatasi stres sebaik mungkin, seperti melakukan yoga dan meditasi secara rutin.
      - Tetap aktif secara social
      - Cari hobi dan aktivitas yang menyenangkan
      - Membatasi penggunaan media sosial yang tidak bermanfaat.- Atur waktu dengan baik
      - Kenali tanda-tanda awalnya
      - Jangan mengisolasi diri
      - Melakukan pola hidup teratur dengan istirahat cukup (6-8 jam sehari) dapat menurunkan tingkat depresi.
      - Menghindari konsumsi minuman beralkohol.
      - Menerapkan gaya hidup sehat, seperti mengonsumsi makanan sehat dengan gizi seimbang, rutin berolahraga, dan lain sebagainya.
      - Mengobati masalah kesehatan yang diderita secara rutin.
      - Berkonsultasi dengan psikolog atau psikiater apabila merasakan sedih yang mendalam dan berkepanjangan.
      - Olahraga dan rekreasi adalah salah satu cara untuk mencegah terjadinya depresi.
      - Sikap hidup yang positif, dengan berpikir rasional dan objektif akan mencegah gejala depresi.
      - Memiliki planning yang rasional dalam hidup, dan dapat menerima kondisi yang tak mungkin dapat diubah.
      - Memiliki kerabat atau sahabat yang dapat sewaktu waktu saling berbagi dan saling membantu.
      - Memiliki me time alias waktu untuk diri sendiri, di antara kesibukan yang padat.
      - Lakukan kegiatan seperti spa, meditasi, yoga, dan relaksasi.
      - Mengembangkan kehidupan spiritual 
               """)

   st.subheader("Penyebab Depresi")
   st.markdown("""
   Berikut adalah beberapa penyebab atau pemicu yang memungkinkan timbulnya Depresi :
      - Pola pikir yang salah, seperti toxic positivity
      - Hilangnya kegiatan atau tujuan hidup setelah pensiun (post power syndrome)
      - Terdapat riwayat keluarga dengan gangguan kesehatan mental, seperti gangguan makan, gangguan kecemasan, atau post-traumatic stress disorder (PTSD).
      - Gangguan senyawa kimia pada otak.
      - Gangguan keseimbangan hormon. Kondisi ini kerap dialami oleh pengidap penyakit tiroid, wanita menopause, ibu hamil, dan wanita sebelum maupun selama periode menstruasi.
      - Stres berat akibat kejadian-kejadian tertentu seperti kesulitan finansial, masalah rumah tangga, kematian orang terdekat, merasa terisolasi, tidak ada dukungan dari orang sekitar, dan lain sebagainya.
      - Trauma masa lalu, seperti pernah menjadi korban bullying, pelecehan seksual, dan lain-lain.
      - Mengidap penyakit serius atau kronis, seperti stroke, kanker, HIV/AIDS, penyakit jantung, dan lain-lain.
      - Efek samping dari obat-obatan tertentu, seperti obat hipertensi atau obat tidur.
      - Memiliki kepribadian tertentu, seperti pesimis, rendah diri, atau terlalu bergantung pada orang lain.
      - Ketergantungan NAPZA atau kecanduan alkohol.
      - Riwayat keluarga
      - Masalah kesehatan fisik
      - Peristiwa kehidupan yang penuh tekanan 
      - Berakhirnya hubungan, ditinggal oleh orang dicintai, masalah keuangan, dan sebagainya
      - Ketergantungan jenis obat tertentu
               """)

   st.subheader("Pengobatan Depresi")
   st.markdown("""
      - Melakukan psikoterapi atau terapi psikologis, untuk membantu mengatasi masalah akibat depresi
      - Memberikan obat antidepresan, untuk mengatasi depresi pasien
      - Menjalani perawatan di rumah sakit jika mengalami depresi yang parah
      - Perawatan mandiri
      - Terapi stimulasi otak
               """)
   

   st.divider()
   c = st.container()
   c.write("_Referensi :_")
   c.write("""Alodokter.com.(2024, 26 April). _Depresi_. Diakses pada 17 Juni 2024,
            dari https://www.alodokter.com/depresi 
         """)
   c.write("""Halodoc.com.(2023)._Depresi?_. Diakses pada 17 Juni 2024,
            dari https://www.halodoc.com/kesehatan/depresi 
          """)
   c.write("""Siloamhospitals.com.(2023, 20 September). _Depresi - Penyebab, Gejala,Diagnosis dan Cara Mengatasinya_. Diakses pada 17 Juni 2024,
            dari https://www.siloamhospitals.com/informasi-siloam/artikel/apa-itu-depresi 
         """)

   c.write("""Mitrakeluarga.com.(2023, 13 September). _Mengenal Gejala Depresi, Penyebab, dan Cara Mengatasinya_. Diakses pada 17 Juni 2024,
            dari https://www.mitrakeluarga.com/artikel/gejala-depresi
         """)

   c.write("""Prudential.co.id. _Apa itu Depresi? Penyebab, Gejala dan Cara Mengatasinya_. Diakses pada 17 Juni 2024,
            dari https://www.prudential.co.id/id/pulse/article/apa-itu-depresi/
         """)
   
   c.write("""National Institute Of Mental Health.(2024, April). Depression_. Diakses pada 17 Juni 2024,
            dari https://www.nimh.nih.gov/health/topics/depression
         """)


with tab4:
   st.header(" :four: Eating Disorder")
   st.write("_Eating Disorder_ adalah gangguan makan atau perilaku terkait makan yang berlangsung terus-menerus sehingga menyebabkan masalah kesehatan serius, baik fisik maupun psikososial. Eating disorder dapat mempengaruhi kemampuan tubuh untuk mendapatkan nutrisi yang dibutuhkan")
   st.subheader("Berbagai Gejala Eating Disorder (Gangguan Makan)")
   st.markdown("#### Bumilia Nervosa ")
   st.markdown("""
      - Sakit tenggorokan
      - Pembengkakan pada wajah atau kelenjar di rahang
      - Gangguan siklus menstruasi
      - Gigi sensitif dan rusak
      - Gusi berdarah
      - Sengaja memuntahkan makanan
      - Olahraga berlebihan
      - Sering ke kamar mandi setelah makan
      """)

   st.markdown("#### Anoreksia Nervosa ")
   st.markdown("""
      - Kulit kering
      - Rambut rontok
      - Tubuh terasa lemas
      - Sering merasa kedinginan akibat suhu tubuh yang rendah
      - Menstruasi menjadi tidak teratur atau bahkan terhenti (amenorrhea)
      - Sembelit atau konstipasi
      - Hipotensi atau tekanan darah rendah
      - Gangguan irama jantung
      - Kerusakan otak
      - Menyangkal rasa lapar
      - Mencari alasan untuk tidak makan
      - kebiasaan olahraga berlebihan 
      """)

   st.markdown("#### Gangguan Makan Berlebihan ")
   st.markdown("""
      - Mengonsumi makanan dalam jumlah banyak
      - Makan dengan sangat cepat
      - Tetap makan saat perut sudah kenyang
      - Bersembunyi saat makan karena malu bila terlihat orang
      - Tidak lapar secara fisik
      - Mengunyah lebih cepat dari orang normal
      - Bisa makan dalam porsi besar walau tidak lapar
      - Merasa jijik, depresi, malu, kesal, atau bersalah pada diri sendiri setelah makan
      - Memiliki perasaan yang sensitif, kesal, atau marah apabila berbicara tentang makanan atau mendengar tentang body shaming.
      - Memiliki perasaan cemas, putus asa, dan rasa percaya diri yang rendah
      - Menimbun makanan
               """)
   
   st.subheader("Cara Mencegah atau Mengatasi Eating Disorder")
   st.markdown("""
      - Menerapkan pola pemikiran yang sehat dalam hal berat badan, bentuk tubuh, dan berat badan.
      - Menghilangkan pola pikir bahwa bentuk tubuh dan berat badan menjadi penentu rasa bahagia dan sukses.
      - Pahami bahwa diet yang berlebihan adalah hal yang tidak sehat dan bisa memicu banyak masalah kesehatan, baik fisik maupun kejiwaan.
      - Konsumsi makanan sehat dengan asupan gizi seimbang.
      - Berolahraga secara rutin.
      - Menerapkan pola makan sehat yang telah dianjurkan oleh dokter,
      - Mengurangi kebiasaan mengisolasi diri dari keluarga dan teman-teman,
      - Belajar lebih mencintai diri sendiri dan tidak membandingkan diri dengan orang lain,
      - Menghindari keinginan untuk menimbang berat badan atau bercermin terlalu sering,
      - Menghentikan penggunaan pil diet atau obat pencahar, dan
      - Mengelola stres dengan berolahraga atau melakukan aktivitas lain yang disenangi.  
               """)

   st.subheader("Penyebab Eating Disorder")
   st.markdown("""
   Berikut adalah beberapa penyebab atau pemicu yang memungkinkan timbulnya Eating Disorder :
      - Genetik. 
      - Biologis. 
      - Keturunan. 
      - Psikologis. 
      - Tekanan masyarakat. 
      - Diet yang berlebihan
      - Stres
               """)

   st.subheader("Pengobatan Eating Disorder")
   st.markdown("""
      - Psikoterapi
      - Obat medis
      - Berdiskusi dengan ahli gizi
               """)
   


   st.divider()
   c = st.container()
   c.write("_Referensi :_")
   c.write("""Alodokter.com.(2022, 10 Maret). _Gangguan Makan_. Diakses pada 17 Juni 2024,
            dari https://www.alodokter.com/gangguan-makan
         """)
   c.write("""Halodoc.com.(2023)._Gangguan Makan_. Diakses pada 17 Juni 2024,
            dari https://www.halodoc.com/kesehatan/gangguan-makan
          """)
   c.write("""Siloamhospitals.com.(2023, 06 Oktober). Kenali Gejala dan Jenis Gangguan Makan (Eating Disorders)_. Diakses pada 17 Juni 2024,
            dari https://www.siloamhospitals.com/informasi-siloam/artikel/kenali-gejala-dan-ragam-jenis-gangguan-makan-eating-disorders
          """)

   c.write("""Hellosehat.com.(2023, 24 Februari). _Eating Disorder (Gangguan Makan)_. Diakses pada 17 Juni 2024,
            dari https://hellosehat.com/mental/gangguan-makan/eating-disorder/
         """)

   c.write("""Emc.id.(2023, 24 Agustus). _Lebih Dekat dengan Ragam Eating Disorder dan Penanganannya_. Diakses pada 17 Juni 2024,
            dari https://www.emc.id/id/care-plus/lebih-dekat-dengan-ragam-eating-disorder-dan-penanganannya
         """)
   
   c.write("""National Institute Of Mental Health.(2024, April). _Eating Disorder_. Diakses pada 17 Juni 2024,
            dari https://www.nimh.nih.gov/health/topics/eating-disorders
         """)
   
with tab5:
   st.header(" :five: OCD (Obsessive Compulsive Disorder)")
   st.write("_Obsessive Compulsive Disorder_ atau disingkat _OCD_ adalah bentuk masalah kesehatan mental yang membuat pengidapnya mempunyai pemikiran dan dorongan yang tidak bisa dikontrol yang sifatnya berulang (obsesi) serta munculnya perilaku (paksaan) kompulsif. Contoh perilaku kompulsif misalnya mencuci tangan hingga berulang kali setelah melakukan kontak langsung terhadap sesuatu yang menurutnya tidak bersih.")
   st.subheader("Berbagai Gejala OCD (Obsessive Compulsive Disorder)")
   st.markdown("#### Gejala Obsesi ")
   st.markdown("""
      - Mengonsumi makanan dalam jumlah banyak
      - Merasa takut terkontaminasi setelah menyentuh benda yang disentuh orang lain.
      - Ragu jika sudah mengunci pintu atau mematikan kompor.
      - Stres yang berlebihan saat benda-benda tersusun secara tidak teratur atau tidak menghadap ke arah tertentu / tidak simetris
      - Memiliki gambaran mengemudi mobil ke arah kerumunan orang.
      - Berpikir ingin meneriakkan umpatan atau bertindak tidak pantas di tempat umum.
      - Menghindari situasi yang bisa memicu obsesi, seperti berjabat tangan.
      - Takut mengatakan sesuatu yang mungkin menyinggung perasaan orang lain
      - Khawatir membuang barang yang telah dikumpulkan atau hoarding disorder
               """)

   st.markdown("#### Gejala Kompulsi")
   st.markdown("""
      - Mencuci tangan terus-menerus sampai kulit menjadi lecet.
      - Memeriksa pintu berkali-kali untuk memastikan sudah terkunci.
      - Memeriksa kompor berulang kali untuk memastikan jika sudah dimatikan.
      - Menghitung dalam pola tertentu.
      - Mengulang sebuah doa, kata, atau frasa.
      - Menyusun barang-barang agar menghadap ke arah yang sama.
      - Mengumpulkan atau menimbun barang-barang, seperti surat atau koran yang tidak terpakai
               """)

   st.subheader("Cara Mencegah atau Mengatasi OCD")
   st.markdown("""
      - Terapi kognitif untuk membantu pasien mengidentifikasi dan memahami kekhawatirannya serta mengajari pasien mengurangi atau mengatasi kekhawatiran itu dengan lebih baik.
      - Terapi perilaku untuk membantu pasien mengubah atau membatasi perilaku obsesif kompulsif.
      - Terapi keluarga terutama bagi orang tua jika pasiennya masih anak-anak agar paham dan terlibat aktif dalam pengobatan pasien.
      - Obat-obatan untuk menaikkan kadar hormon serotonin di otak.
      - Penggunaan antibiotik bila ditemukan kaitan OCD yang diderita dengan infeksi bakteri streptokokus.
      - Menjaga Kesehatan Fisik dan Mental
      - Menjaga Pola Makan yang Sehat
      - Berolahraga secara Teratur
      - Menjaga Hubungan Sosial yang Sehat
      - Menghindari Stres dan Kecemasan
               """)

   st.subheader("Penyebab OCD")
   st.markdown("""
   Berikut adalah beberapa penyebab atau pemicu yang memungkinkan timbulnya OCD :
      - Faktor genetik atau keturunan
      - Pengaruh lingkungan sekitar
      - Gangguan senyawa kimia (neurotransmitter) di dalam otak, seperti norepinefrin dan serotonin
      - Gangguan emosi
      - Trauma
      - Infeksi
      - Lingkungan
               """)

   st.subheader("Pengobatan OCD")
   st.markdown("""
      - Psikoterapi
      - Relaksasi
      - Pengobatan
      - Neuromodulasi
      - Stimulasi magnetik transkranial
               """)
   
   st.divider()
   c = st.container()
   c.write("_Referensi :_")
   c.write("""Alodokter.com.(2022, 04 April). _OCD_. Diakses pada 17 Juni 2024,
            dari https://www.alodokter.com/ocd
         """)
   c.write("""Halodoc.com.(2023)._OCD_. Diakses pada 17 Juni 2024,
            dari https://www.halodoc.com/kesehatan/ocd
          """)
   c.write("""Siloamhospitals.com.(2024, 21 Mei). _Obsessive Compulsive Disorder (OCD) : Penyebab & Pengobatannya_. Diakses pada 17 Juni 2024,
            dari https://www.siloamhospitals.com/informasi-siloam/artikel/apa-itu-obsessive-compulsive-disorder
          """)

   c.write("""Klildokter.com.(2022, 21 Maret). _Obsessive Compulsive Disorder (OCD)_. Diakses pada 17 Juni 2024,
            dari https://www.klikdokter.com/penyakit/masalah-mental/ocd
         """)

   c.write("""Emc.id.(2022, 20 Juli). _Kenali Gejala Obsessive-Compulsive Disorder atau OCD_. Diakses pada 17 Juni 2024,
            dari https://www.emc.id/id/care-plus/kenali-gejala-obsessive-compulsive-disorder-atau-ocd
         """)
   
   c.write("""National Institute Of Mental Health.(2024, April). _Obsessive-Compulsive Disorder_. Diakses pada 17 Juni 2024,
            dari https://www.nimh.nih.gov/health/topics/obsessive-compulsive-disorder-ocd
         """)

with tab6:
   st.header(" :six: PTSD (Post Traumatic Stress Disorder)")
   st.write("_Post Traumatic Stress Disorder_ atau _PTSD_ adalah gangguan mental yang terjadi pada seseorang karena mengalami kejadian traumatis, seperti bencana alam, kecelakaan, terorisme, perang/pertempuran, pelecehan seksual, kekerasan dan sejenisnya.")
   st.subheader("Berbagai Gejala PTSD (Post Traumatic Stress Disorder)")
   st.markdown("""
      - Munculnya ingatan pada peristiwa traumatis
      - Sering bermimpi buruk yang berkaitan dengan kejadian traumatis tersebut
      - Cenderung menghindari tempat atau hal-hal yang berkaitan dengan kejadian traumatis
      - Stres dan sering muncul pikiran negatif
      - Sulit untuk tidur
      - Merasa takut untuk bertemu orang lain
      - Sulit berkonsentrasi
      - Mudah terkejut, takut atau marah
      - Tidak berhasrat untuk melakukan kegiatan yang biasanya digemari
      - Cenderung menyalahkan diri sendiri / orang lain
      - Putus asa tentang masa depan
      - Kesulitan dalam mengingat
      - Merasa jauh dari keluarga dan teman
      - Kurangnya minat pada kegiatan yang disukai sebelumnya
      - Tak ada emosi positif
      - Mati rasa
      - Perilaku merusak diri
      - Selalu waspada terhadap sesuatu / bahaya
               """)

   st.subheader("Cara Mencegah atau Mengatasi PTSD")
   st.markdown("""
      - Bicarakan kepada keluarga, teman, atau terapis mengenai kejadian traumatis yang Anda alami.
      - Konsultasikan ke dokter jika Anda tidak dapat mengatasi perasaan yang timbul setelah mengalami kejadian tidak menyenangkan.
               """)

   st.subheader("Penyebab PTSD")
   st.markdown("""
   Berikut adalah beberapa penyebab atau pemicu yang memungkinkan timbulnya PTSD :
      - Perang dan kekerasan terorganisir: Terlibat dalam pertempuran, pengalaman perang, atau menjadi korban kekerasan terorganisir.
      - Perundungan
      - Pernah menderita penyakit yang bisa mengancam nyawa, contohnya seperti serangan jantung
      - Mengalami peristiwa traumatis.
      - Emosi yang cenderung tidak stabil.
      - Riwayat keluarga kandung yang memiliki gangguan mental.
      - Tidak mendapatkan dukungan dari kerabat dekat.
      - Memiliki pekerjaan yang berisiko mengalami peristiwa traumatis, seperti militer, dokter, dan sejenisnya.
      - Menggunakan obat-obatan terlarang serta mengonsumsi alkohol secara berlebihan.
      - Pengalaman yang tidak menyenangkan
      - Kepribadian bawaan yang temperamen
      - Kekerasan fisik atau seksual: Menjadi korban atau menyaksikan kekerasan fisik atau seksual yang ekstrem.
      - Kecelakaan serius: Terlibat dalam atau menyaksikan kecelakaan serius yang melibatkan risiko kehidupan atau cedera parah.
      - Bencana alam dan kejadian traumatis lainnya: Mengalami bencana alam, kecelakaan besar, atau peristiwa traumatis lainnya yang menyebabkan rasa takut dan ketidakamanan.
      - Ketidakamanan berulang di lingkungan tertentu: Hidup dalam situasi yang terus-menerus tidak aman, misalnya dalam hubungan yang penuh kekerasan atau di lingkungan yang tidak stabil.
      - Kehilangan yang traumatis: Kehilangan yang terasa traumatis, seperti kematian mendadak atau kehilangan yang terkait dengan peristiwa yang penuh trauma.
      - Pengalaman traumatik di masa kanak-kanak: Mengalami trauma yang signifikan selama masa kanak-kanak, seperti kekerasan dalam rumah tangga atau pelecehan seksual.
               """)

   st.subheader("Pengobatan PTSD")
   st.markdown("""
      - Psikoterapi
      - Obat - obatan
      - Terapi EMDR
      - Group Therapy
               """)
   
   st.divider()
   c = st.container()
   c.write("_Referensi :_")
   c.write("""Alodokter.com.(2022, 09 Mei). _PTSD_. Diakses pada 17 Juni 2024,
            dari https://www.alodokter.com/ptsd
         """)
   c.write("""Halodoc.com.(2023)._PTSD_. Diakses pada 17 Juni 2024,
            dari https://www.halodoc.com/kesehatan/ptsd
          """)
   c.write("""Siloamhospitals.com.(2023, 10 November). _Mengenal PTSD : Penyebab, Gejala hingga Pengobatannya_. Diakses pada 17 Juni 2024,
            dari https://www.siloamhospitals.com/informasi-siloam/artikel/post-traumatic-stress-disorder
          """)

   c.write("""Hellosehat.com.(2023, 05 Juni). _Post-Traumatic Stress Disorder (PTSD)_. Diakses pada 17 Juni 2024,
            dari https://hellosehat.com/mental/mental-lainnya/ptsd/#google_vignette
         """)

   c.write("""Emc.id.(2023, 13 Desember). _Serba-Serbi PTSD Mulai dari Gejala, Penyebab, dan Cara Mengobatinya_. Diakses pada 17 Juni 2024,
            dari https://www.emc.id/id/care-plus/serba-serbi-ptsd-mulai-dari-gejala-penyebab-dan-cara-mengobatinya
         """)
   
   c.write("""National Institute Of Mental Health.(2024, April). _Post-Traumatic Stress Disorder_. Diakses pada 17 Juni 2024,
            dari https://www.nimh.nih.gov/health/topics/post-traumatic-stress-disorder-ptsd
         """)

with tab7:
   st.header("	:seven: Skizophrenia")
   st.write("_Skizofrenia_ adalah gangguan mental berat yang dapat memengaruhi tingkah laku, emosi, dan komunikasi. Penderita _skizofrenia_ bisa mengalami halusinasi, delusi, kekacauan berpikir, dan perubahan perilaku.")
   st.subheader("Berbagai Gejala Skizophrenia")
   st.markdown("#### Gejala Negatif")
   st.markdown("""
      - Menurunnya keinginan berbicara dan bersosialisasi.
      - Menurunnya minat dan motivasi.
      - Kehilangan beragam emosi yang biasanya dirasakan dan ditampilkan.
      - Keinginan untuk tetap malas dan lesu serta menolak berubah.
      - Mengabaikan pada penampilan dan kebersihan diri
      - Perubahan pada pola tidur
      - Hilang minat dan motivasi pada berbagai aktivitas
      - Sulit merasa senang atau puas
      - Tanggapan emosional yang tidak wajar terhadap suatu situasi
      - Berkurangnya intensitas berbicara
      - Kurangnya emosi atau ekspresi (tidak melakukan kontak mata, tidak mengubah ekspresi wajah atau berbicara dengan nada monoton)
      - Kesulitan menyelesaikan aktivitas normal sehari-hari
               """)

   st.markdown("#### Gejala Positif")
   st.markdown("""
      - Halusinasi, sering kali berbentuk bayangan atau suara-suara yang tidak nyata.
      - Delusi, contohnya menganggap bahwa dirinya sedang dikejar-kejar orang atau organisasi tertentu.
      - Paranoia, ketika seseorang sangat tidak percaya pada orang lain atau sangat yakin bahwa mereka sedang diikuti atau dianiaya.
      - Perubahan perilaku dan cara bicara menjadi tidak teratur (meracau).
      - Kekacauan dalam berperilaku, seperti berteriak secra tiba" dan marah tanpa alasan
               """)

   st.markdown("#### Gejala Kognitif")
   st.markdown("""
     - Kesulitan berkonsentrasi, berfikir dan sulit fokus
     - Menurunnya fungsi memori.
     - Kesulitan dalam menerima dan memahami sinyal atau tanda-tanda dalam hubungan dengan orang lain.
     - Menurunnya kemampuan untuk mengatur dan cenderung berpikir abstrak.
     - Pemikiran yang tidak teratur, seperti kesulitan memperhatikan
               """)

   st.subheader("Penyebab Skizophrenia")
   st.markdown("""
   Berikut adalah beberapa penyebab atau pemicu yang memungkinkan timbulnya PTSD :
      - Faktor Genetik dan Lingkungan
      - Perbedaan Struktur Otak
      - Ketidakseimbangan Kimia di Otak
      - Penggunaan Obat Tertentu
      - Komplikasi kehamilan dan persalinan
               """)

   st.subheader("Pengobatan Skizophrenia")
   st.markdown("""
      - Obat medis
      - Psikoterapi
      - Terapi elektrokonvulsi
      - Transcranial magnetic stimulation (TMS)
               """)
   

   st.divider()
   c = st.container()
   c.write("_Referensi :_")
   c.write("""Alodokter.com.(2023, 17 Januari). _Skizofrenia_. Diakses pada 17 Juni 2024,
            dari https://www.alodokter.com/skizofrenia
         """)
   c.write("""Halodoc.com.(2023)._Skizofrenia_. Diakses pada 17 Juni 2024,
            dari https://www.halodoc.com/kesehatan/skizofrenia
          """)
   c.write("""Siloamhospitals.com.(2024, 21 Mei). _Schizophrenia - Causes, Symptoms, and Treatments_. Diakses pada 17 Juni 2024,
            dari https://www.siloamhospitals.com/en/informasi-siloam/artikel/skizofrenia-adalah
          """)
   
   c.write("""National Institute Of Mental Health.(2024, April). _Schizophrenia_. Diakses pada 17 Juni 2024,
            dari https://www.nimh.nih.gov/health/topics/schizophrenia
         """)