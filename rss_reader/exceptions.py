class ServerNotFoundError(Exception):
    """Raised when server does not exist"""


class PageDoesNotExistError(Exception):
    """Raised when page does not exist on this server"""


class FeedNotFoundError(Exception):
    """Raised when page does not exist any feed"""


class InvalidDateError(Exception):
    pass


class NoInternetConnectionError(Exception):
    """Raised when user have no connection with internet"""
