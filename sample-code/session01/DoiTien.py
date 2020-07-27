# chuong trinh nay co 3 bien 
SotienUSD=float(input("Nhap so USD can doi:"))
TyGiaUsd2Vnd=float(input("Ty gia USD ra VND:"))
SotienVND=SotienUSD*TyGiaUsd2Vnd
print("So tien VND tuong duong la=",SotienVND)
if SotienVND>50000000:
    print("Nhieu tien qua")
else:
    print("Vua du xai")