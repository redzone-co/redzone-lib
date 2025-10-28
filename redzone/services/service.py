from microgue.asynchronous.services.service import Service as _Service
from microgue.utils import mask_fields_in_data

from ..utils.logger import Logger, logger
from ..utils.trace import Trace


class Service(_Service):
    mask_request_headers_fields: list = [
        "Authorization",
    ]

    class Request(_Service.Request):
        pass

    class Response(_Service.Response):
        pass

    async def invoke(self, request: _Service.Request) -> _Service.Response:
        request.headers["X-Trace-ID"] = Trace.get_trace_id()
        return await super().invoke(request)

    def log_request_data(self, request: _Service.Request) -> None:
        if request.method != "GET":
            if request.data:
                logger.debug(Logger.truncate(f"request.data: {mask_fields_in_data(request.data, self.mask_request_data_fields)}"))
            elif request.json:
                logger.debug(Logger.truncate(f"request.json: {mask_fields_in_data(request.json, self.mask_request_data_fields)}"))

    def log_response_data(self, response: _Service.Response) -> None:
        if response.data:
            logger.debug(Logger.truncate(f"response.data: {mask_fields_in_data(response.data, self.mask_response_data_fields)}"))
