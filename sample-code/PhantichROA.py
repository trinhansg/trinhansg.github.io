# Chuong trinh tinh HQ ROA
lairong=float(input("Lai rong: "))
Taisan=float(input("Tong Tai san: "))
TysoROA=lairong/Taisan
if TysoROA>0.1:
    print("Hieu qua cao")
if TysoROA>=0.05 and TysoROA<0.1:
    print("Hieu qua Trung binh")
if TysoROA<0.05:
    print("Hieu qua thap")