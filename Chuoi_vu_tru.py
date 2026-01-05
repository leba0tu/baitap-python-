'''
Bài 3. Tín hiệu vũ trụ
An nhận được một dãy các kí tự từ tín hiệu của vũ trụ và nhiệm vụ của An là phải đếm xem trong dãy kí tự đó có bao nhiêu số có ba chữ số được tạo bởi 3 ký tự liên tiếp (đọc từ trái sang phải) có tổng các chữ số của nó bằng 16.
Nếu thực hiện đúng An sẽ được thưởng một chuyến du hành thời gian trong vòng 16 ngày, quả là tuyệt vời. Em hãy giúp An đếm xem nhé.
Yêu cầu: Hãy in ra số lượng số có ba chữ số liên tiếp có tổng bằng 16.
Dữ liệu vào: Một dòng duy nhất, chứa một chuỗi n (n ≤ 255).
Dữ liệu ra: In ra kết quả cần tìm.
Ví dụ:
Input
Andemh36739877816915
Output
5
Giải thích
Các số thỏa mãn: 367, 673, 781, 169, 691. Vậy có 5 số.
'''
s = input() # nhập chuỗi
d = 0 # gọi biến đếm d
if len(s) <= 255: # đặt điều kiện thỏa đề bài n <= 255 nói cách khác là độ dài chuỗi nhỏ hoặc bằng 255
    for i in range(len(s)-2): # duyệt biến i qua từng kí tự của độ dài chuỗi - 2 vì mình lấy 3 kí tự phải trừ lùi, nếu 1 thì len(s), nếu 2 thì len(s) - 1
        kt3 = s[i:i+3] # đây là cách lấy từ 1 đến 3 kí tự liên tiếp tính từ chỗ biến i
        if kt3.isdigit(): # kiểm tra nhóm 3 kí tự lấy trên phải là số thì mới thực hiện lệnh bên dưới
            t = int(kt3[0]) + int(kt3[1]) + int(kt3[2]) # đây là tổng 3 kí tự trong nhóm 3 kí tự trên, phải đổi về số nguyên int mới thực hiện tính tổng giá trị con số 
            if t == 16: # đặt điều kiện tổng thỏa đề bài là tổng 3 số phải bằng 16 thì đếm là 1 đơn vị
                d += 1 
    print(d)
