---
title: 'Đưa phản hồi phê bình mà không phá vỡ niềm tin (Tuần 3 — Ngày 11)'
lastmod: '2026-06-07 03:30:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Ngày 11 của [[tech-lead-la-gi|lộ trình 4 tuần]], gần cuối Tuần 3 về code review & feedback. Hai ngày qua ta học cách *cấu trúc* phản hồi trong review ([[code-review-kim-tu-thap-maslow|Ngày 9]]) và *vận hành* nó từ xa ([[code-review-team-tu-xa|Ngày 10]]). Hôm nay là phần khó nhất về mặt con người: nói điều khó nghe mà không khiến đối phương phòng thủ. Đúc kết từ [A Primer on Giving Critical Feedback](https://www.tombartel.me/blog/a-primer-on-giving-critical-feedback/) của Tom Bartel.

Hầu hết chúng ta *né* phản hồi phê bình. Ta sợ phản ứng của người nhận, sợ không khí gượng gạo, sợ bị ghét. Nhưng né tránh không phải là tử tế — nó là bỏ mặc. Một xu hướng xấu không được chỉ ra sẽ lan rộng, và đồng đội mất đi cơ hội sửa khi còn kịp. Tin tốt: đưa phản hồi tốt là một **kỹ thuật học được**, không phải năng khiếu bẩm sinh.

## Một khung 4 bước để dựa vào

Khi không biết bắt đầu từ đâu, hãy đi theo bốn bước này — chúng cho bạn một đường ray để không lạc vào cảm xúc:

1. **Mô tả một tình huống cụ thể** đã xảy ra.
2. **Mô tả hệ quả tiêu cực** của hành vi đó.
3. **Hỏi người nhận** xem họ đề xuất gì để cải thiện.
4. **Chốt một thoả thuận** về bước tiếp theo.

Để ý: bạn chỉ *làm chủ* hai bước đầu (mô tả). Hai bước sau là của họ — giải pháp và cam kết đến từ phía người nhận. Đó là điều giữ cho phản hồi không biến thành bài giảng.

## Cụ thể, đừng chung chung

"Dạo này em làm việc thiếu cẩn thận" — câu này vô dụng. Nó chung chung nên người nghe không biết bám vào đâu, chỉ thấy bị đánh giá tổng thể, và lập tức phòng thủ.

Thay vào đó, hãy neo vào một sự việc cả hai cùng nhớ: *"PR hôm qua merge mà không có test cho nhánh xử lý lỗi."* Cụ thể giúp người nhận sống lại đúng khoảnh khắc đó thay vì cãi về việc họ có "cẩu thả" hay không.

## Đúng lúc — càng sớm càng tốt

Phản hồi để lâu là phản hồi hỏng. Hãy nói **cùng ngày hoặc hôm sau**, khi sự việc còn tươi trong trí nhớ cả hai. Để đến review giữa kỳ ba tháng sau, phản hồi của bạn phụ thuộc vào trí nhớ chủ quan và vào việc lúc đó hai người đang thân hay căng — nó mất hết sức nặng khách quan.

## Tách hành vi khỏi con người

Đây là cốt lõi. Có hai cách diễn đạt thay đổi hoàn toàn cảm giác người nghe:

**Nói về tác động lên *bạn*, đừng nói thay người khác.** Bạn không có quyền tuyên bố "cả team thấy bị xúc phạm" — bạn chỉ biết *bạn* thấy gì.

- ❌ "Bạn xúc phạm tất cả mọi người." → ✅ "Điều bạn nói khiến tôi thấy buồn."
- ❌ "Mọi người thấy bị gây hấn." → ✅ "Tôi thấy bị tấn công."

**Phê bình hành vi, không phê bình tính cách.** Tấn công đặc điểm con người ("bạn cẩu thả") kích hoạt phòng thủ; mô tả một hành động cụ thể thì không.

- ❌ "Bạn làm việc thiếu kỹ lưỡng." → ✅ "Code không có test khiến người khác mất thời gian."
- ❌ "Bạn cứ liên tục xúc phạm người khác." → ✅ "Khi bạn đảo mắt lúc tôi nói, tôi thấy bị coi thường."

Khi *bạn* không phải người trực tiếp bị ảnh hưởng, dùng **câu hỏi tam giác**: *"Bạn nghĩ An cảm thấy thế nào khi PR của cậu ấy bị nhận xét theo cách đó?"* — để người nhận tự đặt mình vào vị trí người kia, thay vì bạn phán hộ.

## Giải pháp phải đến từ họ

Cám dỗ lớn nhất là tự đưa luôn lời giải. Đừng. Người nhận phải là người tự nghĩ ra cách sửa — đó là cách họ giữ **quyền sở hữu và trách nhiệm**. Hãy hỏi thẳng: *"Bạn định làm gì để lần sau tránh chuyện này?"*

