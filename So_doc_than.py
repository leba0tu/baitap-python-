'''Đề bài
Cho số nguyên dương n và dãy n số nguyên dương a₁, a₂, ..., aₙ.
Ta gọi một số aᵢ là độc thân nếu aᵢ ≠ aⱼ, ∀j ≠ i (tức là giá trị aᵢ chỉ xuất hiện đúng một lần trong dãy).
Yêu cầu: Viết chương trình Hãy số lượng số độc thân trong dãy số trên.
Dữ liệu vào:
- Dòng đầu ghi số nguyên dương n.
- Dòng thứ hai chứa n số nguyên dương a₁, a₂, ..., aₙ. Hai số liên tiếp được ghi cách nhau một dấu cách.
    Giới hạn:
    + 80% số điểm có n ≤ 10³ và 1 ≤ aᵢ ≤ 10⁶;
    + 20% số điểm có 10³ < n ≤ 10⁶ và 1 ≤ aᵢ ≤ 10⁹.
Dữ liệu ra:
- Một dòng duy nhất ghi số nguyên là số lượng số độc thân tìm được.
Ví dụ
Input:
5
1 2 2 3 1
Output:
1
Giải thích:
Trong dãy 1 2 2 3 1, chỉ có số 3 xuất hiện đúng một lần nên là số độc thân. Kết quả là 1.
'''
# Nhập dữ liệu
n = int(input())
ds = list(map(int, input().split()))

# Đếm số độc thân
sdt = 0
for i in range(n):
    dem = 0
    for j in range(n):
        if i != j and ds[i] == ds[j]:
            dem = dem + 1    
    if dem == 0:
        sdt += 1
print(sdt)
