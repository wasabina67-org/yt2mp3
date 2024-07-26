from data import yt_list
from utils import validate_yt_list


def main():
    if not validate_yt_list():
        raise RuntimeError("Validation failed.")

    for item in yt_list:
        videoid = item["id"]
        print(videoid)


if __name__ == "__main__":
    main()
