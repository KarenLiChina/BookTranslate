import os
from dotenv import load_dotenv

from ai_model.glm_model import ChatGLMModel
from ai_model.openai_model import OpenAIModel
from translate.book_translator import PDFTranslator
from utils.argument_utils import ArgumentUtils
from utils.load_config import LoadConfig

if __name__ == '__main__':
    load_dotenv()

    # 启动命令中的参数解析和验证，并返回所有参数
    arg_utils = ArgumentUtils()
    args = arg_utils.parse_arg()

    # 读取配置文件 YAML
    load_config = LoadConfig(args.config)
    config = load_config.load_config()

    # 模型的名字：先从命令行参数中获取，否则从配置文件中获取
    model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
    # api key
    api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']

    # 初始化模型对象
    if args.model_type == 'OpenAIModel':
        model = OpenAIModel(model_name, api_key)
    else:
        # model = ChatGLMModel()
        pass
    # 初始化一个翻译器,得到入口文件路径
    file_path: str = args.book if args.book else config['common']['book']
    file_format: str = args.book.file_format if args.book else config['common']['file_format']

    if file_path[file_path.rindex('.')].lower() == '.pdf':
        translator = PDFTranslator(model)
    else:
        pass # 其他格式的书籍
    translator.translate_book(file_path,file_format)
