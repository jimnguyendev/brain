---
enableToc: false
title: 'MOC — Backend & Hệ thống phân tán'
lastmod: '2026-06-07 07:10:00'
tags:
  - moc
---

> **Bản đồ nội dung (Map of Content)** cho cụm backend, hạ tầng & hệ thống phân tán. Bấm logo 🧠 góc trên trái để về trang chủ xem các chủ đề khác.

## Global Flash Sale Engine — kiến trúc chịu tải cực hạn

Chuỗi 4 phần mổ xẻ cách dựng một hệ thống flash sale sống sót khi 1 triệu người ùa vào cùng một mili-giây (kèm code Go 1.26, Redis, Kafka và mô phỏng tương tác):

1. [[flash-sale-thundering-herd|Phần 1: Thundering Herd]] — sống sót qua giây đầu tiên (edge cache, token bucket, single-flight)
2. [[flash-sale-admission-control|Phần 2: Admission Control]] — phòng chờ ảo & vé vào cửa có chữ ký
3. [[flash-sale-distributed-inventory|Phần 3: Tồn kho phân tán]] — bài toán Hot-Row & chống oversell
4. [[flash-sale-payment-idempotency|Phần 4: Thanh toán & Idempotency]] — Saga bù trừ & chống tính tiền 2 lần

## Realtime, cache & hạ tầng backend

- [[polling-realtime-etag|Polling cho realtime + ETag]] — làm polling đúng cách và cắt băng thông với `304 Not Modified`
- [[kafka-avro-2-tier-cache|Kafka Avro Producer + cache 2 tầng trên Laravel Horizon]] — debug incident 502 Schema Registry và câu chuyện "cache trông như có mà không chạy"
