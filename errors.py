from requests import HTTPResponseCode
from datetime import datetime
import logging


logger = logging.getLogger('__name__')


def not_found(request, response):
    response.set_status(HTTPResponseCode.NOT_FOUND)
    response.add_header('Content-Type', 'text/html')
    response.set_body('<h1> 404 Not Found</h1>')
    logger.warning(f'Request Status 404 {datetime.now()}. Info - Страницв {request.url} не найдена')


def internal_server_error(request, response,  exception: Exception):
    response.set_status(HTTPResponseCode.INTERNAL_SERVER_ERROR)
    response.add_header('Content-Type', 'text/html')
    response.set_body(f'<h1> 500 Internal server error</h1><p>{exception.args}</p>')
    logger.error(f"Status 500 {datetime.now()}, Error {exception}")
    logger.info('И тут все поломалось')


