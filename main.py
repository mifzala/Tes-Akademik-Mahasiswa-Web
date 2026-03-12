import streamlit as st

st.header('Soal Tes Akademik Mahasiswa')

soal_jawaban1 = st.radio('1. Pilih kata yang paling dekat maknanya dengan kata “cepat”:', 
                    ["Lambat",
                     "Kilat",
                     "Berat",
                     "Lama"],
                     index = None
                     )

if soal_jawaban1 == "Lambat":
    st.write("Kamu telah Menjawab Lambat")
if soal_jawaban1 == "Kilat":
    st.write("Kamu telah Menjawab Kilat")
if soal_jawaban1 == "Berat":
    st.write("Kamu telah Menjawab Berat")
if soal_jawaban1 == "Lama":
    st.write("Kamu telah Menjawab Lama")

soal_jawaban2 = st.radio('2. Lawan kata dari "jujur" adalah...',
                         ["Tulus",
                          "Bohong",
                          "Baik",
                          "Ramah"],
                          index = None
                          )

if soal_jawaban2 == "Tulus":
    st.write("Kamu telah Menjawab Tulus")
if soal_jawaban2 == "Bohong":
    st.write("Kamu telah Menjawab Bohong")
if soal_jawaban2 == "Baik":
    st.write("Kamu telah Menjawab Baik")
if soal_jawaban2 == "Ramah":
    st.write("Kamu telah Menjawab Ramah")


soal_jawaban3 = st.radio('3. Guru:Sekolah = Dokter:',
                         ["Rumah",
                          "Rumah Sakit",
                          "Apotek",
                          "Pasar"],
                          index = None
                          )

if soal_jawaban3 == "Rumah":
    st.write("Kamu telah Menjawab Rumah")
if soal_jawaban3 == "Rumah Sakit":
    st.write("Kamu telah Menjawab Rumah Sakit")
if soal_jawaban3 == "Apotek":
    st.write("Kamu telah Menjawab Apotek")
if soal_jawaban3 == "Pasar":
    st.write("Kamu telah Menjawab Pasar")

soal_jawaban4 = st.radio('4. "Semua burung memiliki sayap, Elang adalah burung." Kesimpulan yang benar adalah:',
                         ["Elang tidak memiliki sayap",
                          "Elang memiliki sayap",
                          "Semua hewan adalah burung",
                          "Burung adalah elang"],
                          index = None
                          )

if soal_jawaban4 == "Elang tidak memiliki sayap":
    st.write("Kamu telah Menjawab Elang tidak memiliki sayap")
if soal_jawaban4 == "Elang memiliki sayap":
    st.write("Kamu telah Menjawab Elang memiliki sayap")
if soal_jawaban4 == "Semua hewan adalah burung":
    st.write("Kamu telah Menjawab Semua hewan adalah burung")
if soal_jawaban4 == "Burung adalah elang":
    st.write("Kamu telah Menjawab Burung adalah elang")

soal_jawaban5 = st.radio('5. "Rina membaca buku di perpustakaan." Siapa yang membaca buku?',
                         ["Perpustakaan",
                          "Buku",
                          "Rina",
                          "Teman Rina"],
                          index = None
                          )

if soal_jawaban5 == "Perpustakaan":
    st.write("Kamu telah Menjawab Perpustakaan")
if soal_jawaban5 == "Buku":
    st.write("Kamu telah Menjawab Buku")
if soal_jawaban5 == "Rina":
    st.write("Kamu telah Menjawab Rina")
if soal_jawaban5 == "Teman Rina":
    st.write("Kamu telah Menjawab Teman Rina")

soal_jawaban6 = st.radio('6. Sinonim kata "kontradiktif adalah',
                         ["Sejalan",
                          "Bertentangan",
                          "Seimbang",
                          "Netral"],
                          index = None
                          )

if soal_jawaban6 == "Sejalan":
    st.write("Kamu telah Menjawab Sejalan")
