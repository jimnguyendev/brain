---
title: '5 sai lầm lớn nhất khi lên Tech Lead — và cách né (Tuần 2 — Ngày 6)'
lastmod: '2026-06-07 01:00:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Tuần 2 / Ngày 6 của [[tech-lead-la-gi|lộ trình 4 tuần]]. Hôm qua ở [[tech-lead-can-bang-code-va-coaching|Ngày 5]] ta học *làm thế nào* để dẫn dắt đúng; hôm nay ta soi mặt trái — **những cú vấp kinh điển khiến một dev giỏi gần như ghét luôn vai trò TL**. Đúc kết từ bài [Techie to Tech Lead: My Five Biggest Mistakes](https://medium.com/featured-insights/techie-to-tech-lead-my-five-biggest-mistakes-fd7f4a2f1808) của Peter Gillard-Moss (ThoughtWorks).

Đây là một bài viết hiếm hoi: tác giả thú nhận rằng sau khi lên TL, hai năm dẫn dắt đã khiến anh **chán ghét vai trò lãnh đạo** và rút lui về "vùng an toàn của công nghệ" suốt nhiều năm. Mãi sau anh mới hiểu gốc rễ, lấy lại tự tin, và giờ là Head of Technology. Điều đáng giá: khi coaching các lead khác, anh thấy 5 sai lầm của mình *không phải của riêng anh* — chúng phổ biến đến mức gần như là nghi thức nhập môn của mọi dân kỹ thuật lên dẫn dắt.

Dưới đây là 5 cái bẫy, distilled thành dạng dễ soi.

## 1. Đánh đồng "giỏi kỹ thuật" với "có quyền lãnh đạo"

Năng lực kỹ thuật là lý do *dễ thấy nhất* để chọn ai đó làm lead — nên ta dễ nghĩ nó là lý do *duy nhất*. Tác giả tuyển một bạn graduate, vài tháng sau nhận ra bạn ấy giỏi kỹ thuật hơn mình. Đáng lẽ là một cộng sự (thậm chí người kế nhiệm), anh lại xem bạn ấy như **mối đe doạ**, sinh ganh đua và mất lòng tin — phá hỏng một quan hệ làm việc vốn rất tốt.

Cái bẫy này gây hại theo hai chiều ngược nhau:

- **Người tự cao** → hành vi ganh đua, sợ bị "soán ngôi", giấu việc.
- **Người khiêm tốn** → trầm trọng thêm `imposter syndrome` (hội chứng kẻ mạo danh): thấy đồng đội xứng đáng hơn mình, do dự, né ra quyết định.

> Bài học: chức danh lead **không** đến từ việc bạn là người code khỏe nhất phòng. Đây chính là ngộ nhận "TL = người code nhiều nhất" đã mổ xẻ từ [[tech-lead-la-gi|Ngày 1]]. Buông nó ra, bạn mới dám tin tưởng người giỏi hơn mình ở một mảng.

## 2. Đào sâu (depth) thay vì mở rộng (breadth)

Vai trò lead đầu tiên, một dự án greenfield, tác giả hào hứng nhồi vào đủ thứ công nghệ mới: unit testing, ORM, CI, pairing... Nhưng đó chỉ là việc của "iteration 0". Phần *thường ngày* mới khó: làm việc với stakeholder, đánh giá hiệu suất, tuyển dụng, ngân sách, đại diện đội trong các cuộc họp.

Vì khó và lạ, anh **né những việc đó và lao sâu hơn vào công nghệ** — thứ duy nhất anh thấy mình kiểm soát được. Càng né, `imposter syndrome` càng nặng khi ngồi cạnh các quản lý nói trôi chảy về phát triển con người và chiến lược.

Vì sao cái bẫy này dính chặt? Vì kỹ năng kỹ thuật có **lộ trình học rõ ràng**, còn kỹ năng lãnh đạo thì không:

| Kỹ năng kỹ thuật | Kỹ năng lãnh đạo |
|---|---|
| Có "Hello World" để bắt đầu | Không có "Hello World" cho coaching, thuyết phục, quản lý thời gian |
| Biết blog/sách/hội nghị/người để theo dõi | Không biết "theo ai trên Twitter" để học cách truyền đạt quyết định |
| Giá trị thấy ngay, tiếp thu nhanh | Giá trị mờ, dấn thân tốn kém, dễ thấy lạc lối |

