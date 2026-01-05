''' Số siêu đẹp
Cho 2 chữ số 6 và số 8 được gọi là số đẹp. Những số chỉ gồm chữ số 6 hoặc chỉ gồm chữ số 8 hoặc gồm cả 2 loại chữ số trên nhưng lưu ý số 6 luôn đứng trước chữ số 8 thì đều được coi là số siêu đẹp.
Ví dụ: 6, 888, 668, 6688 là các số đẹp. Số 9 không phải số đẹp, số 86 không phải số đẹp vì số 8 đứng trước số 6.
Yêu cầu: Cho một số tự nhiên N, viết chương trình kiểm tra xem số N đó có phải số siêu đẹp hay không.
Dữ liệu vào:
- 1 dòng chứa số nguyên dương N ( N <= 10^16)
Dữ liệu ra:
- 1 dòng ghi kết quả in ra nếu số N nhập vào không phải số đẹp thì trả ra là NO, ngược lại trả kết quả là YES.
Ví dụ:
Input
168
Output
NO
Input2
668
Output2
YES
'''
def sodep(n):
    so8 = False
    for i in str(n):
        if i not in ('6', '8'):
            return False
        if i == '8':
            so8 = True
        if i == '6' and so8:
            return False
    return True
n = int(input())
if not sodep(n):
    print('N')
else:
    print('Y')