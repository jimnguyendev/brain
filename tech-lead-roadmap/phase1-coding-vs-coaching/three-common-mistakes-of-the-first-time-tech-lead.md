---
title: "Ba sai lầm phổ biến của Tech Lead lần đầu"
original_title: "Three Common Mistakes of the First Time Tech Lead"
source: "https://medium.com/featured-insights/three-common-mistakes-of-the-first-time-tech-lead-aac7a900adab"
phase: "Phase 1 — Cân bằng giữa code và dẫn dắt"
---

# Ba sai lầm phổ biến của Tech Lead lần đầu

> Nguồn: [Three Common Mistakes of the First Time Tech Lead](https://medium.com/featured-insights/three-common-mistakes-of-the-first-time-tech-lead-aac7a900adab)

Tác giả: Patrick Kua

Lần đầu tiên một developer bước vào vai trò Tech Lead có thể rất khó khăn. Kỹ năng và kinh nghiệm của một developer dày dạn không tự động chuyển hóa thành những kỹ năng cần thiết cho vai trò Tech Lead. Trên thực tế, một số thói quen của developer có thể gây hại nhiều hơn là có lợi, khi không được áp dụng đúng cách và với nhiều quyền hạn hơn trong vai trò mới này.

Trong bài viết này, chúng ta cùng khám phá ba cái bẫy phổ biến mà một Tech Lead lần đầu thường gặp, và họ có thể làm gì để tránh chúng.

## 1. Code toàn thời gian

Một Tech Lead lần đầu sẽ nhớ việc viết code. Thực ra, họ rất dễ cho rằng mình cần chứng tỏ khả năng lãnh đạo bằng cách viết code liên tục. Mặc dù các Tech Lead hiệu quả vẫn cần dành một phần thời gian để viết, đọc và review code, nhưng những trách nhiệm khác sẽ bị bỏ ngỏ khi họ dành quá nhiều thời gian viết code — chẳng hạn như tạo ra một tầm nhìn kỹ thuật và đảm bảo cả đội hiểu được các thuộc tính chất lượng then chốt của hệ thống.

Việc thiếu một tầm nhìn kỹ thuật có thể dẫn đến ba cách triển khai khác nhau, khi các developer tự ra quyết định riêng lẻ về điều mà họ cho là tốt nhất; hoặc một lần deploy có thể thất bại vì developer không nắm được các ràng buộc vận hành hay sự khác biệt môi trường trên production. Tệ hơn nữa là khi code phải liên tục được làm lại vì một developer chọn làm theo cách khác mà không xét đến việc bảo trì, hay cách hệ thống có thể tiến hóa theo thời gian.

Một Tech Lead giàu kinh nghiệm hơn hiểu rằng họ phải cân bằng thời gian code với các trách nhiệm khác. Họ phân bổ thời gian theo ngày, hoặc ít nhất là theo tuần, để đảm bảo dành thời gian giải quyết những trách nhiệm khác, bao gồm xây dựng một tầm nhìn kiến trúc chung, nhận diện và xử lý các rủi ro kỹ thuật, tham gia các buổi planning, và tập trung vào sự gắn kết, nhất quán của đội ngũ và code.

## 2. Tự mình ra mọi quyết định kỹ thuật

Một Tech Lead lần đầu đôi khi là developer giàu kinh nghiệm nhất trong đội, hoặc cảm thấy áp lực phải tự ra mọi quyết định kỹ thuật để chứng tỏ quyền hạn hay tầm ảnh hưởng của mình. Khi một Tech Lead ra tất cả các quyết định kỹ thuật, họ trở thành điểm nghẽn (bottleneck) trong đội, và đội không thể tiến triển khi Tech Lead vắng mặt. Các thành viên khác có thể cảm thấy mất động lực khi Tech Lead ra mọi quyết định quan trọng, bởi đóng góp của họ bị gạt bỏ, và điều này có thể dẫn đến sự bất mãn.

Một Tech Lead giàu kinh nghiệm hơn nhận ra rằng có nhiều cách khác nhau để ra quyết định, và thường thì quyết định tốt nhất đến từ việc tận dụng bề rộng kinh nghiệm và kiến thức của cả đội. Họ có thể vận dụng những kỹ thuật sau, tùy vào mức độ quan trọng của quyết định, tốc độ cần ra quyết định, và mức độ cam kết họ muốn có từ các thành viên:

- **Chỉ ủy quyền (Delegating)** — Tech Lead giao quyết định cho người khác mà không có bất kỳ tương tác nào khác.
- **Đưa ra lời khuyên (Offering advice)** — Tech Lead ủy quyền quyết định cho người khác, nhưng đóng góp ý kiến và quan điểm của mình để họ cân nhắc.
- **Hỏi lại (Inquiring)** — Tech Lead ủy quyền quyết định cho người khác, nhưng sau đó hỏi lại về kết quả và những yếu tố dẫn đến quyết định đó.
- **Xây dựng đồng thuận (Building consensus)** — Họ tập hợp tất cả thành viên để tìm ra một giải pháp mà mọi người đều hài lòng.
- **Tham vấn cả đội (Consulting with the team)** — Họ mời ý kiến từ các thành viên, tổng hợp thông tin, nhưng cuối cùng tự đưa ra quyết định.
- **Độc đoán (Being autocratic)** — Họ dùng thông tin mình có để ra quyết định, có thể chọn cho hoặc không cho thành viên tham gia, nhưng vẫn thông báo kết quả cho mọi người.

## 3. Quên việc vun đắp văn hóa đội nhóm

Một đội là một nhóm người cùng làm việc hướng đến một mục tiêu chung. Tech Lead lần đầu có thể nhầm lẫn cho rằng vai trò của mình là dẫn dắt mọi khía cạnh kỹ thuật, mà quên mất cách cả đội làm việc cùng nhau. Mặc dù trách nhiệm này có thể được chia sẻ với các vai trò khác như Team Lead hay Project Manager, một Tech Lead cũng phải dẫn dắt cả đội cùng tiến theo một hướng kỹ thuật.

Tech Lead lần đầu rất dễ phớt lờ những cuộc tranh luận gay gắt giữa hai developer, hay làm ngơ trước việc các thành viên kỹ thuật tương tác tệ hoặc thiếu tôn trọng với các thành viên không thuộc mảng kỹ thuật.

Một Tech Lead giàu kinh nghiệm hơn nhận ra rằng phần "lead" (dẫn dắt) trong vai trò của mình cũng quan trọng ngang với phần "tech" (kỹ thuật), và luôn tìm cách xây dựng niềm tin và mối quan hệ giữa mọi người trong đội. Họ vận dụng những thực hành như cùng nhau vẽ sơ đồ kiến trúc trên bảng trắng, cùng đội thiết lập các nguyên tắc về code hay kiến trúc để định hướng các quyết định cá nhân, hoặc chạy các improvement kata hay retrospective định kỳ.

## Kết luận

Tech Lead lần đầu rất dễ sa vào hàng loạt cái bẫy, thường bắt nguồn từ những thói quen hình thành trong thời gian làm developer. Để vượt qua những cái bẫy này, họ phải tìm cách cân bằng giữa các trách nhiệm kỹ thuật và lãnh đạo của mình.

Tìm hiểu thêm về trải nghiệm của những Tech Lead khác trong cuốn sách 'Talking with Tech Leads' của Patrick. Bạn có thể tải bản đọc thử miễn phí của cuốn sách tại đây.

_Bài viết được đăng lần đầu trên www.thoughtworks.com vào ngày 19 tháng 1 năm 2016._
