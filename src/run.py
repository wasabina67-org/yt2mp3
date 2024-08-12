import os
from urllib import request

from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
from PIL import Image
from yt_dlp import YoutubeDL  # type: ignore

from data import yt_list
from utils import check_video_deletion, validate_yt_list

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "outtmpl": None,
}


def set_artwork(videoid, mp3_file_path):
    url = f"https://img.youtube.com/vi/{videoid}/0.jpg"
    artwork_file_path = f"output/{videoid}.jpg"

    with request.urlopen(url) as r:
        data = r.read()
        with open(artwork_file_path, mode="wb") as o:
            o.write(data)

    with Image.open(artwork_file_path) as img:
        resized_img = img.resize((300, 300))
        resized_img.save(artwork_file_path)

    with open(artwork_file_path, mode="rb") as r:
        data = r.read()
        tags = ID3(mp3_file_path)
        tags.add(APIC(mime="image/jpeg", type=3, data=data))
        tags.save()

    os.remove(artwork_file_path)


def set_metadata(metadata, mp3_file_path):
    tags = EasyID3(mp3_file_path)
    tags["title"] = metadata["title"]
    tags["artist"] = metadata["artist"]
    tags.save()


def main():
    if not validate_yt_list():
        raise RuntimeError("Validation failed.")

    for item in yt_list:
        videoid = item["id"]
        output_videoid = f"output/{videoid}"
        mp3_file_path = output_videoid + ".mp3"

        if os.path.isfile(mp3_file_path):
            continue

        url = f"https://i.ytimg.com/vi/{videoid}/hqdefault.jpg"
        if check_video_deletion(url):
            raise RuntimeError(
                f"The Thumbnail Image URL returned a 404 status. ({videoid})"
            )

        ydl_opts["outtmpl"] = output_videoid
        with YoutubeDL(ydl_opts) as ydl:
            url = f"https://www.youtube.com/watch?v={videoid}"
            retcode = ydl.download([url])
            if retcode != 0:
                raise RuntimeError(
                    f"Downloading failed with non-zero return code. ({videoid})"
                )

            set_metadata(item["metadata"], mp3_file_path)
            set_artwork(videoid, mp3_file_path)


if __name__ == "__main__":
    main()
