# Custom library imports:
from .config import *



class KsInvalidTokenError(Exception):
    def __init__(self):
        self.message = 'Invalid API token. After creating an account, generate a new one at https://kleenscan.com/profile.'
        super().__init__(self.message)



class KsApiError(Exception):
    def __init__(self, message):
        super().__init__(f'An error occurred with the kleenscan API: {message}')



class KsNoFileError(Exception):
    def __init__(self):
        super().__init__('No file was provided to the file parameter. Make sure you include the absolute path to the file.')



class KsNoUrlError(Exception):
    def __init__(self):
        super().__init__('No URL string was provided to the url parameter.')



class KsFileTooLargeError(Exception):
    def __init__(self):
        super().__init__(f'The provided file is too large for the kleenscan API (Max: {MAX_FILE_MB} MB).')



class KsFileEmptyError(Exception):
    def __init__(self):
        super().__init__(f'The provided file is empty, provide a file with data.')



class KsRemoteFileTooLargeError(Exception):
    def __init__(self):
        super().__init__(f'The remote file is too large for the kleenscan API (Max: {MAX_FILE_MB} MB).')



class KsGetFileInfoFailedError(Exception):
    def __init__(self, message: str):
        super().__init__(f'Failed to get file info, HTTP statuc code: {message}')



class KsNoFileHostedError(Exception):
    def __init__(self):
        super().__init__(f'No file hosted on provided URL/server. Please provide a URL/server which hosts a file, e.g. https://malicious.com/file.exe')



class KsFileDownloadFailedError(Exception):
    def __init__(self, message: str):
        super().__init__(f'Failed to download file, HTTP status code: {message}')



class KsDeadLinkError(Exception):
    def __init__(self, message: str):
        super().__init__(f'The URL/server hosting the file cannot be conneceted to: {message}')
