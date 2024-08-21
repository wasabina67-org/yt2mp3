import requests  # type: ignore

from data import yt_list


def validate_yt_list():
    """
    Validates the YouTube video list.

    Returns:
        bool: True if validation is successful, False if any check fails.
    """
    seen_ids = set()
    seen_title_artist = set()

    for item in yt_list:
        videoid = item.get("id")
        if not videoid:
            # None or Empty
            return False
        if videoid in seen_ids:
            # Duplicate
            return False
        seen_ids.add(videoid)

        metadata = item.get("metadata")
        if not metadata:
            # None or Empty
            return False

        title = metadata.get("title")
        if not title:
            # None or Empty
            return False

        artist = metadata.get("artist")
        if not artist:
            # None or Empty
            return False

        title_artist = title + artist
        if title_artist in seen_title_artist:
            # Duplicate
            return False
        seen_title_artist.add(title_artist)

        return True


def check_video_deletion(url):
    """
    Check video deletion.

    Args:
        url (str): Thumbnail Image URL

    Returns:
        bool: True if the video is deleted, False otherwise.
    """
    resp = requests.head(url)
    if resp.status_code == 404:
        return True
    return False
