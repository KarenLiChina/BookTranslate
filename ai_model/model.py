class Model:
    """
    AI的模型对象，抽象类
    """

    def request_model(self, prompt):
        """
        请求模型的API接口，父类不提供函数的实现
        :param prompt:
        :return:
        """
        print('send request to Model')
