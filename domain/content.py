from enum import Enum, auto

import pandas as pd


class ContentType(Enum):
    """
    内容的类型，枚举
    """
    TEXT = auto()
    TABLE = auto()
    IMAGE = auto()


class Content:
    """书中的内容"""

    def __init__(self, content_type: ContentType, original, translation=None):
        """
        内容初始化
        :param type: 类型
        :param original: 原文
        :param translation: 翻译
        """
        self.content_type = content_type
        self.original = original
        self.translation = translation
        self.satus = False  # 翻译完成的状态

    def set_translation(self, translation, status):
        """
        设置翻译之后的文本，和翻译的状态
        :param translation:
        :param status:
        :return:
        """
        self.translation = translation
        self.status = status

    def check_translation_type(self, translation):
        pass

class TableContent:
    """表格中的内容"""

    def __init__(self, content_type: ContentType, original, translation=None):
        """
        内容初始化
        :param type: 类型
        :param original: 表格原始内容
        :param translation: 翻译
        """
        df = pd.DataFrame(original)
        self.content_type = content_type
        self.original = df
        self.translation = translation
        self.satus = False  # 翻译完成的状态

    def set_translation(self, translation, status):
        """
        设置翻译之后的文本，和翻译的状态
        :param translation:
        :param status:
        :return:
        """
        self.translation = translation
        self.status = status

    def check_translation_type(self, translation):
        pass
