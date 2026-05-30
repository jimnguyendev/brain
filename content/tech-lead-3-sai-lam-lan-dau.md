---
title: '3 cái bẫy kinh điển của Tech Lead lần đầu (Tuần 2 — Ngày 7)'
lastmod: '2026-06-07 01:30:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Ngày 7 — gần cuối Tuần 2 của [[tech-lead-la-gi|lộ trình 4 tuần]]. Hôm qua ([[tech-lead-5-sai-lam-lon-nhat|Ngày 6]]) ta nghe một TL kể *5 cú vấp cá nhân* của chính anh ta. Hôm nay ta lùi một bước để nhìn bức tranh hệ thống hơn: ba cái bẫy mà *gần như mọi* TL lần đầu đều rơi vào, và vì sao chúng đều mọc ra từ chính những thói quen từng làm bạn thành một developer giỏi. Đúc kết từ bài [Three Common Mistakes of the First Time Tech Lead](https://medium.com/featured-insights/three-common-mistakes-of-the-first-time-tech-lead-aac7a900adab) của Patrick Kua (ThoughtWorks).

Có một nghịch lý cay đắng: kỹ năng và kinh nghiệm của một dev dày dạn **không tự động** biến thành kỹ năng của một TL. Tệ hơn — vài thói quen từng là điểm mạnh của bạn (code nhanh, biết nhiều nhất, tự giải mọi thứ) lại trở thành điểm yếu chí mạng khi bạn có thêm quyền và thêm người trông vào. Ba sai lầm dưới đây chính là ba thói quen tốt-hoá-xấu đó.

## 1. Code toàn thời gian — chứng minh bằng `commit`

Cái bẫy đầu tiên là tự nhủ: *"Mình phải chứng tỏ năng lực lãnh đạo bằng cách code thật nhiều."* TL mới nhớ cảm giác viết code, nhớ luôn cả cái cảm giác hoàn thành rõ ràng mà mỗi `merge` mang lại — nên họ chúi đầu vào IDE.

TL giỏi *vẫn* code, đọc và review — nhưng có chừng mực. Khi bạn dồn 100% giờ vào code, những việc chỉ-bạn-mới-làm-được sẽ bị bỏ trống:

- **Tầm nhìn kỹ thuật chung** không ai vẽ → mỗi dev tự quyết theo ý mình → ba kiểu triển khai cho cùng một bài toán.
- **Thuộc tính chất lượng then chốt** (ràng buộc vận hành, khác biệt môi trường) không ai canh → một lần `deploy` lên production gãy vì không ai nắm bức tranh lớn.
- Code phải làm lại liên tục vì quyết định cá nhân không tính đến bảo trì và hướng tiến hoá của hệ thống.

Lời giải của Kua rất cụ thể: **chia thời gian theo ngày, hoặc chí ít theo tuần** — chừa hẳn ô lịch cho kiến trúc, nhận diện rủi ro kỹ thuật, planning, và sự gắn kết của đội. Đây đúng là câu chuyện "force multiplier" của [[tech-lead-can-bang-code-va-coaching|Ngày 5]]: code là phép cộng, đầu tư vào team là phép nhân.

## 2. Tự ôm mọi quyết định kỹ thuật — thành nút thắt

TL lần đầu thường *là* dev kinh nghiệm nhất đội, hoặc cảm thấy áp lực phải tự chốt mọi thứ để "chứng tỏ quyền hạn". Hệ quả thì sách giáo khoa: bạn thành **bottleneck**, đội đứng hình khi bạn vắng mặt, và — điều ít người để ý — đồng đội *mất động lực* vì đóng góp của họ liên tục bị gạt đi. Đây chính là "điểm nghẽn cổ chai" mà bạn đã nhận diện từ [[tech-lead-vai-tro-hay-bay|Ngày 2]].

TL giỏi hiểu rằng quyết định không chỉ có một cách "tự chốt". Có cả một *quang phổ* cách ra quyết định, chọn tuỳ theo độ quan trọng, tốc độ cần, và mức cam kết muốn có từ đội:

- **Delegating** (ủy quyền) — giao hẳn, không can thiệp.
- **Offering advice** (góp ý) — giao cho người khác quyết, nhưng nêu quan điểm để họ cân nhắc.
- **Inquiring** (hỏi lại) — giao quyết, rồi hỏi lại kết quả và lý do dẫn tới nó.
- **Building consensus** (đồng thuận) — kéo cả đội tìm giải pháp ai cũng hài lòng.
- **Consulting** (tham vấn) — mời ý kiến cả đội, tổng hợp, rồi *tự* chốt.
- **Autocratic** (độc đoán) — tự quyết bằng thông tin mình có, rồi thông báo.

Điểm mấu chốt: không cách nào "đúng" tuyệt đối — kỹ năng của TL là **biết khi nào dùng cái nào**. Một quyết định production khẩn cần autocratic; một lựa chọn kiến trúc dài hạn xứng đáng building consensus.

