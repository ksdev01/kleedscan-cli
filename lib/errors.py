# Custom library imports:
from .config import *



class KsInvalidTokenError(Exception):
    """Exception raised for invalid file extensions."""
    def __init__(self):
        self.message = 'Invalid API token. After creating an account, generate a new one at https://kleenscan.com/profile.'
        super().__init__(self.message)



class KsApiError(Exception):
    """Exception raised for invalid file extensions."""
    def __init__(self, message):
        super().__init__(f"An error occurred with the kleenscan API: {message}")



class KsNoFileError(Exception):
    """Exception raised for invalid file extensions."""
    def __init__(self):
        super().__init__("No file was provided to the file parameter. Make sure you include the absolute path to the file.")



class KsNoUrlError(Exception):
    """Exception raised for invalid file extensions."""
    def __init__(self):
        super().__init__("No URL string was provided to the url parameter.")



class KsFileTooLargeError(Exception):
    """Exception raised for invalid file extensions."""
    def __init__(self):
        super().__init__(f"The provided file is too large for the kleenscan API (Max: {MAX_FILE_MB} MB).")



class KsFileEmptyError(Exception):
    """Exception raised for invalid file extensions."""
    def __init__(self):
        super().__init__(f"The provided file is empty, provide a file with data.")
