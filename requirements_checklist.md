# Checklist Yêu Cầu & Tiến Độ Bài Tập Về Nhà 1 (HW01)
**Mã bài tập:** HW01 AI | **Hình thức:** Cá nhân | **Ngôn ngữ báo cáo:** Tiếng Việt 

---

## 1. Phần khởi động (Warm-up): Bản đồ tư duy (Mindmap) về Quy trình ISTQB & Vai trò QA/QC
- [ ] Yêu cầu một công cụ AI vẽ bản đồ tư duy về quy trình ISTQB / vai trò QA/QC.
- [ ] Tìm ra và chỉ rõ **đúng 3 lỗi sai/thiếu sót** trong bản đồ tư duy do AI tạo ra.
- [ ] Sửa lại các lỗi đó và xuất ra bản đồ tư duy cuối cùng dạng ảnh (`PNG`) hoặc định dạng `Markdown`.

---

## 2. Yêu cầu 1: Thị trường việc làm QA/QC 2026+ (40 điểm)
- [ ] Thu thập **10 tin tuyển dụng QA/QC** được đăng trong vòng 60 ngày gần đây tính đến ngày nộp.
  - [ ] **Bắt buộc:** Ít nhất **3 tin tuyển dụng** yêu cầu kỹ năng về AI/LLM/Automation-AI.
- [ ] Với mỗi tin tuyển dụng, phải thu thập đầy đủ thông tin:
  - [ ] Link gốc của tin tuyển dụng.
  - [ ] Ảnh chụp màn hình có ghi ngày tháng và hiển thị rõ tên tài khoản/tên đăng nhập của bạn ở góc màn hình (Cơ chế chống gian lận - Anti-cheat).
  - [ ] Mô tả công việc (Job description).
  - [ ] Các kỹ năng yêu cầu (Required skills).
  - [ ] Mức lương (Salary).
  - [ ] Viết **1–2 câu phân tích tác động của AI** (AI Impact Analysis) cho từng tin tuyển dụng.

---

## 3. Yêu cầu 2: 20 Lỗi phần mềm nổi tiếng giai đoạn 2022–2026 (20 điểm)
- [ ] Tìm và liệt kê **20 lỗi phần mềm** được công bố công khai từ năm 2022 đến 2026.
  - [ ] **Bắt buộc:** Ít nhất **5 lỗi** liên quan trực tiếp đến AI/LLM (ví dụ: ảo tưởng/hallucination, tấn công prompt injection, thiên kiến/bias, lỗi bảo mật dữ liệu AI).
- [ ] Với mỗi lỗi phần mềm, tài liệu hóa các thông tin sau:
  - [ ] Nguồn/Link dẫn chứng (Source link).
  - [ ] Mô tả lỗi (Description).
  - [ ] Mức độ nghiêm trọng (Severity).
  - [ ] Hậu quả (Consequences).
  - [ ] Giải pháp khắc phục (Solution).
  - [ ] **Kiểm tra thiên kiến/ảo tưởng của AI:** Chỉ ra ít nhất **1 điểm** mà AI trả lời sai, thiên kiến hoặc ảo tưởng khi giải thích về lỗi này (Bắt buộc phải thực hiện cho **từng lỗi trong số cả 20 lỗi**).

---

## 4. Yêu cầu 3: Thiết kế & Thực thi kiểm thử cho thiết bị vật lý (40 điểm)
- [ ] Chọn **1 thiết bị gia dụng cụ thể** (quạt, bộ lọc nước, nồi cơm điện, bóng đèn thông minh, v.v.).
- [ ] Chụp **1 bức ảnh thực tế** của thiết bị chụp chung với **thẻ sinh viên** của bạn trong cùng một khung hình (`.jpg`).
- [ ] Khai báo rõ thông tin thiết bị: Hãng (Brand), Dòng máy (Model), Năm sản xuất (Year), Số seri (Serial Number - ẩn đi 4 ký tự ở giữa).
- [ ] Nhờ AI thiết kế các ca kiểm thử cho thiết bị này.
- [ ] Thiết kế tổng cộng **15 ca kiểm thử (Test cases)** có đầy đủ các cột: Mục tiêu (Objective), Đầu vào (Input), Các bước thực hiện (Steps), Kết quả mong đợi (Expected), Kết quả thực tế (Actual), Đánh giá (Verdict).
  - [ ] **Bắt buộc:** Ít nhất **3 ca kiểm thử** phải là các trường hợp biên/đặc biệt (edge cases) mà **AI không tự nghĩ ra được**.
  - [ ] Cung cấp **ảnh chụp cuộc trò chuyện với AI** minh chứng AI đã bỏ sót các ca biên này cùng với **giải thích bằng văn bản** lý do tại sao AI bỏ sót.
- [ ] Thực thi thực tế ít nhất **5 ca kiểm thử** trên thiết bị thật.
  - [ ] Quay video minh họa ngắn (dưới 60 giây) cho mỗi ca thực thi, có giọng thuyết minh của chính bạn.
  - [ ] Tải các video này lên YouTube ở chế độ **Không công khai (Unlisted)**.
