import os

from pydub import AudioSegment  # type: ignore
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


def main():
    src_dir = "output"
    dest_dir = "output_adjusted"
    target_dbfs = -14

    for filename in os.listdir(src_dir):
        if filename.endswith(".mp3"):
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            audio = AudioSegment.from_mp3(src_path)
            current_dbfs = audio.dBFS
            adjusted_audio = audio.apply_gain(target_dbfs - current_dbfs)

            adjusted_audio.export(dest_path, format="mp3")

            src_mp3 = MP3(src_path, ID3=EasyID3)
            dest_mp3 = MP3(dest_path, ID3=EasyID3)


if __name__ == "__main__":
    main()
