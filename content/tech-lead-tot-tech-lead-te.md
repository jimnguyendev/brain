---
title: 'Tech Lead tốt, Tech Lead tệ — tấm gương soi cuối tuần 1 (Tuần 1 — Ngày 4)'
lastmod: '2026-06-06 09:30:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Bài cuối của Tuần 1 trong [[tech-lead-la-gi|lộ trình 4 tuần]]. Hôm nay ta biến mọi lý thuyết ba ngày qua thành một **tấm gương soi**: ở mỗi tình huống, TL giỏi làm gì và TL tệ làm gì? Đúc kết từ bài kinh điển [Good Tech Lead, Bad Tech Lead](https://medium.com/swlh/good-tech-lead-bad-tech-lead-948b2b806d86).

Ba ngày qua ta đi từ định nghĩa ([[tech-lead-la-gi|Ngày 1]]), tới góc phản biện ([[tech-lead-vai-tro-hay-bay|Ngày 2]]), rồi chọn trục phát triển ([[tech-lead-hay-engineering-manager|Ngày 3]]). Tất cả vẫn còn ở mức "hiểu". Hôm nay ta hạ nó xuống mức "soi": cùng một tình huống, hai kiểu TL hành xử ngược nhau hoàn toàn. Đọc xong, bạn sẽ có một **checklist tự chấm điểm** — đúng đầu việc tổng kết của Tuần 1.

## 9 tấm gương: giỏi vs. tệ

Mỗi dòng là một tình huống thật bạn sẽ gặp. Hãy đọc và tự hỏi: *"Mình đang ngả về cột nào?"*

| Khía cạnh | ✅ Tech Lead giỏi | ❌ Tech Lead tệ |
|---|---|---|
| **Đồng đội** | Nhận việc cực nhọc, dọn vật cản cho team chạy 100%, lan toả kiến thức ra nhiều người | Giành việc hào nhoáng để nhận công, gom kiến thức vào đầu mình |
| **Tầm nhìn kỹ thuật** | Có bức tranh tổng thể & truyền đạt rõ; uỷ thác mảng tính năng và để người khác tự chủ | Áp đặt quyết định, né giải thích, giữ "bản đồ" trong đầu |
| **Tranh luận** | Lắng nghe, đưa ra *khung* để chốt khi bế tắc, sẵn sàng bị thuyết phục | Để cãi vô tận, hoặc cắt sớm "chốt rồi"; coi thắng cãi hơn quyết định đúng |
| **Quản lý dự án** | Chủ động: estimate cùng team, đặt cột mốc, lường rủi ro trước | Bị động: giao việc rồi thả, hy vọng cuối cùng tự khớp, test e2e sát ngày ra mắt |
| **Thực dụng** | Cân giữa *làm đúng* và *làm xong*; cắt góc có chủ đích, không vì lười | Chọn lối tắt lợi ngắn hại dài, để nợ kỹ thuật chất chồng |
| **Giao tiếp** | Coi giao tiếp là phần việc chính; hy sinh năng suất cá nhân cho năng suất team | Tin "code mới là làm việc"; xem giao tiếp & dẫn dắt là phiền toái |
| **Với Product** | Đối thoại với PM/designer, phản biện *kèm* giải pháp thay thế | Ném quyết định "qua bức tường", phản biện suông không giải pháp |
| **Thích ứng** | Bình tĩnh khi spec đổi, thiết kế code đón được thay đổi | Bực khi spec đổi, hoặc tổng quát hoá quá sớm chỗ không cần |
| **Tính cách** | Điềm đạm, quyết đoán, khiêm tốn, nâng đỡ team, luôn cải thiện | Hung hăng, phòng thủ khi nhận feedback, nghĩ chức danh tự mang lại uy quyền |

## Sợi chỉ đỏ xuyên suốt cả tuần

Để ý: cột "giỏi" của hôm nay chính là tổng hợp ba ngày trước.

- **"Lan toả kiến thức, không gom vào đầu mình"** ↔ chính là chống "nút thắt cổ chai" ở [[tech-lead-vai-tro-hay-bay|Ngày 2]] — TL giỏi làm team *bớt* phụ thuộc vào mình.
- **"Coi giao tiếp là phần việc chính, hy sinh năng suất cá nhân"** ↔ chính là rời khỏi ngộ nhận "TL = người code nhiều nhất" ở [[tech-lead-la-gi|Ngày 1]].
- **"Đối thoại với PM, hiểu trade-off sản phẩm"** ↔ chính là ranh giới *How / What / Who* ở [[tech-lead-la-gi|Ngày 1]] và sự nhoè vai ở [[tech-lead-hay-engineering-manager|Ngày 3]].

