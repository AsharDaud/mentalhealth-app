import pandas as pd
import streamlit as st
import time
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Apllication System",
    page_icon=":brain:"
)

df = pd.read_csv("data/survey mental health 2.csv")

X = df.drop('Label', axis=1)
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

model_path = 'model/mental_health_model.joblib'
model = joblib.load(model_path)

questions = {
    'anx1': "Dari skala dibawah ini, Seberapa sering anda merasa gugup, gelisah / tegang?",
    'anx2': "Dari skala di bawah ini, Seberapa sering anda sulit mengendalikan rasa khawatir / kecemasan?",
    'anx3': "Dari skala di bawah ini, Seberapa sering anda berkeringat dingin / berlebihan dan gemetaran?",
    'anx4': "Dari skala di bawah ini, Seberapa sering anda mengalami detak jantung yang meningkat / bernafas dengan cepat?",
    'anx5': "Dari skala di bawah ini, seberapa sering anda kesulitan berkonsentrasi atau pikiran menjadi kosong?",

    'bpl1': "Dari skala di bawah ini, Seberapa sering anda merasa sangat bahagia, antusias, ataupun terlalu bersemangat?",
    'bpl2': "Dari skala di bawah ini, Seberapa sering anda sangat percaya diri, merasa penting, berbakat, ataupun kuat?",
    'bpl3': "Dari skala di bawah ini, Seberapa sering anda memiliki harga diri yang melambung ataupun lebih banyak bicara daripada biasanya?",
    'bpl4': "Dari skala di bawah ini, Seberapa sering anda merasa sangat sedih, putus asa atau merasa diri sendiri tidak berharga dan merasa bersalah yang berlebihan?",
    'bpl5': "Dari skala di bawah ini, Seberapa sering anda mempunyai pikiran tentang kematian yang berulang (bukan hanya rasa takut akan kematian), ide bunuh diri yang berulang tanpa rencana khusus, upaya bunuh diri, atau rencana khusus untuk bunuh diri.",

    'dpr1': "Dari skala di bawah ini, Seberapa sering anda merasa sangat sensitif, mudah marah, tersinggung / frustasi dan cenderung menutup diri dari lingkungan?",
    'dpr2': "Dari skala di bawah ini, Seberapa sering anda merasa minat atau kesenangan yang sangat berkurang?",
    'dpr3': "Dari skala di bawah ini, Seberapa sering anda merasa putus asa atau pesimis?",
    'dpr4': "Dari skala di bawah ini, Seberapa sering Suasana hati anda merasa tertekan?",
    'dpr5': "Dari skala di bawah ini, Seberapa sering anda merasa pernah timbul ide untuk menyakiti diri sendiri atau percobaan bunuh diri?",

    'eat1': "Dari skala di bawah ini, Seberapa sering anda memuntahkan kembali makanan yang telah anda makan?",
    'eat2': "Dari skala di bawah ini, Seberapa sering anda menghindari rasa lapar karena terobsesi kurus?",
    'eat3': "Dari skala di bawah ini, Seberapa sering anda mengonsumsi makanan dalam jumlah banyak dan makan dengan sangat cepat?",
    'eat4': "Dari skala di bawah ini, Seberapa sering anda merasa jijik, depresi, malu, kesal, atau bersalah pada diri sendiri setelah makan?",
    'eat5': "Dari skala di bawah ini, Seberapa sering anda merasa ketakutan yang kuat akan kenaikan berat badan atau menjadi gemuk, atau perilaku terus-menerus yang mengganggu kenaikan berat badan, meskipun berat badannya sangat rendah?",

    'ocd1': "Dari skala di bawah ini, Seberapa sering anda memeriksa pintu. Apakah sudah dikunci ataupun mengecek kompor sudah dimatikan secara berkali - kali?",
    'ocd2': "Dari skala di bawah ini, Seberapa sering anda merasa stres yang berlebihan saat benda-benda tersusun secara tidak teratur atau tidak menghadap ke arah tertentu / tidak simetris?",
    'ocd3': "Dari skala di bawah ini, Seberapa sering anda mmenyusun atau menata barang dengan cara tertentu dan tepat?",
    'ocd4': "Dari skala di bawah ini, Seberapa sering anda mencuci tangan berkali - kali sampai kulit lecet karena merasa masih kotor dan takut akan kuman?",
    'ocd5': "Dari skala di bawah ini, Seberapa sering anda takut lupa, kehilangan, atau salah menaruh sesuatu?",

    'ptsd1': "Dari skala di bawah ini, Seberapa sering anda mengalami munculnya ingatan pada peristiwa traumatis?",
    'ptsd2': "Dari skala di bawah ini, Seberapa sering anda menghindari tempat atau hal-hal yang berkaitan dengan kejadian traumatis?",
    'ptsd3': "Dari skala di bawah ini, Seberapa sering anda bermimpi buruk yang berkaitan dengan kejadian traumatis tersebut?",
    'ptsd4': "Dari skala di bawah ini, Seberapa sering anda merasa mudah terkejut, takut atau mengalami keadaan emosional negatif yang terus-menerus?",
    'ptsd5': "Dari skala di bawah ini, Seberapa sering anda merasa mempuyai tingkat kewaspadaan yang berlebihan?",

    'adhd1': "Dari skala di bawah ini, Seberapa sering anda mengalami kesulitan dalam mempertahankan perhatian pada tugas atau aktivitas tertentu (misalnya, kesulitan tetap fokus selama kuliah, percakapan, atau membaca panjang)?",
    'adhd2': "Dari skala di bawah ini, Seberapa sering anda tampak tidak mendengarkan saat diajak berbicara langsung (misalnya, pikirannya tampak kemana-mana, bahkan tanpa gangguan yang jelas)?",
    'adhd3': "Dari skala di bawah ini, Seberapa sering anda gelisah dengan tangan atau kaki saat duduk, atau bergerak-gerak di tempat duduknya?",
    'adhd4': "Dari skala di bawah ini, Seberapa sering anda kesulitan menunggu giliran (misalnya, saat menunggu dalam antrean)?",
    'adhd5': "Dari skala di bawah ini, Seberapa sering anda menginterupsi atau mengganggu orang lain, misalnya dalam percakapan, permainan, atau kegiatan?",

    }

