#!/usr/bin/python3
import os
from set_publishing_date import format_post
from set_publishing_date import date_pattern

if __name__ == "__main__":
    posts_dir = os.path.join(os.path.dirname(__file__), "..", "_posts")

    for file in os.listdir(posts_dir):
        if bool(date_pattern.search(file)):
            continue
        format_post(os.path.join(posts_dir, file))
