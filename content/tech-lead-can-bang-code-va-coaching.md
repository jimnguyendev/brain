---
title: 'Force multiplier: cân bằng giữa code và coaching (Tuần 2 — Ngày 5)'
lastmod: '2026-06-07 00:30:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Bài mở màn của Tuần 2 trong [[tech-lead-la-gi|lộ trình 4 tuần]]. Tuần 1 ta đã *hiểu* vai trò; từ đây ta bước vào bài toán khó nhất của mọi TL mới: **vừa giữ tay code, vừa dẫn dắt người khác mà không thành nút thắt**. Đúc kết từ bài [Becoming a Tech Lead: Balancing Coding with Coaching](https://medium.com/@HubSpotDev/becoming-a-tech-lead-how-i-ve-balanced-coding-with-coaching-2af82c154488) của Skyler Whorton (HubSpot).

Câu than phiền phổ biến nhất của TL mới là: *"Tôi không còn thời gian để code nữa."* Nghe quen không? Nó đến từ một hiểu lầm tinh vi: ôm `servant leadership` (lãnh đạo phụng sự) quá chặt, mặc định mỗi câu hỏi của đội là việc của riêng mình phải đi tìm lời giải. Càng tận tâm kiểu đó, bạn càng chìm — và nghịch lý là đội cũng *không* lớn lên.

Lời giải nằm ở một câu thần chú duy nhất, xuyên suốt cả bài hôm nay:

> **Hãy trở thành một _force multiplier_ — người nhân bội sức mạnh của người khác — thay vì một người làm-nhiều-nhất.**

Force multiplier nghĩa là: tìm cách làm cho mỗi đồng đội hiệu quả hơn đáng kể, để công sức đó sinh lời theo cấp số nhân theo thời gian. Bạn bỏ ra 30 phút dạy một kỹ năng, đội dùng nó cả trăm lần về sau. Đó là phép nhân; còn tự code hết là phép cộng. Dưới đây là 3 cách cụ thể để chuyển từ cộng sang nhân.

## 1. Dạy đội câu cá — làm bản đồ, đừng làm tài xế

Khi mới lên TL, Whorton tiếp cận mọi câu hỏi như thể *trả lời hộ* là trách nhiệm của mình. Sai lầm: việc đó ngốn sạch thời gian, và giữ quyền sở hữu vấn đề ở sai chỗ.

Cách đúng: **làm tấm bản đồ đường phố, đừng làm tài xế riêng.** Khi ai đó hỏi, thay vì đưa đáp án, hãy:

- Thẳng thắn thừa nhận "mình cũng chưa biết ngay" (thường là vậy thật).
- Mô tả *các bước tiếp theo* bạn sẽ làm để tìm ra, hoặc chỉ ai trong tổ chức biết.
- Kết nối hai người với nhau, hoặc dạy nhanh một công cụ tại chỗ.

Phép nhân ở đây: người hỏi (1) học cách tự dùng công cụ — log, metrics, debugging — để tự trả lời lần sau; (2) biết chỗ tra cứu nguồn — code search, wiki, tài liệu; (3) mở rộng quan hệ trong công ty. Giữ **quyền sở hữu vấn đề ở người đặt câu hỏi** chính là cách đội tích luỹ kỹ năng mà bạn không có — và là biến thể trực tiếp của "lan toả kiến thức thay vì gom vào đầu mình" từ [[tech-lead-tot-tech-lead-te|Ngày 4]].

## 2. Quên vai trò thần Atlas — đừng tự gánh hết "bầu trời"

Atlas bị kết án phải đỡ cả Trái Đất tách khỏi bầu trời. Nhiều TL tự nhận vai đó: che chắn cho đội khỏi mọi việc *ngắt quãng* — support issue, sự cố độ tin cậy, yêu cầu gấp từ đội khác — để đội có "vùng yên tĩnh" mà tập trung vào tính năng lớn.

Nghe rất cao thượng. Nhưng đó là cái bẫy: tự ôm hết việc lặt vặt biến thành **trò đuổi bắt bất tận**, và bạn chẳng còn giờ cho dự án của chính mình, tư duy chiến lược, hay mentor ai cả. Tệ hơn: nếu kỹ sư *không bao giờ* được yêu cầu làm chủ việc của họ, chuyển ngữ cảnh, hay xử lý thứ ngoài vùng an toàn — họ sẽ không bao giờ trưởng thành.

Cách Whorton cân bằng:

- **Khớp mỗi việc phát sinh với kỹ năng từng người.** Bug nằm trong code họ từng viết → giao cho họ, context switch dễ hơn nhiều.
- **Thỉnh thoảng giao một issue lạ** cho người chưa quen — như một cơ hội mở rộng năng lực.
- **Hỏi trước khi gán**, đừng ném thẳng: *"Này, bạn có 1–2 ngày tới xem được support issue này không?"* — mở một cuộc thảo luận minh bạch về ưu tiên thay vì một mệnh lệnh.

