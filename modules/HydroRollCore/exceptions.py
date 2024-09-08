class EventException(BaseException):
    ...


class SkipException(EventException):
    ...


class StopException(EventException):
    ...


class CoreException(Exception):
    ...  # noqa: N818


class GetEventTimeout(CoreException):
    ...


class LoadModuleError(CoreException):
    ...
