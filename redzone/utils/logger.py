from microgue.loggers.logger import Logger as _Logger

from ..settings import PROJECT_NAME


class Logger(_Logger):
    pass

    @classmethod
    def truncate(cls, data: str, max_length: int = 1000) -> str:
        if len(data) > max_length:
            return data[:max_length] + "..."
        return data


logger = Logger(PROJECT_NAME)
