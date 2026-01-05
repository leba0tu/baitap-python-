'''Dãy số

Cho dãy số sau: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, ...
Tìm số ở vị trí thứ n của dãy.
Yêu cầu: Cho số tự nhiên n, in ra số thứ n của dãy số trên.
Dữ liệu vào: Một dòng chứa số tự nhiên n (1 ≤ n ≤ 10¹⁸).
Dữ liệu ra: Một số tự nhiên duy nhất là số ở vị trí n của dãy số.
Ví dụ:
Input
14
Output
55
Giải thích
Số thứ 14 trong dãy là số 55
Ràng buộc:
Có 60% số điểm của bài toán với 1 ≤ n ≤ 10³.
Có 40% số điểm của bài toán với 1 ≤ n ≤ 10⁵.
'''
# Nhập vị trí n từ người dùng
n = int(input())

# Xử lý trường hợp đơn giản: n từ 1 đến 9
if n <= 9:
    print(n)
else:
    # Xác định nhóm chứa số thứ n
    n_con_lai = n - 9  # Trừ đi 9 số của nhóm 1 chữ số
    so_chu_so = 2  # Bắt đầu từ nhóm 2 chữ số
    
    # Tìm nhóm chứa số thứ n
    while n_con_lai > 9:
        n_con_lai -= 9  # Mỗi nhóm có 9 số
        so_chu_so += 1
    
    # Xác định chữ số lặp lại (từ 1 đến 9)
    chu_so = n_con_lai
    
    # Tạo số kết quả bằng cách lặp lại chữ số
    ketqua = int(str(chu_so) * so_chu_so)
    
    # In kết quả
    print(ketqua)
