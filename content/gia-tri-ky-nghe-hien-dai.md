---
title: 'Các giá trị kỹ nghệ hiện đại (Modern Engineering Values) — Christoph Nakazawa'
lastmod: '2026-06-07 07:20:00'
tags:
  - thiết kế phần mềm
  - kỹ năng lãnh đạo
---

> Bản dịch bài [Modern Engineering Values](https://cpojer.net/posts/modern-engineering-values) của **Christoph Nakazawa** (đăng 03/06/2026). Bài này lập luận: coding agent thay đổi *chi phí thực thi*, nhưng **các giá trị nền tảng** thì gần như giữ nguyên. Đọc cùng [[tech-lead-lam-chu-vai-tro-tlm|Tech Lead Manager (TLM)]] — bài mà chính tác giả dẫn lại trong mục "On Management".

Cuối năm ngoái tôi đã chia sẻ quy trình làm việc với LLM trong bài "You are absolutely right!?". Tôi biết nó sẽ nhanh lỗi thời, nhưng không ngờ nó lỗi thời *nhanh đến vậy*.

Thực sự tôi không thể tin được rằng giờ đây mình hiếm khi tự tay viết code nữa. Hay nói đúng hơn, **tôi không thể tin nổi rằng trước đây mình từng viết code bằng tay!** Lập trình đã thay đổi tận gốc, và tôi cứ tự hỏi những giá trị kỹ thuật nào vẫn còn quan trọng.

---

Trước khi bắt đầu, và để tránh bị chỉ trích là "nói mà chẳng làm ra sản phẩm nào", đây là những đóng góp của tôi trong vài tháng qua: xây tính năng bằng Rust cho Vite+ (_90% do AI viết_, dù tôi không biết Rust), _fate_ 1.0 (_100% AI_), Codiff — app review diff (_100% AI_), Athena Crisis với hơn 70 bản sửa lỗi (_100% AI_), và Void — metaframework + nền tảng Cloud (_100% AI_).

Nhìn chung, các coding agent giờ viết code tốt ngang hoặc hơn những gì tôi tự viết, và làm trong vài phút thay vì vài tuần. Vì viết code không còn là nút thắt cổ chai, tôi hoàn thành được rất nhiều việc mà lẽ ra *đã chẳng bao giờ được làm*.

Lấy Athena Crisis làm ví dụ — một codebase thời tiền-AI tôi viết tay. Tôi cho Codex chạy trong một vòng lặp để tìm và sửa lỗi: nó sửa 70 lỗi, thêm tính năng, viết test — tất cả trong lúc tôi đang chờ các agent ở dự án khác. Kết quả: game giờ nhanh hơn, ổn định hơn, nhiều tính năng hơn bao giờ hết. Không điều nào xảy ra được nếu thiếu coding agent.

## Cách tôi dùng LLM bây giờ

Bây giờ tôi dùng Codex CLI với GPT 5.5 high. Tôi thích CLI vì nó khởi đầu với trang giấy trắng. Nó liên tục one-shot ra giải pháp đúng với rất ít prompt, **miễn là các "rào chắn" (guardrails) trong codebase đủ mạnh**. Mức reasoning thấp cho chất lượng kém, còn xhigh thì quá chậm và phức tạp hóa mọi thứ.

Tôi làm việc không hiệu quả khi chạy nhiều phiên agent trong cùng một project. Tôi vẫn review toàn bộ code. Việc **chuyển ngữ cảnh** (context switching) cho phép tôi làm việc hiệu quả trên 3–6 project cùng lúc, và nút thắt thường là thảo luận và review code. Sự đa nhiệm này còn thêm một chiều không gian: mỗi project chiếm một góc màn hình cố định, và bằng cách nào đó việc gán vị trí giúp tôi đa nhiệm tốt hơn.

Khi sửa lỗi, tôi chỉ cho agent vào một bản tái hiện lỗi (repro) và **buộc nó trước tiên tạo một test thất bại**. Điều này tăng đáng kể khả năng nó sửa *đúng vấn đề theo đúng cách*. Giữ model trên dây cương ngắn vẫn là cách tốt nhất để có giải pháp hay; đôi khi tốt hơn là kết thúc phiên và bắt đầu lại. Với thay đổi lớn, tôi chạy vài vòng `/review` ở các khu vực khác nhau. Đến giờ, tôi soi xét **code viết tay kỹ hơn cả code do agent viết**.

Bước tiếp theo tốt nhất là push thẳng lên `main`. Tiếc thay hầu hết team không vận hành vậy, nên khi bước vào giai đoạn PR/cộng tác, bạn gần như đánh mất phần lớn tốc độ LLM mang lại. Tôi tin mọi tổ chức kỹ thuật sẽ phải phá bỏ rào cản nếu muốn thành công.

## Các giá trị kỹ thuật cho 2026 trở đi

Một mặt mọi thứ đã thay đổi, mặt khác lại chẳng bao nhiêu. Tôi không nghĩ code sẽ biến mất: file Markdown chứa đặc tả tiếng Anh là một ngôn ngữ lập trình tệ hại, đầy mơ hồ. **Kỹ nghệ phần mềm đang bớt việc tạo ra code và thiên về điều phối các hệ thống tạo ra code.** Bất kể kỹ sư là người hay AI, các giá trị đều rất giống nhau:

### Quyền sở hữu mạnh mẽ (Strong Ownership)

Agent **khuếch đại** quyền sở hữu: người hiểu sâu sản phẩm thực thi nhanh hơn, kẻ thiếu context tạo ra nhiều "nhiễu" hơn. Vì thế phối hợp trở nên tốn kém, và những team hiệu quả nhất sẽ **nhỏ — thường 2–3 người**, ranh giới sở hữu rõ ràng, repository tách biệt. Sở hữu mạnh nghĩa là hiểu kiến trúc, yêu cầu sản phẩm, đánh đổi, định hướng dài hạn — review việc agent làm, quyết định tự tin, đôi khi push thẳng main. Review code ở team nhỏ nên tập trung vào **sự đồng thuận**, không phải tranh cãi về code.

### Gu thẩm mỹ (Taste, Taste, Taste)

Với agent, ai cũng có thể tạo ra cả đống thứ vô nghĩa suốt ngày. Gu tốt không chỉ là xây sản phẩm tuyệt vời, mà là quyết định **việc gì đáng để dành thời gian ngay từ đầu**. Hãy dành nhiều thời gian hơn để tìm ra điều gì thực sự đáng làm.

### Rào chắn nghiêm ngặt & Vòng phản hồi nhanh

Làm việc với agent về cơ bản giống làm trong tổ chức lớn: bạn liên tục "thả" những kỹ sư mới chưa có context vào codebase — y như agent! Càng nhiều ràng buộc (lint, test tự động, kiểm chứng nhanh), mọi người càng iterate nhanh hơn. Công cụ phải xử lý trên **file đã thay đổi** thay vì toàn repo, và đừng để nó chậm dần khi code phình to. Rào chắn nghiêm ngặt + phản hồi nhanh chính là khác biệt giữa **agent hoàn thành trong 1 phút hay 60 phút**.

### Context nằm trong Repo

Trước đây context phân tán khắp nơi: Notion/Docs, con người, ngầm định, hành vi thật trong production, commit message, code. Vì mỗi phiên agent giống một nhân viên mới không có quyền truy cập tất cả những nơi đó, hãy **gom mọi context liên quan vào repo**, ngay tại chỗ. Đây là nơi tuyệt vời để bơm vào gu, giá trị, nguyên tắc của bạn — và nó khiến codebase dễ tiếp cận hơn cho cả agent lẫn con người. Dù nhìn từng dòng code ít hơn trước, việc **tối ưu code cho việc đọc** lại càng giá trị: code đơn giản, ít hơn thì dễ hiểu và dễ sửa.

### Sở hữu stack của riêng bạn (Own your Stack)

Trước đây 95% code là thư viện bên thứ ba vì viết & bảo trì code vốn chậm và đắt — nhưng điều đó khóa bạn vào một stack không kiểm soát được. Mỗi dependency đưa vào code, kiến trúc, ràng buộc mà cuối cùng *bạn* chịu trách nhiệm. Agent thay đổi các yếu tố chi phí này. Với agent, **không còn lý do chính đáng để giao phó phần cốt lõi của sản phẩm cho bên thứ ba** nếu bạn thực sự có thể tự sở hữu chúng.

### Giá trị tùy chọn (Option Value)

Mỗi thay đổi nên **mở khóa thêm lựa chọn** cho cải tiến tương lai. AI thay đổi tận gốc thời gian cần để làm thay đổi quy mô lớn — nhưng nếu bạn "vibe" mình vào một góc cụt thì rất khó thoát ra. Luôn cân nhắc option value ở mức tối đa để di chuyển nhanh trong khi mọi thứ xung quanh không ngừng đổi.

## Về quản lý (On Management)

Những giới hạn cố hữu về quy mô team, phạm vi, tầng quản lý đang bị đẩy xa ra. Về định hướng, tôi tin quản lý kỹ thuật sẽ trở nên **kỹ thuật hơn, chứ không ít hơn**. Khi thực thi rẻ đi và IC có thêm đòn bẩy, manager không thể chỉ sở hữu kết quả hay định hướng — họ phải giữ chuyên môn sâu, tự tin thay đổi project, và lãnh đạo kỹ thuật. Tôi tin vai trò [[tech-lead-lam-chu-vai-tro-tlm|Tech Lead Manager]] là đúng cho hầu hết manager trong kỷ nguyên agent.

## Nhanh hơn bao nhiêu?

Trong 30 ngày qua tôi push 770 commit, sửa trung bình 15 nghìn dòng/ngày — gấp đôi số commit và gấp 3 lượng code so với cùng kỳ hai năm trước. Commit và số dòng vốn là thước đo tồi, nhưng tôi đang so với chính mình. Ngày code tay tốt nhất của tôi là ~1200 dòng, mỗi tuần được một ngày như thế. Giờ tôi ship nhiều gấp mười, chất lượng cao hơn.

Trước tôi bị nghẽn ở việc viết code, giờ tôi **bị nghẽn ở việc vận dụng phán đoán**. Chúng ta đang mở khóa khả năng ship những thứ tuyệt vời với tốc độ ánh sáng, và cần nhiều người hơn bao giờ hết để làm điều đó. *Hãy cùng ship nào!*

## Liên hệ với Prep Edu (team Learning)

Bài này đáng để soi vào bối cảnh team nhỏ của bạn — backend, đang vibe-code Go bằng AI:

- **Guardrails là đòn bẩy lớn nhất.** Muốn agent (và đồng đội mới) chạy nhanh & đúng, hãy đầu tư vào lint, test tự động, CI nhanh trên file thay đổi. Khớp với [[small-steps-feedback|bước nhỏ + feedback loop]].
- **Gom context vào repo.** AGENTS.md / CLAUDE.md, đặc tả, quy ước — để ngay trong repo thay vì rải ở Notion/đầu người. Vừa giúp agent, vừa giúp người mới.
- **Sở hữu phần cốt lõi.** Với Go + AI, cân nhắc tự viết phần lõi thay vì kéo dependency nặng — bạn chịu trách nhiệm cho nó dù ai viết.
- **Vai trò bạn dịch chuyển về phán đoán.** Đúng tinh thần [[tech-lead-lam-chu-vai-tro-tlm|TLM]]: ít gõ phím hơn, nhiều định hướng/review/gu hơn.
