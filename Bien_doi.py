''' Biến đổi
Từ một số nguyên dương K, ta thực hiện biến đổi số K theo quy tắc biến đổi sau đây:
Nếu K chia hết cho 6 thì thay số K bởi thương K chia cho 6, nếu K không chia hết cho 6 thì thay số K bởi tích 3 x K.
Yêu cầu: Hãy xác định số lần biến đổi theo quy tắc trên để K bằng 1.
Dữ liệu:
- Một dòng duy nhất chứa số nguyên dương K (1 <= K <= 10^9).
Kết quả:
- In ra số nguyên dương m là số lần biến đổi để số K bằng 1.
Trong trường hợp không thể biến đổi K bằng 1 theo quy tắc biến đổi trên thì in ra -1.
Ví dụ:
Input:
12
Output:
3
Giải thích:
Lần 1: Biến đổi K = 12 : 6 = 2
Lần 2: Biến đổi K = 2 x 3 = 6
Lần 3: Biến đổi K = 6 : 6 =1
Input2:
10
Output2:
-1
'''
dem = 0
k = int(input())
while k != 1:
    if k % 6 == 0:
        k //= 6
        dem += 1
    else:
        k *= 3
        dem += 1
        # Nếu K trở nên quá lớn (ví dụ > 10^12), có thể không thành 1
        if k > 10**12:
            dem = -1
            break
if k == 1:
    print(dem)
else:
    print(-1)