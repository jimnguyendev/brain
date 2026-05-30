---
title: "Định nghĩa về một Tech Lead"
original_title: "The Definition of a Tech Lead"
source: "https://medium.com/@patkua/the-definition-of-a-tech-lead-484bb46569f2"
phase: "Phase 0 — Hiểu đúng vai trò Tech Lead"
---

# Định nghĩa về một Tech Lead

> Nguồn: [The Definition of a Tech Lead](https://medium.com/@patkua/the-definition-of-a-tech-lead-484bb46569f2)

## Định nghĩa

**Ngắn gọn:** Tech Lead là một software engineer chịu trách nhiệm dẫn dắt một team và đảm bảo sự thống nhất về định hướng kỹ thuật.

**Đầy đủ:** Tech Lead là một software engineer chịu trách nhiệm dẫn dắt một team và đảm bảo sự thống nhất về định hướng kỹ thuật. Việc đưa ra một định hướng kỹ thuật vững vàng bao gồm: xây dựng tầm nhìn kỹ thuật, giải quyết các bất đồng về mặt kỹ thuật, và quản lý chất lượng kỹ thuật của các sản phẩm mà team bàn giao. Sự dẫn dắt kỹ thuật hiệu quả đảm bảo rằng team áp dụng các engineering practice phù hợp (chẳng hạn như CD hay automated testing), liên tục đầu tư vào việc cải tiến công cụ hoặc xử lý technical debt, và đảm bảo hệ thống tiến hóa để đáp ứng các nhu cầu cũng như môi trường đang thay đổi.

Đôi khi việc *dẫn dắt team* được chia sẻ, nhưng việc *dẫn dắt kỹ thuật* thì hiếm khi như vậy. Một Tech Lead có thể đồng dẫn dắt một team cùng với các vai trò khác như Product Manager hay Engineering Manager/Team Lead. Trong khi Product Manager tập trung vào "*Cái gì*", thì Tech Lead tập trung vào "*Như thế nào*". Trong khi Engineering Manager/Team Lead tập trung vào "*Con người và sự phát triển của team*", thì Tech Lead tập trung vào "*Sự phát triển kỹ thuật*" của các thành viên và của hệ thống. Điểm tập trung đặc trưng của Tech Lead là dẫn dắt định hướng và chất lượng kỹ thuật cho team. Họ cũng có thể mang thêm những trách nhiệm khác tùy thuộc vào từng team cụ thể.

Trong ví dụ ở trên, một team có thể có một Product Manager, một Engineering Manager và một Tech Lead. Vai trò dẫn dắt được chia sẻ giữa ba người, nhưng mỗi người mang một trọng tâm khác nhau. Trong tình huống này, Tech Lead tập trung nhiều hơn vào các chủ đề kỹ thuật. Họ sẽ tham gia sâu hơn vào các cuộc thảo luận và quyết định về kiến trúc. Họ quan sát và quản lý chất lượng của codebase khi nó tiến hóa, cũng như sự phát triển kỹ thuật của team.

Cũng trong ví dụ trên, một team có thể chỉ có một Product Manager và một Tech Lead. Trong tình huống này, Tech Lead kế thừa luôn các trách nhiệm của Engineering Manager. Họ phải tập trung thêm vào phát triển con người (ví dụ feedback hay các cuộc trò chuyện về sự nghiệp) và xây dựng một team hiệu suất cao. Mô hình này hoạt động tốt với các team nhỏ hoặc các hệ thống ít phức tạp. Khi team lớn dần lên về quy mô hoặc hệ thống phức tạp hơn, Tech Lead sẽ có ít thời gian hơn để tập trung vào cả hai mảng. Trong bối cảnh đó, Tech Lead ngầm ưu tiên một mảng hơn mảng còn lại. Theo kinh nghiệm cá nhân của tôi, họ thường ưu tiên các chủ đề kỹ thuật, đôi khi gây thiệt hại cho các chủ đề về con người hay team.

Điều luôn đúng bất kể cấu trúc team là gì, đó chính là vai trò dẫn dắt kỹ thuật của Tech Lead. Một Tech Lead hiệu quả xây dựng tầm nhìn kỹ thuật cùng với team. Họ làm việc với team để cập nhật, phát triển nó và biến nó thành hiện thực. Tech Lead phải tiếp tục gắn bó với code để đưa ra những quyết định có cơ sở, nhận diện các rủi ro kỹ thuật và duy trì sự tin tưởng với các developer. Trong bài thuyết trình "The Geek's Guide to Leading Teams" của mình, tôi đề xuất một mức tối thiểu lý tưởng là dành 30% thời gian cho code.

## Không chỉ là một team lead

Giai đoạn đầu sự nghiệp, tôi từng làm việc trong một team có cả Tech Lead lẫn Team Lead. Người Team Lead không có nền tảng kiến trúc mạnh. Họ chắc chắn vẫn viết code, nhưng họ tạo ra giá trị cho team theo một cách khác. Họ tập trung rất nhiều vào việc phát triển con người. Team Lead có các buổi 1-to-1 với mọi người, tập trung vào feedback và phát triển sự nghiệp. Họ chủ động tổ chức các hoạt động nhằm xây dựng sự an toàn về mặt tâm lý (psychological safety) và nuôi dưỡng niềm tin. Team Lead gặp gỡ các bên liên quan bên ngoài team để giữ luồng thông tin thông suốt, hoặc để gỡ bỏ các vướng mắc.

Trong khi Team Lead tập trung vào các vấn đề của team, thì Tech Lead tập trung vào các chủ đề kỹ thuật có ảnh hưởng tới nhiều hơn một developer. Tech Lead làm trung gian hòa giải cho các cuộc tranh luận kỹ thuật. Họ tham gia xây dựng các giải pháp tối ưu hiệu năng. Họ dẫn dắt các cuộc thảo luận về những quyết định có thể giới hạn hoặc mở rộng các lựa chọn kiến trúc trong tương lai. Họ cũng gặp gỡ các bên liên quan bên ngoài, nhưng tập trung vào các chủ đề kỹ thuật. Họ gặp những người làm hạ tầng để hiểu các thay đổi về mạng hoặc phần cứng. Họ gặp các Tech Lead khác để đảm bảo hệ thống của mình ăn khớp với hệ sinh thái rộng hơn của công ty. Họ gặp những người làm sản phẩm để đảm bảo kiến trúc của họ hỗ trợ được các công việc trong tương lai.

## Trực tiếp "xắn tay" nhiều hơn một Engineering Manager

> "You manage things, you lead people"
> (Bạn quản lý mọi thứ, bạn dẫn dắt con người)
>
> – Grace Hopper

Giống như với Tech Lead, ngành của chúng ta không có một định nghĩa chung cho Engineering Manager. Bạn sẽ thấy chức danh này khác nhau giữa các công ty, và thậm chí khác nhau ngay trong cùng một công ty. Một số Engineering Manager giống như Tech Lead, nhưng cũng có nhiều người rất khác. Ví dụ, nhiều người không viết code hằng ngày. Thay vào đó, họ tập trung vào:

* Duy trì một môi trường làm việc hiệu quả cho các team phát triển
* Xin được ngân sách phù hợp cho việc phát triển nhằm hỗ trợ các mục tiêu kinh doanh
* Đại diện cho góc nhìn công nghệ ở cấp quản lý hoặc cấp hội đồng (board)
* Thiết lập và/hoặc điều phối các chương trình công việc (được triển khai thông qua việc phát triển)
* Tuyển dụng và giữ chân người để đáp ứng nhu cầu nhân sự của team hoặc của bộ phận IT

Một Engineering Manager có thể ngồi ở cấp độ team, nhưng họ cũng ngồi ở cấp độ "team của các team" (team of teams). Nhiều Engineering Manager có thể không có nền tảng phát triển phần mềm. Thay vào đó, họ có thể từng là Project Manager, QA hoặc một vai trò nào đó vẫn liên quan đến phần mềm.

## Một Architect giỏi trông giống như một Tech Lead

Vai trò Architect đảm bảo rằng kiến trúc tổng thể của ứng dụng phù hợp với bối cảnh kinh doanh, cả ở hiện tại lẫn trong tương lai. Ở một số tổ chức, Architect làm việc cùng team để xây dựng *và* kiểm chứng tầm nhìn kiến trúc. Architect cũng quan tâm đến việc tìm ra mức độ chuẩn hóa (standardisation) phù hợp. Một mức chuẩn hóa hợp lý sẽ hỗ trợ năng suất. Chuẩn hóa quá mức sẽ giết chết sự đổi mới.

Một số tổ chức có kiểu "Architect trên tháp ngà" (Ivory Tower Architect) — người sà xuống để tư vấn, chuẩn hóa và viết tài liệu. Họ trôi từ team này sang team khác, khởi động các dự án phần mềm mới, và hiếm khi quay lại theo dõi kết quả của tầm nhìn kiến trúc ban đầu của mình. Đây không phải là hình ảnh của một Tech Lead.

Một Architect hiệu quả trông giống như một Tech Lead giỏi. Họ hiểu mục tiêu của team mình là gì và xây dựng một tầm nhìn kiến trúc phù hợp. Họ làm việc cùng team để điều chỉnh tầm nhìn đó khi team hiểu rõ hơn về vấn đề cũng như về công nghệ được chọn để giải quyết nó.

## Các kỹ năng cốt lõi của một Tech Lead là gì?

Mặc dù phạm vi công việc của một Tech Lead có thể khác nhau, các kỹ năng cần thiết thì không thay đổi. Một Tech Lead cần xây dựng một bộ kỹ năng cân bằng trong các lĩnh vực sau:

* **Development** – Một Tech Lead phải có nền tảng là một developer. Họ cần biết cách viết code và biết code chất lượng tốt trông như thế nào. Họ cần có khả năng hỗ trợ team trong bất kỳ thử thách kỹ thuật nào, ngay cả khi họ không nhất thiết là người giỏi nhất về lĩnh vực đó.
* **Architecture** – Development chỉ là một phần trong việc xây dựng một hệ thống hoạt động. Tech Lead phải có hiểu biết rộng hơn về cách phần mềm khớp vào hệ thống tổng thể. Họ cần hiểu rõ phần mềm sẽ được deploy, quản lý và vận hành như thế nào trong môi trường production.
* **Leadership** – Một Tech Lead hiệu quả cần có kỹ năng lãnh đạo vững vàng, ngay cả khi họ không phải chịu trách nhiệm quản lý trực tiếp (line management). Các kỹ năng lãnh đạo như coaching, gây ảnh hưởng (influencing) và ủy thác (delegation) là chìa khóa cho thành công.

## Vậy Tech Lead là gì, nhắc lại nào?

> "Tech Lead là một software engineer chịu trách nhiệm dẫn dắt một team và đảm bảo sự thống nhất về định hướng kỹ thuật."

Tech Lead là một software engineer chịu trách nhiệm dẫn dắt một team và đảm bảo sự thống nhất về định hướng kỹ thuật. Họ có thể đồng dẫn dắt một team cùng với các vai trò khác như Product Manager hay Team Lead/Engineering Manager. Nhưng Tech Lead có một trọng tâm đặc trưng là các khía cạnh kỹ thuật, hay nói cách khác là phần "Như thế nào". Một Tech Lead hiệu quả hòa quyện được kỹ năng lãnh đạo mạnh, kỹ năng kiến trúc và kỹ năng development. Họ lèo lái team hướng tới một tầm nhìn kỹ thuật chung. Họ chịu trách nhiệm về chất lượng của các sản phẩm kỹ thuật mà team bàn giao.
