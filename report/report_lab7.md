# Báo cáo Lab 7: Thực hành chuyên sâu về Phân tích cú pháp phụ thuộc (Dependency Parsing)

**Sinh viên:** Ninh Nguyen  
**Ngày thực hiện:** 4 tháng 12, 2025

---

## 1. Giới thiệu

Trong bài lab này, tôi đã thực hành phân tích cú pháp phụ thuộc (Dependency Parsing) sử dụng thư viện `spaCy`. Phân tích cú pháp phụ thuộc là một kỹ thuật quan trọng trong xử lý ngôn ngữ tự nhiên giúp xác định các mối quan hệ ngữ pháp giữa các từ trong câu.

### Mục tiêu

- Hiểu về cấu trúc cây phụ thuộc và các quan hệ ngữ pháp
- Sử dụng thư viện spaCy để phân tích câu
- Trực quan hóa cây phụ thuộc bằng displaCy
- Trích xuất thông tin từ cây phụ thuộc
- Xây dựng các hàm xử lý cây phụ thuộc

---

## 2. Phân tích câu và Trực quan hóa

### 2.1. Cài đặt và tải mô hình

Tôi đã cài đặt thư viện `spaCy` và tải mô hình ngôn ngữ tiếng Anh `en_core_web_md`:

```python
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md")
```

### 2.2. Phân tích câu đơn giản

Câu phân tích: **"The quick brown fox jumps over the lazy dog."**

Kết quả phân tích cho thấy:

| Token | Phân tích Cú pháp | Head | Quan hệ |
|-------|-------------------|------|---------|
| The   | DET               | fox  | det     |
| quick | ADJ               | fox  | amod    |
| brown | ADJ               | fox  | amod    |
| fox   | NOUN              | jumps| nsubj   |
| jumps | VERB              | jumps| ROOT    |
| over  | ADP               | jumps| prep    |
| the   | DET               | dog  | det     |
| lazy  | ADJ               | dog  | amod    |
| dog   | NOUN              | over | pobj    |
| .     | PUNCT             | jumps| punct   |

#### Trả lời câu hỏi:

**1. Từ nào là gốc (ROOT) của câu?**

Từ **`jumps`** là gốc (ROOT) của câu. Đây là động từ chính của câu.

**2. `jumps` có những từ phụ thuộc (dependent) nào? Các quan hệ đó là gì?**

- `fox` (quan hệ: `nsubj` - chủ ngữ)
- `over` (quan hệ: `prep` - giới từ)
- `.` (quan hệ: `punct` - dấu câu)

**3. `fox` là head của những từ nào?**

`fox` là head của các từ:
- **The** (quan hệ: `det` - mạo từ)
- **quick** (quan hệ: `amod` - tính từ bổ nghĩa)
- **brown** (quan hệ: `amod` - tính từ bổ nghĩa)

---

## 3. Truy cập các thành phần trong cây phụ thuộc

### 3.1. Phân tích câu phức tạp

Câu phân tích: **"Apple is looking at buying U.K. startup for $1 billion"**

Tôi đã in ra thông tin chi tiết của từng token bao gồm:
- Token text
- Quan hệ phụ thuộc (DEP)
- Head text và POS của head
- Danh sách các token con (children)

Kết quả cho thấy cấu trúc phụ thuộc phức tạp với nhiều mức lồng nhau, trong đó "looking" là động từ chính (ROOT) của câu.

---

## 4. Duyệt cây phụ thuộc để trích xuất thông tin

### 4.1. Trích xuất bộ ba (Chủ ngữ, Động từ, Tân ngữ)

Tôi đã xây dựng thuật toán để tự động trích xuất các bộ ba (Subject, Verb, Object) từ câu:

**Câu:** "The cat chased the mouse and the dog watched them."

**Kết quả:**
```
Found Triplet: (cat, chased, mouse)
Found Triplet: (dog, watched, them)
```

**Phương pháp:**
- Tìm tất cả các token có POS là VERB
- Với mỗi động từ, duyệt qua các token con
- Tìm token con có quan hệ `nsubj` (chủ ngữ)
- Tìm token con có quan hệ `dobj` (tân ngữ trực tiếp)

