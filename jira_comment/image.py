from pathlib import Path
from typing import Optional
from hashlib import sha256
from .base import JiraBase
from .settings import settings

def make_new_name(source: Path):
    suffix = source.suffix
    hasher = sha256()
    hasher.update(source.read_bytes())
    stem = hasher.hexdigest()
    return f"{stem}{suffix}"


class ImageDirChanger:
    def __init__(self, dirname):
        self.dirname = Path(dirname)

    def __enter__(self):
        settings.push_image_directory(self.dirname)

    def __exit__(self, _type, _value, _traceback):
        settings.pop_image_directory()


def image_directory(dirname):
    return ImageDirChanger(dirname)


class Image(JiraBase):
    def __init__(self, src: Path, content_dir: Optional[Path] = None):
        self.src = Path(src).expanduser()
        self.new_name = make_new_name(self.src)
        self.content_dir = Path(content_dir) if content_dir is not None else settings.image_directory
        self.content_dir.mkdir(parents=True, exist_ok=True)

    def render(self):
        dst_filename = self.content_dir / self.new_name
        if not dst_filename.is_file():
            dst_filename.write_bytes(self.src.read_bytes())

        return f"!{self.new_name}|thumbnail!"

