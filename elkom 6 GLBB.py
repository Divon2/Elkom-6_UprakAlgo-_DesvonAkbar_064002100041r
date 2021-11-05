print ('Rumus GLBB') 

#rumusnya adalah vt = v0 + a x t

def hitung_kecepatan_akhir(kecepatan_awal, percepatan, waktu):
    kecepatan_akhir = kecepatan_awal + (percepatan*waktu) 
    print(f'kecepatan awal = {kecepatan_awal} m/s dengan percepatan = {percepatan} m/s^2 ditempuh dalam waktu = {waktu} detik') 
    return kecepatan_akhir 
   
#menghitung kecepatan akhir (rumus pertama) 
print('nomor 1') 
hitung_kecepatan_akhir(5,7,10) 
    
    
    