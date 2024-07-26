from yt_dlp import YoutubeDL  # type: ignore

from data import yt_list
from utils import validate_yt_list

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
    pass


def set_metadata(metadata, mp3_file_path):
    pass


def main():
    if not validate_yt_list():
        raise RuntimeError("Validation failed.")

    for item in yt_list:
        videoid = item["id"]
        output_videoid = f"output/{videoid}"
        mp3_file_path = output_videoid + ".mp3"  # noqa

        # Check MP3 existing

        # check_video_deletion()

        ydl_opts["outtmpl"] = output_videoid
        with YoutubeDL(ydl_opts) as ydl:
            url = f"https://www.youtube.com/watch?v={videoid}"
            retcode = ydl.download([url])
            if retcode != 0:
                raise RuntimeError(
                    f"Downloading failed with non-zero return code. ({videoid})"
                )


if __name__ == "__main__":
    main()
