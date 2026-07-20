# n là số âm --> đếm chữ số và tính tổng chữ số thông qua abs

n = int(input("- Nhập số nguyên n = "))
tongchuso = 0
dem = 0
n_abs = abs(n)
check = True

if (n == 0): 
    tongchuso = 0
    dem = 1
else:
    while n_abs > 0:
        tongchuso += n_abs % 10
        dem += 1
        n_abs //= 10

if n <= 1:
    check = False
else:
    i = 2
    while i < n:
        if n % i == 0:
            check = False
            break
        i += 1

print(f"- Tổng chữ số của n là {tongchuso}")
print(f"- Số chữ số của n là {dem}")
if check == False:
    print(f"- Số n = {n} không phải số nguyên tố!")
else:
    print(f"- So n = {n} là số nguyên tố!")

