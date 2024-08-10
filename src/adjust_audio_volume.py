import os

from pydub import AudioSegment  # type: ignore


def main():
    src_dir = "output"
    dest_dir = "output_adjusted"
    target_dbfs = -14

    for filename in os.listdir(src_dir):
        if filename.endswith(".mp3"):
            audio = AudioSegment.from_mp3(os.path.join(src_dir, filename))
            current_dbfs = audio.dBFS
            adjusted_audio = audio.apply_gain(target_dbfs - current_dbfs)

            path = os.path.join(dest_dir, filename)
            adjusted_audio.export(path, format="mp3")


if __name__ == "__main__":
    main()
