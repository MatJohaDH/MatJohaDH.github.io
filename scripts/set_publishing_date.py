#!/usr/bin/python3
import os
import re
from datetime import datetime
import sys

date_pattern = re.compile(r"\d\d\d\d-\d\d-\d\d")
post_metadata = re.compile(r"^---.+---", flags=re.DOTALL)
meta_extractor = re.compile(r"(\n[^:]+):([^\n]+)")
whites = re.compile(r"\s+")
post_date = re.compile(r"\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d +\d\d:\d\d")

date, time = datetime.isoformat(datetime.now(), timespec="seconds").split("T")


def meta_to_dict(meta):
    print(meta)
    meta_dict = {
        key.strip(): whites.sub(" ", item.strip())
        for key, item in meta_extractor.findall(meta)
    }

    print(meta_dict)

    print(meta_dict["categories"])
    meta_dict["categories"] = [
        category.strip()
        for category in re.sub(r"[\[\]]", "", meta_dict["categories"]).split(",")
    ]
    print(meta_dict["categories"])

    with open("log.txt", "a+") as f:
        f.write(str(meta_dict))

    if "title" not in meta_dict:
        raise AttributeError("Missing title")

    elif len(meta_dict["categories"]) < 1:
        raise ValueError("Post has no categories")

    meta_dict["categories"] = "[" + ", ".join(meta_dict["categories"]) + "]"

    return meta_dict


def format_post(file):
    with open(file, "r", encoding="utf8") as f:
        post = f.read()

    meta = post_metadata.findall(post)[0]

    meta_dict = meta_to_dict(meta)

    if "date" not in meta_dict or not bool(post_date.search(meta_dict["date"])):
        meta_dict["date"] = " ".join((date, time, "+0200"))

    title = meta_dict["title"].replace(" ", "-").replace('"', "")

    meta_dict["layout"] = "post"

    new_meta = (
        "---\n"
        + "\n".join(f"{key}: {item}" for key, item in meta_dict.items())
        + "\n---\n"
    )

    post = post_metadata.sub(new_meta, post)

    print(post)

    with open(file, "w", encoding="utf8") as f:
        f.write(post)

    post_dir = os.path.dirname(file)
    new_file_name = date + "-" + title + ".markdown"
    new_file_path = os.path.join(post_dir, new_file_name.lower())

    os.rename(file, new_file_path)


for file in sys.argv:
    if not file.startswith("_posts/") or not file.endswith(".markdown"):
        continue

    format_post(file)
