---
title: 'Làm chủ vai trò Tech Lead Manager (TLM) — Christoph Nakazawa'
lastmod: '2026-06-07 06:00:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Bản dịch bài [Mastering Tech Lead Management](https://cpojer.net/posts/mastering-tech-lead-management) của **Christoph Nakazawa** (đăng 20/09/2022, cập nhật 04/06/2026). Bài này soi đúng ngã ba mà [[tech-lead-hay-engineering-manager|Ngày 3]] đã đặt ra — không phải "chọn TL hay EM", mà là vai trò **lai** giữa hai bên: vừa quản người, vừa giữ tay nghề kỹ thuật. Đáng đọc cùng [[tech-lead-can-bang-code-va-coaching|bài cân bằng code & coaching]] và [[tech-lead-the-managers-path-tech-lead|chương Tech Lead trong The Manager's Path]].

Hầu hết các kỹ sư đến một thời điểm nào đó trong sự nghiệp đều đối mặt với lựa chọn chuyển sang làm quản lý. Việc chuyển sang Quản lý Kỹ thuật (Engineering Management — EM) hay tiếp tục ở vai trò Cá nhân đóng góp (Individual Contributor — IC) thường có cảm giác là một quyết định trắng-đen, và người ta hay bị áp lực phải chọn một trong hai. Nhưng còn một vai trò lai ít được biết đến hơn ở nhiều công ty: **vai trò Tech Lead Manager (TLM)** (đôi khi cũng được gọi một cách mơ hồ là *"Staff Engineering Manager"*).

## Trách nhiệm

Trách nhiệm của vai trò TLM có thể khá mơ hồ, bao gồm sự pha trộn giữa quản lý con người, lãnh đạo kỹ thuật, và đóng góp cá nhân. Vai trò TLM thường là sự **lai ghép của tất cả** các trách nhiệm EM và IC.

Theo kinh nghiệm của tôi, vai trò TLM là một lựa chọn tuyệt vời cho những Quản lý Kỹ thuật *giàu kinh nghiệm* muốn giữ lại khả năng định hướng và viết code. Tuy nhiên, khá thường xuyên, những IC lần đầu chuyển sang làm quản lý lại tình cờ rơi vào vai trò TLM, và rốt cuộc họ chán ghét quãng thời gian làm EM chính vì điều đó.

Chuyển từ viết code sang quản lý con người là cực kỳ khó và đòi hỏi một bộ kỹ năng hoàn toàn khác. Người ta rất dễ lùi về với việc viết code khi mọi thứ trở nên khó khăn, hoặc khi một quản lý lần đầu cạn ý tưởng cho các đầu việc "quản lý".

## Vai trò TLM có hợp với tôi không?

Nếu một nửa trở lên trong số các đặc điểm sau cộng hưởng với bạn, có lẽ bạn sẽ thích vai trò TLM:

- Bạn là một IC chuyên môn rất sâu và/hoặc năng suất rất cao, và bạn thoải mái với việc **giảm bớt viết code để giúp người khác phát triển**.
- Bạn thực sự thích đảm nhận nhiều loại trách nhiệm: quản lý con người, tuyển dụng, viết code, lãnh đạo, định hướng, và quản lý sản phẩm.
- Bạn *thực sự thực sự* quan tâm đến công nghệ hoặc sản phẩm team mình đang làm. Bạn không chỉ gật gù cho qua — *bạn thật lòng tin* vào sản phẩm và công nghệ đó.
- Không có ai trong team có thể tiếp quản vai trò lãnh đạo kỹ thuật trong một hai năm tới, kể cả khi bạn tuyển thêm. Điều này hiếm, áp dụng cho người hiểu rất sâu hạ tầng nội bộ hoặc là người dẫn đầu ngành.
- Bạn hào hứng giải quyết những bài toán kỹ thuật hóc búa nhất, nhưng cũng **vui vẻ trao** chúng cho người dưới quyền.
- Bạn muốn tiếp tục quản lý một *team nhỏ* và được tạo động lực bởi thử thách kỹ thuật hơn là bởi việc xây một tổ chức lớn hơn.

