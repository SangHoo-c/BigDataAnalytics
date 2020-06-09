# -*- coding: utf-8 -*-
from icrawler.builtin import GoogleImageCrawler


def main():
    # your keyword
    word = '박보영'

    # your image repository
    dir_name = './images/park'

    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': dir_name})

    google_crawler.crawl(keyword=word, offset=0, max_num=200,
                         min_size=(200, 200), max_size=None, file_idx_offset=0)


if __name__ == "__main__":
    main()

