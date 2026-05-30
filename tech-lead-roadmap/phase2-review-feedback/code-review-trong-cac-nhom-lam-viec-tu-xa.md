---
title: "Code review trong các nhóm làm việc từ xa"
original_title: "Code Review in Remote Teams"
source: "https://web.hypothes.is/blog/code-review-in-remote-teams/"
phase: "Phase 2 — Code review & feedback"
---

# Code review trong các nhóm làm việc từ xa

> Nguồn: [Code Review in Remote Teams](https://web.hypothes.is/blog/code-review-in-remote-teams/)

Tác giả: Sean Hammond | 18 tháng 11, 2016

Đây là bản ghi lại một số nghiên cứu mà tôi đã thực hiện cho một buổi trao đổi với nhóm dev của chúng tôi tại Hypothesis về việc làm sao để code review trở thành một trải nghiệm dễ chịu và mang tính trao quyền hơn cho tất cả mọi người. Các liên kết tới nguồn tham khảo được rải rác trong bài viết, và bạn cũng có thể tìm thấy liên kết tới tất cả các nguồn tôi đã dùng (và nhiều hơn nữa) trong bộ sưu tập liên kết về code review của tôi trên Pinboard. Cũng xin cảm ơn engineering manager của chúng tôi, Lena, vì những góp ý.

Bài gốc được đăng tại seanh.cc/posts/code-review

Chúng tôi là một nhóm làm việc hoàn toàn từ xa tại Hypothesis, nên mọi giao tiếp đều diễn ra qua Internet và phần lớn diễn ra theo kiểu bất đồng bộ (asynchronous). Chúng tôi dùng thẻ Trello để mô tả các tính năng, viết code một mình, gửi pull request trên GitHub, và dùng tính năng review pull request của GitHub để gửi các bản code review bằng văn bản. Cách làm này có thể rất khác so với code review trực tiếp tại văn phòng, hay thậm chí so với code review từ xa qua video call.

Nếu bị xem nhẹ, kiểu code review bằng văn bản, bất đồng bộ này có thể là công thức dẫn tới thảm họa, xét về mặt các kiểu giao tiếp và cộng tác tiêu cực. Nhưng nếu cả nhóm chủ động quan tâm đến việc làm cho nó tốt lên, thì tôi nghĩ nó có thể vận hành rất hiệu quả.

## Code review để làm gì?

Trước khi bàn về cách nên và không nên làm code review, sẽ hữu ích nếu ta suy nghĩ xem code review phục vụ mục đích gì trong tổ chức của bạn, để các điều nên và không nên sau đó có thể được đánh giá dựa trên những mục tiêu này. Tôi cũng nghĩ nên nhớ rằng code review không chỉ là tìm bug và các vấn đề về thiết kế code.

Điều tôi muốn nhấn mạnh ở đây là: code review nhằm cải thiện chất lượng code **và tinh thần làm việc (morale)**.

Code review là một trong những cách chính mà các lập trình viên tương tác với nhau trong một ngày làm việc bình thường, nên nó cần là một trải nghiệm tích cực mà các lập trình viên mong chờ và mọi người tham gia đều thực sự muốn góp mặt. Nếu code review thường là một trải nghiệm khó chịu thì tinh thần làm việc sẽ sa sút.

Dưới đây là một số mục tiêu cần cân nhắc khi làm code review:

* **Tạo dựng văn hóa nội bộ của nhóm**. Code review là một trong những nơi chính mà văn hóa nhóm được thể hiện, và những buổi code review khó chịu là hệ quả của việc thiếu một văn hóa nhóm được xây dựng có chủ đích. Hãy dùng code review để chủ động vun đắp một văn hóa tích cực, kiên nhẫn và thân thiện.
* **Cải thiện mối quan hệ làm việc** bằng cách có cơ hội trò chuyện với các lập trình viên đồng nghiệp.
* **Giải tỏa căng thẳng** bằng cách đưa ra phản hồi tích cực cho mọi người.
* **Học hỏi**. Người review có thể học được điều mới từ đoạn code họ đang review, và tác giả có thể học từ những phản hồi họ nhận được.
* **Phá vỡ các "ốc đảo code" (code silo)** bằng cách để mọi người trong nhóm cùng review những thay đổi ở các phần khác nhau của code, từ đó làm quen với toàn bộ codebase.
* **Cố vấn và đào tạo (mentoring and education)**. Code review là cơ hội để các lập trình viên giàu kinh nghiệm hơn cố vấn và dạy dỗ người khác. Nhưng hãy lưu ý rằng code review — sau khi thời gian đã được bỏ ra và code đã được viết — không phải lúc nào cũng là thời điểm tốt nhất cho việc cố vấn và đào tạo. Các lập trình viên nên đã cộng tác về thiết kế kỹ thuật từ trước và trong quá trình viết code.
* **Chất lượng code**. Cuối cùng, đúng vậy, chất lượng code (bao gồm bug, khả năng bảo trì, tài liệu, cách tổ chức, kiến trúc, khả năng sử dụng…) là một trong những mục tiêu của code review.

## Những điều KHÔNG nên làm

Danh sách dài các hành vi xấu này có thể tạo cảm giác hơi tiêu cực, nhưng thành thật mà nói, đây là một bài viết mang tính tích cực, và sau khi đọc xong phần này thì sẽ có một danh sách dài những điều _nên làm_ tiếp theo! Có rất nhiều cách để biến một buổi code review thành khó chịu bằng cách làm sai, nên tôi nghĩ biết được điều gì không nên làm là một điểm khởi đầu tốt. Những buổi code review mang tính đối đầu, thiếu tử tế và khó đoán có thể khiến lập trình viên không hạnh phúc và khiến công việc trở nên khó khăn về mặt cảm xúc.

> "Hiểu được điều cần tránh trong code review có thể là khác biệt giữa việc bản review của bạn là một phần giá trị trong quá trình giao sản phẩm của nhóm, và việc bản review của bạn chỉ đơn thuần là một hình phạt tàn nhẫn và bất thường." (Erik Dietrich)

### Đừng chỉ làm code review trực diện và tối thiểu

(hay còn gọi là _tìm hiểu xem bạn dở đến mức nào_)

Đừng chỉ thẳng thừng và tối thiểu, chỉ ra những chỗ sai của code, nói điều bạn muốn được thay đổi, và không có gì hơn.

Lập trình viên dành rất nhiều thời gian và tự hào về code của họ, và code review là cơ hội để họ thể hiện điều đó. Với kiểu code review trực diện và tối thiểu này, kết quả tốt nhất mà tác giả có thể hy vọng là không có bình luận nào: "LGTM, đã merge." Buổi code review như vậy chẳng khác gì được đặt tiêu đề là _tìm hiểu xem người ta nghĩ bạn dở tệ đến mức nào_.

Giao tiếp cụt lủn và không qua sàng lọc mang theo một cái giá lâu dài. Nó có thể đầu độc văn hóa giao tiếp của nhóm và làm giảm năng suất của lập trình viên. Người ở đầu nhận của nhiều buổi code review kiểu này "thường cảm thấy như đây là một buổi đánh hội đồng được dàn dựng để dập tắt ý chí của họ", và code review có thể trở thành "những trận đấu trí giành phần thắng, nơi người ta nhắm bắn vào một mục tiêu… chính là lập trình viên đã viết đoạn code đó".

### Đừng nghĩ rằng "phê bình code, đừng phê bình người viết code" là đủ

"Phê bình code, đừng phê bình người viết code" có lẽ là lời khuyên nổi tiếng nhất về cách làm code review. Đó là lời khuyên tốt (nếu bạn đang chỉ trích đồng đội như những con người, thay vì bàn về code, thì bạn đang gặp vấn đề). Nhưng nó chưa đủ. Code là công việc sáng tạo mà lập trình viên đặt cả tâm huyết vào, và việc chỉ trích code của ai đó một cách gay gắt hay cộc lốc cũng tương đương với việc chỉ trích chính họ. Bạn phải làm tốt hơn thế, và tìm một cách tích cực hơn để mổ xẻ và đưa ra gợi ý về code.

### Để ý giọng điệu (tone) của bạn

**Đừng dùng giọng điệu cá nhân khi phê bình**. Những câu như "Tại sao bạn lại…?" tạo cảm giác như đang tấn công. Thay vì nói "Cách bạn viết hàm này khiến nó khó đọc, hãy thêm comment vào" (vốn khá cá nhân và ngụ ý người đó đã làm sai gì đó), hãy nói "Bạn nghĩ sao nếu thêm vài comment để hàm này dễ đọc hơn?" (câu này trả lại quyền tự quyết cho tác giả và tập trung vào điều họ có thể làm để cải thiện code).

**Đừng dùng ngôn ngữ đòi hỏi hoặc thách thức**. Tránh những câu mà ý nghĩa toát ra là "bạn sai rồi." Đừng bảo người ta rằng họ sai, hay rằng điều họ nói là vô giá trị, vì điều đó có thể khiến họ cảm thấy bị tấn công. Khi cảm thấy bị tấn công, người ta trở nên phòng thủ, không còn tham gia một cách sáng tạo được nữa, và ngừng học hỏi. Hãy tránh những câu như:

* "Cái đó đơn giản là sai."
* "Cái này hoàn toàn sai."
* "Sao bạn không làm thế này luôn cho rồi…?"

**Đừng dùng lối nói cường điệu khi phê bình**. Bạn không muốn người viết code cảm thấy bị xúc phạm vì cho rằng những lời phê bình của bạn là vô lý hoặc phóng đại. Hãy tránh những từ không cần thiết như "luôn luôn", "không bao giờ", "mãi mãi", và "chẳng có gì" trong lời phê bình.

**Đừng dùng ngôn ngữ xúc phạm**. Hãy tránh những "lời xúc phạm vô tình" bằng cách không dùng những từ như "ngớ ngẩn" hay "ngu ngốc" trong code review, dù bạn không có ý xúc phạm. Loại ngôn ngữ này mang theo các ngữ cảnh và liên tưởng, và có thể định hình tâm trạng của người nhận.

**Đừng dùng ngôn ngữ thiếu kiên nhẫn hoặc kiểu công kích ngầm (passive-aggressive)**. Hãy luôn giữ thái độ kiên nhẫn và thân thiện, tránh những câu khó chịu thể hiện sự bực bội và khiến người ta cảm thấy mình làm chưa đủ tốt:

* "Lại một lần nữa, cái này lẽ ra phải là…"
* "Như tôi đã nói rồi đấy…"

**Đừng dồn ép theo kiểu hội đồng (pile on)**. Sẽ khiến ai đó cảm thấy bị tấn công nếu họ nhận một bình luận phê bình từ một đồng nghiệp, rồi một hoặc nhiều đồng nghiệp khác lại +1 cho bình luận đó hoặc nhảy vào với những bình luận phê bình của riêng họ. Nhiều người cùng phê bình cũng có thể gây bối rối và tạo ra vấn đề "lắm thầy nhiều ma".

### Đừng làm "tài xế ghế sau" (back-seat coder)

Điều này có nghĩa là hãy kiềm chế, và không yêu cầu nhiều thay đổi code mà bạn có thể bị cám dỗ muốn yêu cầu. Phản hồi đòi hỏi quá nhiều thay đổi và tạo cảm giác như phải viết lại từ đầu có thể gây nản lòng, nên hãy cân nhắc kỹ các gợi ý của bạn và chọn ra những cái tốt nhất.

Đúng, một trong những mục tiêu của code review là tìm và sửa bug cũng như các vấn đề thiết kế của code. Nhưng đừng dùng code review để cố ép tác giả viết lại code theo cách mà chính bạn sẽ viết. Hãy nhớ rằng nhiều thứ trong phần mềm là vấn đề quan điểm, có nhiều giải pháp mà mỗi cái đều có ưu và nhược điểm riêng. Với mỗi "chỉnh sửa" mà bạn muốn gợi ý, hãy tự hỏi liệu đó có chỉ là sự khác biệt về quan điểm hay không? Trong những trường hợp tác giả đã cân nhắc các giải pháp khác nhau và chọn một giải pháp vì lý do nào đó, hãy cân nhắc việc trao quyền cho người viết code và tôn trọng quyền ra quyết định của họ.

> "Mặc dù lập trình viên có thể đã code theo cách khác với cách bạn sẽ làm, điều đó không nhất thiết là sai. Mục tiêu là code chất lượng, dễ bảo trì. Nếu nó đạt những mục tiêu đó và tuân theo các chuẩn coding, thì đó là tất cả những gì bạn có thể đòi hỏi." (Robert Bogue)

> "Bạn sẽ không bao giờ ép được ai đó viết ra đúng đoạn code mà bạn sẽ viết, và cố làm vậy là phản tác dụng. (Thành thật mà nói, nếu bạn có thái độ đó thì lẽ ra ngay từ đầu bạn nên tự viết code đi.)" (Erik Dietrich)

### Đừng phá vỡ quy tắc "không có bất ngờ"

Đừng vi phạm quy tắc không có bất ngờ. Hãy có một thỏa thuận chung, được ghi lại từ trước về kỳ vọng và tiêu chuẩn đối với pull request, và làm cho các buổi review dựa trên bằng chứng chứ không dựa trên ý kiến chủ quan.

### Đừng nói chỉ để được nghe giọng của chính mình

Trước khi đưa ra phản hồi, hãy nghĩ xem bạn nhắm đạt được điều gì khi làm vậy và cân nhắc xem mỗi bình luận có thực sự cần thiết không. Hãy nhớ rằng bạn đang cố giúp đỡ một cách xây dựng, chứ không phải cố chứng minh quan điểm. Khi viết một bản code review, tôi xem lại các bình luận của mình trước khi đăng, tự hỏi liệu mỗi bình luận có thực sự hữu ích hay cần thiết không, và cuối cùng xóa đi rất nhiều bình luận trước khi đăng bản review. Việc xem lại bình luận sau khi viết có thể giúp việc này dễ dàng hơn. Trong lúc đang đắm chìm trong code, cố gắng hiểu nó và hình thành suy nghĩ về nó, bạn có thể viết ra bao nhiêu bình luận tùy thích. Sau đó, bạn có thể quyết định điều gì thực sự muốn gửi cho người viết code.

> "Việc 'thật ra là…' chỉ vì muốn được đúng không phải lúc nào cũng hữu ích (hay được trân trọng), và đôi khi giữ kiểu phản hồi đó cho riêng mình lại có lợi cho mối quan hệ lâu dài của bạn với một người." (Katherine Daniels)

### Đừng nghĩ rằng bạn buộc phải tìm ra một vấn đề trong mỗi buổi code review

Nếu code tốt và có thể merge mà không cần thay đổi gì, thì điều đó hoàn toàn ổn!

## Những điều NÊN làm

**Mọi chuyện không nhất thiết phải như vậy!** Dưới đây là một số gợi ý yêu thích của tôi, thu thập từ khắp nơi trên Internet, về cách xoay chuyển code review và biến chúng thành một trải nghiệm tích cực, mang tính cộng tác.

### Khen ngợi code tốt

Hãy nhớ dành nhiều thời gian khen ngợi những điểm tốt của code, trước khi chỉ ra vấn đề và đưa ra gợi ý.

> "Bản chất con người là chúng ta muốn và cần được ghi nhận cho những thành công của mình, chứ không chỉ bị chỉ ra lỗi sai. Vì phát triển phần mềm tất yếu là một công việc sáng tạo mà lập trình viên dồn cả tâm hồn vào, nó thường rất gần gũi với trái tim họ. Điều này khiến nhu cầu được khen ngợi càng quan trọng hơn." (Robert Bogue)

Bạn muốn mọi người mong chờ code review như một trải nghiệm tích cực và xây dựng, chứ không sợ hãi nó như một sự chỉ trích thuần túy. Phản hồi tích cực cũng giải tỏa căng thẳng giữa người với người và giúp mọi người phản ứng tốt hơn với bất kỳ phản hồi mang tính phê bình nào.

Phần khó là tìm cách đưa ra bình luận tích cực mà không khiến chúng có vẻ sáo rỗng hay khen giả tạo, hoặc lộ rõ kiểu cấu trúc "bánh sandwich kẹp lời chê".

Hãy tránh **lời khen mỉa mai (backhanded compliment)**, những câu như "Làm tốt lắm, nhưng…" (theo sau là tất cả những thay đổi bạn muốn) có thể tạo cảm giác thiếu chân thành.

Một số cách để khen ngợi tự nhiên, chân thành và cụ thể hơn:

* Trân trọng nhiều phần hay khía cạnh cụ thể tốt đẹp của code, và cố gắng nói ra _tại sao_ bạn thích chúng.
* Để lại một "dòng độc thoại" về suy nghĩ của bạn trong lúc bạn đọc và hiểu code. "Ok, mình hiểu cái này làm gì rồi… Tốt, nó kết nối với cái này và gọi cái kia, được rồi… và đoạn đó phụ thuộc vào cả hai cái này, ổn."

    Việc thấy một lập trình viên khác thể hiện sự thấu hiểu công việc của bạn tự nó đã là một hình thức công nhận công việc đó, và khi gặp những phần code bạn không hiểu, bạn có thể hỏi để được giải thích.

### Đặt một bản tóm tắt tích cực ở đầu

Hãy tạo không khí bằng cách thể hiện, trong một câu tóm tắt tích cực ở đầu bản review, rằng bạn vui mừng và biết ơn vì đoạn code. Các tính năng review code mới của GitHub khiến việc này dễ hơn nhiều, bằng cách cho phép bạn viết nhiều bình luận theo dòng rồi đăng tất cả cùng một lúc (thay vì mỗi bình luận được đăng ngay khi bạn lưu nó), và cho phép bạn thêm một bản tóm tắt (hiển thị ở đầu bản review) trước khi đăng các bình luận.

### Tránh những lời buộc tội ngầm

**Hỏi, đừng khẳng định**. Hãy đặt câu hỏi thay vì đưa ra các phát biểu:

> "Một câu khẳng định mang tính buộc tội. 'Bạn đã không tuân theo chuẩn ở đây' là một sự tấn công — dù cố ý hay không. Còn câu hỏi 'Lý do đằng sau cách tiếp cận bạn dùng là gì?' là đang tìm kiếm thêm thông tin." (Robert Bogue)

Việc đặt câu hỏi thay vào đó sẽ cải thiện không khí, thay đổi giọng điệu của cuộc trò chuyện tiếp theo bằng cách mở ra cánh cửa cho đối thoại và học hỏi, đồng thời khuyến khích lập trình viên giải thích lý lẽ của họ hoặc tự hỏi liệu có cách nào tốt hơn không.

Lý tưởng nhất, nếu có một bug trong code thì nó sẽ được chính tác giả phát hiện ra để phản hồi lại lời nhắc qua câu hỏi, hoặc nếu có một cải tiến nào đó cho code, thì nó sẽ được chính tác giả đề xuất.

> "Nếu bạn thấy những thứ có thể là lỗi, bạn không cần phải bảo người ta rằng họ sai, thường thì một câu 'Bạn nghĩ điều gì sẽ xảy ra nếu tôi truyền null vào method này?' là đủ, vì người đó có lẽ sẽ nói 'Ồ, mình chưa nghĩ tới điều đó — mình sẽ sửa khi xong việc ở đây.' Để họ tự giải quyết vấn đề và đề xuất cải tiến là một sự trao quyền, và _tốt hơn rất, rất_ nhiều so với việc ra lệnh cho họ sửa đoạn code thiếu sót của mình." (Erik Dietrich)

Không nên:

* "Bạn đã không tuân theo chuẩn ở đây"
* "Cái này sai, dùng B thay vào đi."
* "Đoạn code này khó hiểu."
* "Bạn đã không khởi tạo các biến này"

Nên:

* "Lý do đằng sau cách tiếp cận bạn dùng là gì?"
* "Bạn nghĩ gì khi dùng A thay vì B?"
* "Tôi chưa hiểu đoạn này. Bạn giải thích giúp tôi được không?"
* "Tôi không thấy chỗ các biến này được khởi tạo"

**Tránh câu hỏi "tại sao" mang tính buộc tội**. Giống như các câu khẳng định, câu hỏi "tại sao" cũng có thể mang tính buộc tội, và việc tránh chúng có thể cải thiện không khí.

Không nên:

* "Tại sao bạn không tuân theo các chuẩn ở đây?"
* "Tại sao bạn không làm thế này luôn…?"

Nên:

* "Lý do đằng sau việc đi chệch khỏi các chuẩn ở đây là gì?"
* "Bạn nghĩ gì khi bạn…?"

### Hãy khiêm tốn

**Đặt câu hỏi, đừng ra yêu sách**. Thay vì chỉ bảo tác giả thực hiện một thay đổi bạn muốn, hãy đặt cho họ một câu hỏi về code của họ hoặc đưa ra một gợi ý và hỏi xem họ có nghĩ đó là một cải tiến không. Cách này đẩy quả bóng về phần sân của họ và tôn trọng quyền tự quyết của tác giả, cho họ cơ hội giải thích quyết định của mình hoặc tự quyết định xem một gợi ý có phải là cải tiến hay không.

> "Thay vì nói 'Hãy đặt tên biến đó là userName vì nó không rõ ràng', hãy diễn đạt gợi ý của bạn dưới dạng câu hỏi, như sau: 'Bạn nghĩ sao về việc đặt tên cái này là userName? Tên hiện tại khiến tôi thấy không rõ ràng vì nó cũng được dùng trong một ngữ cảnh khác ở someotherfile.js.'" (Daniel Bader)

**Khi đưa ra một gợi ý, cũng hãy nêu lý do tại sao** bạn cho rằng thay đổi này có thể là một cải tiến.

**Dùng ví dụ từ chính bản thân**. Hãy để tác giả biết rằng họ không phải người duy nhất từng mắc lỗi này. Đây có thể là một cách tuyệt vời để khiến lời phê bình dễ chịu hơn: "Tôi học được điều này theo cách khó khăn…", hoặc "Tôi từng cũng làm y như vậy…"

**Đồng ý rằng không phải câu hỏi nào cũng cần được trả lời**. Hãy thỏa thuận từ trước rằng không phải câu hỏi nào cũng cần được phản hồi. Điều này cho phép bạn đưa vào bản review những câu hỏi gợi mở tư duy mà không nhất thiết phải được giải quyết hay thậm chí trả lời để code được merge, nhưng vẫn có thể khiến lập trình viên suy nghĩ và cải thiện chất lượng của toàn bộ codebase về lâu dài.

### Đừng phá vỡ quy tắc "không có bất ngờ"

**Dùng checklist**:

> "Rất có thể mỗi người trong nhóm bạn đều mắc cùng 10 lỗi lặp đi lặp lại. Đặc biệt các lỗi do bỏ sót là khó tìm nhất, vì khó mà review được thứ không hề tồn tại. Checklist là cách hiệu quả nhất để loại bỏ những lỗi thường gặp và để đối phó với thách thức của việc phát hiện những thứ bị bỏ sót." (SmartBear)

Dù không thể bao quát hết mọi thứ, một checklist tốt về những gì một pull request cần có trước khi được merge / những gì người review nên tìm kiếm khi review một pull request là một công cụ hữu ích cho cả người viết code lẫn người review. Một checklist có thể đồng nghĩa với chất lượng code tốt hơn và nhất quán hơn, và có thể giúp tránh phá vỡ quy tắc không có bất ngờ. Việc ghi lại những gì được kỳ vọng đặc biệt hữu ích cho các thành viên mới khi họ gửi pull request đầu tiên và làm những buổi code review đầu tiên.

Đây là một ví dụ để bạn bắt đầu:

- Nhánh của bạn nên chứa một phần công việc tách biệt về mặt logic và không chứa các thay đổi không liên quan.
- Bạn nên có các commit message tốt.
- Nhánh của bạn nên chứa test mới hoặc đã thay đổi cho bất kỳ code mới hoặc đã thay đổi nào, và tất cả test nên pass trên nhánh của bạn.
- Nhánh của bạn nên chứa tài liệu mới hoặc đã cập nhật cho bất kỳ code mới hoặc đã cập nhật nào.
- Nhánh của bạn nên cập nhật theo nhánh master và có thể merge mà không xung đột, nên hãy rebase nhánh của bạn lên trên master trước khi gửi pull request.
- Bất kỳ code mới nào cũng nên tuân theo kiến trúc code và các style guide Python, JavaScript, HTML và CSS của chúng tôi.
- Nếu code mới có thay đổi schema cơ sở dữ liệu, nó nên kèm một database migration.
- Nếu code chứa thay đổi phá vỡ tính tương thích ngược cho plugin, API client hay theme, thì sự phá vỡ đó có cần thiết không, hay lợi ích của thay đổi có biện minh được cho sự phá vỡ đó không? Các thay đổi gây phá vỡ đã được thêm vào changelog chưa?
- Code mới có thêm dependency nào không (ví dụ import module Python bên thứ ba mới)? Nếu có, dependency mới đó có chính đáng không và đã được thêm theo đúng quy trình chưa?
- Code đã được test bằng dữ liệu production chưa?
- Nếu có thay đổi UI, chúng đã được test trên các kích thước màn hình khác nhau và trên các trình duyệt khác nhau chưa?
- Nếu có thay đổi UI, chúng có đáp ứng tiêu chuẩn về khả năng tiếp cận (accessibility) của chúng tôi không?
- Nếu có chuỗi văn bản mới hiển thị cho người dùng, chúng đã được quốc tế hóa (internationalize) chưa?

**Có bộ chuẩn coding toàn diện và được ghi lại**:

Chuẩn coding là một "thỏa thuận chung mà các lập trình viên có với nhau", một tập hợp hướng dẫn chung có sự đồng thuận của tất cả mọi người, về điều gì tạo nên code chất lượng và dễ bảo trì trong tổ chức này. Chuẩn coding là nền tảng của code review (chuẩn coding chính là tiêu chuẩn mà bạn dùng để đối chiếu code khi review). Thay vì nêu ra những yêu cầu không có trong chuẩn coding của bạn, hãy gửi một pull request để bổ sung chúng vào chuẩn.

Nếu không có dự án chung là chuẩn coding làm điểm tham chiếu, các lập trình viên có thể rơi vào tình trạng không biết vấn đề tiếp theo sẽ đến từ đâu trong buổi code review. Điều này không trao quyền cho lập trình viên đóng góp một cách hiệu quả.

Chuẩn coding nên toàn diện. PEP 8 là một phong cách định dạng code, nó không phải là một chuẩn đủ trọn vẹn cho code review.

### Review đúng những thứ cần review và để công cụ lo phần còn lại

Các vấn đề về định dạng code gần như không bao giờ nên xuất hiện trong một buổi code review. Code review nên khơi gợi những suy nghĩ và thảo luận hữu ích, và việc dành quá nhiều thời gian cho phong cách và định dạng code sẽ không giúp ích cho điều đó. Hãy dùng các công cụ như linter và code formatter thay thế.

## Kết luận

Bài viết này nói về cách đưa ra phản hồi tích cực cũng như cách phê bình, và về cách đưa ra gợi ý thành công khi làm code review. Đề xuất của tôi về việc nên làm gì với bài này cho nhóm dev của chúng tôi tại Hypothesis, và bất kỳ nhóm nào khác quan tâm đến việc làm code review hiệu quả hơn, là hãy làm một phiên bản súc tích, dạng gạch đầu dòng của hướng dẫn này và áp dụng nó như tài liệu "cách làm code review" của nhóm. Đặt nó trong một git repo mà các thành viên có thể mở issue và gửi pull request, để bản hướng dẫn này trở thành một sự cộng tác chung.

Ngoài những gì diễn ra tại thời điểm code review, tôi nghĩ cũng đáng để suy nghĩ về việc code đang được review được tạo ra như thế nào ngay từ đầu. Tôi nghĩ bạn muốn người viết code và người review về cơ bản đồng bộ với nhau về thiết kế kỹ thuật cho một tính năng _trước khi_ bất kỳ dòng code nào đi vào review. Hãy biết trước ai sẽ là người viết code và ai sẽ là người review cho một tính năng, và khuyến khích họ làm việc như một nhóm hai người để hoàn thành tính năng, thảo luận về thiết kế code và các phiên bản trung gian của code trước khi nó đến bản review cuối cùng. Mục tiêu là có được thiết kế code tốt hơn (hai cái đầu tốt hơn một), nhưng cũng để tránh phải tranh luận tại thời điểm review giữa hai giải pháp hoàn toàn khác nhau (một trong số đó sẽ đòi hỏi viết lại đoạn code đã viết).

Nếu đã có nhiều sự cộng tác giữa người viết code và người review trước thời điểm code review, thì khả năng cao là sẽ có ít vấn đề cần nêu ra trong buổi review hơn, và như vậy bạn đã có một khởi đầu tốt.
