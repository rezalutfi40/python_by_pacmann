def bunga_terendah(saldo, bunga): 
    hari = 30
    tahun = 365
    tabungan = saldo * (((bunga*0.01)*hari)/tahun)
    return round(tabungan, 2)

def bunga_anuitas(pinjaman, bunga): 
    hari = 30
    tabungan = pinjaman * bunga * hari
    return tabungan