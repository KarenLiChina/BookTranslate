from typing import Optional
from .pdf_parser import parse_pdf
from ai_model.model import Model
from utils.log_utils import log


class PDFTranslator:
    """
    翻译PDF文件的书籍
    """

    def __init__(self, model: Model):
        self.model = model

    def translate_book(self, file_path: str, out_file_format: str = 'PDF', target_language: str = '中文',
                       out_file_path: str = None, pages: Optional[int] = None):
        """
        翻译一本书
        :param file_path:
        :param out_file_format:
        :param target_language:
        :param out_file_path:
        :param pages:
        :return:
        """
        pass
        self.book = parse_pdf(file_path, pages)  # 解析文件得到一个book对象

        for page_index, page in enumerate(self.book.pages):
            for content_index, content in enumerate(page.contents):
                # 翻译每一个内容
                # 1. 得到翻译的提示文本
                prompt = self.model.make_prompt(content, target_language)
                log.debug('大语言模型的提示信息：' + prompt)
                translation_test, status = self.model.request_model(prompt)

                log.debug(f'翻译之后的内容是：{translation_test}')
                #把翻译之后的文本和状态设置到content对象中
                self.book.pages[page_index].contents[content_index].set_translate(translation_test, status)