### 4.2. Trích xuất tính từ bổ nghĩa cho danh từ

**Câu:** "The big, fluffy white cat is sleeping on the warm mat."

**Kết quả:**
```
Danh từ 'cat' được bổ nghĩa bởi các tính từ: ['big', 'fluffy', 'white']
Danh từ 'mat' được bổ nghĩa bởi các tính từ: ['warm']
```

**Phương pháp:**
- Tìm tất cả các token có POS là NOUN
- Với mỗi danh từ, duyệt qua các token con
- Thu thập các token con có quan hệ `amod` (adjective modifier)

---

## 5. Bài tập tự luyện

### 5.1. Tìm động từ chính của câu

Tôi đã xây dựng hàm `find_main_verb()` để tìm động từ chính (ROOT) của câu:

```python
def find_main_verb(doc):
    """Tìm và trả về Token là động từ chính (ROOT) của câu."""
    for token in doc:
        if token.dep_ == "ROOT":
            return token
    return None
```

**Kiểm tra:**

1. **Câu 1:** "The international conference will take place in Paris."
   - **Động từ chính:** `take`

2. **Câu 2:** "She quickly wrote a detailed report for the manager."
   - **Động từ chính:** `wrote`

### 5.2. Trích xuất các cụm danh từ (Noun Chunks)

Tôi đã xây dựng hàm `extract_simple_noun_chunks()` để trích xuất các cụm danh từ:

```python
def extract_simple_noun_chunks(doc):
    noun_chunks = []
    for token in doc:
        if token.pos_ == "NOUN":
            chunk_words = []
            
            # Thêm các từ bổ nghĩa trực tiếp (children)
            for child in token.children:
                if child.dep_ in ("det", "amod", "compound", "nummod"):
                    chunk_words.append(child)
            
            # Thêm danh từ chính
            chunk_words.append(token)
            
            # Sắp xếp theo vị trí xuất hiện
            chunk_words.sort(key=lambda t: t.i)
            
            # Kết hợp thành cụm
            noun_chunk = " ".join([t.text for t in chunk_words])
            noun_chunks.append(noun_chunk)
    
    return noun_chunks
```

**Câu kiểm tra:** "The detailed quarterly report, written by the experienced analyst, was accepted."

**So sánh kết quả:**
- **spaCy Noun Chunks:** `['The detailed quarterly report', 'the experienced analyst']`
- **Custom Noun Chunks:** `['The detailed quarterly report', 'the experienced analyst']`

Hàm tự xây dựng cho kết quả tương tự với hàm có sẵn của spaCy cho các cụm danh từ đơn giản.

### 5.3. Tìm đường đi ngắn nhất trong cây

Tôi đã xây dựng hàm `get_path_to_root()` để tìm đường đi từ một token bất kỳ lên đến ROOT:

```python
def get_path_to_root(token):
    """
    Tìm và trả về danh sách các Token trên đường đi 
    từ Token hiện tại lên đến gốc (ROOT).
    """
    path = [token]
    current = token
    
    while current.dep_ != "ROOT":
        current = current.head
        path.append(current)
        
        # Guard: Tránh vòng lặp vô hạn
        if len(path) > len(token.doc):
            break
    
    return path
```

**Kiểm tra với câu:** "The quick brown fox jumps over the lazy dog."

**Token mục tiêu:** `lazy` (vị trí 6)

**Đường đi:**
```
[lazy (amod)] -> [dog (pobj)] -> [over (prep)] -> [jumps (ROOT)]
```

Kết quả cho thấy `lazy` bổ nghĩa cho `dog`, `dog` là object của giới từ `over`, và `over` là giới từ của động từ chính `jumps`.

---

## 6. Kết luận

### 6.1. Kiến thức đạt được

Qua bài lab này, tôi đã:

1. **Hiểu về cấu trúc cây phụ thuộc:** Mỗi câu có một gốc (ROOT) là động từ chính, và các từ khác có quan hệ phụ thuộc với nhau theo cấu trúc cây.

