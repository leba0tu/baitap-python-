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
n = int(input())
a = int(input())
b = int(input())
d = 0
for i in range(1, n+1):
    if i % a == 0 or i % b == 0:
        d += 1
print(n-d)