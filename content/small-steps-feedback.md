---
title: '"Bước nhỏ, có chủ đích" — Triết lý feedback-driven development'
lastmod: '2026-05-29 10:40:00'
tags:
  - quy trình phát triển
  - The Pragmatic Programmer
---

Câu này lại đến từ **"The Pragmatic Programmer"** của Thomas & Hunt, nằm trong phần bàn về **Pragmatic Paranoia** (sự hoang tưởng thực dụng) và cách viết code đáng tin cậy. Đây là một trong những lời khuyên có vẻ đơn giản nhưng có chiều sâu đáng ngạc nhiên.

## Phân tích từng phần

Câu này có 3 mệnh đề ngắn, nhưng mỗi cái đều mang một bài học riêng:

**1. "Always take small steps"** — Luôn bước những bước nhỏ
**2. "The rate of feedback is your speed limit"** — Tốc độ nhận phản hồi chính là giới hạn tốc độ của bạn
**3. "Never take on a task that's too big"** — Đừng bao giờ nhận một task quá lớn

## 1. Tại sao phải "bước nhỏ"?

Hãy tưởng tượng hai cách viết code:

**Cách A — Bước lớn:**
Bạn ngồi code liên tục 4 tiếng, viết 500 dòng code, implement 3 chức năng mới, refactor luôn 2 module cũ. Cuối cùng chạy thử → **lỗi**. Lỗi ở đâu? Không biết. Trong 4 tiếng vừa rồi, bạn đã thay đổi rất nhiều thứ, không thể xác định cái nào gây lỗi. Bạn phải **debug toàn bộ**.

**Cách B — Bước nhỏ:**
Bạn viết 10 dòng → chạy thử → ok. Viết 15 dòng nữa → chạy thử → ok. Viết 20 dòng nữa → chạy thử → **lỗi**. Bạn biết ngay lỗi nằm trong 20 dòng vừa viết. Sửa trong 2 phút.

Sự khác biệt: **không gian tìm kiếm lỗi**. Bước càng lớn, không gian càng rộng, debug càng khổ. Bước càng nhỏ, không gian càng hẹp, vấn đề càng dễ cô lập.

## 2. "Rate of feedback is your speed limit" — Ý sâu nhất của câu này

Đây là phần đắt giá nhất. Thomas & Hunt nói: **tốc độ bạn có thể tiến lên = tốc độ bạn nhận được phản hồi từ thực tế**.

### Feedback là gì trong lập trình?

- Compiler báo lỗi syntax → feedback (vài giây)
- Chạy unit test → feedback (vài giây đến vài phút)
- Chạy integration test → feedback (vài phút)
- Deploy lên staging, QA test → feedback (vài giờ)
- Người dùng thật sử dụng → feedback (vài ngày đến vài tuần)
- Khách hàng nhận ra "không phải cái họ muốn" → feedback (vài tháng)

### Vì sao "rate of feedback" lại là "speed limit"?

Tưởng tượng bạn đang lái xe **bịt mắt**, và mỗi 30 giây có người mở băng bịt mắt cho bạn nhìn đường 1 giây. Bạn dám lái nhanh không? Không, vì giữa 2 lần "nhìn", bạn không biết mình đang đi đúng hay sai. Bạn buộc phải đi chậm.

**Lập trình cũng vậy.** Nếu phải mất 1 giờ mới biết code của bạn đúng hay sai (vì test chạy chậm, hoặc vì bạn không test mà cố code "1 phát ăn ngay"), thì cứ mỗi 1 giờ bạn có thể đang đi sai hướng mà không biết. Bạn không thể "code nhanh" hơn được — vì nhanh hơn nghĩa là đâm vào tường mà không biết.

**Ngược lại, nếu feedback siêu nhanh** (compile vài giây, test chạy 5 giây, hot reload tức thì) → bạn có thể tiến với tốc độ rất cao, vì sai là biết ngay, sửa ngay.

### Hệ quả thực tế

Đây là lý do các engineer giỏi **đầu tư rất nhiều vào việc làm cho feedback loop nhanh hơn**:

- Viết unit test → biết lỗi trong vài giây thay vì sau khi deploy
- Hot reload, live preview → thấy kết quả ngay khi gõ
- CI/CD nhanh → biết build có pass không trong 5 phút thay vì 1 tiếng
- Logging tốt, observability tốt → biết hệ thống đang ra sao mà không cần đoán
- Demo cho khách hàng sớm và thường xuyên → biết mình có đang làm đúng cái họ cần không

**Đầu tư vào feedback loop không phải là "phụ trợ" — nó chính là đầu tư vào tốc độ phát triển.** Team có feedback loop tốt có thể tiến nhanh gấp 10 lần team có feedback loop tệ, dù kỹ năng cá nhân ngang nhau.

## 3. "Never take on a task that's too big"

Đây là góc nhìn thứ ba: về **kích thước của task**.

