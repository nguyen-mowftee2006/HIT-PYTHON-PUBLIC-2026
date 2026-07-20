thang = int(input("- Nhập tháng: "))
nam = int(input("- Nhập năm: "))

if thang in (1, 3, 5, 7, 8, 10, 12):
    ngay = 31
elif thang in (4, 6, 9, 11):
    ngay = 30
elif thang == 2:
    if ((nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)):
        ngay = 29
    else:
        ngay = 28
else:
    print("Tháng không hợp lệ!")

if ngay in (28,29,30,31):
    print(f"---> Tháng {thang} năm {nam} có {ngay} ngày!")