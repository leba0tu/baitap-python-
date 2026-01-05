''' Cho một chuỗi kí tự S có độ dài không quá 10^16 đơn vị và chỉ chứa kí tự A duy nhất và không chứa kí tự nào khác.
Yêu cầu: Viết chương trình đếm số lượng chuỗi đối xứng con (có độ dài từ 2 trở lên) có trong chuỗi S đó.
Dữ liệu vào: Một dòng chứa chuỗi kí tự S gồm ít nhất 1 và nhiều nhất 52 kí tự đều là các chữ cái viết hoa.
Dữ liệu ra: Số lượng chuỗi đối xứng con có trong chuỗi kí tự S.
Input:
AAA
Output:
3
Giải thích:
Có 3 chuỗi đối xứng con: "AA" (từ vị trí 0-1), "AAA" (từ vị trí 0-2), và "AA" (từ vị trí 1-2)
'''
s = input()
dem = s.count('A')
if dem != len(s):
    print('Không hợp lệ')
else:
    if len(s) <= 10**16:
        kq = len(s)*(len(s)-1)//2
    print(kq)