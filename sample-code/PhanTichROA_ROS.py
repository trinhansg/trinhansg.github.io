# Chuong trinh tinh HQ ROA ROS
loinhuan=float(input("Loi nhuan sau thue: "))
Tongtaisan=float(input("Tong Tai san: "))
Doanhthuthuan=float(input("Doanh thu thuan:"))
ROA=loinhuan/Tongtaisan
print("ROA = ", ROA)
if ROA>=0.1:
    print("ROA Hieu qua cao")
if ROA>=0.05 and ROA<0.1:
    print("ROA Hieu qua Trung binh")
if ROA<0.05:
    print("ROA Hieu qua thap")
ROS=loinhuan/Doanhthuthuan
print("ROS = ", ROS)
if ROS>0.05:
    print("ROS Hieu qua cao")
if ROS>=0.02 and ROS<0.05:
    print("ROS Hieu qua Trung binh")
if ROS<0.02:
    print("ROS Hieu qua thap")