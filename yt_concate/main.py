from pipeline.pipeline import Pipeline
from pipeline.steps.get_video_list import GetVideoList

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'  # 不变的变量 一般全大写


def main():
    inputs = {
        'channel_id': CHANNEL_ID,

    }
    steps = [
        GetVideoList(),  # 写成多行，增加易读性（最后一个建议有，）
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
