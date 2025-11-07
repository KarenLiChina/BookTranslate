import time
from utils.log_utils import log
import openai
from openai import OpenAI

from ai_model.model import Model


class OpenAIModel(Model):
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.client = OpenAI(api_key=api_key)

    def request_model(self, prompt):
        """
        请求模型的API接口
        返回两个值：1. 翻译之后的文本，2. boolean 表示翻译是否成功
        设计思路：如果失败尝试再去调用API，最多调用三次
        :param prompt:
        :return:
        """
        count = 0  # 调用API的次数
        while count < 3:
            try:
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {'role': 'user', 'content': prompt}
                    ]
                )
                translation = resp.choices[0].message.content.strip()
                return translation, True
            except openai.RateLimitError as e:  # 网络的原因，没有正常返回
                count = count + 1
                if count < 3:
                    # 发出警告，并休眠30s，再次调用API
                    log.warning('调用API失败，30s后自动重试。。。')
                    time.sleep(30)
                else:
                    raise Exception('已经连续调用API接口3次，都失败了，请检测网络')
            except Exception as e:
                log.error(e.__cause__)  # 日志的详细信息
                return '', False
            return '', False
