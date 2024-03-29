
class UserNotFoundException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class InvalidRequestException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class AccessDeniedException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