Một câu tóm cả bài: **TL giỏi tối ưu cho năng suất của cả team; TL tệ tối ưu cho cái tiện nhất với bản thân.** Mọi dòng trong bảng trên đều là biến thể của đúng câu này.

## Liên hệ với team nhỏ của bạn (prepedu)

Với team 2 BE vừa code vừa dẫn, vài cái bẫy trong bảng *đặc biệt* dễ sa vào:

- **"Giành việc hào nhoáng"** → ở team nhỏ rất dễ tự ôm hết phần khó/vui vì "mình làm nhanh hơn". Đó chính là cách giết cơ hội trưởng thành của đồng đội. Hãy *cố tình* nhường một task ngon.
- **"Gom kiến thức vào đầu"** → khi chỉ 2 người, bạn là kho tri thức sống. Hãy biến nó thành tài liệu/pairing — nối thẳng với danh sách "điểm nghẽn" bạn đã liệt kê ở [[tech-lead-vai-tro-hay-bay|Ngày 2]].
- **"Coi giao tiếp là phiền toái"** → cái bẫy lớn nhất của một dev quen code sâu. Communication overhead không phải lãng phí; nó là *công việc* của TL.

## Checklist tự chấm điểm cuối Tuần 1

Đây là đầu ra cụ thể của tuần. Với mỗi dòng dưới đây, tự cho điểm **1–5** (1 = đang ở cột "tệ", 5 = vững ở cột "giỏi"):

- [ ] Tôi lan toả kiến thức ra team thay vì giữ trong đầu — **__/5**
- [ ] Tôi truyền đạt được định hướng kỹ thuật, không áp đặt — **__/5**
- [ ] Tôi đưa ra khung để chốt tranh luận, sẵn sàng bị thuyết phục — **__/5**
- [ ] Tôi chủ động đặt cột mốc & lường rủi ro, không "thả rồi mong" — **__/5**
- [ ] Tôi cân được "làm đúng" và "làm xong", không để nợ kỹ thuật trôi — **__/5**
- [ ] Tôi coi giao tiếp/dẫn dắt là phần việc chính, không phải xao nhãng — **__/5**
- [ ] Tôi đối thoại & phản biện với Product *kèm* giải pháp — **__/5**
- [ ] Tôi bình tĩnh khi yêu cầu thay đổi — **__/5**
- [ ] Tôi khiêm tốn, không phòng thủ khi nhận feedback — **__/5**

Khoanh tròn **2 dòng điểm thấp nhất** — đó là trọng tâm luyện tập của các tuần tới.

## Tự phản chiếu

1. Trong 9 khía cạnh trên, đâu là khía cạnh tôi *tưởng mình giỏi* nhưng thật ra đang ở cột "tệ"?
2. Có hành vi "TL tệ" nào tôi đang vô tình làm chỉ vì nó *tiện cho tôi* (vd: tự code cho nhanh thay vì hướng dẫn)?
3. Nếu nhờ đồng đội chấm tôi theo bảng này, điểm họ cho có khớp với tôi tự chấm không?

## Hành động nhỏ — đóng Tuần 1 (15 phút)

Gộp lại thành **1 trang "TL ở prepedu nên làm gì"** (đầu việc thực hành của tuần): viết 5 dòng, mỗi dòng bắt đầu bằng một động từ, lấy thẳng từ 2 khía cạnh điểm thấp nhất của bạn. Mang trang này vào buổi khớp kỳ vọng với sếp.

> *Ví dụ một dòng:* "Mỗi sprint, chủ động giao 1 task quan trọng cho dev còn lại và pair 30 phút thay vì tự làm."

---

**Hết Tuần 1.** Bạn đã: hiểu vai trò, thấy mặt trái của chức danh, chọn được trục phát triển, và có checklist tự soi. **Tuần 2** ta bước vào bài toán khó nhất của TL mới: **cân bằng giữa code và coaching** — làm sao vừa giữ tay nghề vừa không thành nút thắt.
