'''Cho một danh sách gồm n phần tử.
Yêu cầu: Viết chương trình in ra những phần tử có tổng các chữ số cho đến khi chỉ còn 1 chữ số duy nhất có kết quả là 9 và xác định được phần tử ở vị trí đó.
Dữ liệu vào:
- 1 dòng chứa số nguyên dương n
- 1 dòng chứa dãy nhập số danh sách phụ thuộc số lượng n.
Kết quả::
- 1 dòng chứa dãy số danh sách có các phần tử có tổng chỉ còn 1 chữ số duy nhất là 9.
- 1 dòng là vị trí phần tử của danh sách chứa kết quả tổng chỉ còn 1 chữ số duy nhất là 9
Ví dụ:
Input:
5
234 45 12 9 52
Output:
234 45 9
1 2 4
'''
def t1s(k):
    while k >= 10:
        t = 0
        while k > 0:
            t += k % 10
            k = k // 10
        k = t
    return k
n = int(input())
ds = list(map(int,input().split()))
dst = []
dsvt = []
vt = 0
if len(ds) == n:
    for i in ds:
        vt += 1
        if t1s(i) == 9:
            dst.append(i)
            dsvt.append(vt)
    print(*dst)
    print(*dsvt)
else:
    print('')