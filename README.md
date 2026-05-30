# Bộ não thứ hai công khai (Second Brain)

Một *digital garden* cá nhân — nơi ghi lại và kết nối những gì tôi học được, theo
tinh thần [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten). Xem tại
[jimnguyendev.github.io/brain](https://jimnguyendev.github.io/brain).

Dự án được **fork** từ [Quartz](https://github.com/jackyzha0/quartz)
([v3](https://github.com/jackyzha0/quartz/tree/hugo), chạy trên Hugo) và bản mở rộng
của [sspaeti/second-brain-public](https://github.com/sspaeti/second-brain-public),
sau đó được **đổi giao diện theo phong cách Claude / Anthropic** và **bản địa hoá
tiếng Việt**.

## Đặc điểm chính

- **Giao diện Claude / Anthropic** — bộ ba màu cream `#faf9f5` + coral `#cc785c` +
  navy, font Cormorant Garamond + Inter + JetBrains Mono. Toàn bộ quy chuẩn nằm
  trong [`DESIGN.md`](DESIGN.md); token được ánh xạ trong `assets/styles/custom.scss`.
- **Tiếng Việt** — chuỗi giao diện (`i18n/en.toml`), định dạng ngày `dd/MM/yyyy`,
  popover dùng locale `vi-VN`.
- **Liên kết & đồ thị** — wikilink `[[...]]`, backlink và graph dựng bằng
  [hugo-obsidian](https://github.com/jackyzha0/hugo-obsidian).
- **Nội dung giàu kiểu Claude.ai**:
  - Sơ đồ **Mermaid** render trực tiếp từ code block.
  - **HTML / SVG / `<canvas>` + `<script>`** nhúng thẳng trong ghi chú để tạo
    minh hoạ tương tác (goldmark `unsafe=true`).
  - SPA router chạy lại script nhúng sau khi điều hướng.
- **Thẻ (tag)** — quy ước 2–3 thẻ/ghi chú, mỗi thẻ nhóm ≥2 ghi chú, dùng bộ từ
  vựng kiểm soát; hiển thị dạng `badge-pill`.

## Cấu trúc

- `content/` — các ghi chú Markdown (commit trực tiếp trong repo này).
- `layouts/`, `assets/`, `i18n/`, `data/` — theme Hugo/Quartz đã tuỳ biến.
- `DESIGN.md` — quy chuẩn thiết kế (nguồn chân lý cho HTML/CSS).
- `CLAUDE.md` — hướng dẫn cho Claude Code khi làm việc trong repo.
- `utils/` — script xử lý nội dung (xem bên dưới).

## Lệnh thường dùng

```bash
# Chạy server phát triển cục bộ (xem ghi chú baseURL bên dưới)
hugo server --enableGitInfo --minify --baseURL "http://localhost:1313/brain/" --appendPort=false

# Build tĩnh
hugo --gc --minify

# Tạo lại index backlink/graph (cần Go)
go install github.com/jackyzha0/hugo-obsidian@latest
hugo-obsidian -input=content -output=assets/indices -index=true -root=.
```

> **Lưu ý baseURL khi chạy cục bộ:** theme dựng đường dẫn CSS/JS theo `baseURL`
> tuyệt đối, nên phải ép `--baseURL "http://localhost:1313/brain/"`, nếu không trang
> sẽ tải CSS từ domain production và bị 404 (mất hoàn toàn style).

## Triển khai (GitHub Pages)

`.github/workflows/deploy.yaml` tự động build và deploy lên GitHub Pages mỗi khi
push lên nhánh `hugo`: checkout → cài `hugo-obsidian` → dựng index → `hugo --minify`
→ `upload-pages-artifact` → `deploy-pages`.

Cần làm một lần trên GitHub:

1. **Settings → Pages → Source: GitHub Actions**.
2. Theme hardcode đường dẫn `/brain/`. Để URL chạy đúng, repo nên đặt tên **`brain`**
   (→ `https://<user>.github.io/brain/`) hoặc dùng custom domain phục vụ tại `/brain/`.

## Quy trình nội dung

Ghi chú được viết bằng [Obsidian](https://obsidian.md) rồi đưa vào `content/` dưới
dạng Markdown thường (frontmatter `title`, `lastmod`, `tags`; phần đầu có thể chứa
wikilink và sơ đồ Mermaid). Các tiện ích trong `utils/` (kế thừa từ repo gốc) hỗ trợ
tự động hoá việc xuất bản từ vault Obsidian:

- **`utils/obsidian-quartz/`** — CLI viết bằng Rust xử lý ghi chú gắn `#publish`:
  frontmatter, ảnh, tạo OG image, chuẩn hoá callout… Xem
  [utils/obsidian-quartz/README.md](./utils/obsidian-quartz/README.md).
- **`utils/find-publish-notes.py`** — phương án Python (cũ).
- **`utils/split_articles.py`** — script một lần dùng để tách các bài viết khởi tạo
  từ `docs/` thành ghi chú riêng.

## Ghi nhận (Credits)

- [Quartz](https://github.com/jackyzha0/quartz) của Jacky Zhao.
- [hugo-obsidian](https://github.com/jackyzha0/hugo-obsidian).
- Bản mở rộng & nhiều tính năng xuất bản từ
  [sspaeti/second-brain-public](https://github.com/sspaeti/second-brain-public).
