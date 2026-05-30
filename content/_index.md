---
enableToc: false
title: "Bộ não thứ 2 🧠"
lastmod: '2026-05-29 11:00:00'
---

Đây là **bộ não thứ hai** (second brain) công khai của tôi — một [[digital-garden|khu vườn số]] nơi tôi ghi lại và kết nối những gì mình học được.

## Cách dùng
Bạn có thể lang thang trong não tôi bằng cách bấm vào các liên kết `[[...]]` để đi sâu hơn, dùng ô tìm kiếm góc trên bên phải, hoặc `cmd+k` (`ctrl+k` trên Windows).

## Map of Content (MOC)

### Triết lý thiết kế phần mềm
Một chuỗi bài về vì sao phần mềm trở nên khó, và làm sao chống lại điều đó:

1. [[complexity-ousterhout|Complexity của Ousterhout]] — kẻ thù số một của phần mềm
2. [[software-entropy|Software Entropy]] — vì sao code tự mục nát theo thời gian
3. [[no-one-knows-what-they-want|No one knows what they want]] — sự thật phũ phàng về requirements
4. [[the-design-concept|The Design Concept (Brooks)]] — conceptual integrity làm kim chỉ nam
5. [[small-steps-feedback|Bước nhỏ + Feedback loop]] — tốc độ đến từ vòng lặp phản hồi ngắn
6. [[tactical-vs-strategic-programming|Tactical vs Strategic Programming]] — hai tư duy lập trình

### Global Flash Sale Engine — kiến trúc chịu tải cực hạn
Chuỗi 4 phần mổ xẻ cách dựng một hệ thống flash sale sống sót khi 1 triệu người ùa vào cùng một mili-giây (kèm code Go 1.26, Redis, Kafka và mô phỏng tương tác):

1. [[flash-sale-thundering-herd|Phần 1: Thundering Herd]] — sống sót qua giây đầu tiên (edge cache, token bucket, single-flight)
2. [[flash-sale-admission-control|Phần 2: Admission Control]] — phòng chờ ảo & vé vào cửa có chữ ký
3. [[flash-sale-distributed-inventory|Phần 3: Tồn kho phân tán]] — bài toán Hot-Row & chống oversell
4. [[flash-sale-payment-idempotency|Phần 4: Thanh toán & Idempotency]] — Saga bù trừ & chống tính tiền 2 lần

### Realtime, cache & hạ tầng backend
- [[polling-realtime-etag|Polling cho realtime + ETag]] — làm polling đúng cách và cắt băng thông với `304 Not Modified`
- [[kafka-avro-2-tier-cache|Kafka Avro Producer + cache 2 tầng trên Laravel Horizon]] — debug incident 502 Schema Registry và câu chuyện "cache trông như có mà không chạy"

### Trên đường thành Tech Lead — lộ trình 4 tuần
Hành trình tự học chuyển từ developer sang Tech Lead, mỗi ngày một bài đúc kết kèm liên hệ thực tế team nhỏ:

1. [[tech-lead-la-gi|Tech Lead thực ra là gì?]] — gỡ ngộ nhận "TL = sếp/coder giỏi nhất", phân vai What/Who/How
2. [[tech-lead-vai-tro-hay-bay|Tech Lead có thật sự là một vai trò?]] — góc nhìn phản biện: TL giỏi là TL làm team bớt phụ thuộc vào mình
3. [[tech-lead-hay-engineering-manager|Chọn Tech Lead hay Engineering Manager?]] — hai trục phát triển, ranh giới mờ, và sức mạnh của 1:1
4. [[tech-lead-tot-tech-lead-te|Tech Lead tốt, Tech Lead tệ]] — 9 tấm gương giỏi/tệ + checklist tự chấm điểm đóng tuần 1
5. [[tech-lead-can-bang-code-va-coaching|Force multiplier: cân bằng code và coaching]] — làm bản đồ thay vì tài xế, bỏ vai Atlas, chia sẻ "viên đá cưng"
6. [[tech-lead-5-sai-lam-lon-nhat|5 sai lầm lớn nhất khi lên Tech Lead]] — những cú vấp kinh điển của TL mới và cách né
7. [[tech-lead-3-sai-lam-lan-dau|3 cái bẫy của Tech Lead lần đầu]] — code toàn thời gian, ôm hết quyết định, bỏ quên văn hoá đội
8. [[tech-lead-khong-tung-hung-uu-tien|Người lãnh đạo giỏi không tung hứng ưu tiên]] — tập trung một việc thay vì tung hứng tất cả *(hết Tuần 2)*
9. [[code-review-kim-tu-thap-maslow|Kim tự tháp Maslow của code review]] — review theo đúng thứ tự: Đúng → An toàn → Dễ đọc → Thanh lịch
10. [[code-review-team-tu-xa|Code review từ xa: viết review như viết một lá thư]] — giao tiếp bất đồng bộ, rõ ràng, đúng giọng
11. [[tech-lead-dua-phan-hoi-phe-binh|Đưa phản hồi phê bình mà không phá vỡ niềm tin]] — khung phản hồi, tách hành vi khỏi con người
12. [[tech-lead-the-hien-lanh-dao-tu-cach-ic|Lãnh đạo không cần chức danh]] — dẫn dắt khi bạn vẫn là Individual Contributor *(hết Tuần 3)*
13. [[tech-lead-the-managers-path-mentoring|Mentoring — bài tập lãnh đạo đầu tiên]] — *The Manager's Path*, chương Mentoring
14. [[tech-lead-the-managers-path-tech-lead|Tech Lead trong The Manager's Path]] — ba chiếc mũ của TL, dẫn bằng ảnh hưởng *(hết Tuần 4)*
15. [[tech-lead-chot-lo-trinh-4-tuan|Chốt lộ trình 4 tuần]] — tổng kết, checklist tự chấm điểm & kế hoạch một tháng tới ✅
