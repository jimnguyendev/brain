---
title: 'Ghi chú riêng tư (mẫu)'
lastmod: '2026-06-07 09:00:00'
private: true
build:
  list: never
  render: always
tags:
  - riêng tư
---

> Đây là một note **riêng tư** mẫu. Nó đã được render thành HTML nhưng bị mã hoá
> bằng StatiCrypt khi deploy — phải nhập mật khẩu chung mới xem được. Note này
> KHÔNG xuất hiện trong tìm kiếm, đồ thị tương tác, backlinks, hay trang chủ.

Thay nội dung này bằng ghi chú riêng của bạn. Cách tạo một note riêng tư:

1. Tạo file `.md` mới trong `content/`.
2. Thêm vào front matter hai dòng quan trọng:
   - `private: true`
   - khối `build:` với `list: never` và `render: always`.
3. Deploy như bình thường — pipeline sẽ tự mã hoá trang này.

Mọi thứ bên dưới chỉ hiển thị sau khi nhập đúng mật khẩu.
