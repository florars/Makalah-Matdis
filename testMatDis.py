import string
from itertools import product
from time import time


def bruteloop(password, generator):
    for c in generator:
        if ''.join(c) == password:
            print('\nKata sandi:', ''.join(c))
            return ''.join(c)
    return False


# program melakukan bruteforce sederhana dengan maksimum panjang kata sandi 12 karakter
def mainloop(password,starttime):
    chars=string.printable[:-5]
    for i in range(1,13):
        print("\nMencoba kata sandi dengan panjang",i,"karakter...")
        lap=time()
        print('Waktu: %.2f detik' % (lap - starttime))
        generator=product(chars,repeat=i)
        test=bruteloop(password,generator)
        if (test!=False):
            return test

# MAIN
p=input("Masukkan kata sandi yang akan di brute force ")
start = time()
mainloop(p,start) 
end = time()
print('Waktu yang diperlukan: %.2f detik' % (end - start))
