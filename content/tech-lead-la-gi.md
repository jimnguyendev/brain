---
title: 'Tech Lead thực ra là gì? (Tuần 1 — Ngày 1)'
lastmod: '2026-06-04 09:00:00'
tags:
  - tech lead
  - kỹ năng lãnh đạo
---

> Bài học mở đầu trong lộ trình 4 tuần tự học để chuyển từ developer sang Tech Lead. Đúc kết từ bài [The Definition of a Tech Lead](https://medium.com/@patkua/the-definition-of-a-tech-lead-484bb46569f2) của Pat Kua.

Ngộ nhận lớn nhất của một dev sắp lên Tech Lead là nghĩ rằng *Tech Lead = sếp, = người quản lý, = người code giỏi nhất team*. Cả ba đều sai. Hôm nay ta gỡ ngộ nhận đó và trả lời cho được: **Tech Lead khác gì với Engineering Manager và với một senior dev bình thường?**

## Định nghĩa một câu

> **Tech Lead là một software engineer chịu trách nhiệm dẫn dắt một team và đảm bảo sự thống nhất về định hướng kỹ thuật.**

Bóc tách định nghĩa này ra ba tầng:

**1. Vẫn là một engineer.** Tech Lead không rời code. Pat Kua đề xuất mức tối thiểu **~30% thời gian dành cho code** — không phải để "làm cho xong việc", mà để ra quyết định *có cơ sở*, nhận diện rủi ro kỹ thuật, và **giữ được sự tin tưởng của các dev khác**. Một Tech Lead không còn đụng vào code sẽ mất uy tín kỹ thuật rất nhanh.

**2. Trọng tâm là "Như thế nào", không phải "Cái gì".** Đây là cách phân vai dễ nhớ nhất trong một team:

| Vai trò | Lo về | Câu hỏi |
|---|---|---|
| Product Manager | Sản phẩm | **What** — làm tính năng gì |
| Engineering Manager | Con người | **Who** — phát triển, feedback, sự nghiệp |
| **Tech Lead** | Kỹ thuật | **How** — kiến trúc, chất lượng, định hướng |

**3. Dẫn dắt kỹ thuật là phần KHÔNG bao giờ chia sẻ.** Việc dẫn dắt con người có thể chia cho nhiều người, nhưng *technical direction* gần như luôn thuộc về Tech Lead: xây tầm nhìn kỹ thuật, hòa giải tranh luận kỹ thuật, quản chất lượng codebase, quyết định các practice (CI/CD, automated test), và chủ động trả technical debt.

## Ba nhóm kỹ năng cốt lõi

Phạm vi công việc của Tech Lead có thể khác nhau giữa các team, nhưng bộ kỹ năng thì không đổi:

- **Development** — nền tảng là một dev thực thụ, biết code chất lượng tốt trông như thế nào.
- **Architecture** — hiểu hệ thống tổng thể: phần mềm được deploy, vận hành, mở rộng ra sao trong production.
- **Leadership** — coaching, gây ảnh hưởng (influencing), và đặc biệt là **ủy thác (delegation)**.

## Liên hệ với một team nhỏ (không có Engineering Manager)

Đây là phần quan trọng nhất, áp dụng cho rất nhiều team thực tế ở Việt Nam — nơi chỉ có vài dev và không có Engineering Manager riêng. Pat Kua mô tả đúng tình huống này:

> *"Một team có thể chỉ có một Product Manager và một Tech Lead. Trong tình huống này, Tech Lead **kế thừa luôn các trách nhiệm của Engineering Manager**... Mô hình này hoạt động tốt với các team nhỏ."*

Dịch ra thực tế:

- Team nhỏ, không có EM → Tech Lead sẽ là **TL kiêm EM**: vừa lo *How* (kỹ thuật) vừa lo *Who* (phát triển con người, feedback cho đồng đội).
- Cái bẫy lớn nhất: khi quá tải, Tech Lead thường **ngầm ưu tiên chuyện kỹ thuật và bỏ bê chuyện con người**. Người vốn quen "code rất nhiều" càng dễ rơi vào bẫy này — và đó chính là rủi ro cần chủ động bù lại bằng 1:1 và feedback đều đặn.
- Tin tốt: với team nhỏ, mức "30% code" rất khả thi. Không cần ép mình rời code, chỉ cần **giải phóng ~70% còn lại** cho việc dẫn dắt.

## Tự phản chiếu

Ba câu hỏi nên tự trả lời (viết ra 2–3 dòng mỗi câu):

1. Hiện tại tôi dành bao nhiêu % thời gian cho code? Nếu lên Tech Lead, con số đó *nên* là bao nhiêu, và 70% kia tôi dùng vào việc gì?
2. Trong ba nhóm kỹ năng (Development / Architecture / Leadership), tôi mạnh nhất và yếu nhất ở đâu?
3. Trong team tôi, ai đang giữ vai "Cái gì" (Product)? Tôi có cần làm rõ ranh giới trách nhiệm với người đó không?

## Kim chỉ nam

Viết đúng một câu này và dán ở nơi hay nhìn — nó là kim chỉ nam cho cả hành trình:

> *Là Tech Lead, công việc của tôi là dẫn dắt định hướng & chất lượng kỹ thuật cho team, kiêm phát triển con người — chứ không phải là người viết nhiều code nhất.*