> Bài học: hiểu rằng vai trò đòi hỏi **chiều rộng** — gây ảnh hưởng, coaching, tư duy chiến lược — và *cố tình* đầu tư vào chúng dù khó chịu, thay vì rút về thế mạnh cũ cho nhẹ đầu.

## 3. Vẫn tưởng mình là một "producer"

Vài tháng vào vai trò, tác giả thấy mình làm cả đống việc mà "chẳng năng suất": họp, email, trả lời stakeholder. Story mang tên anh không nhúc nhích. Anh **hy sinh thời gian cá nhân để bù giờ code** và nhanh chóng kiệt sức.

Gốc rễ: trong một delivery team, có hai loại hoạt động — *trực tiếp tạo giá trị* (viết code) và *tối đa hoá tác động của giá trị đó* (dọn vật cản cho người khác). Khi lên TL, bạn dịch chuyển từ nhóm thứ nhất sang nhóm thứ hai. Nhưng nếu vẫn tự đo mình bằng "hôm nay tôi code được bao nhiêu", bạn sẽ:

- bực bội vì "quá nhiều họp", đòi giữ "giờ vàng" để code;
- cực đoan hơn: cự tuyệt mọi việc "phi kỹ thuật" như nói chuyện với stakeholder;
- tự xem mình là người **không thể thay thế** — nguy hiểm nhất ở đội nhỏ có khoảng cách kỹ năng lớn giữa lead và phần còn lại.

> Bài học: thước đo thành công của bạn giờ là **năng suất của cả team**, không phải dòng code của riêng bạn. Đây đúng là cú "force multiplier" của [[tech-lead-can-bang-code-va-coaching|Ngày 5]] — và là ranh giới *giao tiếp là phần việc chính* trong tấm gương [[tech-lead-tot-tech-lead-te|Ngày 4]].

## 4. Cố kiểm soát mọi thứ

Hai câu chuyện cùng một lỗi. (a) Bị hỏi về một con bug ở mảng chưa từng đụng, vì sợ lộ ra mình không biết, anh **đoán bừa một câu nghe có cơ sở** — các đội khác tin theo, sửa cả đống thứ, rồi phát hiện anh sai. (b) Anh chúi mũi pairing mấy ngày để "nắn" một đoạn code procedural thành OOP, trong khi bỏ lỡ một thay đổi *kiến trúc lớn* đang gây bug.

Phản hồi của sếp: bạn cần **biết chọn trận mà đánh**.

- Nói *"Tôi không biết, để tôi kiểm tra lại với đội"* thì **ổn** — vô tình lan truyền thông tin sai mới có hại.
- Một chút code procedural chưa hoàn hảo thì **ổn** — một thay đổi kiến trúc lớn không có ai giám sát thì **không**.
- `mentoring` và `code review` theo nhóm cải thiện code base lâu dài hiệu quả hơn nhiều so với việc tự tay vá từng vấn đề nhỏ.

> Bài học: bạn *không thể* tham gia mọi việc — đó là bất khả thi với con người. Tin tưởng giao trách nhiệm, và dành sự chú ý cho thứ thật sự quan trọng.

## 5. Bỏ lỡ các tín hiệu

Anh dự họp, đề xuất cải tiến, nhưng *chẳng có gì thay đổi*: thử cho QA làm cùng dev một lần rồi quay về cũ; ai cũng gật "dev nên làm chủ database" rồi vẫn chờ DBA; coaching TDD được một iteration thì cả đội bỏ. Cảm giác như một "cái chợ nói suông".

Lý do: khi code là từng phút trong ngày, bạn nhạy với những **feedback loop kỹ thuật** đã được dựng sẵn — build xanh, story lên production (endorphin); build vỡ, story kẹt (cortisol). Nhưng khi lên lãnh đạo, **tín hiệu đến từ con người**, và chúng tinh vi hơn nhiều:

- ai đang *thực sự* tin ý tưởng của bạn, ai chỉ gật cho qua;
- ai đang quá tải và cần hỗ trợ;
- chỗ nào trong cấu trúc giao tiếp đang rò khiến cả đội không rõ đích đến.

