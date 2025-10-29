import logging

from microgue.loggers.logger import Logger as _Logger

from ..settings import PROJECT_NAME

MAX_LOG_LENGTH = 1000


class Logger(_Logger):
    __instance = None

    def log(self, message, priority=None, level=logging.DEBUG):
        message = str(message)
        if len(message) > MAX_LOG_LENGTH:
            message = message[:MAX_LOG_LENGTH] + "... (truncated)"
        super().log(message, priority, level)


logger = Logger(PROJECT_NAME)