Tránh gói nó thành vấn đề của "chúng ta" ("mình cùng xem nhé") — cách nói đó nghe dễ chịu nhưng pha loãng trách nhiệm của họ. Và nếu gợi ý đầu tiên còn hời hợt, hãy **dùng sự im lặng** và đề nghị họ nói cụ thể hơn. Khoảng lặng cho thấy bạn nghiêm túc, không để họ thoát bằng câu trả lời cho có.

## Chốt lại và quay lại kiểm tra

Đừng dừng ở chỗ "đã nói rồi". Hẹn một buổi nói chuyện ngắn sau đó để xem tiến triển. Việc quay lại cho thấy bạn đầu tư vào sự phát triển của họ — đây là phản hồi để *giúp họ lớn lên*, không phải một lần xả rồi quên.

## Nghịch lý của người dẫn dắt

Có một sự thật khó nuốt: kiên trì đưa phản hồi có thể khiến bạn *không* được yêu quý ngay lúc đó. Như Dick Costolo nói: *"Quản lý bằng cách cố được người khác yêu quý là con đường dẫn đến diệt vong."* Phản hồi trung thực là một hành động tử tế dài hạn — nó khó chịu lúc đầu nhưng sẽ dễ dần khi luyện. Và phần thưởng kép: khi bạn dạy đồng đội cùng kỹ năng này, phản hồi trở thành chuyện *bình thường* trong team thay vì sự kiện đáng sợ.

## Liên hệ với team nhỏ của bạn (prepedu)

Bạn là BE dev ở prepedu, code nhiều, trong một team chỉ 2 BE và đang hướng tới TL. Đưa phản hồi cho một **đồng cấp mà bạn ngồi code cạnh mỗi ngày** là tình huống tế nhị nhất — không có "khoảng cách chức danh" để núp sau, và mai vẫn phải pair với nhau.

- **Vì gần, hãy càng cụ thể.** Ở team 2 người, một câu chung chung sẽ ám cả tuần. Neo vào đúng một PR, đúng một dòng — *"chỗ retry này thiếu test"* — để phản hồi là về *việc*, không phải về *người ngồi cạnh*.
- **Nói "tôi", không nói "team".** Bạn không thay mặt được ai khi cả team chỉ có hai người — nói "team thấy phiền" là lộ liễu giả tạo. *"Khi mình review mà thiếu mô tả PR, mình mất thời gian đoán ý"* là thật và khó cãi.
- **Để họ tự chốt cách sửa.** Cám dỗ "để mình fix luôn cho nhanh" rất mạnh khi bạn code khoẻ hơn — nhưng đó đúng là cái bẫy "giành việc" ở [[tech-lead-tot-tech-lead-te|Ngày 4]]. Hỏi họ định làm gì, rồi im lặng chờ.

Và đừng quên: feedback đi **cả hai chiều**. Ngày 4 đã cảnh báo TL tệ là người *phòng thủ khi nhận feedback*. Nếu bạn muốn đồng đội đón nhận lời phê bình một cách cởi mở, bạn phải khiêm tốn khi đến lượt mình bị góp ý — đó là điều xây nên sự an toàn tâm lý để cả khung 4 bước trên hoạt động.

## Tự phản chiếu

1. Lần gần nhất tôi *né* một phản hồi khó nói — tôi né vì lợi ích của đồng đội, hay chỉ để mình đỡ ngại?
2. Khi góp ý, tôi đang phê bình *hành vi cụ thể* hay vô tình dán nhãn *tính cách* ("cẩu thả", "lười")?
3. Lần cuối đồng đội góp ý cho tôi, phản ứng đầu tiên của tôi là lắng nghe hay là giải thích để bảo vệ mình?

## Hành động nhỏ (15 phút)

Chọn **một phản hồi nhỏ bạn đang trì hoãn** với đồng đội. Viết ra hai câu theo khung: (1) một tình huống cụ thể đã xảy ra, (2) tác động lên *bạn* — dùng "tôi", tả hành vi chứ không tả tính cách. Rồi nhắn họ hẹn 10 phút *hôm nay hoặc mai*, khi sự việc còn tươi. Một phản hồi đúng lúc và cụ thể đáng giá hơn mười lần "để dịp khác nói".

> *Mẹo:* trước khi mở lời, đọc lại câu của bạn và gạch bỏ mọi từ "luôn", "lúc nào cũng", "mọi người" — chúng là dấu hiệu bạn đang nói về con người, không phải hành vi.

---

**Ngày mai (Ngày 12)** đóng lại Tuần 3: [Thể hiện lãnh đạo với tư cách Individual Contributor](#) — dẫn dắt bằng ảnh hưởng chứ không bằng chức danh, đúng vị trí bạn đang đứng ở prepedu.
