''' Tô màu bóng
Ban tổ chức (BTC) THT có N quả bóng xếp thành một hàng từ trái sang phải đánh số từ 1 đến N để cho các bạn học sinh chơi trò chơi.
    + Đầu tiên, BTC tô màu đỏ lên những quả bóng có số thứ tự chia hết cho a;
    + Sau đó, BTC tô màu xanh lên những quả bóng có số thứ tự chia hết cho b;
    + Cuối cùng, BTC tô các quả bóng còn lại bằng màu vàng.
Yêu cầu: Em hãy tính số lượng quả bóng được tô màu vàng?
Input:
- Gồm ba số tự nhiên N,a,b (a,b≤N). Mỗi số trên một dòng.
Output
- Một số tự nhiên duy nhất là kết quả của bài toán.
Scoring
+ Có 50% số test ứng với 50% số điểm: N≤100;
+ 50% số test còn lại ứng với 50% số điểm: 100<N≤10^8; b = a+1
Ví dụ:
Input:
10
2
5
Output:
4
'''
# Nhập dữ liệu
# Hàm tìm ước chung lớn nhất (gcd)
def gcd(a, b):
    # Duyệt từ số nhỏ nhất giữa a và b xuống 1
    for i in range(min(a, b), 0, -1):
        # Nếu cả a và b đều chia hết cho i, thì i là gcd
        if a % i == 0 and b % i == 0:
            return i
    return 1  # Nếu không tìm thấy, trả về 1 (trường hợp a hoặc b là 0)

# Nhập dữ liệu từ người dùng
N = int(input("Nhập N: "))
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

# Tính gcd của a và b
gcd_ab = gcd(a, b)

# Tính lcm của a và b: lcm = (a * b) // gcd
if a == 0 or b == 0:
    lcm_ab = 0  # Nếu a hoặc b là 0, lcm là 0
else:
    lcm_ab = (a * b) // gcd_ab

# Tính số lượng số chia hết cho a
count_a = N // a if a != 0 else 0

# Tính số lượng số chia hết cho b
count_b = N // b if b != 0 else 0

# Tính số lượng số chia hết cho lcm(a, b)
count_lcm = N // lcm_ab if lcm_ab != 0 else 0

# Tính số lượng số chia hết cho a hoặc b
count_a_or_b = count_a + count_b - count_lcm

# Tính số lượng số không chia hết cho cả a và b
result = N - count_a_or_b

# In kết quả
print("Số lượng số không chia hết cho cả a và b là:", result)
