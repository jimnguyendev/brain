---
title: 'Tech Lead trong The Manager''s Path — tấm gương sát nhất với bạn (Tuần 4 — Ngày 14)'
lastmod: '2026-06-07 05:00:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Ngày 14 — bài đọc cuối cùng của Tuần 4 trong [[tech-lead-la-gi|lộ trình 4 tuần]], ngay trước bài chốt. Hôm qua ([[tech-lead-the-managers-path-mentoring|Ngày 13]]) ta học mentoring qua *The Manager's Path*; hôm nay ta đọc tiếp chương kế của chính cuốn đó — chương **"Tech Lead"** trong *The Manager's Path* (Camille Fournier, O'Reilly). Trong toàn bộ lộ trình, đây là chương **soi đúng hoàn cảnh của bạn nhất**: một kỹ sư vẫn code, được giao dẫn dắt, chưa phải manager.

Có một điều Fournier nói thẳng mà nhiều người bỏ lỡ: Tech Lead **không phải** một bậc trên đường thăng tiến quản lý, và cũng **không phải** "kỹ sư giỏi nhất đội". Nó là một **bộ kỹ năng** bạn khoác vào — và bạn vẫn là **một kỹ sư trong những kỹ sư** (`first among equals`), chứ không phải sếp của họ.

## Luận điểm gốc: lãnh đạo bằng ảnh hưởng, không bằng quyền

Fournier lật ngược kỳ vọng thường thấy. Làm TL **dạy bạn thành một kỹ sư tốt hơn** — vì lần đầu bạn buộc phải nghĩ vượt khỏi code của riêng mình: tại sao đội xây thứ này, nó khớp vào bức tranh lớn ra sao, đánh đổi nào đáng.

Mấu chốt: TL **không có quyền lực chính thức** với đồng đội. Bạn không đánh giá lương thưởng họ, không tuyển/sa thải. Thứ duy nhất bạn có là **ảnh hưởng** (`influence`) — uy tín kỹ thuật, sự tin cậy, khả năng thuyết phục. Đây là lý do nhiều kỹ sư giỏi *thất bại* khi lên TL: họ quen ra lệnh cho máy tính (luôn nghe lời) và bối rối khi con người thì không.

## Những "chiếc mũ" của một Tech Lead

Fournier mô tả TL là người liên tục **đổi mũ** — không có hai ngày giống nhau. Ba vai chính cô đặt tên:

- **Systems Architect & Business Analyst (Kiến trúc sư hệ thống & Phân tích nghiệp vụ).** Xác định các phần hệ thống trọng yếu để đạt mục tiêu *kinh doanh*, không chỉ kỹ thuật. Bạn phải hiểu *vì sao* xây, không chỉ *xây cái gì* — đây là cầu nối giữa yêu cầu sản phẩm và thiết kế kỹ thuật.
- **Project Planner (Người lập kế hoạch dự án).** Chia nhỏ công việc thành các phần khả thi, gỡ thế bí, tìm cách *song song hoá* để đội cùng tiến. Mục tiêu không phải có kế hoạch hoàn hảo, mà là khai phá đủ chi tiết để tránh bất ngờ muộn.
- **Software Developer & Team Leader (Lập trình viên & Trưởng nhóm).** Vẫn viết code — nhưng giờ phải cân nó với việc dẫn dắt: giao tiếp, gỡ vướng cho người khác, giữ đội đi đúng hướng.

Điểm chung: cả ba mũ đều đòi bạn **mở rộng tầm nhìn ra ngoài bàn phím của mình**, và không cái nào cho bạn đứng yên ở vùng an toàn thuần kỹ thuật.

## "Quản lý dự án" ≠ "quản lý người"

Một phân biệt Fournier nhấn mạnh, rất hữu ích cho người mới: TL **quản lý dự án**, manager **quản lý người**. Quản lý dự án nghĩa là làm chủ *công việc* — bóc tách độ phức tạp, sắp thứ tự, lường rủi ro, giữ mọi người đồng bộ về *cái cần làm tiếp*. Nó **không** có nghĩa là bạn thành sếp.

Việc này nghe hành chính và nhàm, nên nhiều kỹ sư né. Nhưng Fournier xem nó là kỹ năng nền: một TL không quản nổi tiến độ của chính dự án mình thì không dẫn được ai. Đây cũng chính là cột "Quản lý dự án — chủ động vs. bị động" bạn đã thấy ở [[tech-lead-tot-tech-lead-te|Ngày 4]].

## Căng thẳng lớn nhất: buông bớt code để có chỗ cho lãnh đạo

Đây là phần Fournier dành nhiều tâm sức nhất, và là **bài học khó nhất** của mọi TL mới.