if 'responses' not in st.session_state:
    st.session_state.responses = {key: 1 for key in questions}

# Function to reset radio buttons
def reset_radio_buttons():
    for key in questions.keys():
        st.session_state.responses[key] = 1  # Reset all responses to initial value (1)
    st.session_state.identification_result = None  # Reset the identification result
    st.experimental_rerun()  # Force a rerun to immediately update the UI

st.title("Test System")
st.warning(""" 
        **:warning: Peringatan !!!**
        
        - Sistem yang dibuat hanya sebagai deteksi dini dan tidak dapat digunakan sebagai acuan diagnosis gangguan yang di alami.
        - Hasil dari identifikasi hanya sebagai prediksi kondisi kesehatan mental dan sebagai rujukan untuk penanganan lebih lanjut.
        - Apabila anda merasa memiliki masalah (gangguan) dan memerlukan penanganan lebih lanjut, di harapkan menghubungi seorang profesional / pakar terkait kesehatan mental.
           """)
st.divider() 

st.sidebar.info("**Note:** Skala 1 - 8 menunjukkan seberapa sering anda mengalami gejala tersebut. Semakin tinggi skala, semakin sering Anda mengalami gejala tersebut. Sebagai contoh, dalam rentang waktu 1 minggu, skala 1 dapat menunjukkan bahwa gejala tidak pernah muncul, sedangkan skala 8 menunjukkan bahwa gejala tersebut dialami setiap hari. ")

responses = {}
num_columns = 1  # Adjust this number based on how many radio buttons you want per row
columns = st.columns(num_columns)

# Display the questions with radio buttons
for idx, (key, question) in enumerate(questions.items()):
    col_idx = idx % num_columns
    with columns[col_idx]:
        responses[key] = st.radio(
            question,
            options=list(range(1, 9)),
            index=list(range(1, 9)).index(st.session_state.responses[key]),
            horizontal=True,
            key=key
        )

if responses != st.session_state.responses:
    st.session_state.responses.update(responses)

def predict_mental_health(responses, model):
    response_values = list(responses.values())
    X_pred = pd.DataFrame([response_values], columns=responses.keys())
    
    # Ensure the response DataFrame has the same columns as the training data
    X_train_columns = pd.get_dummies(df.drop('Label', axis=1)).columns
    X_pred = pd.get_dummies(X_pred)
    X_pred = X_pred.reindex(columns=X_train_columns, fill_value=0)
    
    predicted_mental_health = model.predict(X_pred)[0]
    
    return predicted_mental_health

def identify_mental_health(responses):
    # Define the mapping of questions to mental health conditions
    conditions = {
        "Anxiety": ["anx1", "anx2", "anx3", "anx4", "anx5"],
        "Bipolar": ["bpl1", "bpl2", "bpl3", "bpl4", "bpl5","dpr1", "dpr2", "dpr3", "dpr4", "dpr5"],
        "Depresi": ["bpl4", "bpl5", "dpr1", "dpr2", "dpr3", "dpr4", "dpr5"],
        "Eating Disorder": ["eat1", "eat2", "eat3", "eat4", "eat5"],
        "OCD": ["ocd1", "ocd2", "ocd3", "ocd4", "ocd5"],
        "PTSD": ["ptsd1", "ptsd2", "ptsd3", "ptsd4", "ptsd5"],
        "ADHD": ["adhd1", "adhd2", "adhd3", "adhd4", "adhd5"]
    }

    scores = {condition: 0 for condition in conditions}

    for condition, question_keys in conditions.items():
        scores[condition] = sum(responses[key] for key in question_keys)

    # Sort conditions by score in descending order
    sorted_conditions = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    # Identify conditions with scores above 50% threshold
    identified_conditions = [condition for condition, score in sorted_conditions if score > 16]

    if not identified_conditions:
        # If no condition exceeds the threshold, choose the one with the highest score
          identified_conditions = [sorted_conditions[0][0]]  # Get the condition with the highest score

    return identified_conditions, sorted_conditions

col1, col2, col3 = st.columns(3)

with col1:
    identify_button = st.button('Prediksi Mental Health')

with col2:
    reset_button = st.button('Reset', type="primary")

