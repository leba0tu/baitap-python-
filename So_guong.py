'''Số gương
Đề bài: Một số được gọi là số "gánh" nếu nó có dạng ABBA, trong đó A và B là các chữ số từ 0 đến 9.
Ví dụ: 1001, 2552, 9119 là các số "gánh", còn 1234, 5678 thì không.
Yêu cầu: Cho một số tự nhiên có 4 chữ số, viết chương trình kiểm tra xem số đó có phải là số "gương" hay không.
Dữ liệu vào:
- 1 dòng duy nhất chưa số tự nhiên có 4 chữ số
Dữ liệu ra:
- 1 dòng là kết quả ghi ra YES nếu là số gương, ngược lại là NO.
Ví dụ:
Input:
1221
Output:
YES
Input2:
1212
Output2:
NO
'''
so = input().strip()
if len(so) == 4 and so[0] == so[3] and so[1] == so[2]:
    print("YES")
else:
    print("NO")