**Task quá lớn** = task mà bạn không thể hoàn thành trong thời gian đủ ngắn để nhận được phản hồi giữa chừng.

Ví dụ:
- ❌ "Build cái dashboard mới" (mất 3 tuần) — quá lớn
- ✅ "Hôm nay: làm xong layout HTML tĩnh của dashboard" — vừa
- ✅ "Tiếp theo: kết nối data thật cho 1 widget" — vừa
- ✅ "Tiếp theo: thêm filter date" — vừa

Tại sao task lớn nguy hiểm? Vì:

**1. Bạn có thể đi sai hướng cả tuần mà không biết.** Đến khi xong, demo cho team/khách thì mới biết mình hiểu sai requirement → mất cả tuần.

**2. Khó ước lượng.** Task lớn = nhiều cái không biết. Bạn nói "3 tuần", thực tế thành 6 tuần. Đây là lý do phần lớn dự án phần mềm trễ deadline.

**3. Tạo áp lực tâm lý.** Một task khổng lồ nhìn vào là thấy nản, dễ trì hoãn (procrastinate). Task nhỏ thì "thôi làm nhanh cho xong" → momentum tốt hơn.

**4. Không thể commit / merge giữa chừng** → blocking người khác, dễ conflict, khó review.

## Cách áp dụng thực tế

**1. Chia task lớn thành các task nhỏ có thể "ship được" trong vài giờ.**
Mỗi task nhỏ phải có **deliverable rõ ràng** (cái gì đó chạy được, test được, demo được). Không phải "viết được nửa hàm".

**2. Commit nhỏ và thường xuyên.**
Một commit = một bước đi. Nếu commit nào cũng chứa 1000 dòng thay đổi → bạn đang bước quá dài.

**3. Test sau mỗi thay đổi nhỏ.**
Đừng viết 100 dòng rồi mới chạy test. Viết 10 dòng → chạy. Đây là nguyên tắc cốt lõi của **TDD (Test-Driven Development)** — biến feedback loop thành thứ tức thì.

**4. Demo sớm, demo thường xuyên.**
Đừng giấu sản phẩm 3 tháng rồi mới cho khách xem. Cho xem mockup sau 1 tuần, prototype sau 2 tuần, version chạy được sau 1 tháng → phản hồi sớm = ít rủi ro.

**5. Khi thấy task "quá lớn" → dừng lại, chia nhỏ trước khi bắt đầu.**
Đây là kỷ luật. Khi nhận một task, câu hỏi đầu tiên không phải "làm thế nào?" mà là *"làm sao chia nó thành các bước nhỏ hơn?"*.

## Kết nối với các slide trước

Để ý chuỗi logic đang được xây dựng:

- **Ousterhout:** Complexity là kẻ thù
- **Software Entropy:** Code mục nát nếu không giữ gìn
- **No one knows what they want:** Requirements luôn mơ hồ
- **The Design Concept:** Cần một concept rõ ràng làm kim chỉ nam
- **Small steps + feedback:** Trong một thế giới mơ hồ và biến động như vậy, **cách duy nhất để tiến lên an toàn là bước nhỏ, kiểm tra liên tục với thực tế, và không bao giờ đặt cược lớn vào một giả định không kiểm chứng**.

## Liên hệ rộng hơn

Triết lý này thực ra không chỉ riêng cho lập trình. Nó là nguyên tắc của:

- **Khoa học:** Thí nghiệm nhỏ, lặp lại, đo lường → tiến bộ
- **Lean Startup:** Build → Measure → Learn cycle thật nhanh
- **OODA loop trong quân sự:** Observe → Orient → Decide → Act — ai vòng nhanh hơn sẽ thắng
- **Học tập:** Học một chút → kiểm tra hiểu chưa → học tiếp (thay vì đọc cả cuốn sách rồi mới làm bài tập)

Tất cả đều dựa trên cùng một insight: **trong một thế giới phức tạp và bất định, ai có vòng lặp feedback ngắn hơn sẽ học nhanh hơn, ít sai lầm hơn, và cuối cùng đi nhanh hơn**.

## Tóm gọn

**Tốc độ thực sự không đến từ việc bước dài, mà đến từ việc bước nhỏ thật nhanh và kiểm tra liên tục.**

Người mới hay nghĩ "code nhanh = viết nhiều code, ít test, không dừng lại". Người có kinh nghiệm hiểu ngược lại: **code nhanh = vòng lặp feedback ngắn**. Bước càng nhỏ, sai càng sớm phát hiện, sửa càng rẻ, tiến càng vững. Đây là một trong những bài học khó dạy nhất, vì nó **phản trực giác** — nhưng cũng là một trong những bài học giá trị nhất khi đã ngấm.

---
## Liên quan
- [[no-one-knows-what-they-want|No one knows what they want]]
- [[tactical-vs-strategic-programming|Tactical vs Strategic Programming]]