Tôi thấy vai trò TLM xuất hiện ở các team **hạ tầng** nhiều hơn team sản phẩm. Ở big tech, vai trò này có thể được định nghĩa rõ — nên tìm tài liệu nội bộ về kỳ vọng cụ thể. Ở startup hoặc công ty nhỏ, phần lớn quản lý có thể rốt cuộc lại là TLM dù chức danh ghi "Engineering Manager". Nếu kỳ vọng không khớp chức danh, hãy trò chuyện với quản lý để làm rõ trách nhiệm (hoặc chức danh).

---

Vai trò TLM *khó*. Bạn rất dễ rơi vào cảm giác bị kỳ vọng làm 200% khối lượng — vừa 100% EM vừa 100% IC — điều đó **không bền vững**, và không nhất thiết phải như vậy. Dưới đây là những gì đã hiệu quả với tôi để trở nên *thực sự giỏi* trong vai trò TLM:

## Quản lý con người trước, Kỹ thuật sau

Quản lý con người là việc *thử thách*. Quản lý nhiều người, kỳ vọng sự nghiệp của họ, mục tiêu công ty và tổ chức, đồng thời quản lý *chính mình* — đó là một ván Tetris không hồi kết. Con người phát triển chậm, nên "phần thưởng" của quản lý có thể mất hàng tháng mới hiện ra. Trong khi đó, đến công ty 9 giờ sáng thứ Hai, lao vào code, deploy một tính năng trước 5 giờ chiều, rời công ty chiều thứ Sáu với cảm giác *tuyệt vời* — thì dễ hơn nhiều. Nhưng trong lúc đó, team đang chật vật: họ bị tắc nghẽn, có mâu thuẫn bạn không hay biết, và họ không có đủ thời gian với bạn.

Khi ở vai trò TLM, **tôi bắt đầu mỗi tuần bằng việc tập trung vào con người trước, tác động kỹ thuật sau**. Tôi dồn tất cả các buổi 1:1 vào **nửa đầu tuần** để đạt đồng thuận, giải phóng lịch cho đóng góp kỹ thuật ở nửa cuối tuần, và check-in async với những người ít tương tác hơn.

Cách này khiến mọi người thấy được quan tâm, và để lại khoảng đệm để xử lý "hỏa hoạn", drama, mâu thuẫn. Có những tuần bạn không làm gì về kỹ thuật cho đến chiều thứ Sáu, và bạn phải chấp nhận điều đó. **Bạn chỉ thành công nếu giúp team thành công, và họ luôn được ưu tiên.**

## Phát triển siêu năng lực định hướng

Là một lãnh đạo có uy tín, **mọi người muốn nghe định hướng từ bạn**. TLM là chuyên gia trong lĩnh vực của mình, ý kiến kỹ thuật của bạn có sức nặng cả trong lẫn ngoài team — hãy tận dụng! Cứ mỗi hai ba tuần tôi thích tóm tắt những gì đang bận tâm, thứ ảnh hưởng đến team, thậm chí cả cảm xúc của mình. Đó là cách lãnh đạo bằng sự minh bạch, mời gọi thảo luận, và **gieo mầm cho những thay đổi sắp tới** — vì *người ta ghét bất ngờ*.

Là TLM, bạn còn cần siêu năng lực **định hướng bên ngoài team**. Nhiều EM quản người giỏi nhưng thiếu bối cảnh kỹ thuật về những gì team họ *thực sự* đang làm (nghiêm túc đấy — hãy tìm cho tôi một người chưa từng có một quản lý không biết team mình đang làm gì 🙃). TLM có khả năng độc đáo là **kết hợp kỹ năng quản lý dự án với năng lực kỹ thuật** giữ được nhờ làm việc kỹ thuật hằng ngày — dẫn tới quyết định sáng suốt và vững vàng hơn. Làm đúng, bạn sẽ được các EM khác săn đón vì ý kiến kỹ thuật, và ảnh hưởng được tới định hướng của những nhóm lớn hơn, thậm chí cả công ty.

