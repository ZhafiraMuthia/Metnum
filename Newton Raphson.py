# Mendefinisikan fungsi matematika f(x) = x^2 - 2x - 8
def f(x):
    return x**2 - 2*x - 8

# Mendefinisikan turunan dari f(x) = 2x - 2
def g(x):
    return 2*x - 2

# Metode Newton-Raphson untuk mencari akar f(x)
def newtonRaphson(x0, e, N):
    step = 1  # Inisialisasi langkah awal
    flag = 1  # Penanda jika metode konvergen
    condition = True  # Kondisi iterasi dimulai

    while condition:
        if g(x0) == 0.0:
            print('Terjadi pembagian oleh 0.')
            break

        # Iterasi Newton-Raphson
        x1 = x0 - f(x0) / g(x0)
        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step += 1

        # Berhenti jika langkah melebihi N atau error sudah mencukupi
        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    # Hasil akhir
    if flag == 1:
        print('\nAkar yang ditemukan: %0.8f' % x1)
    else:
        print('\nMetode tidak konvergen')

# Input dari pengguna
x0 = input('Perkiraan awal: ')
x0 = float(x0)
e = input('Toleransi error: ')
e = float(e)
N = input('Jumlah maksimum langkah: ')
N = int(N)

# Menjalankan metode Newton-Raphson
newtonRaphson(x0, e, N)