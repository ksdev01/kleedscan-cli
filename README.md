
# Kleenscan

Kleenscan is a Python library and command-line tool for scanning files and URLs using various antivirus engines provided by [Kleenscan](https://kleenscan.com).
<img width="1638" alt="image" src="https://github.com/ksdev01/kleenscan-cli/assets/174640881/4a58916d-b807-4da3-95ac-3bdc10c8ba2a">


## Installation

Install Kleenscan using pip3 or pip:

```sh
pip install kleenscan
```

## Command Line Usage

```sh
# Display help
kleenscan -h

# Scan a local file with a maximum wait time of 1 minute
kleenscan -t <api_token> -f binary.exe --minutes 1

# Scan a remote file with a maximum wait time of 1 minute
kleenscan -t <api_token> --urlfile https://example.com/binary.exe --minutes 1

# Scan a URL with a maximum wait time of 1 minute
kleenscan -t <api_token> -u https://example.com --minutes 1

# List available antivirus engines
kleenscan --token <api_token> -l

# Scan a local file using specified antivirus engines
kleenscan -t <api_token> -f binary.exe --minutes 1 --antiviruses avg microsoftdefender avast

# Scan a URL using specified antivirus engines
kleenscan -t <api_token> -u https://google.com --minutes 1 --antiviruses avg microsoftdefender avast

# Scan a file and output results in YAML format, suppressing real-time output
kleenscan -t <api_token> -f binary.exe --format yaml --silent --minutes 1

# Scan a file and output results in TOML format, storing results in a file and displaying them
kleenscan -t <api_token> -f binary.exe --format toml --show --outfile results.toml --minutes 1

# Scan a URL and output results in JSON format, storing results in a file
kleenscan -t <api_token> -u https://example.com --format json --outfile results.json --minutes 1
```

## Python Library

### Importing `Kleenscan` and `errors`

```python
from kleenscan import Kleenscan
from kleenscan.lib.errors import *
```

### Listing anti-virus engines, scanning URLs, local & remote files
```python
# Initialize Kleenscan with API token, default verbose is True for outputting scan progress, and arbitary API objects retrieved.
ks = Kleenscan('<api_token>', verbose=False)

# Scan a local file
result = ks.scan('binary.exe')
print(result)

# Scan a remote file
result = ks.scan_urlfile('https://example.com/binary.exe')
print(result)

# Scan a URL
result = ks.scan_url('http://example.com')
print(result)

# List available antivirus engines
result = ks.av_list()
print(result)

# Scan a local file with specified antivirus engines
result = ks.scan('binary.exe', av_list=['avg', 'avast'])
print(result)

# Scan a local file and output in YAML format
result = ks.scan('binary.exe', output_format='yaml')
print(result)

# Scan a local file and store results in a YAML file
result = ks.scan('binary.exe', out_file='result.yaml', output_format='yaml')
print(result)

# Scan a URL and output in YAML format
result = ks.scan_url('http://example.com', output_format='yaml')
print(result)

# Scan a URL and store results in a YAML file
result = ks.scan_url('http://example.com', out_file='result.yaml', output_format='yaml')
print(result)

# List available antivirus engines and output in YAML format
result = ks.av_list(output_format='yaml')
print(result)

# List available antivirus engines and store results in a YAML file
result = ks.av_list(out_file='result.yaml', output_format='yaml')
print(result)
```


## Documentation 

### Kleenscan Class Constructor

```python
Kleenscan(x_auth_token: str,   # API token from https://kleenscan.com/profile (required)
 verbose: bool = True,         # Enable verbose output (default is True)
 max_minutes: int = None       # Maximum scan duration in minutes (optional)
)
```
Raises:
- `KsNoTokenError`: No token was provided to the `x_auth_token` argument
- `KsInvalidTokenError`: Invalid `x_auth_token`
- `KsApiError`: Low-level API request error.

### Kleenscan Methods

  **scan_file**: Scan a file locally on disk
  ```python
Kleenscan.scan(file: str,            # Absolute path to file on local disk to be scanned.
   av_list: list,                      # Antivirus list e.g. ['avg', 'avast', 'mirosoftdefender'] (not required and can be omitted).
   output_format: str,                 # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
   out_file: str                       # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str
  ```
Raises:

- `KsNoFileError`: No `file` provided for scanning
- `KsFileTooLargeError`: `file` exceeds size limits
- `KsFileEmptyError`: Empty `file` cannot be scanned
- `KsApiError`: Low-level API request error.


**scan_urlfile**: Scan a file hosted on a URL
  ```python
Kleenscan.scan_urlfile(url: str,     # URL/server hosting file to be scanned, include scheme, domain and port number if any (required).
   av_list: list,                      # Antivirus list e.g. ['avg', 'avast', 'mirosoftdefender'] (not required and can be omitted).
   output_format: str,                 # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
   out_file: str                       # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str
  ```
Raises:
- `KsNoUrlError`: No `url` provided for remote file scanning
- `KsRemoteFileTooLargeError`: Remote file exceeds size limits
- `KsGetFileInfoFailedError`: Failed to get information on remote file
- `KsNoFileHostedError`: No file hosted on the provided `url`
- `KsFileDownloadFailedError`: Remote file cannot be downloaded
- `KsDeadLinkError`: Cannot connect to the provided `url`
- `KsApiError`: Low-level API request error.

  
**scan_url**: Scan a URL
  ```python
Kleenscan.scan_url(url: str,         # URL to be scanned, include scheme, domain and port number if any (required).
   av_list: list,                      # Antivirus list e.g. ['avg', 'avast', 'mirosoftdefender'] (not required and can be omitted).
   output_format: str,                 # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
   out_file: str                       # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str

  ```
Raises:
- `KsNoUrlError`: No `url` provided for scanning
- `KsApiError`: Low-level API request error.

  
**av_list**: List available antivirus engines
  ```python
Kleenscan.av_list(output_format: str # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
   out_file: str                       # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str 
  ```
- `KsApiError`: Low-level API request error.
