import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_filepath = self.get_caption_filepath(url)
        self.video_filepath = self.get_video_filepath(url)
        self.captions = None

    def get_caption_filepath(self, url):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_filepath(self, url):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def __str__(self):
        return '<YT(' + self.id + ')>'

    def __repr__(self):
        content = ' : '.join([
            'id=' + str(self.id),
            'caption_filepath=' + str(self.caption_filepath),
            'video_filepath=' + str(self.video_filepath)
        ])
        return '<YT(' + content + ')>'