> Bài học: những tín hiệu này gần như một *giác quan thứ sáu* — khi chưa nhạy, bạn thậm chí không biết chúng tồn tại. Nhưng chúng **học được**, không phải ma thuật. Bắt đầu bằng cách: sau mỗi cuộc họp, tự hỏi "người ta thực sự nghĩ gì, có gì khác lời họ nói không?".

## Sợi chỉ đỏ: 5 sai lầm này nuôi nhau

Tác giả nhấn mạnh chúng **đan xen**: khó ngừng xem mình là producer (sai lầm 3) khi bạn tin năng lực kỹ thuật là lý do mình được lãnh đạo (sai lầm 1); điều đó lại khiến phát triển kỹ năng khác (sai lầm 2) càng khó. Cách chúng nuôi nhau chính là "vòng xoáy tử thần" đã đẩy anh rời bỏ vai trò.

Và một an ủi quan trọng: **hành trình lãnh đạo không tuyến tính.** Nhận vai lead rồi quay lại thuần kỹ thuật là chuyện bình thường — nó chỉ khiến bạn thành một dev giỏi hơn.

## Liên hệ với team nhỏ của bạn (prepedu)

Là BE dev ở prepedu, code nhiều, team 2 người, ba sai lầm này *đặc biệt* rình bạn:

- **Sai lầm 3 (vẫn là producer)** — nguy hiểm nhất với team nhỏ có khoảng cách kỹ năng. Khi bạn là người biết nhiều nhất trong 2 người, rất dễ tin "mình mà dừng code thì cả team đứng". Nhưng đó chính là "điểm nghẽn / single point of failure" ở [[tech-lead-vai-tro-hay-bay|Ngày 2]]. Hãy đo mình bằng sản lượng của *cả hai*, không phải mình bạn.
- **Sai lầm 4 (kiểm soát mọi thứ)** — với chỉ 1 đồng đội, bạn dễ review/sửa từng dòng cho "chuẩn". Hãy chọn trận: chấp nhận code chưa hoàn hảo ở chỗ nhỏ, dồn sự giám sát vào thay đổi lớn — và dùng pairing/review như công cụ *nâng người*, không phải để nắn từng commit.
- **Sai lầm 2 (chỉ đào sâu kỹ thuật)** — ở startup edtech, việc "phi kỹ thuật" (nói với PM, ước lượng, giải thích trade-off) chính là nơi bạn tạo khác biệt. Đừng trốn vào refactor cho dễ thở.

Một câu nối cả tuần: tất cả những cú vấp này đều là **rút về thế mạnh cũ khi thấy sợ**. Cách chữa không phải code nhiều hơn, mà là *cố ý* bước vào vùng khó — đúng tinh thần "force multiplier" của [[tech-lead-can-bang-code-va-coaching|Ngày 5]].

## Tự phản chiếu

1. Có lần nào tuần qua tôi **đoán bừa** một câu chỉ vì sợ lộ ra "mình không biết" — thay vì nói thẳng "để tôi kiểm tra lại với đội"?
2. Tôi đang đo thành công của mình bằng *dòng code của tôi* hay bằng *sản lượng của cả team*?
3. Khi đồng đội gật đầu trong cuộc họp gần nhất — họ thật sự tin, hay chỉ đang cho qua mà tôi không đọc ra tín hiệu?

## Hành động nhỏ (15 phút)

Lấy một việc *phi kỹ thuật* bạn đang âm thầm né (vd: làm rõ trade-off với PM, ước lượng giúp đồng đội, viết một dòng kỳ vọng cho team). Đặt nó vào lịch tuần này như một việc *thật* — và khi làm, **đừng** mở editor ra code song song. Đó là bài tập "mở rộng chiều rộng" cụ thể nhất, trực diện với sai lầm 2.

> *Mẹo:* lần tới bị hỏi điều bạn không chắc, thử câu thần chú — *"Tôi không biết, để tôi kiểm tra lại với đội."* Nó mạnh hơn một phỏng đoán sai rất nhiều.

---

**Ngày mai (Ngày 7)** ta thu hẹp ống kính: [3 sai lầm phổ biến của Tech Lead lần đầu](https://www.theengineeringmanager.com/growth/three-common-mistakes-of-the-first-time-tech-lead/) — những cú vấp *đầu tiên* gần như TL mới nào cũng dính trong vài tuần đầu, để bạn nhận ra và sửa trước khi nó thành thói quen.
