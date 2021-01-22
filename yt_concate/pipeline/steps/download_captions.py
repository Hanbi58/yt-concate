from pytube import YouTube

from .step import Step
from .step import StepException
from yt_concate.utils import Utils
import time


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print('Downloading caption for: ', url)
            if utils.caption_file_exists(url):
                continue

            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading caption for', url)
                continue

            text_file = open(Utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('Spent', end - start, 'seconds')
