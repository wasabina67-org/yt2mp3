import os

from pydub import AudioSegment  # type: ignore


def main():
    src_dir = "output"
    dest_dir = "output_adjusted"  # noqa
    target_dbfs = -14  # noqa

    for filename in os.listdir(src_dir):
        if filename.endswith(".mp3"):
            audio = AudioSegment.from_mp3(os.path.join(src_dir, filename))
            print(audio.dBFS)


if __name__ == "__main__":
    main()
