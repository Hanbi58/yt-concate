from pipeline.pipeline import Pipeline
from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.initialize_yt import InitializeYT
from pipeline.steps.download_captions import DownloadCaptions
from utils import Utils
from pipeline.steps.preflight import Preflight
from pipeline.steps.postflight import Postflight
from pipeline.steps.read_caption import ReadCaption
from pipeline.steps.search import Search
from pipeline.steps.download_videos import DownloadVideos
from pipeline.steps.edit_video import EditVideo

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'  # 不变的变量 一般全大写


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,

    }
    steps = [
        Preflight(),
        GetVideoList(),  # 写成多行，增加易读性（最后一个建议有，）
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
