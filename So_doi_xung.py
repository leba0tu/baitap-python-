'''Cho danh sách gồm n phần tử
Yêu cầu: Viết chương trình in ra các số đối xứng có trong danh sách trên.
Ví dụ:
Input:
N = 6
121 5 898 74 61 5665
Output:
121 898 5665'''
def sdx(n):
    n = str(n)
    sn = n[::-1]
    if n == sn:
        return True
    else:
        return False
n = int(input())
ds = list(map(int,input().split()))
kq = []
if len(ds) == n:
    for i in ds:
        if sdx(i):
            kq.append(i)
    print(*kq)
else:
    print('')