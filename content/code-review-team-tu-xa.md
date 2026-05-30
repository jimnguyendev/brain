---
title: 'Code review từ xa: viết review như viết một lá thư (Tuần 3 — Ngày 10)'
lastmod: '2026-06-07 03:00:00'
tags:
  - tech lead
  - code review
  - kỹ năng lãnh đạo
---

> Ngày 10 — bài thứ hai của Tuần 3 ("Code review & feedback") trong [[tech-lead-la-gi|lộ trình 4 tuần]]. Hôm qua ở [[code-review-kim-tu-thap-maslow|Ngày 9]] ta xếp các tầng giá trị của review thành một kim tự tháp. Hôm nay ta zoom vào một bối cảnh rất giống team bạn: **review hoàn toàn qua văn bản, bất đồng bộ, không nhìn mặt nhau**. Đúc kết từ [Code Review in Remote Teams](https://web.hypothes.is/blog/code-review-in-remote-teams/) của Sean Hammond (Hypothesis).

Ở team từ xa, một bình luận review không kèm giọng nói, không kèm nét mặt, không kèm cái cười xoa dịu. Người nhận chỉ có **chữ trên màn hình** — và họ sẽ tự lấp đầy phần cảm xúc còn thiếu, thường là theo hướng tệ nhất. Một câu cụt lủn "cái này sai" qua GitHub nặng hơn nhiều so với chính câu đó nói trực tiếp. Đó là lý do review async đòi hỏi một sự cẩn trọng mà review tại bàn không cần tới.

Luận điểm gốc của Hammond, cũng là sợi chỉ xuyên cả bài: **code review không chỉ để bắt bug — nó để cải thiện cả chất lượng code _lẫn_ tinh thần (morale) của team.** Review là một trong những lần hiếm hoi các dev "chạm" nhau mỗi ngày; nếu lần chạm đó khó chịu, văn hóa team sa sút theo.

## Mục tiêu thật sự của review (đừng quên cái thứ hai)

Trước khi bàn nên/không nên, hãy nhớ review phục vụ nhiều mục tiêu — chất lượng code chỉ là *một* trong số đó:

- **Vun văn hóa team** — review là nơi văn hóa lộ ra rõ nhất.
- **Phá "code silo"** — mọi người review chéo để cùng quen toàn bộ codebase.
- **Mentor & học hỏi** — nhưng lưu ý: lúc code đã viết xong *không* phải thời điểm tốt nhất để mentor. Việc đó nên xảy ra **trước và trong** lúc viết code.
- **Chất lượng code** — bug, khả năng bảo trì, kiến trúc, tài liệu.

Giữ tầm nhìn này thì mọi lời khuyên dưới đây mới có chỗ neo.

## Giao tiếp async: chữ viết phải gánh hết

Review trực diện và tối thiểu — chỉ ra chỗ sai, nói muốn đổi gì, hết — là công thức độc hại nhất. Với kiểu đó, kết quả *tốt nhất* tác giả mong là không có bình luận nào: "LGTM, merged". Hammond ví nó như một bản review mang tên *"để xem người ta nghĩ bạn dở đến mức nào"*.

Vì async không có cơ hội nói lại ngay, chữ viết phải làm tốt mấy việc cùng lúc:

- **Mở bằng một câu tóm tắt tích cực ở đầu** — thể hiện bạn vui và biết ơn vì đoạn code, *trước khi* vào chi tiết. Tính năng review của GitHub cho gom nhiều bình luận theo dòng rồi đăng một lượt kèm phần tóm tắt — dùng đúng nó.
- **Khen cụ thể, nói rõ _tại sao_ thích** — tránh khen sáo, tránh "sandwich kẹp chê", và tuyệt đối tránh **lời khen mỉa mai** kiểu "Làm tốt lắm, nhưng…".
- **Để lại "dòng độc thoại" khi đọc code** — "Ok mình hiểu đoạn này rồi, nó nối với cái kia…". Việc thấy người khác *thật sự đọc hiểu* code mình đã là một dạng công nhận.

## Sự rõ ràng bằng văn bản: hỏi, đừng khẳng định

Nguyên tắc lớn nhất để chữ viết không hóa thành đòn tấn công: **đặt câu hỏi thay vì ra phán quyết.** Một câu khẳng định mang tính buộc tội; một câu hỏi là đi tìm thông tin.

| Đừng (khẳng định) | Nên (hỏi) |
|---|---|
| "Bạn không tuân chuẩn ở đây." | "Lý do đằng sau cách tiếp cận này là gì?" |
| "Cái này sai, dùng B đi." | "Bạn nghĩ sao về việc dùng A thay vì B?" |
| "Đoạn này khó hiểu." | "Mình chưa hiểu đoạn này, giải thích giúp được không?" |
| "Bạn quên khởi tạo biến." | "Mình không thấy chỗ các biến này được khởi tạo." |

Lý tưởng nhất: nếu có bug, *chính tác giả* phát hiện ra khi trả lời câu hỏi của bạn — "Ồ mình chưa nghĩ tới, để mình sửa". Để họ tự tìm ra và tự đề xuất là một sự **trao quyền**, tốt hơn rất nhiều so với ra lệnh sửa. Thêm hai thói quen khiêm tốn: **nêu lý do** khi gợi ý, và **dùng ví dụ từ chính mình** — "Mình từng học cái này theo cách khó khăn…".

## Tone trong văn bản: né những cú trượt vô tình

Vì không có giọng nói đỡ lời, vài thói quen ngôn ngữ trở nên nguy hiểm hơn hẳn khi viết:

- **Đừng dùng giọng cá nhân:** "Tại sao bạn lại…?" nghe như công kích. Câu hỏi "tại sao" mang tính buộc tội — đổi thành "Lý do đằng sau việc… là gì?".
- **Đừng cường điệu:** bỏ "luôn luôn", "không bao giờ", "chẳng có gì" khỏi lời chê.
- **Đừng ngôn ngữ xúc phạm:** né "ngớ ngẩn", "ngu ngốc" — kể cả khi không có ý.
- **Đừng passive-aggressive:** "Như tôi đã nói rồi đấy…", "Lại một lần nữa…" — toát ra sự bực bội.
- **Đừng dồn hội đồng (pile on):** nhiều người cùng +1 một bình luận chê khiến tác giả thấy bị "đánh hội đồng".
- **Đừng làm "tài xế ghế sau":** đừng ép tác giả viết lại theo cách *bạn* sẽ viết. Nhiều thứ chỉ là khác quan điểm — với mỗi gợi ý, tự hỏi "đây có phải chỉ là khẩu vị của mình không?".

Và một sự giải thoát: **không bắt buộc phải tìm ra lỗi trong mọi PR.** Code tốt, merge thẳng — hoàn toàn ổn.

## Múi giờ & nhịp bất đồng bộ: quy tắc "không có bất ngờ"

Review async chạy lệch múi giờ, không thể hỏi đáp tức thì, nên mọi kỳ vọng phải được **ghi ra từ trước** để không ai bị bất ngờ giữa buổi review:

- **Checklist cho PR & cho người review** — vì cả team thường lặp lại cùng 10 lỗi, và lỗi do *bỏ sót* là khó thấy nhất. Checklist đặc biệt cứu các thành viên mới ở PR đầu tiên.
- **Chuẩn coding toàn diện, được ghi lại** — đây mới là "tiêu chuẩn" bạn đối chiếu khi review. Muốn thêm yêu cầu mới? Gửi PR vào *chuẩn*, đừng bịa ra giữa lúc review.
- **Thỏa thuận: không phải câu hỏi nào cũng cần trả lời** — cho phép gửi câu hỏi gợi mở mà không chặn merge.

## Tooling: để máy lo phần máy làm được

Vấn đề **định dạng code gần như không bao giờ nên xuất hiện** trong một buổi review từ xa — nó đốt thời gian async quý giá vào thứ vô nghĩa. Giao hết cho **linter và formatter**. Review của con người để dành cho những thứ máy không làm được: thiết kế, đánh đổi, ý định.

## Liên hệ với team nhỏ của bạn (prepedu)

Bạn là BE dev ở prepedu, team chỉ 2 BE, code nhiều và đang tập làm TL — bối cảnh của bạn *gần như trùng khít* với bài này: review qua PR, async, ít khi ngồi cạnh nhau.

- **Team 2 người ⇒ mỗi bình luận nặng gấp đôi.** Không có người thứ ba pha loãng; một câu cụt lủn của bạn là 100% giọng điệu mà đồng đội nhận được. Câu "tóm tắt tích cực ở đầu" gần như bắt buộc.
- **Bạn là người review chính ⇒ dễ thành "tài xế ghế sau".** Bạn biết nhiều hơn, nên rất dễ ép code về đúng cách mình viết — đúng cái bẫy "giành việc/áp đặt" ở [[tech-lead-tot-tech-lead-te|Ngày 4]]. Hãy hỏi, đừng phán.
- **Review là kênh giao tiếp chính của team 2 người.** Nhớ [[tech-lead-can-bang-code-va-coaching|Ngày 5]]: giao tiếp *là* việc của TL, không phải phiền toái. Mỗi PR là một buổi mentor async — nhưng nhớ Hammond: mentor thật sự nên xảy ra *trước* khi code viết xong, nên hãy align thiết kế với đồng đội *trước* khi họ mở PR.
- **Viết checklist + chuẩn coding ngay khi team còn 2 người.** Đây là lúc rẻ nhất để làm; nó là tài sản chống "code silo" khi team lên 3–4 người.

## Tự phản chiếu

1. Bình luận review gần nhất tôi viết — nếu *tôi* là người nhận nó qua màn hình, không giọng nói kèm theo, tôi sẽ thấy nó như góp ý hay như đòn tấn công?
2. Tôi đang yêu cầu thay đổi vì code *thật sự* có vấn đề, hay chỉ vì "mình sẽ viết khác"?
3. Team tôi đã có checklist PR và chuẩn coding viết ra chưa, hay mọi tiêu chuẩn vẫn nằm trong đầu tôi?

## Hành động nhỏ (15 phút)

Mở PR gần nhất bạn vừa review. **Viết lại 1 bình luận dạng khẳng định thành dạng câu hỏi** ("Cái này sai" → "Lý do đằng sau cách này là gì?"), và **thêm một câu tóm tắt tích cực ở đầu** nêu rõ một điểm bạn thật sự thích — kèm *tại sao*. Để ý phản ứng của đồng đội ở lần review sau.

> *Mẹo:* trước khi nhấn "Submit review", đọc lại toàn bộ bình luận một lượt và xóa những câu bạn viết chỉ để "được nghe giọng mình". Đắm trong code thì viết bao nhiêu cũng được — nhưng chỉ gửi đi cái thật sự cần.

---

**Ngày mai (Ngày 11)** — *Cẩm nang đưa phản hồi mang tính phê bình*: khi lời góp ý buộc phải "khó nghe", làm sao để nó vẫn xây dựng, cụ thể và giữ được mối quan hệ.
