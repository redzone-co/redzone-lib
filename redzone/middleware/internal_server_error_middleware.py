import traceback

import sentry_sdk
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from ..utils.logger import logger


class InternalServerErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            return await call_next(request)
        except Exception as e:
            sentry_sdk.capture_exception(e)
            sentry_sdk.flush(2)
            logger.debug("internal server error", priority=1)
            logger.debug("{}: {}".format(e.__class__.__name__, e))
            logger.debug(traceback.format_exc())
            return JSONResponse(status_code=500, content={"message": "internal server error"})
