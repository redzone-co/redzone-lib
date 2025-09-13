from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .. import bootstrap  # noqa
from ..middleware.database_session_middleware import DatabaseSessionMiddleware
from ..middleware.internal_server_error_middleware import InternalServerErrorMiddleware
from ..middleware.logging_middleware import LoggingMiddleware
from ..middleware.trace_middleware import TraceMiddleware
from ..schemas.index_schemas import IndexResponse
from ..settings import ENVIRONMENT, PROJECT_NAME, REGION, VERSION


class AppCreator:

    @staticmethod
    def create(
        include_database_middleware: bool = True,
    ) -> FastAPI:
        app = FastAPI(
            title=PROJECT_NAME.capitalize(),
            version=VERSION,
            root_path=f"/{ENVIRONMENT}" if ENVIRONMENT != "local" else "",
        )

        app.add_middleware(InternalServerErrorMiddleware)
        if include_database_middleware:
            app.add_middleware(DatabaseSessionMiddleware)
        app.add_middleware(LoggingMiddleware)
        app.add_middleware(TraceMiddleware)
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @app.get("/")
        async def index() -> IndexResponse:
            return IndexResponse.create(
                {
                    "project": PROJECT_NAME,
                    "environment": ENVIRONMENT,
                    "region": REGION,
                    "version": VERSION,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
            )

        return app
