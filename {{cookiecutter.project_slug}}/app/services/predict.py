import os
from os.path import join as pjoin
from typing import Callable

from core.config import MODEL_DIR, MODEL_NAME
from core.errors import ModelLoadException, PredictException
from loguru import logger



class MachineLearningModelHandlerScore(object):
    model = None

    @classmethod
    def predict(cls, input, load_wrapper: Callable =None, method="predict"):
        """使用load_warpper.predict来进行预测

        Args:
            input (Any): 可以被load_wrapper加载得到的对象进行predict的输入
            load_wrapper (func, optional): 用来加载模型的函数. Defaults to None.
            method (str, optional): mode.method. Defaults to "predict".

        Raises:
            PredictException: model没有method方法

        Returns:
            Any: 预测结果
        """
        clf = cls.get_model(load_wrapper)
        if hasattr(clf, method):
            return getattr(clf, method)(input)
        raise PredictException(f"'{method}' attribute is missing")

    @classmethod
    def get_model(cls, load_wrapper: Callable):
        """使用load_wrapper获得model，或者使用self.model获得model

        Args:
            load_wrapper (func): 加载模型的函数

        Returns:
            _type_: 
        """
        if cls.model is None and load_wrapper:
            cls.model = cls.load(load_wrapper)
        return cls.model

    @staticmethod
    def load(load_wrapper: Callable):
        """加载模型

        Args:
            load_wrapper (func): 加载模型的函数

        Raises:
            FileNotFoundError: 没有找到模型文件
            ModelLoadException: 模型函数无法加载该模型文件

        Returns:
            _type_: 模型对象
        """
        model = None
        path = pjoin(MODEL_DIR, MODEL_NAME)
        if not os.path.exists(path):
            message = f"Machine learning model at {path} not exists!"
            logger.error(message)
            raise FileNotFoundError(message)
        model = load_wrapper(path)
        if not model:
            message = f"Model {model} could not load!"
            logger.error(message)
            raise ModelLoadException(message)
        return model