- [ ] Lưu vết các lỗi tìm thấy (mục tiêu $\ge$ 5 lỗi) dưới dạng **Issues** trên kho lưu trữ GitHub cá nhân của bạn.
  - [ ] Chụp ảnh màn hình trang Issues trên GitHub hiển thị rõ tên tài khoản GitHub (username) của bạn.

---

## 5. Giao thức hợp tác AI & Báo cáo tuân thủ (AI Compliance)
- [ ] Ký cam kết nhận thức của sinh viên: Đảm bảo file `AI 06 Student Acknowledgement` đã được ký (bắt buộc trước khi chấm bài).
- [ ] **Báo cáo kiểm toán AI (AI Audit Report - AI 02):** Thực hiện điền đầy đủ mẫu 5 phần cho từng tạo tác do AI hỗ trợ (một lượt prompt tạo ra nhiều test cases tính là 1 tạo tác):
  1. Prompt đã dùng + Tên công cụ AI + Nhãn thời gian (giờ, ngày/tháng/năm).
  2. Kết quả phản hồi đầy đủ của AI (hoặc ảnh chụp màn hình có viền đỏ chú thích).
  3. Đánh giá kết quả (VALID / INVALID / INCOMPLETE).
  4. Lập luận dựa trên ISTQB hoặc tài liệu môn học (2-5 câu).
  5. Phần sửa đổi của sinh viên (Student fix) - làm nổi bật phần thay đổi.
- [ ] Tóm tắt tỷ lệ chính xác của AI và kết luận khi nào nên/không nên dùng AI cho công việc này ở cuối báo cáo kiểm toán.
- [ ] **Nhận xét về AI (AI Critique):** Viết một đoạn văn từ 200–300 từ đánh giá hiệu quả, sai sót của AI và bài học rút ra khi cộng tác với AI trong bài tập này.
- [ ] **Khai báo bắt buộc (Mandatory Disclosure):** Điền vào mẫu khai báo tiêu chuẩn ở cuối báo cáo (trước phần phụ lục).
- [ ] **Bản tự đánh giá điểm số (Self-Assessment Grade):** Tự chấm điểm theo rubric ở cuối báo cáo (điền điểm 3 chữ số, ví dụ `000` đến `100`).
- [ ] Hoàn thành và ký các biểu mẫu:
  - [ ] `AI 03 AI Disclosure Form`
  - [ ] `AI 05 AI Privacy Checklist`

---

## 6. Danh sách minh chứng chống gian lận (Anti-Cheat Constraints - Cấm dùng AI tạo)
- [ ] Ảnh chụp thiết bị vật lý chung với thẻ sinh viên.
- [ ] Các video thực thi kiểm thử có giọng đọc thuyết minh thật của sinh viên.
- [ ] 10 ảnh chụp màn hình tin tuyển dụng hiển thị rõ tên đăng nhập trên nền tảng.
- [ ] File lịch sử trò chuyện prompt (`Prompt log .md`) có đầy đủ nhãn thời gian cho mọi câu lệnh gửi lên AI.

---

## 7. Quy định nộp bài & Cấu trúc file `.zip` nộp trên Moodle
- [ ] Đặt tên file nén: `MSSV_HW01_AI_<điểm_tự_đánh_giá>.zip` (ví dụ: `21127000_HW01_AI_095.zip`).
- [ ] Các tệp tin bắt buộc bên trong file `.zip`:
  - [ ] **Báo cáo chính (PDF):** Chứa các nội dung Job Market, Defects, Test Design, AI Critique, Mandatory Disclosure, Self-Assessment và các phụ lục đính kèm.
  - [ ] **Appendix A (Phụ lục A):** File nhật ký prompt đầy đủ (`.md` hoặc `.txt`) kèm mốc thời gian gửi.
  - [ ] **File Excel:** Danh sách ca kiểm thử (Test Cases), Checklist và Báo cáo tóm tắt kiểm thử (Test Summary Report).
  - [ ] **Ảnh chụp màn hình GitHub Issues** hiển thị các lỗi tìm được cùng với username GitHub của bạn.
  - [ ] **Ảnh chụp thiết bị vật lý + thẻ sinh viên** (`.jpg`).
  - [ ] **Đường liên kết YouTube Unlisted** cho $\ge$ 5 video chạy thử thực tế.
  - [ ] **Bản đồ tư duy quy trình QA/QC** (`.png` hoặc `.md`).
  - [ ] Các biểu mẫu AI đã điền đầy đủ và ký tên:
    - [ ] `AI 02` (Báo cáo kiểm toán AI - đính kèm phụ lục báo cáo chính hoặc tệp riêng).
    - [ ] `AI 03` (Bản khai báo cộng tác AI).
    - [ ] `AI 05` (Checklist bảo mật thông tin AI).
