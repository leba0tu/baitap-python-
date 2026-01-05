'''Số lộc phát
Một số được gọi là số "lộc phát" nếu nó chỉ chứa hai chữ số 6 và 8.
Ví dụ: 68, 86, 668, 886 đều là số "lộc phát", còn 123, 678 thì không.
Yêu cầu: Cho một số tự nhiên N, hãy kiểm tra xem N có phải là số "lộc phát" hay không.
Dữ liệu vào:
- 1 dòng chứa số nguyên dương N ( N <= 10^16)
Dữ liệu ra:
- 1 dòng ghi ra kết quả là YES nếu là số lộc phát, ngược lại là NO
Ví dụ:
Input:
686886
Output:
YES
Input2:
76868684
Output2:
NO
'''
def slp(n):
    for i in str(n):
        if i != '6' and i != '8':
            return False
    return True
k = int(input())
if slp(k):
    print('Y')
else:
    print('N')
