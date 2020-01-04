class NoUrlOrDataArgsError(Exception):
    """Raise when it is no one data-related args and no link in function call"""


class NotAbsoluteURIError(Exception):
    """Only absolute URIs are allowed"""


class ServerNotFoundError(Exception):
    """Raised when server does not exist"""


class PageDoesNotExistError(Exception):
    """Raised when page does not exist on this server"""


class InvalidPathError(Exception):
    """Raise when folder to save do no exist"""


class InvalidFolderToSaveError(Exception):
    """Raised when user have no rights to write file in this folder"""


class FeedNotFoundError(Exception):
    """Raised when page does not exist any feed"""


class InvalidDateError(Exception):
    """Raised when --date argument input with invalid date"""


class NoInternetConnectionError(Exception):
    """Raised when user have no connection with internet"""