## 3. Quên vun đắp văn hoá đội — chỉ lo phần "tech", bỏ phần "lead"

Một đội không phải là tổng các cá nhân code giỏi; nó là *một nhóm người cùng hướng về một mục tiêu*. TL lần đầu dễ tưởng việc của mình là dẫn dắt mọi khía cạnh **kỹ thuật**, mà quên rằng phải dẫn dắt cả cách đội **làm việc với nhau**.

Biểu hiện kinh điển: phớt lờ một cuộc tranh cãi gay gắt giữa hai dev, hay làm ngơ khi một thành viên kỹ thuật cư xử thiếu tôn trọng với người ngoài mảng tech (PM, designer). "Không phải việc của mình" — bạn nghĩ vậy, và để vết nứt âm ỉ lan ra.

TL giỏi nhận ra phần **"lead"** quan trọng *ngang* phần **"tech"** — đúng tinh thần "giao tiếp là phần việc chính" của [[tech-lead-tot-tech-lead-te|Ngày 4]]. Họ chủ động xây niềm tin bằng những thực hành cụ thể:

- Cùng nhau vẽ kiến trúc trên bảng trắng — để bức tranh nằm trong đầu cả đội, không riêng bạn.
- Cùng đội đặt các **nguyên tắc** về code/kiến trúc, để định hướng cho quyết định cá nhân (giảm luôn cái bẫy số 2).
- Chạy retrospective hay improvement kata định kỳ — biến việc cải thiện thành thói quen tập thể.

## Liên hệ với team nhỏ của bạn (prepedu)

Là một BE dev code sâu, đang dẫn một team 2 BE và muốn lên TL — ba cái bẫy này không hề "lý thuyết xa vời" với bạn, mà *gần* hơn bạn tưởng:

- **Bẫy "code toàn thời gian":** team nhỏ, bạn là người mạnh tay nhất, nên rất dễ tự nhủ "cứ code cho xong đã". Nhưng nếu không ai vẽ tầm nhìn chung, hai bạn sẽ phân kỳ thầm lặng — mỗi người một quy ước. Hãy chừa **một ô lịch cố định mỗi tuần** cho việc-không-phải-code.
- **Bẫy "tự ôm quyết định":** ở team 2 người, bạn rất dễ chốt hết vì "hỏi qua hỏi lại mất thời gian". Đúng là nhanh — nhưng đồng đội duy nhất của bạn sẽ mãi không tự chủ, và bạn vĩnh viễn là single point of failure. Hãy thử *xuống thang* từ autocratic sang **inquiring**: giao họ quyết, rồi hỏi lý do.
- **Bẫy "quên văn hoá":** team chỉ 2 người nên dễ chủ quan "anh em hiểu nhau là đủ". Nhưng văn hoá *dễ* xây nhất chính khi team còn nhỏ — vài nguyên tắc code chung viết ra hôm nay sẽ là nền móng khi team lên 5, 10 người.

Một câu nối cả ba: cả ba cái bẫy đều là **thói quen của dev giỏi áp dụng sai chỗ**. Lên TL không phải bỏ đi con người dev của bạn — mà là biết *khi nào* nên gác nó lại.

## Tự phản chiếu

1. Tuần qua tôi đã dành bao nhiêu % thời gian cho code, và bao nhiêu cho tầm nhìn/rủi ro/đội? Tỉ lệ đó có *cố ý* hay chỉ là quán tính của một dev?
2. Quyết định kỹ thuật gần nhất tôi tự chốt — nó thực sự cần autocratic, hay tôi chỉ ngại tốn thời gian tham vấn?
3. Có "vết nứt" nào trong cách đội làm việc với nhau (hay với PM/designer) mà tôi đang làm ngơ vì nghĩ "không phải việc tech"?

## Hành động nhỏ (15 phút)

Nhìn lại **một quyết định kỹ thuật bạn đang định tự chốt tuần này**. Trước khi chốt, gắn nhãn cho nó theo quang phổ ở mục 2 — bạn *đang* dùng cách nào? Rồi thử hạ một nấc: nếu đang định autocratic, chuyển sang **consulting** (hỏi đồng đội một câu trước khi quyết); nếu đang consulting một việc nhỏ, thử **delegating** hẳn. Ghi lại cảm giác của bạn — đó là bài tập "không-làm-nút-thắt" cụ thể nhất.

> *Mẹo:* lần tới khi tay bạn tự động mở IDE để "làm cho nhanh", dừng 3 giây và hỏi — *"Việc này chỉ mình làm được, hay chỉ là mình làm quen tay?"*

---

**Ngày mai (Ngày 8)** ta đóng Tuần 2 bằng một góc nhìn sắc lẹm về quản lý ưu tiên: [Great Leaders Don't Juggle Priorities](https://www.thoughtworks.com/insights) — vì sao **lãnh đạo giỏi không tung hứng ưu tiên** mà chọn dứt khoát một thứ quan trọng nhất.
