# Quản lý thời gian cho Tech Lead — khi bạn vẫn là dev chính

> Ghi chú cá nhân (không xuất bản). Hoàn cảnh: BE duy nhất, kiêm dẫn dắt ~8 người, dự án 5 năm nhiều nợ kỹ thuật, CEO ép gấp liên tục. Đọc cùng `quan-ly-nguoc-khi-moi-thu-deu-gap.md`.

## Bẫy tư duy phải gỡ trước tiên

Bạn đang đo lường sai. Câu "tôi không đủ thời gian code" giả định rằng **mục tiêu là tối đa hóa giờ code của bạn**. Sai. Với một tech lead, giờ code của *bạn* là tài nguyên đắt nhất và **kém co giãn nhất** — không nên là thứ bạn cố nhồi thêm. Thứ cần tối đa hóa là **năng lực ship của cả team**, mà phần lớn không đến từ tay bạn.

Quản lý thời gian cho TL **không phải** là các mẹo cá nhân (pomodoro, to-do list đẹp). Nó là **kiến trúc lại cách thời gian của bạn tạo ra đòn bẩy**. Có 3 đòn bẩy, theo thứ tự sức mạnh giảm dần:

1. **Delegation** (tạo thời gian bằng cách bớt việc khỏi mình) — mạnh nhất.
2. **Saying no / managing up** (chặn việc không đáng làm ngay từ đầu).
3. **Protecting deep work** (bảo vệ khối thời gian sâu cho phần việc còn lại).

Đa số người mới làm TL nhảy thẳng vào #3 (mẹo năng suất) và bỏ qua #1, #2 — nên không bao giờ thoát quá tải.

## Đòn bẩy 1 — Delegation: nguồn thời gian lớn nhất bạn chưa khai thác

Bạn là BE duy nhất → đây vừa là điểm đau, vừa là nơi có dư địa lớn nhất.

- **+1 BE không phải để "có thêm tay sai vặt"**, mà để *sở hữu* một mảng. Mục tiêu 3 tháng: một service/domain chạy được mà **không cần bạn**. Nếu sau 3 tháng bạn vẫn phải review từng dòng và quyết mọi thứ → bạn đã tuyển một cái cổ chai thứ hai, không phải giải phóng mình.
- **Phép thử "tôi biến mất 1 tuần"**: liệt kê mọi thứ sẽ kẹt nếu bạn nghỉ. Mỗi mục trong danh sách đó là một việc cần được *viết tài liệu* hoặc *pair-chuyển giao*. Đây là to-do list quan trọng nhất của bạn, quan trọng hơn cả sprint backlog.
- **Delegate cả sang FE/QC/BA/PO**, không chỉ BE. Bạn đang dẫn cross-functional team — nhiều việc bạn đang ôm (làm rõ requirement, viết test case, điều phối) có thể đẩy về đúng vai. Bạn không phải là người duy nhất "lo nhiều thứ" — bạn đang *giành* việc của người khác mà không nhận ra.

> Delegation chậm lúc đầu (mất công hướng dẫn) nhưng là khoản đầu tư duy nhất có lãi kép. Ôm việc thì nhanh hôm nay, phá sản thời gian sau 2 tháng.

## Đòn bẩy 2 — Chặn việc từ đầu (xem ghi chú "quản lý ngược")

Thời gian rẻ nhất là thời gian bạn không phải bỏ ra. Mỗi mục tiêu "gấp" bạn đẩy ngược lên cho CEO chọn (X hay Y) là vài ngày code bạn vừa cứu được. Quản lý thời gian và quản lý ngược là **một**, không phải hai việc tách rời.

## Đòn bẩy 3 — Kiến trúc lại tuần làm việc

Sau khi đã delegate và chặn bớt, phần còn lại mới đến lượt sắp xếp:

- **Tách "maker time" và "manager time".** Code/thiết kế cần khối liền 2–4 tiếng không bị cắt; họp/1:1/review/trả lời team là việc bị cắt vụn. Trộn lẫn hai loại = không loại nào ra hồn. Gợi ý cụ thể:
  - **Sáng = maker block** (deep work: code phần khó, thiết kế kiến trúc). Tắt thông báo, không họp.
  - **Chiều = manager block** (1:1, review PR, gỡ vướng cho team, làm việc với PO/BA/business).
- **Gộp các ngắt quãng (batching).** Đừng phản hồi team ngay mỗi lần bị hỏi — hẹn 2–3 cửa sổ cố định/ngày để giải đáp. Việc "luôn sẵn sàng trả lời" là kẻ giết deep work số một của TL.
- **Bảo vệ cứng 20–30% thời gian KHÔNG code** cho việc lead (đã nói ở roadmap). Với bạn, vì đang quá tải, hãy đảo lại tư duy: không phải "code xong dư đâu thì lead", mà "chặn lịch lead trước, code trong phần còn lại".
- **Một "ngày không họp"/tuần** nếu giành được — để xử lý phần kỹ thuật khó cần tập trung sâu.

## Phân loại việc của bạn (làm thử ngay)

Lấy mọi thứ bạn đang ôm, xếp vào 4 ô:

| | Chỉ mình bạn làm được | Người khác làm được |
|---|---|---|
| **Tạo đòn bẩy cao** | Làm (maker block) | **Delegate** |
| **Đòn bẩy thấp** | Tự động hóa / cắt bỏ | **Delegate / chặn** |

Mục tiêu: ô "chỉ mình bạn làm được" phải **co lại theo thời gian** (qua tài liệu hóa + chuyển giao). Nếu nó phình ra, bạn đang đi sai hướng tech lead.

## Tự phản chiếu

1. Trong tuần qua, bao nhiêu % việc tôi làm là thứ *chỉ mình tôi* làm được? Bao nhiêu % lẽ ra delegate được nhưng tôi ôm?
2. Tôi có khối deep work liền mạch nào không, hay cả ngày bị cắt vụn bởi câu hỏi của team?
3. Nếu tôi nghỉ 1 tuần, danh sách "kẹt" dài bao nhiêu? Tháng này tôi rút ngắn được mục nào?

## Hành động tuần này

- Chặn **một khối maker 2 tiếng buổi sáng** vào lịch, lặp lại mỗi ngày. Bất khả xâm phạm.
- Chọn **một việc** trong ô "delegate được nhưng đang ôm" → giao đi (kèm hướng dẫn, chấp nhận nó chậm hơn nếu mình tự làm).
- Bắt đầu danh sách **"tôi biến mất 1 tuần"** — viết ra 5 thứ sẽ kẹt.
