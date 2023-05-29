import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
ARCHIVES = []
MY_OTHER = []


REGISTER_EXTENSION = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "MP3": MP3_AUDIO,
    "ZIP": ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def Scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in (
                "archives",
                "video",
                "audio",
                "documents",
                "images",
                "other",
            ):
                FOLDERS.append(item)
                scan(item)
            continue
        ext = get_extension(item.name)
        full_name = folder / item.name
        if not ext:
            MY_OTHER.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(full_name)


def normalize(text):
    translit_dict = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "",
        "ю": "iu",
        "я": "ia",
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "H",
        "Ґ": "G",
        "Д": "D",
        "Е": "E",
        "Є": "Ye",
        "Ж": "Zh",
        "З": "Z",
        "И": "Y",
        "І": "I",
        "Ї": "Yi",
        "Й": "Y",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "Kh",
        "Ц": "Ts",
        "Ч": "Ch",
        "Ш": "Sh",
        "Щ": "Shch",
        "Ь": "",
        "Ю": "Yu",
        "Я": "Ya",
    }

    normalized_text = ""
    for char in text:
        if char.isalpha() and char in translit_dict:
            normalized_text += translit_dict[char]
        elif char.isdigit() or char.isalpha():
            normalized_text += char
        else:
            normalized_text += "_"

    return normalized_text


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix[1:].upper()  # Отримуємо розширення файлу
            if extension in ["JPEG", "JPG", "PNG", "SVG"]:
                # Додати файл до відповідного списку для зображень
                pass
            elif extension in ["AVI", "MP4", "MOV", "MKV"]:
                # Додати файл до відповідного списку для відео
                pass
            elif extension in ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"]:
                # Додати файл до відповідного списку для документів
                pass
            elif extension in ["MP3", "OGG", "WAV", "AMR"]:
                # Додати файл до відповідного списку для аудіо
                pass
            elif extension in ["ZIP", "GZ", "TAR"]:
                # Додати файл до відповідного списку для архівів
                pass
            else:
                # Додати файл до списку для невідомих розширень
                pass
        elif item.is_dir():
            # Додати папку до списку папок
            pass


def main():
    folder_for_scan = sys.argv[1]
    print(f"Start in folder: {folder_for_scan}")

    scan(Path(folder_for_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Audio mp3: {MP3_AUDIO}")
    print(f"ARCHIVES: {ARCHIVES}")
    print("*" * 25)
    print(f"Types of file in folder: {EXTENSIONS}")
    print(f"UNKNOWN: {MY_OTHER}")


if __name__ == "__main__":
    main()
