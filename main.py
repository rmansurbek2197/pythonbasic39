def eng_uzun_so_z(matsn):
    so_zlar = matsn.split()
    eng_uzun = max(so_zlar, key=len)
    return eng_uzun

so_z = "Men python dasturlash tili haqida biliman"
print(eng_uzun_so_z(so_z))