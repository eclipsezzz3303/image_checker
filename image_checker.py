from pathlib import Path
from PIL import Image

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}

def check_image(path):
    path = Path(path)

    if path.suffix.lower() not in IMAGE_EXTENSIONS:
        return {
            "name": path.name,
            "status": "not_image",
            "width": None,
            "height": None,
            "format": None,
        }
    
    try:
        with Image.open(path) as img:
            img.verify()

        with Image.open(path) as img:
            return {
                "name": path.name,
                "status": "ok",
                "width": img.width,
                "height": img.height,
                "format": img.format
            }
    except Exception:
        # print(f"[DEBUG] {path.name} 打开失败: {type(e).__name__}: {e}")
        return {
            "name": path.name,
            "status": "broken",
            "width": None,
            "height": None,
            "format": None
        }
    
def scan_folder(folder):
    folder = Path(folder)
    results = []

    for item in sorted(folder.iterdir()):
        if item.is_file():
            results.append(check_image(item))
    return results   

def summarize(results):
    summary = {
        "total": len(results),
        "ok": 0,
        "broken": 0,
        "not_image": 0
    }
    for r in results:
        status = r["status"]
        summary[status] += 1
    return summary

def build_report_text(results):

    summary = summarize(results)

    lines = []
    lines.append("=" * 50)
    lines.append("图片检查报告")
    lines.append("=" * 50)
    lines.append(f"总文件数 : {summary['total']}")
    lines.append(f"正常     : {summary['ok']}")
    lines.append(f"损坏     : {summary['broken']}")
    lines.append(f"非图片   : {summary['not_image']}")
    lines.append("-" * 50)

    print(lines)

    lines.append(f"{'文件名':<16}{'状态':<12}{'尺寸':<12}{'格式'}")
    lines.append("-" * 50)
    for r in results:
        size = f"{r['width']}x{r['height']}" if r["width"] is not None else "-" 
        fmt = r["format"] if r["format"] else "-"
        lines.append(f"{r['name']:<20}{r['status']:<12}{size:<15}{fmt}")

    return "\n".join(lines)

def print_report(results):
    print(build_report_text(results))

def save_report(results, output_path="report.txt"):
    text = build_report_text(results)
    Path(output_path).write_text(text, encoding="utf-8")
    print(f"报告已保存到：{output_path}")

if __name__ == "__main__":
    results = scan_folder("images")
    print_report(results)
    save_report(results, "report.txt")