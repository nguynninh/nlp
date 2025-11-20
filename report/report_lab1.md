## Các bước triển khai
1. Với lab01

Bước 1. Phân tích đề bài, xác định yêu cầu và dữ liệu đầu vào.

Bước 2. Thực hành
+ Tạo interface chung cho các bộ tách từ (tokenizer)
+ Dùng SimpleTokenizer để cài đặt bộ tách từ đơn giản bằng vòng for và theo cách suy nghĩ của chúng ta
+ Dùng RegexTokenizer để cài đặt bộ tách từ nâng cao hơn sử dụng biểu thức chính quy

Bước 3. Thử nghiệm và đánh giá kết quả
+ Áp dụng các bộ tách từ đã cài đặt lên một phần của tập dữ liệu đơn giản để quan sát và so sánh kết quả.
+ Áp dụng các bộ tách từ đã cài đặt lên một phần của tập dữ liệu thực tế UD_English-EWT để quan sát và so sánh kết quả
=> So sánh kết quả của tách từ đơn giản và biểu thức chính quy trên cùng một đoạn văn bản nếu sai thì tiến hành tinh chỉnh code

Bước 4. Kết luận
+ Đa số các kết quả đều đúng, tuy nhiên vẫn còn một số trường hợp sai sót do cách cài đặt chưa bao quát hết các trường hợp đặc biệt trong văn bản.
+ RegexTokenizer có độ chính xác cao hơn SimpleTokenizer do sử dụng biểu thức chính quy để nhận diện các mẫu phức tạp hơn.

2. Với lab02

Bước 1. Phân tích đề bài, xác định yêu cầu và dữ liệu đầu vào.

Bước 2. Thực hành
+ Tạo interface chung cho CountVectorizer
+ Cài đặt CountVectorizer sử dụng bộ tách từ đã xây dựng ở Lab 1
+ + fit(corpus: List[str])
Phân tích toàn bộ tập văn bản (corpus), tách token bằng tokenizer, thu thập tất cả các token duy nhất, sắp xếp chúng và xây dựng từ điển (vocabulary) ánh xạ mỗi token sang một chỉ số duy nhất.

+ + transform(documents: List[str])
Chuyển đổi danh sách văn bản thành các vector đếm (count vector) dựa trên từ điển đã được xây dựng. Mỗi vector thể hiện số lần xuất hiện của từng token trong văn bản đó.

+ + fit_transform(corpus: List[str])
Kết hợp cả hai bước: vừa xây dựng từ điển (fit), vừa chuyển đổi tập văn bản thành các vector đếm (transform). Tiện lợi khi muốn thực hiện cả hai thao tác liên tiếp.

Bước 3. Thử nghiệm và đánh giá kết quả
+ Áp dụng CountVectorizer lên một tập văn bản đơn giản để kiểm tra chức năng cơ bản.
+ Áp dụng CountVectorizer lên tập dữ liệu UD_English-EWT để thấy cách văn bản được chuyển đổi thành các vector số, sẵn sàng cho các mô hình học máy
=> Kiểm tra kết quả đầu ra của CountVectorizer xem có đúng với mong đợi

Bước 4. Kết luận
+ CountVectorizer hoạt động đúng chức năng, chuyển đổi văn bản thành ma trận tầnsố từ.
+ Kết quả đầu ra phù hợp với kỳ vọng, sẵn sàng cho các bước xử lý tiếp theo trong NLP.

## Cách chạy code và ghi log kết quả
- Cài đặt các thư viện cần thiết:
```zsh
pip install -r requirements.txt
```
- Chạy các file kiểm thử hoặc main:
```zsh
python test/main.py
```
- Kết quả sẽ được in ra màn hình hoặc ghi vào file log (dùng `print()`)