[^2]: Ý tôi là, nghiêm túc đấy, hãy tìm cho tôi một người chưa từng có một quản lý không biết team mình đang làm gì 🙃

## Nhân rộng bản thân thông qua ủy quyền (Delegation)

Những TLM giỏi không chỉ định hướng, họ còn cần kỹ năng con người để **ủy quyền** thành công những dự án có phạm vi ngày càng lớn. Điều này đòi hỏi khả năng mentor và sự quan tâm thật sự đến việc giúp người khác phát triển. Quan trọng hơn, **một TLM phải ủy quyền để không bị quá tải**.

Cách tốt nhất là xác định đúng cơ hội và ghép nó với một người đã sẵn sàng gánh thêm trách nhiệm — vừa giúp họ lớn lên, vừa giúp bạn nhân rộng chính mình. Nhờ ở gần công việc kỹ thuật, tôi mentor sát hơn, và các mối quan hệ với người dưới quyền cũng ý nghĩa hơn.

## Bỏ qua các buổi 1:1 và các cuộc họp khác

Ở hầu hết công ty công nghệ, bạn được kỳ vọng gặp mỗi người dưới quyền ít nhất một lần/tuần. Hủy 1:1 là một tội lỗi lớn. Nhưng là TLM, bạn phải hết sức bảo vệ thời gian. Nhìn theo chu kỳ tháng/quý, việc chủ động **hủy tất cả 1:1 mỗi năm đến sáu tuần một lần** là chấp nhận được — miễn vẫn khiến mọi người thấy được hỗ trợ.

Hãy đặt đúng kỳ vọng, check-in qua chat trong tuần, và cho họ biết bạn sẽ dành thời gian gặp trực tiếp nếu cần. Nhiều khả năng bạn còn phản hồi *nhanh hơn* vì lịch được chặn cho thời gian tập trung. Lưu ý: một số người nhạy cảm hơn về chuyện này — tìm hiểu nhu cầu từng người, tránh hủy 1:1 với ai thấy việc trao đổi với bạn là vô cùng quý giá.

Nhìn chung, mọi người nên mạnh dạn hơn trong việc từ chối và hủy họp. **Người ta cần thời gian rảnh để làm việc chuyên sâu — điều này đúng với EM y như với IC.**

## Giảm bớt deadline cho việc viết code

Là TLM, bạn sẽ có những tuần không theo kế hoạch và chẳng tiến triển gì về kỹ thuật. Hãy hạn chế tác động tiêu cực điều đó lên lộ trình team: **đừng nằm trên đường găng (critical path)** của công việc kỹ thuật; thay vào đó tìm cách giúp team hiệu quả hơn, hoặc nhận việc bạn ở vị trí đặc biệt phù hợp để giải.

Kịch bản tệ nhất là cam kết làm việc kỹ thuật nằm trên đường găng của trọng tâm team. Khi bạn phải rút ra để lo việc quản lý, nó tạo căng thẳng cho người dưới quyền. Bạn vẫn làm được việc tác động lớn nếu đảm bảo **không ai đang chờ tính năng của bạn *ngay lúc này***. Không phải đừng bao giờ đặt deadline — mà phải **hết sức có chủ đích với cam kết, và quản lý thời gian tốt là then chốt.** Đây cũng là lý do TLM thường hợp với vai trò hạ tầng hơn: khi khách hàng là kỹ sư nội bộ, họ thường ổn với việc chờ lâu hơn chút.

## Tránh gây áp lực lên người dưới quyền

Là TLM, bạn vừa quản lý team vừa là một phần của team với vai trò IC. Bất kỳ ngày nào bạn cũng có thể cần một câu trả lời, một lượt review code, hoặc bị tắc bởi chính người dưới quyền.

Dù bạn cẩn trọng đến đâu, **vẫn có những động lực quyền lực (power dynamics)**: một số người sẽ bỏ dở việc đang làm để làm hài lòng sếp, rồi tụt lại ở việc quan trọng hơn. Tệ hơn, họ có thể thấy áp lực phải duyệt code không đạt chuẩn, chỉ vì sếp đang cố ship gì đó thật nhanh tối thứ Sáu. Trường hợp tệ nhất: bạn gây ra sự cố trong khi họp cả ngày, để mặc team xử lý hậu quả.

