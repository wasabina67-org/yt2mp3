import os

from mutagen.id3 import ID3
from pydub import AudioSegment  # type: ignore


def main():
    """
    Adjust the volume of audio files in a directory to a target dBFS.

    Returns:
        None
    """
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

            src_id3 = ID3(src_path)
            dest_id3 = ID3(dest_path)
            dest_id3.update(src_id3)
            dest_id3.save()


if __name__ == "__main__":
    main()
