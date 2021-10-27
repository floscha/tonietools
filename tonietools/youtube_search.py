from typing import List

from youtubesearchpython import VideosSearch


def _marshal_search_result(result: dict) -> dict:
    return {
        "title": result["title"],
        "url": result["link"],
        "duration": result["duration"],
        "thumbnail": result["thumbnails"][0]["url"],
    }


def search(query: str, limit: int = 5) -> List[dict]:
    results = VideosSearch(query, limit=limit).result()["result"]
    return [_marshal_search_result(r) for r in results]


if __name__ == "__main__":
    import sys
    from pprint import pprint

    pprint(search(sys.argv[1]))
