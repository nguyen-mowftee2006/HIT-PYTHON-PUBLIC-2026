# Bài 1: 

**Python là ngôn ngữ "thông dịch" (interpreted language).**

**Vì:**

- Mã nguồn Python không được dịch thẳng ra mã máy để CPU chạy trực tiếp, mà được "trình thông dịch" (Interpreter - CPython) đọc và thực thi "từng dòng lệnh một" ngay tại thời điểm chạy.
- Không cần một bước biên dịch riêng để tạo ra file thực thi (.exe) như ở C/C++, người dùng chỉ cần gõ "python file.py" là chương trình chạy ngay.
- Lỗi cú pháp hay lỗi logic sẽ được phát hiện "ngay tại dòng đang thực thi", chứ không kiểm tra toàn bộ chương trình trước như ngôn ngữ biên dịch.
- Vì phải dịch "song song" trong lúc chạy nên tốc độ thực thi thường "chậm hơn" so với ngôn ngữ biên dịch.
- Đổi lại, Python "dễ viết, dễ sửa lỗi" (debug), và có thể chạy trên nhiều hệ điều hành khác nhau (Windows, Linux, macOS) mà không cần biên dịch lại mã nguồn

# Bài 2: 

## Các kiểu dữ liệu trong Python

- "int" – kiểu số nguyên, không giới hạn độ lớn (ví dụ: "5", "-100")
- "float" – kiểu số thực (dấu phẩy động), dùng cho số có phần thập phân (ví dụ: "3.14")
- "complex" – kiểu số phức, gồm phần thực và phần ảo (ví dụ: "2 + 3j")
- "str" – kiểu chuỗi ký tự, dùng để lưu văn bản (ví dụ: "Hello")
- "bool" – kiểu luận lý, chỉ có 2 giá trị "True" hoặc "False"
- "list" – danh sách, tập hợp các phần tử "có thứ tự" và "có thể thay đổi" (thêm/xóa/sửa)
- "tuple" – tương tự list nhưng "không thể thay đổi" sau khi tạo
- "set" – tập hợp các phần tử "không trùng lặp", không có thứ tự cố định
- "dict" – từ điển, lưu dữ liệu theo cặp "key–value" (khóa–giá trị)
- "NoneType" – kiểu đặc biệt chỉ có một giá trị duy nhất là "None", dùng để biểu diễn "không có gì"

## Các toán tử trong Python

- "Toán tử số học": "+" (cộng), "-" (trừ), "*" (nhân), "/" (chia lấy số thực), "//" (chia lấy phần nguyên), "%" (chia lấy dư), "**" (lũy thừa)
- "Toán tử so sánh": "==" (bằng), "!=" (khác), ">", "<", ">=", "<=" — dùng để so sánh 2 giá trị, kết quả trả về là "True" hoặc "False"
- "Toán tử gán": "=" (gán giá trị), và các dạng rút gọn như "+=", "-=", "*=", "/=" (vừa tính toán vừa gán lại)
- "Toán tử logic": "and" (và), "or" (hoặc), "not" (phủ định) — dùng để kết hợp nhiều điều kiện
- "Toán tử định danh": "is", "is not" — kiểm tra 2 biến có cùng trỏ đến "một vùng nhớ" hay không (khác với so sánh giá trị "==")
- "Toán tử thành viên": "in", "not in" — kiểm tra một phần tử có nằm trong list/tuple/string/dict hay không
- "Toán tử bitwise": "&", "|", "^", "~", "<<", ">>" — thao tác trực tiếp trên từng bit của số nguyên

## Mệnh đề điều kiện và vòng lặp

- "if / elif / else" – dùng để rẽ nhánh chương trình: kiểm tra điều kiện đúng/sai rồi thực hiện khối lệnh tương ứng
- "for" – vòng lặp dùng khi biết trước số lần lặp hoặc muốn duyệt qua từng phần tử của list, tuple, string, dict...
- "while" – vòng lặp thực hiện "liên tục khi điều kiện còn đúng", thường dùng khi không biết trước số lần lặp
- "break" – dừng và thoát ngay khỏi vòng lặp, kể cả khi điều kiện lặp vẫn còn đúng
- "continue" – bỏ qua phần code còn lại trong lần lặp hiện tại, nhảy sang lần lặp tiếp theo
- "pass" – câu lệnh trống, không làm gì cả, thường dùng để giữ chỗ cú pháp khi chưa viết code cụ thể

## Kiểu dữ liệu True, False

- "True" và "False" thuộc kiểu "bool" (Boolean), dùng để biểu diễn giá trị đúng/sai trong logic
- Về bản chất, "bool" là kiểu con của "int": "True" có giá trị số là "1", "False" có giá trị số là "0", nên có thể dùng trong các phép toán số học
- Các giá trị được coi là "falsy" (tương đương False khi ép kiểu bool): số "0", "0.0", chuỗi rỗng "", list rỗng "[]", dict rỗng "{}", tuple rỗng "()", và "None"
- Tất cả các giá trị còn lại (khác 0 và không rỗng) đều được coi là "truthy" (tương đương True)