if soal_jawaban6 == "Bertentangan":
    st.write("Kamu telah Menjawab Bertentangan")
if soal_jawaban6 == "Seimbang":
    st.write("Kamu telah Menjawab Seimbang")
if soal_jawaban6 == "Netral":
    st.write("Kamu telah Menjawab Teman Netral")

soal_jawaban7 = st.radio('7. Jika 2x + 5 = 17, maka nilai x adalah',
                         ["4",
                          "5",
                          "6",
                          "7"],
                          index = None
                          )

if soal_jawaban7 == "4":
    st.write("Kamu telah Menjawab 4")
if soal_jawaban7 == "5":
    st.write("Kamu telah Menjawab 5")
if soal_jawaban7 == "6":
    st.write("Kamu telah Menjawab 6 ")
if soal_jawaban7 == "7":
    st.write("Kamu telah Menjawab 7")

soal_jawaban8 = st.radio('8. Peristiwa Sumpah Pemuda terjadi pada tahun...',
                         ["1908",
                          "1928",
                          "1945",
                          "1950"],
                          index = None
                          )

if soal_jawaban8 == "1908":
    st.write("Kamu telah Menjawab 1908")
if soal_jawaban8 == "1928":
    st.write("Kamu telah enjawab 1928")
if soal_jawaban8 == "1945":
    st.write("Kamu telah Menjawab 1945")
if soal_jawaban8 == "1950":
    st.write("Kamu telah Menjawab 1950")

soal_jawaban9 = st.radio('9. Satuan gaya dalam sistem Internasional (SI) adalah... ',
                         ["Joule",
                          "Newton",
                          "Watt",
                          "Pascal"],
                          index = None
                          )

if soal_jawaban9 == "Joule":
    st.write("Kamu telah menjawab Joule")
if soal_jawaban9 == "Newton":
    st.write("Kamu telah Menjawab Newton")
if soal_jawaban9 == "Watt":
    st.write("Kamu telah Menjawab Watt")
if soal_jawaban9 == "Teman Rina":
    st.write("Kamu telah Menjawab Pascal")

soal_jawaban10 = st.radio('10. "Siapa sebenarnya pembuat website ini?',
                         ["Michael Jordan",
                          "Christiano Ronaldo",
                          "Justin Bieber",
                          "Azam"],
                          index = None
                          )

if soal_jawaban10 == "Michael Jordan":
    st.write("Dipikir lagi broo sebelum jawab:unamused:")
if soal_jawaban10 == "Christiano Ronaldo":
    st.write("Ihh masa nda tau sih pembuat website ini:symbols_over_mouth:")
if soal_jawaban10 == "Justin Bieber":
    st.write("Nda taulah nyerah sama orang kek kamu:rage:")
if soal_jawaban10 == "Azam":
    st.write("hehehe yap betul sekali:hugs:")




    # Tombol submit
if st.button("Submit Jawaban"):

    skor = 0

    # Kunci jawaban
    kunci = {
        1: "Kilat",
        2: "Bohong",
        3: "Rumah Sakit",
        4: "Elang memiliki sayap",
        5: "Rina",
        6: "Bertentangan",
        7: "6",
        8: "1928",
        9: "Newton",
        10: "Azam"

    }

    jawaban_user = {
        1: soal_jawaban1,
        2: soal_jawaban2,
        3: soal_jawaban3,
        4: soal_jawaban4,
        5: soal_jawaban5,
        6: soal_jawaban6,
        7: soal_jawaban7,
        8: soal_jawaban8,
        9: soal_jawaban9,
        10: soal_jawaban10
    }

    for nomor in kunci:
        if jawaban_user[nomor] == kunci[nomor]:
            st.success(f"Soal {nomor} Benar")
            skor += 10
        else:
            st.error(f"Soal {nomor} Salah. Jawaban benar: {kunci[nomor]}")

    st.subheader(f"Nilai kamu: {skor}")