2. **Nắm vững các quan hệ phụ thuộc phổ biến:**
   - `nsubj`: Chủ ngữ danh từ
   - `dobj`: Tân ngữ trực tiếp
   - `amod`: Tính từ bổ nghĩa
   - `det`: Mạo từ
   - `prep`: Giới từ
   - `pobj`: Tân ngữ của giới từ
   - `ROOT`: Gốc của câu

3. **Sử dụng thành thạo spaCy:** Truy cập các thuộc tính như `token.text`, `token.pos_`, `token.dep_`, `token.head`, `token.children`.

4. **Xây dựng các thuật toán xử lý:** Trích xuất thông tin, duyệt cây, tìm đường đi.

### 6.2. Ứng dụng thực tế

Phân tích cú pháp phụ thuộc có nhiều ứng dụng trong NLP:

- **Trích xuất thông tin:** Tìm các bộ ba (subject-verb-object), trích xuất quan hệ
- **Trả lời câu hỏi:** Hiểu cấu trúc câu hỏi và tìm câu trả lời
- **Dịch máy:** Chuyển đổi cấu trúc câu giữa các ngôn ngữ
- **Tóm tắt văn bản:** Xác định các thành phần quan trọng trong câu
- **Kiểm tra ngữ pháp:** Phát hiện lỗi cấu trúc câu

### 6.3. Khó khăn gặp phải

Trong quá trình thực hiện lab, tôi đã gặp một số khó khăn:

1. **Hiểu các quan hệ phụ thuộc phức tạp:**
   - Ban đầu, việc phân biệt các quan hệ như `prep`, `pobj`, `dobj`, `nsubj` khá khó khăn
   - Một số quan hệ không rõ ràng với câu phức tạp có nhiều mệnh đề
   - Giải pháp: Tham khảo tài liệu Universal Dependencies và visualize nhiều câu để làm quen

2. **Xử lý các trường hợp đặc biệt:**
   - Câu có nhiều động từ (compound verbs, auxiliary verbs)
   - Cấu trúc câu phức với mệnh đề quan hệ, mệnh đề phụ
   - Các cụm danh từ lồng nhau phức tạp
   - Giải pháp: Test với nhiều loại câu khác nhau và debug từng trường hợp

3. **Xây dựng thuật toán trích xuất chính xác:**
   - Hàm `extract_simple_noun_chunks()` chỉ xử lý được các cụm danh từ đơn giản
   - Không bắt được các cụm có mệnh đề quan hệ hoặc cụm giới từ phức tạp
   - Các quan hệ như `conj` (liên từ) làm phức tạp việc trích xuất
   - Giải pháp: Bắt đầu với các trường hợp đơn giản, sau đó mở rộng dần

4. **Hiệu suất với văn bản dài:**
   - Duyệt cây phụ thuộc có thể chậm với văn bản lớn
   - Cần tối ưu thuật toán để tránh duyệt lại nhiều lần
   - Giải pháp: Cache kết quả, sử dụng comprehension thay vì loops khi có thể

5. **Trực quan hóa trong Jupyter Notebook:**
   - Cần thiết lập đúng tham số `jupyter=True` cho `displacy.render()`
   - Một số câu dài bị hiển thị không rõ ràng
   - Giải pháp: Điều chỉnh tham số `options` như `distance`, `compact`

### 6.4. Đề xuất phát triển

#### 6.4.1. Cải thiện hệ thống hiện tại

1. **Xây dựng các hàm trích xuất nâng cao:**
   - Trích xuất cụm giới từ (Prepositional Phrases)
   - Xác định mệnh đề quan hệ và mệnh đề phụ
   - Phân tích cấu trúc câu ghép, câu phức
   - Trích xuất các thành phần câu hoàn chỉnh (S-V-O-A)

2. **Phát triển công cụ phân tích ngữ nghĩa:**
   - Kết hợp dependency parsing với semantic role labeling
   - Xác định vai trò ngữ nghĩa (Agent, Patient, Instrument, Location, etc.)
   - Trích xuất quan hệ ngữ nghĩa giữa các thực thể

