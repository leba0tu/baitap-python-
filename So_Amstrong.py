''' Số Amstrong
Số tự nhiên N có k chữ số được gọi là Amstrong nếu N bằng tổng các luỹ thừa bậc k của các chữ số của nó.
Ví dụ: số 153 có 3 chữ số là số Amstrong vì 1^3 +  5^3 + 3^3 = 1x1x1 + 5x5x5 + 3x3x3 = 153
Yêu cầu: Viết chương trình nhập số k, in ra các số Amstrong có k chữ số.
Dữ liệu:
- Một dòng duy nhất chứa số nguyên dương k (1 <= k <= 5).
Kết quả:
- In ra các số Amstrong có k chữ số cách nhau bởi một dấu cách. Nếu không tồn tại số Amstrong có k chữ số, in ra -1.
Ví dụ:
Dữ liệu:
2
Kết quả:
-1
Dữ liệu 2:
3
Kết quả:
153 137 371 407
'''
k = int(input())
l = 10**(k-1)
r = 10**k
ds = [] 
for i in range(l, r):
    s = 0
    for j in str(i):
        s += int(j)**k
    if s == i:
        ds.append(str(i))
if ds:
    print(' '.join(ds))
else:
    print(-1)