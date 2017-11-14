from functools import wraps
from app import db
from .Log import storage_log, parser_log


def db_commit_decorator(func):
    @wraps(func)
    def session_commit(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            storage_log.error('db operation error，here are details: {}'.format(e))
            storage_log.warning('transaction rollbacks')
            db.session.rollback()
    return session_commit


def parse_decorator(return_value):
    """
    :param return_value: catch exceptions when parsing pages, return the default value
    :return: the default value is 0,'',[],False,{} or None
    """
    def page_parse(func):
        @wraps(func)
        def handle_error(*keys):
            try:
                return func(*keys)
            except Exception as e:
                parser_log.error(e)
                return return_value
        return handle_error
    return page_parse
