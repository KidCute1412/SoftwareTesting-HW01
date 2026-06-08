**Faculty of Information Technology (FIT) – Ho Chi Minh City University of Science (HCMUS)**

**CS423 / CSC13003 – Software Testing (AI-augmented · 2026)**

**AI POLICY · TEMPLATES — 2026 v1.0**

# **AI Use Disclosure Form**

*Attach to assignments where AI was used in any permitted capacity.*

*Adapted from Med Kharbach, PhD (2026) — AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0. This adaptation is prepared for FIT@HCMUS – CS423 / CSC15003 Software Testing course.*

## **1. Course & Student Info**

| Field | Value |
| :---- | :---- |
| **Course:** | CS423 / CSC13003 – Software Testing |
| **Assignment ID:** | HW\#01 |
| **Assignment Title:** | Job Market Analysis, Software Defects, and Test Case Design for Physical Product |
| **AI Use Category (1–5):** | Category 3: AI-Assisted (permitted with disclosure) |
| **Date:** | 08/06/2026 |
| **Student name:** | Lê Tuấn Lộc |
| **Student ID:** | 23127404 |

## **2. Disclosure Questions**

### **1. AI tool(s) used:**

Gemini 3.5 Flash in Antigravity

### **2. Stage(s) of the assignment where AI was used:**

*Tick all that apply: [x] brainstorming  [ ] outlining  [x] drafting  [ ] feedback  [x] revision  [ ] coding  [ ] data analysis  [ ] visual design  [ ] other (specify).*

AI was utilized in the brainstorming and initial drafting stages to outline the report structure based on the assignment checklist. It was also used to generate the draft lists of 20 software defects and 15 functional test cases for a stand fan SUT, followed by subsequent revision sessions to correct inaccuracies.

### **3. Main prompts or tasks given to the AI:**

* **Prompt 1 (Drafting Report Template):**
  `"dựa vào checklist, hãy tạo template mẫu cho report/Report.md. Có trang bìa đầy đủ."`

* **Prompt 2 (Drafting Software Defects):**
  `"Bạn là một Chuyên gia Đảm bảo Chất lượng Phần mềm (QA Engineer) cấp cao với khả năng nghiên cứu và phân tích kỹ thuật sâu. Hãy thực hiện nhiệm vụ sau đây dựa trên yêu cầu: Tìm kiếm và liệt kê 20 lỗ hổng/lỗi phần mềm (Software Defects) nổi tiếng được công bố trong giai đoạn 2022–2026. Yêu cầu bắt buộc: Phải có ít nhất 5 lỗi liên quan trực tiếp đến AI/LLM..."`

* **Prompt 3 (Drafting Fan Test Cases):**
  `"Act as a QA/QC Engineer. Design exactly 15 functional test cases for a standard household electric stand fan (cây quạt máy đứng bình thường). The fan has the following basic features: Power cord and plug; 3 speed buttons; Oscillation knob; Height adjustment clutch/screw; Safety grill and plastic fan blades. Please output the test cases in a markdown table format..."`

### **4. Specific parts of the work AI contributed to:**

* AI generated the structural template and outline for the main report (`Report.md`).
* AI generated the initial list of 20 software defects and the baseline 15 functional test cases for the stand fan.
* AI did NOT contribute to the physical device test execution, video recording, screenshots, GitHub issue tracking, or writing the AI Critique section.

### **5. How I reviewed, revised, or verified the AI output:**

* **Report Template:** Verified against the `requirements_checklist.md` to ensure all mandatory sections were mapped.
* **Software Defects:** Manually cross-checked each CVE on the official NVD NIST website. I identified and removed 5 incorrect/broken links, replacing them with verified CVEs (e.g. CVE-2023-7028, CVE-2023-38831) and manually corrected their descriptions.
* **Fan Test Cases:** Inspected SUT features and removed the height adjustment test cases (since the physical fan has a fixed height). Replaced them with head-tilt test cases and manually designed 3 complex physical/environmental edge cases (TC13, TC14, TC15) which the AI missed.

### **6. Citation (if required by course style guide):**

Google. (2026). Gemini 3.5 Flash in Antigravity [Large language model]. https://gemini.google.com

## **3. Statement of Honesty**

*By signing below, I confirm that the disclosure above is accurate and complete. I understand that undisclosed or false disclosure of AI use is treated as academic misconduct and may result in a 0 grade for the assignment and disciplinary referral.*

## **Signature**

| Student name (printed): | Lê Tuấn Lộc |
| :---- | :---- |
| **Student ID:** | 23127404 |
| **Class / Cohort:** | 23KTPM3 |
| **Course:** | CS423 / CSC13003 – Software Testing |
| **Instructor:** | Dr. Lam Quang Vu / Dr. Tran Duy Hoang / MSc. Tran Thi Bich Hanh / MSc. Truong Phuoc Loc / MSc. Ho Tuan Thanh |
| **Date:** | 08/06/2026 |
| **Signature:** | <img src="images/Signal.png" width="100" /> |

## **References**

* Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.  
* ISTQB Foundation Level Syllabus (latest version).  
* Hardman, P. (2025). A Post-AI Learning Taxonomy.  
* Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.  
* Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.  
* Anthropic (2025). Building reliable AI test agents — engineering blog.  
* DeepEval & Promptfoo documentation — testing frameworks for LLM systems.