Nguyên tắc cốt lõi: **giữ "nỗi đau bảo trì" gắn với người tạo ra thay đổi.** Ai viết code nấy chịu trách nhiệm hệ quả — điều này khiến cả đội code cẩn thận hơn, và hiểu sâu hệ thống hơn là vá bug kiểu "ghé qua". Đóng vai Atlas, về dài, là gánh nặng không đáng mang. Tốt hơn nhiều là chia nó cho cả đội.

## 3. Chia sẻ "viên đá cưng" — đừng giấu bài toán hay

Là kỹ sư, ta nghiện giải đố. Rất cám dỗ khi *giành* lấy một bài toán thú vị rồi âm thầm nghĩ cách giải. Thoả mãn về trí tuệ thật, nhưng đó không phải cách hoàn thành việc tốt và nhanh.

Câu chuyện của Whorton: dự án Java build ngày càng chậm, anh không có thời gian xử lý nên chỉ **ghi lại toàn bộ chi tiết vào một issue GitHub công khai** rồi quay lại việc khác. Hai tuần sau, một kỹ sư trong đội tự để ý, lặng lẽ debug mà chẳng ai nhắc, và **cắt trọn 10 phút khỏi thời gian build** cho cả đội. Nếu anh cứ ôm khư khư hiểu biết của mình, chuyện đó đã không xảy ra — hoặc xảy ra muộn hơn nhiều.

Bài học: **làm việc ngoài ánh sáng.** Ghi lại các bài toán giá trị ở nơi cả đội thấy (issue, board, bản tin quý ngắn về "các dự án lớn & vì sao ta quan tâm"). Khi đến lúc giao một việc mới, bạn sẽ thấy nó *đã quen thuộc* với người nhận, đôi khi họ còn sẵn ý tưởng. Chia sẻ cởi mở nâng "mức độ sẵn sàng chung" của cả đội — và bạn chẳng mất gì cả.

## Liên hệ với team nhỏ của bạn (prepedu)

Với team 2 BE vừa code vừa dẫn, ba cái bẫy này *đặc biệt* sắc:

- **Bẫy "tài xế":** team nhỏ, bạn là người biết nhiều nhất, nên trả lời hộ luôn cho nhanh. Nhưng chỉ có 1 đồng đội — nếu họ không tự câu cá được, bạn vĩnh viễn là single point of failure. Đây chính là "điểm nghẽn" bạn đã liệt kê ở [[tech-lead-vai-tro-hay-bay|Ngày 2]].
- **Bẫy Atlas:** rất dễ tự nhận hết mọi support/incident để "đồng đội yên tâm code". Ở team 2 người, làm vậy nghĩa là bạn *không bao giờ* có khối thời gian sâu cho việc của mình, và đồng đội mãi không học cách vận hành production.
- **Bẫy "viên đá cưng":** task khó/vui chỉ có 2 người tranh, bạn dễ tự ôm vì "mình làm nhanh hơn" — đúng cái bẫy "giành việc hào nhoáng" ở [[tech-lead-tot-tech-lead-te|Ngày 4]]. Hãy *cố tình* ghi nó ra và nhường.

Một câu nối cả tuần lại: lời than "không còn giờ code" không giải bằng cách *code thêm giờ*, mà bằng cách **đầu tư sớm vào tính tự chủ, quyền sở hữu và giao tiếp của đội** — để sau này bạn tự nhiên có lại nhiều giờ code hơn.

## Tự phản chiếu

1. Tuần qua tôi đã *trả lời hộ* câu hỏi nào mà lẽ ra nên chỉ đường để họ tự giải?
2. Có việc ngắt quãng nào tôi đang tự ôm chỉ vì "che chắn cho đội" — nhưng thật ra đang giữ họ ngoài vùng trưởng thành?
3. Tôi có "viên đá cưng" nào đang giữ riêng trong đầu mà chưa ghi ra nơi cả đội thấy không?

## Hành động nhỏ (15 phút)

Mở backlog/issue của bạn, chọn **1 bài toán thú vị bạn đang âm thầm muốn tự làm**. Viết nó ra thành một issue công khai *đủ chi tiết để người khác bắt tay vào* (bối cảnh + manh mối + vì sao đáng làm), rồi nhắc nó trong standup thay vì gán cho mình. Đó là bài tập "force multiplier" cụ thể nhất.

> *Mẹo:* lần tới khi đồng đội hỏi bạn một câu, thử dừng 3 giây và tự hỏi — *"Mình đang làm tài xế hay làm bản đồ?"*

---

**Ngày mai (Ngày 6)** ta soi mặt trái: [5 sai lầm lớn nhất khi lên Tech Lead](https://www.theengineeringmanager.com/growth/techie-to-tech-lead-my-five-biggest-mistakes/) — những cú vấp kinh điển mà gần như TL mới nào cũng dính, để bạn né trước khi sa vào.
