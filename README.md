# Story Narration Skills (sn-*)

Bộ **7 skill cho Claude Code** để viết **kịch bản video kể chuyện dài 30–120+ phút** (truyện có lời dẫn, truyện audio, phim truyện kể), đầu ra **tiếng Việt**: từ ý tưởng → hồ sơ truyện → dàn ý → lời dẫn từng chương → **review chi tiết bắt buộc** → danh sách shot để sinh prompt ảnh/video.

*A Claude Code plugin with 7 skills for writing long (30–120+ min) narrated story videos with Vietnamese output — from idea to a verified script and a shot list. Skill instructions are in English; the scripts they produce are in Vietnamese.*

## Cài đặt

Trong Claude Code:

```
/plugin marketplace add soul0710/story-narration-skills
/plugin install story-narration@story-narration
```

Hoặc chép tay 7 thư mục trong `plugins/story-narration/skills/` vào `~/.claude/skills/` (giữ nguyên chúng nằm cạnh nhau — các skill con dùng chung tài liệu và script trong `sn-studio`).

Yêu cầu: Python 3 (chỉ dùng thư viện chuẩn) cho script kiểm tra `sn.py`.

## Cách dùng

Bắt đầu luôn bằng:

```
/sn-studio
```

rồi nói ý tưởng, ví dụ: *"Bắt đầu dự án truyện mới: 45 phút, về một cô gái về quê tìm ra bức thư của người ông đã mất."* `sn-studio` sẽ dẫn qua từng bước; sau mỗi bước bạn duyệt rồi mới đi tiếp.

| Bước | Skill | Làm gì |
|---|---|---|
| 0 | `sn-studio` | Điểm vào: tạo / tiếp tục dự án, xem tiến độ, chọn bước |
| 1 | `sn-premise` | Ý tưởng hoặc truyện gốc → logline, thể loại, chế độ *dramatic / calm*, người kể, **ngân sách thời lượng theo âm tiết** (có đo tốc độ giọng thật) |
| 2 | `sn-bible` | Nhân vật (muốn / cần / nỗi sợ / giới hạn / giọng / xưng hô), thế giới, bối cảnh, đạo cụ, **khóa canon**, chi tiết đời thực cần kiểm chứng |
| 3 | `sn-outline` | Chia chương 4–7 phút: bước ngoặt, nguyên nhân → lựa chọn → hậu quả, đường cong cường độ, móc cuối chương, cài – trả chi tiết |
| 4 | `sn-write` | Viết lời dẫn tiếng Việt từng chương, định dạng có thẻ `[HÌNH] [DẪN] [THOẠI] [ÂM] [NHẠC] [NGỪNG]`, hình ảnh dựng được bằng AI video, **review chi tiết sau mỗi chương** |
| 5 | `sn-review` | Soát toàn truyện theo thứ tự logic → nhân vật → câu chữ; mỗi lỗi có trích dẫn, căn cứ, phân loại; xuất file TTS, file lồng tiếng, mốc thời gian YouTube |
| 6 | `sn-shots` | Chương → `kich_ban_chNN.md` (STYLE ANCHOR + SHOT) cho các skill sinh prompt ảnh/video, kèm bản đồ lời dẫn theo từng shot |

## Script kiểm tra `sn.py`

```
python3 sn-studio/scripts/sn.py <lệnh> <thư-mục-dự-án>
```

| Lệnh | Kiểm tra |
|---|---|
| `init`, `budget` | Tạo dự án; tính số âm tiết cần cho thời lượng |
| `outline` | Tổng thời lượng, cài trước trả sau, móc lặp, vùng chết, vị trí cao trào, nhân quả |
| `duration` | Thời lượng từng chương (±10%) |
| `continuity` | Nhân vật chết mà xuất hiện, giải chi tiết trước khi cài, nhân vật dùng thông tin chưa biết |
| `lint` | Cụm từ "giọng AI" tiếng Việt, câu quá dài khó nghe, chữ số trong lời dẫn, hình ảnh khó dựng |
| `audit` | Toàn truyện: lặp qua các chương, kết chương giống nhau, tên riêng ngoài canon, giọng từng nhân vật, nhịp cảnh, chi tiết đời thực chưa kiểm chứng |
| `segment`, `shots` | Chia lời dẫn theo clip 8 giây; kiểm tra shot phủ đủ lời dẫn, đúng thứ tự |
| `snapshot`, `changes` | Lưu phiên bản trước khi sửa; liệt kê thay đổi, báo dòng lời dẫn bị xóa |
| `export` | `narration.txt` cho TTS, bản cho người lồng tiếng, mốc thời gian YouTube |

Lỗi cấu trúc là `✗` (chặn); lỗi về tay nghề / khẩu vị là `!` (cảnh báo, có thể giữ nếu có lý do).

## Nguyên tắc chính

- **Review chi tiết sau mỗi lần viết** — đọc lại toàn văn từ file và soát theo checklist; script chạy qua hay "nhớ lúc viết" đều không tính là review.
- **Sửa theo thứ tự: logic → nhân vật & nhịp → câu chữ.**
- **Đề xuất của AI không tự thành sự thật trong truyện** — chi tiết mới vào `bible/proposals.md`, chỉ thành canon khi người dùng duyệt.
- **Nhìn cả truyện, không chỉ từng chương** — lỗi nguy hiểm nhất của AI là từng chương ổn mà cả truyện không ổn.
- Checklist 30 lỗi AI thường gặp: [`ai-failure-modes.md`](plugins/story-narration/skills/sn-studio/references/ai-failure-modes.md); quy trình review: [`review-protocol.md`](plugins/story-narration/skills/sn-studio/references/review-protocol.md).

## Ví dụ

[`examples/buc-thu-cua-ong/`](examples/buc-thu-cua-ong/) — truyện thử 30 phút *"Bức thư của ông"* (gia đình / bí ẩn, miền Tây) chạy trọn quy trình: brief, hồ sơ truyện, dàn ý, 6 chương lời dẫn (tổng ước tính 29:10; giọng TTS thật đọc hết 29:03 trước các khoảng ngừng), 4 lượt review có ghi lỗi và cách sửa, shot list chương 1 (40 shot).

## Tương thích

Đầu ra của `sn-shots` theo định dạng `kich_ban.md` (STYLE ANCHOR + SHOT) dùng được với các skill sinh prompt ảnh/video dạng *scene* hoặc *storyboard* (trường `Nhạc` cho nhánh nhịp chậm, `Âm thanh` + `Hình ảnh` cho nhánh điện ảnh).

## Ghi công

Phương pháp được chắt lọc và viết lại từ các dự án mã nguồn mở (MIT / Apache-2.0): [0xsline/short-drama](https://github.com/0xsline/short-drama), [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills), [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills), [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode), [jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills), [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills). Chi tiết từng phần lấy từ đâu: [`CREDITS.md`](plugins/story-narration/skills/sn-studio/CREDITS.md); giấy phép gốc: [`licenses/`](plugins/story-narration/skills/sn-studio/licenses/). Trong tài liệu, mỗi ý được đánh dấu **[src]** (từ nguồn) hoặc **[sn]** (bổ sung riêng của bộ này).

## Giấy phép

MIT — xem [LICENSE](LICENSE).