Bạn **không thể** cứ code y như trước rồi gánh thêm việc dẫn dắt — sẽ quá tải, hoặc một trong hai sẽ hỏng. Nhưng nghịch lý: bạn cũng **không nên** ngừng code hẳn. Một TL không còn động vào code sẽ mất "cảm giác mặt đất", mất uy tín kỹ thuật — chính thứ tạo ra *ảnh hưởng* nói ở trên.

Lời khuyên của Fournier: hãy **chủ động chọn buông** một phần code, đặc biệt là các task trên-đường-tới-hạn (`critical path`) mà nếu bạn ôm rồi bị họp/gỡ vướng kéo đi, cả đội sẽ kẹt vì chờ bạn. Đừng tự nhận phần "đường găng" rồi thành nút thắt. Giữ lại đủ code để vẫn là kỹ sư thật — nhưng nhường những mảnh mà việc bạn chậm sẽ chặn người khác. Đây là phiên bản sách-giáo-khoa của thế cân bằng `force multiplier` ta đã mổ ở [[tech-lead-can-bang-code-va-coaching|Ngày 5]].

## Partner với manager của bạn

Fournier coi quan hệ TL ↔ manager là một **quan hệ đối tác**, không phải báo cáo một chiều. Manager lo về *con người* và sự nghiệp của đội; TL lo về *thực thi kỹ thuật*. Hai vai bổ trợ nhau. Một TL khôn ngoan sẽ chủ động khớp với sếp: ai quyết cái gì, thông tin chảy ra sao, khi nào cần sếp can thiệp. Ranh giới TL/EM mờ này chính là thứ ta đã phân định ở [[tech-lead-hay-engineering-manager|Ngày 3]].

## Liên hệ với team nhỏ của bạn (prepedu)

Trong cả 4 tuần, **đây là chương khớp hoàn cảnh của bạn nhất**: một BE dev code nhiều, được trao dẫn một team 2 BE, đang hướng tới TL nhưng chưa muốn rời code. Fournier viết như viết cho bạn vậy.

- **`First among equals` rất thật ở team 2 người.** Bạn không phải sếp của đồng đội kia — bạn chỉ có ảnh hưởng. Mọi quyết định kỹ thuật phải *thuyết phục được*, không áp đặt. May là khoảng cách quyền lực nhỏ khiến việc xây ảnh hưởng dễ hơn nếu bạn làm đúng.
- **Căng thẳng "buông code" bị khuếch đại.** Team 2 người: nếu bạn ôm hết phần đường găng, đồng đội vừa kẹt chờ vừa không lớn lên. Hãy *cố ý* nhường một mảng critical path và chấp nhận nó nhích chậm hơn lúc đầu.
- **Ba chiếc mũ, một cái đầu.** Ở team lớn, ba vai có thể chia. Ở đây *bạn đội cả ba*: vừa phân tích nghiệp vụ với PM, vừa bóc task & lường rủi ro, vừa code. Đừng kỳ vọng làm xuất sắc cả ba mỗi ngày — học cách *đổi mũ có ý thức* theo nhu cầu từng tuần.
- **Partner với sếp = phao cứu sinh.** Vì bạn không có quyền chính thức, hãy mượn "đòn bẩy" của manager khi cần (khớp ưu tiên, bảo vệ thời gian sâu cho đội). Một buổi 1:1 đều đặn với sếp đáng giá hơn mọi nỗ lực tự gánh.

## Tự phản chiếu

1. Tôi đang đội chiếc mũ nào nhiều nhất — Architect/Analyst, Project Planner, hay Developer — và cái nào tôi đang né vì nó "không phải code"?
2. Có task đường găng nào tôi đang ôm chỉ vì "mình làm nhanh hơn", trong khi việc tôi bận sẽ chặn đồng đội?
3. Tôi đang dẫn dắt bằng *ảnh hưởng* hay đang ngầm mặc định chức danh/uy tín cho mình quyền ra lệnh?

## Hành động nhỏ (15 phút)

Nhìn vào dự án hiện tại của bạn, liệt kê mọi task trên **đường găng** (thứ mà nếu trễ sẽ kéo lùi cả team). Khoanh tròn những task bạn đang tự ôm, rồi chọn **đúng 1 cái để giao lại** cho đồng đội còn lại — và viết một câu bạn sẽ nói để trao nó đi mà vẫn giữ vai hỗ trợ, không phải vai ra lệnh.

> *Mẹo:* lần tới khi định tự nhận một task vì "nhanh hơn", hỏi: *"Việc này có nằm trên đường găng không? Nếu có, tôi đang giúp đội hay đang sắp thành nút thắt?"*

---

**Ngày mai (Ngày 15) — bài chốt lộ trình 4 tuần.** Ta gói lại cả hành trình: recap những trụ cột lớn của bốn tuần (vai trò, mặt trái chức danh, cân bằng code/coaching, mentoring, *The Manager's Path*), một bản **tự đánh giá toàn diện**, và một kế hoạch hành động để bạn bước tiếp con đường TL của riêng mình. Hẹn gặp ở vạch đích.
