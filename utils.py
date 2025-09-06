# =========================
# utils.py
# Modul konversi suhu
# =========================

def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    satuan_valid = ['c', 'f', 'k']
    if dari not in satuan_valid or ke not in satuan_valid:
        return "Error: Satuan tidak valid. Harap gunakan 'c', 'f', atau 'k'."

    if dari == 'k' and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."

    if dari == 'f':
        suhu_celsius = (nilai - 32) * 5/9
    elif dari == 'k':
        suhu_celsius = nilai - 273.15
    else: 
        suhu_celsius = nilai

    if ke == 'f':
        hasil_akhir = (suhu_celsius * 9/5) + 32
    elif ke == 'k':
        hasil_akhir = suhu_celsius + 273.15
    else:
        hasil_akhir = suhu_celsius

    return hasil_akhir