Là TLM bạn phải đặt kỳ vọng rõ ràng: **đóng góp kỹ thuật từ sếp phải được nhìn nhận như của đồng nghiệp, và giữ ở cùng tiêu chuẩn (hoặc cao hơn)**. TLM là hình mẫu — mọi người noi theo lãnh đạo, nên hãy **dẫn dắt bằng việc làm gương**: đặt tiêu chuẩn kỹ thuật mẫu mực, viết test, và chủ động xử lý mọi sự cố mình gây ra.

## Quản lý cấp trên (Managing Up)

Khi team khỏe mạnh, bạn có thể thử giảm bớt thời gian quản người và đo xem rút lui được tới đâu mà không tổn hại đến con người và team. Đó là sự cân bằng tinh tế vì nhu cầu hỗ trợ luôn thay đổi: có chu kỳ bạn nhận phản hồi tốt từ người dưới quyền nhưng thấy ít thỏa mãn kỹ thuật; có chu kỳ ngược lại. Điều này có thể là có chủ đích — nhưng phải **truyền đạt chủ ý này cho quản lý của bạn** để họ đặt phản hồi vào đúng bối cảnh.

## Cho nó 1 năm

Hãy cho bản thân **ít nhất một năm** để trải qua nhiều chu kỳ đánh giá và thấy kết quả từ sự hỗ trợ của bạn. Nhưng nếu phát hiện mình hoàn toàn không thích quản lý con người, hãy quay lại vai trò cũ. Một IC từng có kinh nghiệm quản lý mang lại góc nhìn cực kỳ giá trị, và bạn vẫn có thể chọn tiếp tục những phần EM mình yêu thích.

---

Theo kinh nghiệm của tôi, vai trò TLM **thử thách nhưng vô cùng xứng đáng**. Bạn có thể là một Quản lý Kỹ thuật mà vẫn giữ đôi chân trên mặt đất, cùng team giải những bài toán hóc búa. Tôi nhận ra **mọi người tin tôi hơn trong việc đưa ra quyết định đúng** — vì tôi biết stack *thực sự* vận hành ra sao, bởi tôi đã xây phần lớn nó. Thật bức bối khi báo cáo cho một người quản lý thuần túy không hiểu nổi team đang xây gì; bước vào vai trò TLM là cách chống lại điều đó.

TLM thường thấy quá tải vì quá nhiều trách nhiệm. **Cảm thấy như vậy là bình thường** — và hy vọng bạn đang dao động giữa hạnh phúc cá nhân và những con người dưới quyền hạnh phúc.

## Liên hệ với Prep Edu (team Learning)

Bài này gần như mô tả đúng vai trò của bạn ở Prep Edu: vừa mới lên Tech Lead, team nhỏ, vẫn code nhiều, vẫn có sếp phía trên. Vài điều rút ra rất cụ thể:

- **Bạn đang là một TLM trên thực tế** — dù chức danh là Tech Lead. Đừng cố ép mình thành 100% EM lẫn 100% IC; chấp nhận có tuần nửa đầu lo người, nửa sau mới code.
- **Đừng nằm trên đường găng kỹ thuật.** Khi bị cuốn vào họp/định hướng, đừng để cả sprint kẹt vì một tính năng chỉ bạn làm được. Đây đúng là cái bẫy "không tung hứng được ưu tiên" ở [[tech-lead-khong-tung-hung-uu-tien|bài này]].
- **Giữ chuẩn code của mình ngang đồng đội.** Ở team nhỏ, power dynamics càng dễ khiến đồng đội nể nang duyệt PR của sếp — hãy chủ động yêu cầu review thật.
- **Khớp kỳ vọng vai trò với sếp** — bạn nghiêng về trục kỹ thuật (TL) tới đâu, gánh phần con người (EM) tới đâu? Đây là việc đã nêu ở [[tech-lead-hay-engineering-manager|Ngày 3]].
