# 📘 GHI NHỚ GITHUB + VS CODE (SỔ TAY CÁ NHÂN)

> Dùng cho: **đổi máy – quên thao tác – cần làm lại từ đầu**
>
> Nguyên tắc sống còn: **Chưa commit = chưa xong việc**

---

## I. CÀI ĐẶT BAN ĐẦU (LÀM 1 LẦN DUY NHẤT)

### 1. Cài Git trên macOS
```bash
git --version
```
- Có version → OK
- Chưa có → cài:
```bash
xcode-select --install
```

📌 Không có Git → GitHub không làm việc.

---

### 2. VS Code
- Cài xong là dùng
- Không cần cấu hình phức tạp

---

### 3. Tài khoản GitHub
- Dùng để lưu repo
- Copilot Pro **không liên quan dung lượng**

---

## II. PHẦN I — QUY TRÌNH GITHUB TỪ A → Z

### Bước 1: Tạo repo trên GitHub Web
- New repository
- Tên repo (vd: `baitap-python`)
- ✅ Tick **Add README**
- ❌ Không cần `.gitignore`
- ❌ Không cần License

---

### Bước 2: Clone repo về máy (VS Code)
```text
Cmd + Shift + P → Git: Clone → dán link HTTPS → Open
```
📌 Dùng **HTTPS**, không cần SSH.

---

### Bước 3: Làm việc trong repo
- Tạo / chép file vào thư mục repo
- Ví dụ:
```text
bai1.py
bai2.py
```

---

### Bước 4: Chạy Python trên Mac
```bash
python3 ten_file.py
```
⚠️ macOS dùng `python3`, **không dùng `python`**

---

### Bước 5: Commit & Push (QUAN TRỌNG NHẤT)

Quy trình chuẩn:
1. Source Control (biểu tượng nhánh cây)
2. Dấu **+** (Stage file)
3. Commit message rõ ràng
4. **Commit**
5. **Sync / Push**

📌 GitHub **chỉ nhận bài khi đã commit + push**.

---

### Bước 6: Thiết lập danh tính Git (chỉ lần đầu)
```bash
git config --global user.name "Bao Tu"
git config --global user.email "emailcuaban@example.com"
```

---

## III. QUY TRÌNH LÀM VIỆC HẰNG NGÀY (NHỚ 5 BƯỚC)

```text
Sửa / thêm file
→ Lưu
→ Stage
→ Commit
→ Push
```

---

## IV. NHỮNG VIỆC THƯỜNG GẶP

### 1. Sửa file đã commit
👉 Cứ sửa → commit lại → push

### 2. Đổi tên file
👉 Được, Git xử lý được
- Nên dùng: **không dấu, không khoảng trắng**

### 3. Xoá file
👉 Xoá → commit → push → file mất trên GitHub

### 4. Kéo thả file vào repo
👉 Được, **nhưng phải commit + push**

---

## V. COPILOT & AGENT (NHỚ ĐÚNG VAI)

- Copilot: gợi ý, trợ giảng
- Agent: làm theo nhiệm vụ lớn (soạn bài, sinh bài tập)

📌 Không bắt buộc dùng khi chỉ đang đưa bài cũ lên GitHub.

---

## VI. GITHUB LÀ GÌ ĐỐI VỚI MÌNH?

- Kho bài tập
- Sổ tay nghề
- Giáo án số
- Trí nhớ ngoài

Copilot hết hạn ❌ **không ảnh hưởng dữ liệu**

---

## VII. CÂU NHẮC NHỚ CUỐI CÙNG

> **Chưa commit = chưa xong việc.**
>
> Commit rồi = yên tâm tắt máy.

---

✍️ Ghi chú thêm của riêng mình:

-
-
-

