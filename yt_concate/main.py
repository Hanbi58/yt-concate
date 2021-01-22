from pipeline.pipeline import Pipeline
from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.download_captions import DownloadCaptions
from utils import Utils
from pipeline.steps.preflight import Preflight
from pipeline.steps.postflight import Postflight

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'  # 不变的变量 一般全大写


def main():
    inputs = {
        'channel_id': CHANNEL_ID,

    }
    steps = [
        Preflight(),
        GetVideoList(),  # 写成多行，增加易读性（最后一个建议有，）
        DownloadCaptions(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