3. **Tối ưu hiệu suất:**
   - Sử dụng batch processing cho nhiều câu
   - Cache các kết quả phân tích thường dùng
   - Parallel processing với spaCy's `nlp.pipe()`
   - Chỉ load các component cần thiết của pipeline

#### 6.4.2. Ứng dụng thực tế

1. **Hệ thống trích xuất thông tin tự động:**
   - Xây dựng knowledge graph từ văn bản
   - Trích xuất các bộ ba (subject-predicate-object) để lưu vào database
   - Ứng dụng trong phân tích tin tức, báo cáo tài chính

2. **Chatbot và hệ thống hỏi đáp:**
   - Phân tích cấu trúc câu hỏi để xác định loại câu hỏi (who, what, when, where, why, how)
   - Mapping câu hỏi với câu trả lời dựa trên dependency structure
   - Sinh câu trả lời tự nhiên dựa trên cấu trúc ngữ pháp

3. **Công cụ hỗ trợ học ngoại ngữ:**
   - Visualize cấu trúc câu để người học hiểu ngữ pháp
   - Phân tích lỗi ngữ pháp dựa trên dependency tree
   - Gợi ý cải thiện cấu trúc câu

4. **Phân tích sentiment và opinion mining:**
   - Xác định aspect-based sentiment (tính từ bổ nghĩa cho danh từ nào)
   - Trích xuất opinion holder, opinion target, opinion expression
   - Phân tích mức độ của tính từ và trạng từ

#### 6.4.3. Mở rộng sang ngôn ngữ khác

1. **Dependency parsing cho tiếng Việt:**
   - Sử dụng VnCoreNLP hoặc PhoBERT
   - Xử lý đặc thù của tiếng Việt (từ nhiều âm tiết, từ đơn/từ ghép)
   - Xây dựng bộ dữ liệu labeled cho tiếng Việt

2. **So sánh cross-lingual:**
   - So sánh cấu trúc phụ thuộc giữa tiếng Anh và tiếng Việt
   - Xây dựng hệ thống dịch máy dựa trên dependency structure
   - Transfer learning từ mô hình đa ngôn ngữ

#### 6.4.4. Nghiên cứu nâng cao

1. **Kết hợp với Deep Learning:**
   - Sử dụng Graph Neural Networks (GNN) trên dependency tree
   - Fine-tune BERT/Transformer models với dependency information
   - Neural dependency parsing với attention mechanism

2. **Multi-task learning:**
   - Kết hợp parsing với NER, POS tagging, sentiment analysis
   - Joint learning để cải thiện accuracy cho tất cả các tác vụ
   - Transfer learning giữa các tác vụ liên quan

3. **Xử lý văn bản phức tạp:**
   - Parsing cho văn bản đối화 (conversation)
   - Xử lý câu không đầy đủ, câu cảm thán
   - Parsing cho văn bản social media (slang, emoji, abbreviation)

4. **Đánh giá và cải thiện mô hình:**
   - Xây dựng test suite cho các trường hợp đặc biệt
   - Fine-tune model trên domain-specific data
   - Ensemble methods kết hợp nhiều parsers

#### 6.4.5. Công cụ và visualization

1. **Xây dựng web application:**
   - Interface để người dùng nhập câu và xem dependency tree
   - So sánh kết quả của nhiều parsers khác nhau
   - Export kết quả dưới nhiều format (JSON, XML, CoNLL)

2. **Dashboard phân tích corpus:**
   - Thống kê các quan hệ phụ thuộc phổ biến
   - Phân tích độ phức tạp của câu
   - Tìm các pattern cú pháp lặp lại

3. **Interactive learning tool:**
   - Game hóa việc học dependency parsing
   - Bài tập tương tác với feedback tức thì
   - Leaderboard và progress tracking

---

## 7. Tài liệu tham khảo

1. spaCy Documentation: https://spacy.io/
2. Universal Dependencies: https://universaldependencies.org/
3. Dependency Grammar and Dependency Parsing - Joakim Nivre
