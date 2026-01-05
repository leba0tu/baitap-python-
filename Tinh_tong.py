'''Tính tổng
Cho hai số tự nhiên A và B. Hãy tính tổng các số tự nhiên X thỏa mãn tất cả bốn điều kiện sau:
    + X lớn hơn A;
    + X nhỏ hơn B;
    + X chia hết cho 2;
    + X không chia hết cho 3.
Dữ liệu: Nhập vào hai số tự nhiên A và B (1≤A≤B≤10^9). Mỗi số được ghi trên một dòng.
Kết quả: Ghi ra tổng các số X thỏa mãn điều kiện đề bài.
Ví dụ:
Dữ liệu:
4
8
Kết quả:
0
Giải thích:
Không có số nào thỏa mãn nên in ra tổng là 0.
Dữ liệu 2:
1
10
Kết quả 2:
14
Giải thích 2:
Các số 2,3,4,5,6,7,8,9 thì có số 2,4,8 là các số chia hết cho 2 mà lại không chia hết cho 3.
Vậy cần đưa ra đáp án là tổng của 3 số 2,4,6 là 10.
'''
A = int(input())
B = int(input())
tong = 0
# Duyệt qua tất cả các số từ A+1 đến B-1
for X in range(A + 1, B):
    if X % 2 == 0 and X % 3 != 0:
        tong += X
print(tong)
