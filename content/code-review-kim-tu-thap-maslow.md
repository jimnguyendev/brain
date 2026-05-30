---
title: 'Kim tự tháp Maslow của code review — review theo đúng thứ tự (Tuần 3 — Ngày 9)'
lastmod: '2026-06-07 02:30:00'
tags:
  - tech lead
  - code review
  - kỹ năng lãnh đạo
---

> Bài mở màn của Tuần 3 trong [[tech-lead-la-gi|lộ trình 4 tuần]]. Tuần 2 ta học cách *cân bằng* code và dẫn dắt; từ đây ta bước vào kỹ năng diễn ra **mỗi ngày** của một TL: **code review & feedback**. Bắt đầu bằng câu hỏi gốc — *khi mở một PR ra, nên nhìn cái gì trước?* Đúc kết từ bài [Maslow's pyramid of code review](http://www.dein.fr/2015-02-18-maslows-pyramid-of-code-review.html) của Sebastien Dein.

Có một sai lầm kinh điển trong review: nhảy thẳng vào *bắt lỗi đặt tên biến* trong khi đoạn code đang **tính tiền nhầm khách hàng**. Dein mượn tháp nhu cầu Maslow để giải thích vì sao: cũng như con người phải no bụng trước khi nghĩ tới lẽ sống, **mỗi tầng review chỉ có ý nghĩa khi tầng dưới nó đã được thoả mãn**. Một dòng code đẹp long lanh nhưng *sai* thì sự đẹp đó vô nghĩa.

Hôm nay ta dựng lại cái tháp đó — như một **thứ tự ưu tiên** để bạn (và đội) review không lạc trọng tâm.

## Năm tầng của tháp

Đọc từ **đáy lên đỉnh**. Tầng càng thấp càng *không thể thoả hiệp*; tầng càng cao càng là "điểm cộng" — nhưng đừng bao giờ đánh đổi tầng dưới để lấy tầng trên.

| # | Tầng | Câu hỏi cốt lõi khi review |
|---|---|---|
| 1 | **Đúng (Correct)** | Code có làm đúng việc cần làm? Có xử lý edge case? Đã test đủ để vẫn đúng khi người khác sửa? Hiệu năng đủ cho ca dùng này? |
| 2 | **An toàn (Secure)** | Có lỗ hổng bảo mật? Dữ liệu lưu an toàn? PII xử lý đúng? Có thể bị DOS? Input validation đã đủ chưa? |
| 3 | **Dễ đọc (Readable)** | Người sau đọc có hiểu? Có làm rõ yêu cầu nghiệp vụ? Tên biến/hàm/class hợp lý? Domain model ánh xạ đời thực, giảm tải nhận thức? Theo quy ước nhất quán? |
| 4 | **Tao nhã (Elegant)** | Có dùng pattern đã được kiểm chứng? Đạt mục tiêu mà vẫn đơn giản, súc tích? Bạn có *thích* làm việc với đoạn code này? |
| 5 | **Vị tha (Altruist)** | PR này có làm codebase **tốt hơn lúc trước**? Có truyền cảm hứng cho người khác cải thiện code họ? Có dọn code chết, sửa tài liệu, refactor nhỏ kéo cả vùng lên? |

Cách dùng tháp trong đầu khi mở một PR:

1. **Khoá ở tầng 1–2 trước.** Đừng để một comment kiểu *"đổi tên biến này nhé"* trôi nổi cùng hạng với *"chỗ này thiếu kiểm tra null nên crash production"*. Nếu tầng "Đúng" hoặc "An toàn" còn vấn đề, đó là thứ duy nhất đáng nói tới — phần còn lại tạm gác.
2. **Tầng 3 là nơi review *sinh lời nhất* về lâu dài** — code được viết cho *con người* đọc. Một codebase dễ đọc rẻ hơn nhiều khi bảo trì.
3. **Tầng 4–5 là khát vọng, không phải rào chắn.** Đừng *chặn* một PR đúng và an toàn chỉ vì nó "chưa thật tao nhã". Hãy gợi ý, đừng gác cổng.

Cái hay của mô hình: nó cho bạn **một ngôn ngữ chung để phân loại comment**. Mỗi nhận xét, tự hỏi *"mình đang ở tầng mấy?"* — và nếu đang ở tầng 4 trong khi tầng 1 còn thủng, hãy quay xuống.

## Liên hệ với team nhỏ của bạn (prepedu)

Bạn là BE dev ở prepedu, code nhiều, trong một team **chỉ 2 BE**. Code review ở quy mô 2 người là một ca *rất đặc biệt* — và cái tháp này càng quý:

- **Bạn vừa là reviewer gần như duy nhất, vừa là người bị review duy nhất.** Không có "đám đông" để pha loãng ý kiến. Nếu mỗi review của bạn đều sa đà vào tầng 3–4 (nitpick style, đặt tên), đồng đội sẽ thấy review là *phiền* và *nhỏ nhặt* — đúng cái bẫy "coi giao tiếp là phiền toái" ở [[tech-lead-tot-tech-lead-te|Ngày 4]]. Hãy cho thấy review **bắt đúng cái quan trọng**: tầng 1–2 trước.
- **Đừng để review thành chỗ phô diễn quyền lực.** Team 2 người, bạn dễ thành người "luôn đúng". Cái tháp giúp bạn tách *"điều này sai/nguy hiểm"* (phải sửa) khỏi *"tôi sẽ làm khác"* (sở thích). Phân biệt này chính là tinh thần coaching ở [[tech-lead-can-bang-code-va-coaching|Ngày 5]] — review để đội **giỏi lên**, không phải để code giống ý bạn.
- **Tận dụng tầng 5 (Vị tha) như đòn bẩy dạy nghề.** Với chỉ 2 người, mỗi PR là một dịp pairing không đồng bộ. Một comment kiểu *"chỗ này nếu tách ra hàm nhỏ sẽ tái dùng được ở module kia"* dạy nhiều hơn mười dòng bắt lỗi style.
- **Cảnh báo riêng cho team 2:** vì ít người, áp lực *merge cho nhanh* rất lớn, dễ bỏ qua cả tầng 1–2. Hãy thống nhất một luật tối thiểu: **không PR nào merge khi tầng "Đúng" và "An toàn" chưa được một người khác xác nhận** — kể cả khi đang gấp.

Nối với hôm qua: ở [[tech-lead-khong-tung-hung-uu-tien|Ngày 8]] ta đóng Tuần 2 bằng việc *ưu tiên có hệ thống*. Cái tháp Maslow này chính là **ưu tiên áp vào từng dòng code** — cùng một tư duy, hạ xuống cấp độ review.

## Tự phản chiếu

1. Lần review gần nhất, tôi dành phần lớn comment cho tầng nào? Nếu là tầng 3–4 trong khi tầng 1–2 chưa chắc, vì sao?
2. Tôi có đang *chặn* PR của đồng đội vì lý do "sở thích" (tầng 4) thay vì "sai/nguy hiểm" (tầng 1–2) không?
3. Nếu đồng đội mô tả phong cách review của tôi bằng một từ, đó sẽ là từ gì — và tôi có muốn nó là từ đó không?

## Hành động nhỏ (15 phút)

Mở PR gần nhất bạn từng review (hoặc tự review lại một PR của chính mình). **Gắn nhãn mỗi comment bằng số tầng (1–5)**. Đếm xem chúng rơi vào đâu. Nếu thấy mình đổ dồn vào tầng cao trong khi tầng 1–2 trống, đó là tín hiệu rõ ràng cần đảo lại thứ tự ưu tiên review từ lần sau.

> *Mẹo:* lần tới khi định gõ một comment review, dừng 2 giây và tự hỏi — *"Đây là tầng mấy? Tầng dưới đã ổn chưa?"*

---

**Ngày mai (Ngày 10)** ta mở rộng cái tháp này ra một bối cảnh khắc nghiệt hơn: **code review trong các nhóm làm việc từ xa** — khi không còn được quay sang bàn bên cạnh hỏi một câu, mọi context phải nằm trọn trong PR.
