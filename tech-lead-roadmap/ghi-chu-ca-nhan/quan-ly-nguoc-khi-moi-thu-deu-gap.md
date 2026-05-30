---
title: 'Quản lý ngược & sống sót khi "mọi thứ đều gấp"'
lastmod: '2026-06-04 10:00:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Bài chuyên sâu theo tình huống thực tế: **BE duy nhất** kiêm dẫn dắt một team ~8 người, dự án 5 năm tuổi nhiều nợ kỹ thuật, công ty khó khăn, thị trường bị clone nhanh, CEO liên tục ép mục tiêu gấp. Nối tiếp [[tech-lead-vai-tro-hay-bay|bài Ngày 2 — đừng làm nút thắt cổ chai]].

## Sự thật đầu tiên phải nuốt: "tất cả đều gấp" = không gì được ưu tiên

Khi business và CEO dán nhãn "gấp" lên mọi thứ, đó không phải là ưu tiên — đó là sự **vắng mặt của ưu tiên**. Và nếu bạn lặng lẽ nhận hết, bạn không phải đang "chịu khó". Bạn đang:

1. **Tiếp tay cho sự rối loạn** — CEO không bao giờ phải đối diện với cái giá của việc muốn-mọi-thứ-cùng-lúc, vì bạn đã âm thầm hấp thụ nó.
2. **Tự bảo đảm hai kết cục**: burnout của chính bạn, và nợ kỹ thuật phình to (vì cái gì cũng làm vội).

Gánh giỏi không phải là phẩm chất của tech lead. **Làm cho cái giá trở nên hữu hình** mới là.

## Nguyên tắc cốt lõi: đẩy quyết định đánh đổi ngược lên trên

Bạn không có quyền (và cũng không nên) tự ý nói "không" với CEO. Nhưng bạn **luôn có quyền buộc người ra lệnh phải chọn**. Đây là khác biệt giữa một dev nhận việc và một tech lead.

Đừng nói: *"Em không làm kịp đâu."* (nghe như than, như từ chối)

Hãy nói:

> **"Với năng lực team hiện tại, sprint này làm được X *hoặc* Y, không thể cả hai. Anh muốn ưu tiên cái nào?"**

> **"Mình ship nhanh như anh muốn được — đổi lại sẽ vay nợ kỹ thuật ở chỗ thanh toán, và hóa đơn đến sau ~3 tháng dưới dạng bug khó sửa. Anh chấp nhận đánh đổi đó chứ?"**

> **"Nếu chen task này vào giữa sprint, task Z đã hứa với khách sẽ trễ. Em đổi không, hay giữ nguyên?"**

Cả ba câu đều có chung một cấu trúc: **nêu ràng buộc thật → đưa ra lựa chọn → trả quyền quyết định về cho người có thẩm quyền.** Bạn không cãi, không trốn. Bạn làm cho sự đánh đổi mà CEO vốn đang né tránh trở nên không thể né được.

## Công cụ thực chiến: bắt buộc xếp hạng (forced ranking)

Khi nhận một loạt yêu cầu "đều gấp", đừng cố làm song song. Mang cả danh sách quay lại và yêu cầu **xếp hạng tuyệt đối**:

> *"Em có 5 việc đang được gọi là gấp. Team em làm tuần tới được 2. Anh đánh số 1 đến 5 giúp em — em làm từ trên xuống."*

Không cho phép hai việc cùng hạng 1. Sự khan hiếm (chỉ làm được 2) ép người ra quyết định phải thật sự ưu tiên — điều mà câu "tất cả đều gấp" cho phép họ né.

## Áp dụng cho nợ kỹ thuật của bạn

Cùng một logic. Đừng hỏi *"có nên trả nợ kỹ thuật không?"* — câu trả lời luôn là "có, nhưng không phải bây giờ" trong mắt business. Hãy gắn nợ vào hậu quả business hữu hình:

- **Nợ trên đường đi của mục tiêu gấp / đang gây incident** → trả, và **gói vào trong feature** đang làm (không mở "dự án refactor" riêng).
- **Nợ chỉ làm code xấu nhưng không chặn gì** → ghi vào sổ, đóng băng. Trong một công ty đang đánh nhau để sống, đây là thứ xa xỉ.
- Khi cần thuyết phục: nói bằng tiền và thời gian, không nói bằng "clean code". *"Chỗ này mỗi lần thêm tính năng tốn gấp đôi thời gian và hay sinh bug; bỏ 3 ngày dọn giờ thì 2 tháng tới mỗi feature nhanh hơn 40%."*

## Một insight chiến lược: code không phải lợi thế của bạn

Vì sản phẩm của các bạn có thể bị AI/đối thủ clone nhanh, **độ sạch của kiến trúc không phải là moat**. Moat là tốc độ ra tính năng, là dữ liệu, là khách hàng. Điều này nghĩa là: lúc này, **vay nợ kỹ thuật có chủ đích để thắng cửa sổ thời gian** đôi khi là quyết định *đúng* của một tech lead — miễn là bạn ghi nợ lại và biết khi nào trả. Biết khi nào nên vay cũng quan trọng ngang biết khi nào nên trả.

## Tự phản chiếu

1. Lần gần nhất nhận một mục tiêu "gấp", tôi đã hấp thụ nó hay đã đẩy lựa chọn đánh đổi ngược lên?
2. Trong danh sách "đều gấp" hiện tại, nếu bị ép chỉ chọn 1 việc làm tuần này, tôi đoán CEO sẽ chọn cái nào? Tôi đã bao giờ hỏi thẳng chưa?
3. Nợ kỹ thuật tôi đang trả — nó đang chặn mục tiêu nào của business, hay tôi trả vì khó chịu với code xấu?

## Hành động nhỏ tuần này

Chọn **một** mục tiêu gấp sắp tới. Trước khi lao vào làm, gửi sếp đúng một câu đánh đổi dạng "X hoặc Y" (hoặc "nhanh = nợ chỗ này"). Quan sát phản ứng — và quan sát cả cảm giác của chính bạn khi không còn âm thầm gánh hết.