# Logic for buttons
if identify_button:
    # Check if all responses are at minimum value (1)
    if all(value == 1 for value in responses.values()):
        e = RuntimeError('Tolong isi data terlebih dahulu')
        st.exception(e)
    else:
        # Check if all responses have the same value
        if len(set(responses.values())) == 1:
            e = RuntimeError('Semua data sama, tolong sesuaikan datanya')
            st.exception(e)
        else:
            # Show spinner while processing
            with st.spinner('Mengidentifikasi...'):
                time.sleep(2)  # Simulate some processing time
                identified_conditions, sorted_conditions = identify_mental_health(responses)
                result_message = f"Anda mungkin mengalami gangguan: **{', '.join(identified_conditions)}**"
                st.success(result_message)
                
                st.subheader("Penjelasan Terkait Masalah Kesehatan Mental yang Diidentifikasi")

                # List untuk menyimpan deskripsi kondisi mental yang teridentifikasi
                descriptions = []
                
                for condition, score in sorted_conditions:
                    if condition in identified_conditions:
                        if condition == "Anxiety":
                            # Deskripsi tentang kondisi
                            st.markdown("""
                            **Anxiety** adalah respons alami tubuh terhadap stres, yang ditandai dengan perasaan khawatir, gelisah atau takut yang berlebihan. 
                            Gejala fisik mungkin termasuk detak jantung yang cepat, pernapasan cepat, berkeringat, dan kelelahan.
                            """)

                            # Rekomendasi menggunakan st.expander
                            with st.expander("**Rekomendasi untuk Anxiety**", expanded=False):
                                st.markdown("""
                                #### Psychotherapy
                                **Psikoterapi**, atau "terapi bicara" dapat membantu orang dengan gangguan kecemasan. Agar efektif, psikoterapi harus diarahkan pada kecemasan spesifik Anda dan disesuaikan dengan kebutuhan Anda.
                                
                                #### Cognitive behavioral therapy
                                **Terapi perilaku kognitif (CBT)**, adalah salah satu contoh jenis psikoterapi yang dapat membantu orang dengan gangguan kecemasan. Ini mengajarkan orang cara berpikir, berperilaku, dan bereaksi terhadap situasi yang berbeda untuk membantu Anda merasa kurang cemas dan takut. CBT telah dipelajari dengan baik dan merupakan standar emas untuk psikoterapi.\n
                                Terapi perilaku kognitif (CBT) adalah salah satu contoh jenis psikoterapi yang dapat membantu orang dengan gangguan kecemasan. Ini mengajarkan orang cara berpikir, berperilaku, dan bereaksi terhadap situasi yang berbeda untuk membantu Anda merasa kurang cemas dan takut. CBT telah dipelajari dengan baik dan merupakan standar emas untuk psikoterapi.

                                #### Acceptance and commitment therapy
                                **Terapi penerimaan dan komitmen (ACT)**, adalah pilihan perawatan lain untuk beberapa gangguan kecemasan. ACT mengambil pendekatan yang berbeda dari CBT terhadap pikiran negatif. Ini menggunakan strategi seperti kesadaran dan penentuan tujuan untuk mengurangi ketidaknyamanan dan kecemasan. Dibandingkan dengan CBT, ACT adalah bentuk terapi psikoterapi yang lebih baru, sehingga lebih sedikit data yang tersedia tentang keefektifannya.

                                #### Medication
                                **Medication**, Obat tidak menyembuhkan gangguan kecemasan tetapi dapat membantu meredakan gejalanya. Penyedia layanan kesehatan, seperti psikiater atau penyedia layanan kesehatan utama, dapat meresepkan obat untuk kecemasan. Beberapa negara bagian juga memungkinkan psikolog yang telah menerima pelatihan khusus untuk meresepkan obat psikiatrik. Kelas obat yang paling umum digunakan untuk melawan gangguan kecemasan adalah antidepresan, obat anti-kecemasan (seperti benzodiazepin), dan beta-blocker. 

                                #### Antidepressants
                                **Antidepresan**, digunakan untuk mengobati depresi, tetapi juga dapat membantu mengobati gangguan kecemasan. Mereka mungkin membantu meningkatkan cara otak Anda menggunakan bahan kimia tertentu yang mengendalikan suasana hati atau stres. Anda mungkin perlu mencoba beberapa obat antidepresan yang berbeda sebelum menemukan yang meningkatkan gejala Anda dan memiliki efek samping yang dapat dikelola.\n
                                Antidepresan dapat memakan waktu beberapa minggu untuk mulai bekerja, jadi penting untuk memberikan kesempatan kepada obat sebelum mencapai kesimpulan tentang keefektifannya. Jika Anda mulai mengonsumsi antidepresan, jangan berhenti mengonsumsinya tanpa bantuan penyedia layanan kesehatan. Penyedia layanan kesehatan Anda dapat membantu Anda mengurangi dosis secara perlahan dan aman. Menghentikannya secara tiba-tiba dapat menyebabkan gejala penarikan.\n
                                Dalam beberapa kasus, anak-anak, remaja, dan orang dewasa yang berusia kurang dari 25 tahun mungkin mengalami peningkatan pikiran atau perilaku bunuh diri saat mengonsumsi obat antidepresan, terutama dalam beberapa minggu pertama setelah memulai atau ketika dosis diubah. Karena alasan ini, orang-orang dari semua usia yang mengonsumsi antidepresan harus diawasi secara ketat, terutama selama beberapa minggu pertama pengobatan.

                                #### Anti-anxiety medications
                                **Obat anti-kecemasan**, dapat membantu mengurangi gejala kecemasan, serangan panik, atau ketakutan dan kekhawatiran yang ekstrim. Obat anti-kecemasan yang paling umum disebut benzodiazepin. Meskipun benzodiazepin kadang-kadang digunakan sebagai perawatan lini pertama untuk gangguan kecemasan umum, mereka memiliki manfaat dan kelemahan.\n
                                Benzodiazepin efektif dalam meredakan kecemasan dan mulai bekerja lebih cepat daripada obat antidepresan. Namun, beberapa orang mengembangkan toleransi terhadap obat-obatan ini dan membutuhkan dosis yang lebih tinggi dan lebih tinggi untuk mendapatkan efek yang sama. Beberapa orang bahkan menjadi bergantung pada mereka.\n
                                Untuk menghindari masalah ini, penyedia layanan kesehatan biasanya meresepkan benzodiazepin untuk jangka waktu singkat.\n
                                Jika orang tiba-tiba berhenti mengonsumsi benzodiazepin, mereka mungkin mengalami gejala penarikan atau kecemasan mereka mungkin kembali. Oleh karena itu, benzodiazepin harus dikurangi secara perlahan. Penyedia layanan kesehatan Anda dapat membantu Anda mengurangi dosis secara perlahan dan aman.
                                            
                                #### Beta-blockers
                                **Beta-blockers**, Meskipun beta-blocker paling sering digunakan untuk mengobati tekanan darah tinggi, mereka dapat membantu meredakan gejala fisik kecemasan, seperti detak jantung cepat, gemetar, bergetar, dan tersipu. Obat-obatan ini dapat membantu orang menjaga gejala fisik di bawah kendali ketika dikonsumsi untuk jangka waktu singkat. Mereka juga dapat digunakan "seperlunya" untuk mengurangi kecemasan akut, termasuk untuk mencegah beberapa bentuk kecemasan kinerja yang dapat diprediksi. 

                                #### Choosing the right medication
                                **Memilih obat yang tepat**, Beberapa jenis obat mungkin bekerja lebih baik untuk jenis gangguan kecemasan tertentu, sehingga orang harus bekerja sama dengan penyedia layanan kesehatan untuk mengidentifikasi obat mana yang terbaik untuk mereka. Zat-zat tertentu seperti kafein, beberapa obat bebas batuk, obat-obatan terlarang, dan suplemen herbal dapat memperburuk gejala gangguan kecemasan atau berinteraksi dengan obat yang diresepkan. Orang harus berbicara dengan penyedia layanan kesehatan, sehingga mereka dapat mempelajari zat mana yang aman dan mana yang harus dihindari.\n
                                Memilih obat, dosis obat, dan rencana perawatan yang tepat harus dilakukan di bawah perawatan ahli dan harus didasarkan pada kebutuhan seseorang dan situasi medis mereka. Anda dan penyedia layanan kesehatan Anda mungkin mencoba beberapa obat sebelum menemukan yang tepat.

                                #### Support groups
                                **Support groups**, Beberapa orang dengan gangguan kecemasan mungkin mendapat manfaat dari bergabung dengan kelompok swadaya atau kelompok pendukung dan berbagi masalah serta pencapaian mereka dengan orang lain. Kelompok pendukung tersedia baik secara langsung maupun online. Namun, setiap saran yang Anda terima dari anggota kelompok pendukung harus digunakan dengan hati-hati dan tidak menggantikan rekomendasi perawatan dari penyedia layanan kesehatan.

                                #### Stress management techniques
                                **Stress management techniques**, Teknik manajemen stres, seperti olahraga, kesadaran, dan meditasi, juga dapat mengurangi gejala kecemasan dan meningkatkan efek psikoterapi. Anda dapat mempelajari lebih lanjut tentang bagaimana teknik-teknik ini bermanfaat bagi perawatan Anda dengan berbicara dengan penyedia layanan kesehatan.

                                """)
                        
                        elif condition == "Bipolar":
                            st.markdown("""
                            **Bipolar** adalah gangguan mental yang menyebabkan perubahan suasana hati, energi, aktivitas, dan kemampuan untuk menjalani aktivitas sehari-hari. 
                            Ini termasuk periode manik (perasaan sangat bahagia atau sangat mudah tersinggung) dan periode depresi (perasaan sangat sedih atau putus asa).
                            """)
                            
                            with st.expander("**Rekomendasi untuk Bipolar**", expanded=False):
                                st.markdown("""
                                #### Medication
                                Obat-obatan tertentu dapat membantu mengelola gejala gangguan bipolar. Beberapa orang mungkin perlu mencoba obat yang berbeda dan bekerja dengan penyedia layanan kesehatan mereka untuk menemukan obat yang paling efektif.\n
                                Jenis obat yang paling umum yang diresepkan oleh penyedia layanan kesehatan termasuk mood stabilizer dan antipsikotik atipikal. Mood stabilizer seperti lithium atau valproate dapat membantu mencegah episode mood atau mengurangi keparahannya. Lithium juga dapat mengurangi risiko bunuh diri. Penyedia layanan kesehatan mungkin memasukkan obat yang menargetkan tidur atau kecemasan sebagai bagian dari rencana perawatan.\n
                                Meskipun depresi bipolar sering diobati dengan obat antidepresan, mood stabilizer harus dikonsumsi juga—mengambil antidepresan tanpa mood stabilizer dapat memicu episode manik atau siklus cepat pada seseorang dengan gangguan bipolar.\n
                                Karena orang dengan gangguan bipolar lebih cenderung mencari bantuan ketika mereka depresi daripada ketika mereka mengalami mania atau hipomania, penting bagi penyedia layanan kesehatan untuk mengambil riwayat medis yang cermat untuk memastikan bahwa gangguan bipolar tidak salah dianggap sebagai depresi.\n
                                Orang yang memakai obat harus:\n
                                - Berbicara dengan penyedia layanan kesehatan mereka untuk memahami risiko dan manfaat obat tersebut.
                                - Beri tahu penyedia layanan kesehatan mereka tentang semua obat resep, obat bebas, atau suplemen yang mereka konsumsi saat ini.
                                - Laporkan segera setiap kekhawatiran tentang efek samping kepada penyedia layanan kesehatan. Penyedia layanan kesehatan mungkin perlu mengubah dosis atau mencoba obat yang berbeda.
                                - Ingat bahwa obat untuk gangguan bipolar harus dikonsumsi secara konsisten, seperti yang diinstruksikan, bahkan ketika seseorang merasa baik.
                                            
                                #### Psychotherapy
                                Psikoterapi, juga disebut terapi bicara, dapat menjadi bagian efektif dari pengobatan untuk orang dengan gangguan bipolar. Psikoterapi adalah istilah untuk teknik pengobatan yang bertujuan membantu orang mengidentifikasi dan mengubah emosi, pikiran, dan perilaku yang mengganggu. Jenis terapi ini dapat memberikan dukungan, pendidikan, dan bimbingan kepada orang dengan gangguan bipolar dan keluarga mereka.\n
                                Terapi perilaku kognitif (CBT) adalah pengobatan penting untuk depresi, dan CBT yang disesuaikan untuk pengobatan insomnia dapat sangat membantu sebagai bagian dari pengobatan untuk depresi bipolar.\n
                                Perawatan juga dapat mencakup terapi yang lebih baru yang dirancang khusus untuk pengobatan gangguan bipolar, termasuk terapi ritme interpersonal dan sosial (IPSRT) dan terapi berfokus keluarga.
                                            
                                #### Other treatment options
                                Beberapa orang mungkin menemukan perawatan lain bermanfaat dalam mengelola gejala bipolar mereka:
                                - **Electroconvulsive therapy / Terapi elektrokonvulsif (ECT)** adalah prosedur stimulasi otak yang dapat membantu meredakan gejala bipolar yang parah. Penyedia layanan kesehatan mungkin mempertimbangkan ECT ketika penyakit seseorang tidak membaik setelah perawatan lain, atau dalam kasus yang memerlukan respons cepat, seperti pada orang yang memiliki risiko bunuh diri tinggi atau katatonia (keadaan tidak responsif).    
                                - **Repetitive transcranial magnetic stimulation / Stimulasi magnetik transkranial berulang (rTMS)** adalah jenis stimulasi otak yang menggunakan gelombang magnetik untuk meredakan depresi selama serangkaian sesi pengobatan. Meskipun tidak sekuat ECT, rTMS tidak memerlukan anestesi umum dan memiliki risiko rendah terhadap efek negatif pada memori dan pemikiran.
                                - **Light therapy / Terapi cahaya** adalah pengobatan berbasis bukti terbaik untuk gangguan afektif musiman (SAD), dan banyak orang dengan gangguan bipolar mengalami perburukan musiman depresi atau SAD di musim dingin. Terapi cahaya juga dapat digunakan untuk mengobati bentuk perburukan depresi bipolar musiman yang lebih rendah.
                                """)

                        elif condition == "Depresi":
                            st.markdown("""
                            **Depresi** adalah gangguan suasana hati yang ditandai dengan perasaan sedih yang mendalam 
                            dan kehilangan minat terhadap aktivitas yang biasanya dinikmati, menutup diri dari lingkungan sosial. 
                            Gejala lain mungkin termasuk perubahan nafsu makan, masalah tidur, kelelahan, dan perasaan tidak berharga atau bersalah.
                            """)
                            
                            with st.expander("**Rekomendasi untuk Depresi**", expanded=False):
                                st.markdown("""
                                #### Psychotherapies
                                Beberapa jenis psikoterapi (juga disebut terapi bicara atau konseling) dapat membantu orang dengan depresi dengan mengajarkan mereka cara berpikir dan berperilaku baru serta membantu mereka mengubah kebiasaan yang berkontribusi pada depresi. Pendekatan berbasis bukti untuk mengobati depresi termasuk terapi perilaku kognitif (CBT) dan terapi interpersonal (IPT). Pelajari lebih lanjut tentang psikoterapi.\n
                                Pertumbuhan telehealth untuk layanan kesehatan mental, yang menawarkan alternatif untuk terapi tatap muka, telah membuatnya lebih mudah dan lebih nyaman bagi orang untuk mengakses perawatan dalam beberapa kasus. Bagi orang-orang yang mungkin ragu untuk mencari perawatan kesehatan mental di masa lalu, perawatan kesehatan mental virtual mungkin merupakan pilihan yang lebih mudah.

                                #### Medications
                                Antidepresan adalah obat yang biasa digunakan untuk mengobati depresi. Obat-obatan ini bekerja dengan mengubah cara otak memproduksi atau menggunakan bahan kimia tertentu yang terlibat dalam suasana hati atau stres. Anda mungkin perlu mencoba beberapa antidepresan yang berbeda sebelum menemukan yang meningkatkan gejala Anda dan memiliki efek samping yang dapat dikelola. Obat yang telah membantu Anda atau anggota keluarga dekat di masa lalu sering kali akan dipertimbangkan terlebih dahulu.\n
                                Antidepresan membutuhkan waktu biasanya 4 sampai 8 minggu untuk bekerja, dan masalah dengan tidur, nafsu makan, dan konsentrasi seringkali membaik sebelum suasana hati terangkat. Penting untuk memberikan kesempatan kepada obat untuk bekerja sebelum memutuskan apakah itu tepat untuk Anda.\n
                                Pilihan lain untuk depresi resisten pengobatan adalah mengonsumsi antidepresan bersamaan dengan jenis obat lain yang dapat membuatnya lebih efektif, seperti obat antipsikotik atau antikonvulsan. Penelitian lebih lanjut diperlukan untuk mengidentifikasi peran obat-obatan yang lebih baru ini dalam praktik rutin.\n
                                Jika Anda mulai mengonsumsi antidepresan, jangan berhenti mengonsumsinya tanpa berbicara dengan penyedia layanan kesehatan. Terkadang orang yang mengonsumsi antidepresan merasa lebih baik dan berhenti mengonsumsi obat-obatan sendiri, dan gejala depresi mereka kembali. Ketika Anda dan penyedia layanan kesehatan telah memutuskan bahwa sudah waktunya untuk berhenti mengonsumsi obat, biasanya setelah menjalani pengobatan selama 9-12 bulan, penyedia layanan kesehatan akan membantu Anda mengurangi dosis secara perlahan dan aman. Menghentikan obat secara tiba-tiba dapat menyebabkan gejala penarikan.\n
                                Jika Anda sedang mempertimbangkan untuk mengonsumsi antidepresan dan sedang hamil, berencana untuk hamil, atau menyusui, bicaralah dengan penyedia layanan kesehatan tentang risiko kesehatan apa pun bagi Anda atau anak Anda yang belum lahir atau menyusui dan bagaimana menimbang risiko tersebut terhadap manfaat dari pilihan pengobatan yang tersedia.
                        
                                #### Brain stimulation therapies
                                Jika psikoterapi dan obat-obatan tidak mengurangi gejala depresi, terapi stimulasi otak mungkin merupakan pilihan yang dapat dipertimbangkan. Di Indonesia, terapi stimulasi otak seperti Electroconvulsive Therapy (ECT) dan Repetitive Transcranial Magnetic Stimulation (rTMS) tersedia di beberapa rumah sakit besar dan pusat kesehatan mental. Meskipun terapi ini tidak seumum di negara-negara seperti Amerika Serikat, ECT dan rTMS digunakan untuk mengobati depresi berat yang tidak merespons perawatan lain. Terapi lain seperti Vagus Nerve Stimulation (VNS) dan Deep Brain Stimulation (DBS) masih jarang digunakan dan biasanya dianggap sebagai terapi tambahan atau eksperimental.\n
                                Terapi stimulasi otak di Indonesia kurang sering digunakan dibandingkan psikoterapi dan obat-obatan, namun dapat memainkan peran penting dalam mengobati gangguan mental pada orang yang tidak merespons perawatan lain. Terapi ini umumnya digunakan setelah psikoterapi dan obat-obatan dicoba, dan biasanya digunakan bersamaan dengan perawatan tersebut.\n
                                erapi stimulasi otak bekerja dengan mengaktifkan atau menghambat aktivitas otak menggunakan listrik atau medan magnet. Listrik dapat diberikan secara langsung melalui elektroda yang ditanamkan di otak atau secara tidak langsung melalui elektroda yang ditempatkan di kulit kepala. Listrik juga dapat diinduksi dengan menerapkan medan magnet ke kepala.\n
                                Terapi stimulasi otak yang umum digunakan di Indonesia adalah:
                                - Electroconvulsive therapy (ECT)
                                - Repetitive transcranial magnetic stimulation (rTMS)
                                            
                                ECT memiliki sejarah penggunaan yang paling lama di Indonesia dan lebih umum digunakan dibandingkan rTMS, yang merupakan metode yang lebih baru. Terapi stimulasi otak lainnya, seperti VNS dan DBS, jarang digunakan dan sering kali masih dalam tahap penelitian atau dianggap eksperimental untuk beberapa gangguan mental tertentu.\n
                                Meskipun tidak seumum di negara lain, ECT dan rTMS di Indonesia dapat menjadi pilihan untuk mengobati depresi berat yang tidak merespons pengobatan lain, terutama dalam kasus-kasus yang membutuhkan respons cepat, seperti pada pasien dengan gejala katatonia atau yang berisiko tinggi bunuh diri. Konsultasikan dengan penyedia layanan kesehatan untuk memahami manfaat dan risiko sebelum menjalani terapi stimulasi otak.\n

                                """)

                        elif condition == "Eating Disorder":
                            st.markdown("""
                            **Gangguan Makan** adalah kondisi serius yang berkaitan dengan perilaku makan yang berlebihan atau terlalu sedikit, 
                            serta kekhawatiran berlebihan tentang berat badan atau bentuk tubuh. 
                            Contoh gangguan makan termasuk anoreksia nervosa, bulimia nervosa, dan gangguan makan berlebihan.
                            """)
                            
                            with st.expander("**Rekomendasi untuk Eating Disorder**", expanded=False):
                                st.markdown("""
                                #### Psychotherapies
                                Terapi berbasis keluarga, sejenis psikoterapi di mana orang tua dari remaja dengan anoreksia nervosa mengambil tanggung jawab untuk memberi makan anak mereka, tampaknya sangat efektif dalam membantu orang meningkatkan berat badan dan memperbaiki kebiasaan makan dan suasana hati.\n
                                Untuk mengurangi atau menghilangkan perilaku makan berlebihan dan memuntahkan, orang dapat menjalani terapi perilaku kognitif / cognitive behavioral therapy (CBT), yang merupakan jenis psikoterapi lain yang membantu seseorang belajar bagaimana mengidentifikasi pola pikir yang terdistorsi atau tidak membantu dan mengenali serta mengubah keyakinan yang tidak akurat. 

                                #### Medication
                                Bukti juga menunjukkan bahwa obat-obatan seperti antidepresan, antipsikotik, atau mood stabilizer juga dapat membantu mengobati gangguan makan dan penyakit penyerta lainnya seperti kecemasan atau depresi.
                                """)

                        elif condition == "OCD":
                            st.markdown("""
                            **Gangguan Obsesif-Kompulsif (OCD)** adalah gangguan mental yang ditandai dengan pikiran obsesif (gangguan) yang tidak diinginkan dan berulang, 
                            serta perilaku kompulsif (dorongan untuk melakukan sesuatu) yang berulang untuk mengurangi kecemasan yang disebabkan oleh obsesi tersebut.
                            """)
                            
                            with st.expander("**Rekomendasi untuk OCD**", expanded=False):
                                st.markdown("""
                                #### Psychotherapy
                                Psikoterapi dapat menjadi pengobatan yang efektif untuk orang dewasa dan anak-anak dengan OCD. Penelitian menunjukkan bahwa beberapa jenis psikoterapi, termasuk terapi perilaku kognitif dan terapi terkait lainnya, dapat sama efektifnya dengan obat-obatan bagi banyak orang. Bagi yang lain, psikoterapi mungkin paling efektif ketika dikombinasikan dengan obat-obatan.\n
                                - **Terapi perilaku kognitif / Cognitive behavioral therapy (CBT)**: CBT adalah jenis terapi bicara yang membantu orang mengenali cara berpikir yang berbahaya atau tidak benar sehingga mereka dapat melihat dan merespons situasi menantang dengan lebih jelas. CBT membantu orang belajar mempertanyakan pikiran negatif ini, menentukan bagaimana hal itu memengaruhi perasaan dan tindakan mereka, dan mengubah pola perilaku yang merusak diri sendiri. CBT telah dipelajari dengan baik dan dianggap sebagai "standar emas" psikoterapi bagi banyak orang. CBT bekerja paling baik ketika disesuaikan untuk mengobati karakteristik unik dari gangguan mental tertentu, termasuk OCD.
                                - **Terapi pencegahan respons dan paparan / Exposure and response prevention therapy (ERP)**: Penelitian menunjukkan bahwa ERP, jenis CBT tertentu, secara efektif mengurangi perilaku kompulsif, bahkan untuk orang yang tidak merespons dengan baik terhadap obat-obatan. Dengan ERP, orang menghabiskan waktu di lingkungan yang aman yang secara bertahap mengekspos mereka pada situasi yang memicu obsesi mereka (seperti menyentuh benda kotor) dan mencegah mereka melakukan perilaku kompulsif tipikal mereka (seperti mencuci tangan). Meskipun pendekatan ini awalnya dapat menyebabkan kecemasan, menciptakan risiko putus pengobatan secara prematur, kompulsi menurun bagi sebagian besar orang saat mereka melanjutkan pengobatan.
                                Children with OCD may need additional help from family members and health care providers to recognize and manage their OCD symptoms. Mental health professionals can work with young children to identify strategies for managing stress and increasing support so they can control their OCD symptoms.
                                
                                #### Medication
                                Penyedia layanan kesehatan dapat meresepkan obat untuk membantu mengobati OCD. Obat yang paling umum diresepkan untuk OCD adalah antidepresan yang menargetkan serotonin, neurotransmitter di otak yang terlibat dalam depresi dan OCD. Kategori antidepresan terbesar disebut selective serotonin reuptake inhibitors.\n
                                Pengobatan antidepresan dapat memakan waktu 8-12 minggu sebelum gejala mulai membaik, dan pengobatan OCD mungkin memerlukan dosis yang lebih tinggi daripada yang biasanya digunakan untuk mengobati depresi. Bagi sebagian orang, obat-obatan ini dapat menyebabkan efek samping seperti sakit kepala, mual, atau kesulitan tidur. Sebagian besar orang dengan OCD menemukan bahwa obat-obatan, seringkali dikombinasikan dengan psikoterapi, dapat membantu mereka mengelola gejala mereka.\n
                                Penyedia layanan kesehatan Anda dapat menyesuaikan dosis obat dari waktu ke waktu untuk meminimalkan efek samping atau gejala penarikan. Jangan berhenti mengonsumsi obat Anda tanpa terlebih dahulu berbicara dengan penyedia layanan kesehatan Anda. Mereka dapat bekerja sama dengan Anda untuk memantau kesehatan Anda dan menyesuaikan rencana perawatan Anda secara aman dan efektif.

                                """)

                        elif condition == "PTSD":
                            st.markdown("""
                            **Gangguan Stres Pasca-Trauma (PTSD)** adalah kondisi mental yang terjadi setelah seseorang mengalami atau menyaksikan peristiwa traumatis. 
                            Gejala dapat mencakup kilas balik, mimpi buruk, kecemasan yang parah, serta pikiran yang tidak terkendali tentang peristiwa tersebut.
                            """)
                            
                            with st.expander("**Rekomendasi untuk PTSD**", expanded=False):
                                st.markdown("""
                                #### Psychotherapy
                                Psikoterapi (kadang disebut terapi bicara) mencakup berbagai teknik pengobatan yang digunakan oleh para profesional kesehatan mental untuk membantu orang mengidentifikasi dan mengubah emosi, pikiran, dan perilaku yang mengganggu. Psikoterapi dapat memberikan dukungan, pendidikan, dan bimbingan kepada orang dengan PTSD dan keluarga mereka. Perawatan dapat berlangsung satu lawan satu atau dalam kelompok dan biasanya berlangsung 6 hingga 12 minggu tetapi dapat berlangsung lebih lama.\n
                                Beberapa jenis psikoterapi menargetkan gejala PTSD, sementara yang lain berfokus pada masalah sosial, keluarga, atau pekerjaan. Psikoterapi yang efektif seringkali menekankan beberapa komponen utama, termasuk mempelajari keterampilan untuk membantu mengidentifikasi pemicu dan mengelola gejala.\n
                                Salah satu jenis psikoterapi yang umum, disebut terapi perilaku kognitif, dapat mencakup terapi paparan dan restrukturisasi kognitif:
                                - **Exposure therapy**  membantu orang belajar mengelola ketakutan mereka dengan secara bertahap mengekspos mereka, dengan cara yang aman, terhadap trauma yang mereka alami. Sebagai bagian dari terapi paparan, orang dapat memikirkan atau menulis tentang trauma atau mengunjungi tempat kejadiannya. Terapi ini dapat membantu orang dengan PTSD mengurangi gejala yang menyebabkan mereka tertekan.
                                - **Restrukturisasi kognitif** membantu orang memahami peristiwa traumatis. Terkadang orang mengingat peristiwa tersebut berbeda dari kejadian sebenarnya. Mereka mungkin merasa bersalah atau malu tentang sesuatu yang bukan salah mereka. Restrukturisasi kognitif dapat membantu orang dengan PTSD berpikir tentang apa yang terjadi secara realistis.

                                #### Medications
                                Di Indonesia, penggunaan selective serotonin reuptake inhibitors (SSRI), sejenis obat antidepresan, juga menjadi salah satu pilihan pengobatan untuk PTSD (Post-Traumatic Stress Disorder). SSRI dapat membantu mengelola gejala PTSD, seperti perasaan sedih, cemas, marah, dan mati rasa secara emosional. Di Indonesia, penyedia layanan kesehatan, seperti psikiater dan dokter umum yang berpengalaman, dapat meresepkan SSRI dan obat-obatan lain sesuai dengan kondisi pasien, seringkali bersamaan dengan psikoterapi. Beberapa obat lainnya juga digunakan untuk mengatasi gejala spesifik PTSD, seperti masalah tidur dan mimpi buruk. Penting untuk berkonsultasi dengan tenaga kesehatan profesional untuk mendapatkan diagnosis yang tepat dan menentukan pengobatan yang paling sesuai.\n
                                Orang harus bekerja sama dengan penyedia layanan kesehatan mereka untuk menemukan obat atau kombinasi obat terbaik dan dosis yang tepat.
                                """)

                        elif condition == "Skizophrenia":
                            st.markdown("""
                            **Skizofrenia** adalah gangguan mental serius yang mempengaruhi cara seseorang berpikir, merasakan, dan berperilaku. 
                            Orang dengan skizofrenia mungkin tampak seperti kehilangan kontak dengan kenyataan dan dapat mengalami halusinasi, delusi, serta kesulitan dalam berpikir dan konsentrasi.
                            """)
                            
                            with st.expander("**Rekomendasi untuk Skizophrenia**", expanded=False):
                                st.markdown("""
                                #### Antipsychotic medications
                                Obat antipsikotik dapat membantu membuat gejala psikotik kurang intens dan kurang sering. Obat-obatan ini biasanya diminum setiap hari dalam bentuk pil atau cairan. Beberapa obat antipsikotik diberikan sebagai suntikan satu atau dua kali sebulan.\n
                                Jika gejala seseorang tidak membaik dengan obat antipsikotik biasa, mereka mungkin akan diberikan clozapine. Orang yang mengonsumsi clozapine harus menjalani tes darah rutin untuk memeriksa efek samping yang berpotensi berbahaya yang terjadi pada 1-2% pasien.\n
                                Orang merespons obat antipsikotik dengan cara yang berbeda. Penting untuk melaporkan setiap efek samping kepada penyedia layanan kesehatan. Banyak orang yang mengonsumsi obat antipsikotik mengalami efek samping seperti kenaikan berat badan, mulut kering, gelisah, dan kantuk ketika mereka mulai mengonsumsi obat-obatan ini. Beberapa efek samping ini mungkin hilang seiring waktu, sementara yang lain mungkin bertahan.\n
                                
                                #### Psychosocial treatments
                                Perawatan psikososial membantu orang menemukan solusi untuk tantangan sehari-hari dan mengelola gejala saat bersekolah, bekerja, dan menjalin hubungan. Perawatan ini sering digunakan bersama dengan obat antipsikotik. Orang yang berpartisipasi dalam perawatan psikososial rutin cenderung tidak mengalami gejala kambuh atau dirawat di rumah sakit.\n
                                Contoh perawatan semacam ini meliputi jenis psikoterapi seperti terapi perilaku kognitif, pelatihan keterampilan perilaku, pekerjaan dengan dukungan, dan intervensi perbaikan kognitif.

                                #### Education and support
                                Program pendidikan dapat membantu keluarga dan teman mempelajari gejala skizofrenia, pilihan pengobatan, dan strategi untuk membantu orang yang dicintai dengan penyakit ini. Program-program ini dapat membantu teman dan keluarga mengelola kesusahan mereka, meningkatkan keterampilan penanganannya sendiri, dan memperkuat kemampuan mereka untuk memberikan dukungan.

                                #### Coordinated specialty care
                                Program perawatan khusus terkoordinasi / Coordinated specialty care (CSC) adalah program yang berfokus pada pemulihan bagi orang dengan episode psikosis pertama, tahap awal skizofrenia. Penyedia layanan kesehatan dan spesialis bekerja sama sebagai tim untuk menyediakan CSC, yang meliputi psikoterapi, pengobatan, manajemen kasus, dukungan pekerjaan dan pendidikan, serta pendidikan dan dukungan keluarga. Tim perawatan bekerja sama dengan individu untuk membuat keputusan perawatan, melibatkan anggota keluarga sebanyak mungkin.\n
                                Dibandingkan dengan perawatan biasa, CSC lebih efektif dalam mengurangi gejala, meningkatkan kualitas hidup, dan meningkatkan keterlibatan dalam pekerjaan atau sekolah.

                                #### Assertive community treatment
                                Perawatan komunitas asertif / Assertive community treatment (ACT) dirancang khusus untuk orang dengan skizofrenia yang kemungkinan besar akan mengalami beberapa kali rawat inap atau tunawisma. ACT biasanya diberikan oleh tim penyedia layanan kesehatan yang bekerja sama untuk memberikan perawatan kepada pasien di komunitas.

                                #### Treatment for drug and alcohol misuse
                                Orang dengan skizofrenia mungkin juga mengalami masalah dengan narkoba dan alkohol. Program perawatan yang mencakup perawatan untuk skizofrenia dan penyalahgunaan zat penting untuk pemulihan karena penyalahgunaan zat dapat mengganggu pengobatan untuk skizofrenia.

                                """)

                # Display the descriptions
                for description in descriptions:
                    st.markdown(description)

                # Menampilkan pesan peringatan sekali di akhir
                if descriptions:
                    st.warning("**Perlu diingat bahwa sistem ini merupakan alat identifikasi dini dan bukan acuan untuk melakukan diagnosis kesehatan mental. Sebaiknya anda menemui seorang profesional untuk mengetahui lebih lanjut terkait kondisi mental anda.**")

if reset_button:
     reset_radio_buttons()

# Display model accuracy
with col3:
    st.write(f"Model Accuracy: {accuracy * 100:.2f}%")

st.divider()
st.write("_Referensi :_")
st.markdown("[_Denpasar Mental Health Centre_](https://www.denpasarmentalhealthcentre.my.id/about)")
st.markdown("[_National Institute of Mental Health_](https://www.nimh.nih.gov/)")
st.markdown("_DSM-5\u2122 (Diagnostic and Statistical Manual of Mental Health)_")

# st.sidebar.time_input(datetime)

