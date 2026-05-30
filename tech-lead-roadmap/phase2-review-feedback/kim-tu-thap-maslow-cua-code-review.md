---
title: "Kim tự tháp Maslow của code review"
original_title: "Maslow's pyramid of code review"
source: "http://www.dein.fr/2015-02-18-maslows-pyramid-of-code-review.html"
phase: "Phase 2 — Code review & feedback"
---

# Kim tự tháp Maslow của code review

> Nguồn: [Maslow's pyramid of code review](http://www.dein.fr/2015-02-18-maslows-pyramid-of-code-review.html)

Giống như trong kim tự tháp Maslow, mỗi tầng đòi hỏi tầng phía dưới nó phải được thỏa mãn trước. Sẽ chẳng có ý nghĩa gì khi một đoạn code tính tiền nhầm khách hàng lại được viết dễ đọc.

Code nên đạt được những phẩm chất sau:

* **Đúng (Correct)**: Code có làm đúng những gì nó cần làm không? Nó có xử lý được các trường hợp biên (edge case) không? Nó đã được test đầy đủ để đảm bảo vẫn đúng đắn ngay cả khi các kỹ sư khác chỉnh sửa nó hay chưa? Hiệu năng của nó có đủ tốt cho tình huống sử dụng này không?

* **An toàn (Secure)**: Code có lỗ hổng bảo mật nào không? Dữ liệu có được lưu trữ an toàn không? Thông tin định danh cá nhân (PII) có được xử lý đúng cách không? Code có thể bị lợi dụng để gây tấn công từ chối dịch vụ (DOS) không? Việc kiểm tra dữ liệu đầu vào (input validation) đã đủ toàn diện chưa?

* **Dễ đọc (Readable)**: Code có dễ đọc và dễ hiểu không? Nó có làm rõ được các yêu cầu nghiệp vụ không (code được viết để con người đọc, không phải để máy tính đọc)? Các test có đủ súc tích không? Các biến, hàm và class đã được đặt tên hợp lý chưa? Các mô hình miền (domain model) có ánh xạ thế giới thực một cách rõ ràng để giảm tải nhận thức không? Code có tuân theo quy ước viết code nhất quán không?

* **Tao nhã (Elegant)**: Code có tận dụng những pattern phổ biến và đã được kiểm chứng không? Nó có đạt được mục tiêu mà không phải hy sinh tính đơn giản và súc tích không? Bạn có hào hứng khi làm việc với đoạn code này không? Bạn có tự hào về đoạn code này không?

* **Vị tha (Altruist)**: Code có khiến codebase trở nên tốt hơn so với trước đó không? Nó có truyền cảm hứng để các kỹ sư khác cũng cải thiện code của họ không? Nó có dọn dẹp code không dùng đến, cải thiện tài liệu, hay giới thiệu những pattern tốt hơn thông qua việc tái cấu trúc (refactoring) ở quy mô nhỏ không?
