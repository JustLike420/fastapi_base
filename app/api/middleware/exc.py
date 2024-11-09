import logging
from typing import Callable

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR


logger = logging.getLogger(__name__)


class HTTPExceptionMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next: Callable
    ) -> JSONResponse:

        try:
            response = await call_next(request)
        except Exception as e:
            exc = {
                'exc_type': 'INTERNAL',
                'info': 'Internal Error'
            }

            logger.exception(e, exc_info=True)
            return JSONResponse(
                exc,
                status_code=HTTP_500_INTERNAL_SERVER_ERROR
            )
        return response
