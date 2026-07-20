n = int(input("- Nhập số xu: "))
while n <=0:
    n = int(input("- Nhập lại số xu"))
GIA = 28
DOI = 3
sochai = n // GIA

if sochai > 0:
    vochai = sochai
    while vochai >= DOI:
        sochai += (vochai//DOI)
        vochai -= (vochai//DOI)*DOI

print(f"- Với {n} xu, số chai bia tối đa có thể uống là {sochai}")