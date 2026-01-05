'''Đếm kí tự
Xâu là một dãy các kí tự liên tiếp bao gồm các kí tự chữ cái, kí tự số, kí tự đặc biệt và có thể dấu cách.
Ví dụ: abc1@gmail.com, Da Nang,...
Yêu cầu: Với một xâu bất kỳ, hãy đưa ra các kí tự chữ cái tiếng Anh (không phân biệt chữ hoa hay thường) có mặt trong xâu và số lần xuất hiện của nó.
Ví dụ: Xâu kí tự "Tran Thi Ngoc Nga" có kí tự "a" xuất hiện 2 lần, tương tự thì c(1), g(2)...
Dữ liệu vào: Xâu S có N kí tự thể hiện trên một dòng (0 < N < 2.10^7).
Dữ liệu ra: Gồm 1 dòng chứa kí tự ch là kí tự có mặt trong xâu S và một số nguyên dương k là số lần xuất hiện của ch trong S.
Các kí tự ch được thể hiện theo thứ tự tăng dần và là các chữ cái viết thường.
Ví dụ:
Input: Tran Thi Ngoc Nga
Output:
a2
c1
g2
h1
i1
n3
o1
r1
t2'''
s = input()
s = s.lower() # lower() là hàm chuyển chữ cái thường
print(s)
ds = [] # Đây là danh sách các chữ cái chứa kết quả
kt = [] # Đây là danh sách chứa các kí tự đã kiểm tra
# Lưu ý: nếu chỉ dùng 1 kí tự duy nhất thì chỉ cần for i in s (OK)
# Nhưng nếu, lấy 2 kí tự trong một xâu S (hoặc danh sách) thì phải dùng for i, for j, thì phải dùng range(len(s)) (OK)
for i in range(len(s)):
    # Đề yêu cầu chỉ đếm số lượng chữ cái trong cái chuỗi S đó, thì giới hạn về chữ cái a-z
    if 'a' <= s[i] <= 'z' and s[i] not in kt: # s[i] là kí tự giới hạn từ a đến z mà không lệ thuộc kí tự nào khác (@,!,345486..), và kiểm tra chưa có trong danh sách thì chạy lệnh
        dem = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                dem += 1
        ds.append(s[i] + str(dem)) # đưa vào danh sách kết hợp của 1 kí tự và 1 biến đếm (thì đếm bắt buộc phải chuyển về chuỗi để kết hợp chữ cái)
        kt.append(s[i]) # đưa kí tự vào danh sách kiểm tra nghĩa là kí tự đó đã được kiểm tra và không còn kí tự giống nhau nữa.
print(ds) # In danh sách kết quả
sapxep = sorted(ds) # Sắp xếp lại danh sách theo thứ tự tăng dần (dùng hàm sorted)
print(sapxep) # In danh sách đã sắp xếp tăng dần
for i in sapxep: # Duyệt i qua từng phần tử của danh sách để in
    print(i) # In mỗi dòng mỗi kí tự theo danh sách
