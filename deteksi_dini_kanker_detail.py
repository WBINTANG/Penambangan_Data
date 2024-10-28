import pandas as pd

# Data untuk dataset deteksi dini kanker yang lebih detail
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Jenis_Kanker": [
        "Kanker Payudara", "Kanker Prostat", "Kanker Paru-Paru", 
        "Kanker Serviks", "Kanker Kulit", "Kanker Usus Besar", 
        "Kanker Lambung", "Kanker Ovarium", "Kanker Pankreas", "Kanker Testis"
    ],
    "Metode_Deteksi": [
        "Mammogram", "Tes PSA", "CT Scan", "Pap Smear", 
        "Pemeriksaan Kulit", "Kolonoskopi", "Endoskopi", 
        "Ultrasonografi", "MRI", "Pemeriksaan Fisik"
    ],
    "Tujuan_Deteksi": [
        "Mengidentifikasi kanker payudara sejak dini",
        "Mendeteksi kanker prostat pada pria lanjut usia",
        "Mendeteksi perubahan di paru-paru untuk risiko kanker",
        "Mengidentifikasi perubahan sel pada serviks",
        "Mengetahui adanya pertumbuhan abnormal di kulit",
        "Menemukan polip atau tumor di usus besar",
        "Menemukan tanda kanker di lambung atau saluran pencernaan",
        "Mengetahui adanya tumor pada ovarium",
        "Deteksi awal untuk meningkatkan kesembuhan",
        "Deteksi dini kanker pada testis untuk pemuda"
    ],
    "Populasi_Disarankan": [
        "Wanita usia 40 tahun ke atas", "Pria usia 50 tahun ke atas",
        "Perokok dan mantan perokok", "Wanita usia 21-65 tahun",
        "Individu dengan risiko tinggi paparan sinar UV",
        "Individu usia 50 tahun ke atas", "Individu dengan gejala pencernaan",
        "Wanita dengan risiko keturunan", "Individu dengan riwayat keluarga kanker",
        "Pria usia 20-35 tahun"
    ]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan dataset
print("Dataset Deteksi Dini Kanker yang Lebih Detail:")
print(df)

# Menyimpan dataset ke dalam file CSV
df.to_csv("deteksi_dini_kanker_detail.csv", index=False)
