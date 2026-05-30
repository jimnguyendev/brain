---
title: 'Giải thích định nghĩa "Complexity" của John Ousterhout'
lastmod: '2026-05-29 10:00:00'
tags:
  - thiết kế phần mềm
  - A Philosophy of Software Design
---

Câu này đến từ cuốn sách nổi tiếng **"A Philosophy of Software Design"** của John Ousterhout (giáo sư khoa học máy tính tại Stanford). Đây là một trong những định nghĩa cốt lõi nhất của cuốn sách.

## Dịch nghĩa

> "Độ phức tạp là bất cứ thứ gì liên quan đến **cấu trúc** của một hệ thống phần mềm khiến nó **khó hiểu** và **khó sửa đổi**."

## Phân tích từng phần

**"Anything related to the structure"** — Ousterhout không nói về complexity của thuật toán (Big-O) hay độ khó của bài toán. Ông nói về complexity *phát sinh từ cách code được tổ chức*: cách chia module, đặt tên, thiết kế interface, phân chia trách nhiệm... Đây là loại complexity do **con người tạo ra**, và cũng do con người có thể loại bỏ.

**"Makes it hard to understand"** — Khi bạn (hoặc đồng đội) đọc code và không hiểu nó làm gì, hoặc phải đọc 5 file mới hiểu được 1 chức năng → đó là complexity. Ví dụ: tên biến `data`, `temp`, `process()` không nói lên gì cả.

**"Hard to modify"** — Khi muốn thêm một feature nhỏ mà phải sửa 10 chỗ khác nhau, hoặc sợ "động vào chỗ này thì chỗ kia hỏng" → đó là complexity. Ousterhout gọi hiện tượng này là **"change amplification"** (một thay đổi nhỏ bị khuếch đại thành nhiều thay đổi).

## Tại sao định nghĩa này quan trọng?

Điểm tinh tế là Ousterhout định nghĩa complexity theo **trải nghiệm của developer**, chứ không phải theo các thước đo kỹ thuật như số dòng code hay cyclomatic complexity. Một hệ thống 100,000 dòng code có thể *đơn giản* nếu dễ hiểu, dễ sửa. Một hệ thống 1,000 dòng có thể *phức tạp* nếu mỗi lần đụng vào là phải đọc lại từ đầu.

Trong sách, ông chỉ ra 3 dấu hiệu của complexity:
1. **Change amplification** — một thay đổi đòi hỏi sửa nhiều nơi
2. **Cognitive load** — phải nhớ quá nhiều thứ mới làm được việc
3. **Unknown unknowns** — không biết mình cần phải biết điều gì để sửa code an toàn

Cái thứ 3 là tệ nhất, vì bạn không thể tránh được điều mình không biết là tồn tại.

## Ý nghĩa thực tế

Định nghĩa này định hướng toàn bộ triết lý code: **mục tiêu của thiết kế phần mềm tốt không phải là làm code "đẹp" hay "thông minh", mà là làm cho người tiếp theo (kể cả chính bạn 6 tháng sau) đọc và sửa được dễ dàng**. Complexity tích tụ dần qua từng quyết định nhỏ, và chính những "vết xước" nhỏ này — chứ không phải một thảm họa kiến trúc lớn — mới là thứ giết chết codebase theo thời gian.

---
## Liên quan
- [[software-entropy|Software Entropy]]
- [[tactical-vs-strategic-programming|Tactical vs Strategic Programming]]
- [[the-design-concept|The Design Concept (Brooks)]]
