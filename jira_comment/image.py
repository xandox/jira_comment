from pathlib import Path
from typing import Optional
from hashlib import sha256
from .base import JiraBase

def make_new_name(source: Path):
    suffix = source.suffix
    hasher = sha256()
    hasher.update(source.read_bytes())
    stem = hasher.hexdigest()
    return f"{stem}{suffix}"



GLOBAL_IMAGE_DIR = Path("./images")

class ImageDirChanger:
    def __init__(self, dirname):
        self.dirname = Path(dirname)
        self.global_old_value = GLOBAL_IMAGE_DIR

    def __enter__(self):
        global GLOBAL_IMAGE_DIR
        GLOBAL_IMAGE_DIR = self.dirname

    def __exit__(self, _type, _value, _traceback):
        global GLOBAL_IMAGE_DIR
        GLOBAL_IMAGE_DIR = self.global_old_value


def image_directory(dirname):
    return ImageDirChanger(dirname)


class Image(JiraBase):
    def __init__(self, src: Path, content_dir: Optional[Path] = None):
        self.src = Path(src).expanduser()
        self.new_name = make_new_name(self.src)
        self.content_dir = Path(content_dir) if content_dir is not None else GLOBAL_IMAGE_DIR
        self.content_dir.mkdir(parents=True, exist_ok=True)

    def render(self):
        dst_filename = self.content_dir / self.new_name
        if not dst_filename.is_file():
            dst_filename.write_bytes(self.src.read_bytes())

        return f"!{self.new_name}|thumbnail!"

