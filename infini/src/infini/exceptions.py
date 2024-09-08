class InfiniException(Exception):
    """Infini 异常基类"""


class KeyError(InfiniException):
    """键值错误"""


class UnknownEvent(InfiniException):
    """文本事件不存在"""


class UnknownEventType(InfiniException, TypeError):
    """事件类型不存在"""


class ValueError(InfiniException, ValueError):
    """错误的数据"""
