---
title: 'Software Entropy — Chương trong "The Pragmatic Programmer"'
lastmod: '2026-05-29 10:10:00'
tags:
  - nợ kỹ thuật
  - The Pragmatic Programmer
---

Đây là một khái niệm nổi tiếng từ cuốn sách kinh điển **"The Pragmatic Programmer"** (1999) của **David Thomas & Andrew Hunt** — một trong những cuốn sách gối đầu giường của lập trình viên. "Software Entropy" là một trong những chương đầu tiên và đáng nhớ nhất.

## Entropy là gì?

Trong vật lý, **entropy** là thước đo độ "hỗn loạn" của một hệ thống. Định luật thứ 2 của nhiệt động lực học nói rằng: entropy trong vũ trụ luôn có xu hướng **tăng lên** — mọi thứ tự nhiên sẽ trở nên hỗn loạn hơn theo thời gian, trừ khi có ai đó bỏ năng lượng vào để duy trì trật tự.

Phòng của bạn không tự dọn dẹp. Nó chỉ tự bừa bộn thêm.

## Software Entropy = Sự "thối rữa" của code

Thomas & Hunt áp dụng ý tưởng này vào phần mềm: **code có xu hướng tự nhiên trở nên hỗn loạn theo thời gian**. Họ gọi hiện tượng này là **"software rot"** (code mục nát) hoặc **"software entropy"**.

Một codebase mới thì sạch sẽ, gọn gàng. Nhưng sau 1 năm, 2 năm... nó dần trở thành một mớ hỗn độn không ai muốn động vào. Tại sao?

## Lý thuyết "Broken Windows" (Cửa sổ vỡ)

Đây là phần hay nhất của chương. Hai tác giả mượn một lý thuyết tội phạm học nổi tiếng:

> Các nhà nghiên cứu phát hiện ra: một tòa nhà bỏ hoang có thể đứng vững nhiều năm. Nhưng **chỉ cần một cửa sổ bị vỡ và không được sửa**, trong vài tuần, toàn bộ tòa nhà sẽ bị phá hoại — graffiti, rác rưởi, người vào chiếm dụng...

Tại sao? Vì một cửa sổ vỡ gửi đi một **tín hiệu**: *"Không ai quan tâm đến nơi này cả."* Và khi mọi người tin rằng không ai quan tâm, họ cũng ngừng quan tâm.

**Code cũng vậy.**

Khi trong codebase có:
- Một đoạn code xấu mà không ai sửa
- Một bug được "workaround" thay vì fix gốc
- Một cái TODO bị bỏ quên 6 tháng
- Một tên biến tệ mà ai cũng thấy nhưng không ai đổi

→ Nó gửi tín hiệu: *"Ở đây code xấu cũng được."* Và rồi lập trình viên tiếp theo cũng viết code xấu, vì "chỗ này vốn đã xấu rồi mà". Cứ thế, codebase mục nát rất nhanh.

## Bài học rút ra

Thomas & Hunt đưa ra một nguyên tắc đơn giản nhưng mạnh mẽ:

> **"Don't live with broken windows."** — Đừng sống chung với cửa sổ vỡ.

Cụ thể:

**1. Sửa ngay khi thấy.** Thấy code xấu? Sửa luôn, dù chỉ là đổi một cái tên biến. Không có thời gian sửa? Ít nhất hãy **comment `// FIXME` hoặc tạo ticket**, để thể hiện rằng "tôi biết chỗ này có vấn đề, tôi quan tâm".

**2. Hành động nhỏ ngăn chặn sụp đổ lớn.** Bạn không cần refactor toàn bộ hệ thống. Chỉ cần đừng để code xấu tích tụ mà không ai phản ứng. Mỗi lần đi qua, dọn một chút.

**3. Văn hóa quan trọng hơn kỹ thuật.** Nếu team có văn hóa "thấy là sửa", entropy sẽ thấp. Nếu team có văn hóa "kệ đi, không phải việc của mình", code sẽ thối nhanh chóng dù ai cũng giỏi.

## Ngược lại: Hiệu ứng tích cực

Điều thú vị là **hiệu ứng này cũng hoạt động theo chiều ngược lại**. Khi bạn vào một codebase cực sạch, được chăm chút kỹ lưỡng, bạn sẽ tự nhiên **muốn viết code đẹp** để xứng đáng với nó. Bạn sợ làm "vấy bẩn" nó.

Đó là lý do vì sao những codebase tốt có xu hướng ngày càng tốt hơn, còn những codebase tệ thì càng ngày càng tệ — như một hiệu ứng tự củng cố.

## Tóm gọn

**Software Entropy = Code mục nát theo thời gian là một xu hướng tự nhiên, không thể tránh hoàn toàn — nhưng có thể chống lại bằng cách không bao giờ để "cửa sổ vỡ" tồn tại trong codebase.**

Đây là một trong những lý do tại sao "clean code" không phải chuyện làm đẹp, mà là chuyện **sống còn của dự án về lâu dài**. Nó kết nối rất chặt với câu Ousterhout ở slide trước: complexity tích tụ qua từng "vết xước" nhỏ — và mỗi vết xước không sửa chính là một cửa sổ vỡ.

---
## Liên quan
- [[complexity-ousterhout|Complexity của Ousterhout]]
- [[tactical-vs-strategic-programming|Tactical vs Strategic Programming]]
