---
title: '"No-one knows exactly what they want" — Sự thật phũ phàng về requirements'
lastmod: '2026-05-29 10:20:00'
tags:
  - quy trình phát triển
  - The Pragmatic Programmer
---

Câu này cũng đến từ **"The Pragmatic Programmer"** của Thomas & Hunt, nằm trong phần bàn về **requirements gathering** (thu thập yêu cầu). Đây là một trong những bài học khiến nhiều lập trình viên trẻ bị "vỡ mộng" nhất khi đi làm thực tế.

## Vấn đề: Khoảng cách giữa "nói" và "muốn"

Khi bạn mới đi làm, bạn nghĩ quy trình sẽ là:
1. Khách hàng/PM nói họ muốn gì
2. Bạn code đúng như vậy
3. Mọi người vui vẻ

**Thực tế thì:**
1. Khách hàng nói họ muốn X
2. Bạn code X hoàn hảo
3. Khách hàng nhìn vào và nói: *"Ơ, không, ý tôi không phải vậy"*
4. Bạn muốn khóc

Tại sao? Vì **không ai thực sự biết mình muốn gì cho đến khi họ nhìn thấy thứ mình KHÔNG muốn.**

## Tại sao điều này xảy ra?

**1. Con người không suy nghĩ bằng specification.** Khách hàng không có sẵn một bản thiết kế chi tiết trong đầu. Họ có một **cảm giác mơ hồ** về vấn đề cần giải quyết, và họ dùng ngôn ngữ tự nhiên (vốn đầy mơ hồ) để diễn đạt nó.

**2. Họ nói về giải pháp, không phải vấn đề.** Ví dụ kinh điển: khách nói "Tôi cần một cái nút màu đỏ ở góc trên." Bạn làm xong. Họ vẫn không hài lòng. Hóa ra vấn đề thực sự là *"Người dùng không tìm thấy chức năng đặt hàng"* — và cái nút đỏ chỉ là **giải pháp họ tự nghĩ ra**, mà có thể không phải giải pháp tốt nhất.

**3. Yêu cầu thay đổi khi họ thấy sản phẩm.** Nhìn thấy phiên bản đầu tiên khiến họ nhận ra những gì họ thực sự cần — những thứ không hiện ra trong đầu khi mới bắt đầu. Đây không phải là họ "lật kèo", mà là cách bộ não con người hoạt động.

**4. Có những yêu cầu ngầm họ không nói ra** vì nghĩ là "hiển nhiên". Ví dụ: "tất nhiên là phải có mobile rồi", "tất nhiên là không cho user xóa nhầm chứ"...

## Bài học từ Thomas & Hunt

Họ đưa ra một thay đổi tư duy quan trọng:

> **"Đừng thu thập requirements — hãy đào tìm chúng."** (Don't Gather Requirements — Dig for Them.)

Tức là yêu cầu nằm **bên dưới bề mặt**, không phải thứ bạn chỉ cần hỏi là có. Vai trò của lập trình viên giỏi không phải là "thư ký ghi chép yêu cầu", mà là **thám tử khám phá vấn đề thực sự**.

## Cách đối phó trong thực tế

**1. Hỏi "Tại sao?" nhiều lần.** Khi khách nói họ muốn X, đừng hỏi "X cụ thể thế nào?". Hãy hỏi *"Anh muốn X để làm gì?"*, *"Vấn đề anh đang gặp là gì?"*. Thường giải pháp thực sự khác hoàn toàn với X.

**2. Show, don't tell.** Thay vì viết spec dài 20 trang rồi code 3 tháng, hãy làm **prototype, mockup, demo nhỏ** sớm nhất có thể. Cho khách nhìn thấy thứ gì đó cụ thể → họ sẽ ngay lập tức biết "à không, không phải vậy" hoặc "à đúng rồi, nhưng thêm cái này nữa". Phản hồi từ một bản demo xấu xí có giá trị hơn 10 cuộc họp bàn về spec.

**3. Lặp lại nhiều vòng nhỏ (iterate).** Đây là nền tảng của Agile. Không cố làm đúng 100% ngay lần đầu, mà chấp nhận sẽ sai, và xây dựng quy trình **phát hiện cái sai sớm, sửa nhanh, lặp lại**.

**4. Đừng đổ lỗi cho khách hàng.** Khi requirement thay đổi, đừng nghĩ "khách ngu quá, không biết mình muốn gì". Hãy nhớ: **đây là bản chất của công việc**, không phải lỗi của ai cả. Lập trình viên kỳ vọng requirement cố định = lập trình viên sẽ luôn khổ.

## Ý nghĩa sâu xa

Câu này thực ra đánh đổ một niềm tin sai lầm phổ biến trong nghề: rằng *"nếu chỉ business analyst làm việc kỹ hơn, viết spec rõ hơn, thì developer chỉ cần thực thi là xong"*.

Sự thật là: **phát triển phần mềm về bản chất là một quá trình khám phá**, không phải quá trình sản xuất. Bạn không đang lắp ráp một chiếc xe theo bản thiết kế có sẵn — bạn đang **đồng thời thiết kế chiếc xe và tìm ra mình thật sự cần loại xe gì**.

## Tóm gọn

**"No one knows exactly what they want"** không phải lời than vãn — nó là một **nguyên lý nền tảng** của ngành phần mềm. Khi bạn chấp nhận nó:
- Bạn ngừng kỳ vọng requirement hoàn hảo từ đầu
- Bạn xây dựng quy trình để **phát hiện** cái mình thực sự cần, thay vì cố **đoán** ngay từ đầu
- Bạn trở thành đối tác giúp khách hàng *khám phá* vấn đề, chứ không chỉ là "thợ code" làm theo lệnh

Đây cũng là lý do vì sao các phương pháp như **Agile, Lean Startup, MVP, prototyping** ra đời và thành công — chúng được thiết kế xoay quanh chính sự thật phũ phàng này.

---
## Liên quan
- [[small-steps-feedback|Bước nhỏ + Feedback loop]]
- [[the-design-concept|The Design Concept (Brooks)]]
