
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

### Catching low level API errors and parsing the JSON result
```python
import json

# Initialize Kleenscan with API token, default verbose is True for outputting scan progress, and arbitary API objects retrieved.
ks = Kleenscan('<api_token>', verbose=False)

try:
  ks.scan('binary.exe', av_list=['non_existent_av_engine_to_invoke_error'])
except KsApiError as e:
  # Error example: {"success":false,"httpResponseCode":500,"message":"Antivirus strj does not exist.","data":null}
  api_data = json.loads(e.message)
  print(api_data['message']) # Outputs: "Antivirus non_existent_av_engine_to_invoke_error does not exist."


```

### Putting things together
```python
import json

TOKEN = '<insert_api_token_here>'

def get_av(api_data, av_quey):
    av_query = av_query.lower()
    for av_name, av_desc in api_data.items():
        if av_query in av_name or av_query in av_desc.lower():
            return av_name
    raise ValueError(f'{av_query} not found')

# Target AV query.
av_query = 'defender'

# Silent mode (useful for applications which don't want excessive output).
ks = Kleenscan(TOKEN, max_minutes=1, verbose=False)

# List available antivirus engines..
result = ks.av_list()
api_data = json.loads(result)

# Get AV engines for file scanning.
file_avs = api_data['data']['file']

# Get target antivirus name ID for file scanning.
av_name = get_av(file_avs, av_query)

# Scan file with target antivirus engine.
result = ks.scan('malware.ps1', av_list=[av_name])
print(result)

# Scan remote file with target antivirus engine and store result to YAML file.
result = ks.scan_urlfile('https://example.com/binary.exe', av_list=[av_name], out_file='out.yaml', output_format='yaml')
print(result)

# Get all url avs.
url_avs = api_data['data']['url']

# Get target antivirus name ID.
av_name = get_av(url_avs, av_query)

# Scan URL and output to a TOML string.
result = ks.scan_url('https://example.com', av_list=[av_name], output_format='toml')
print(result)
```


## Documentation 

### Kleenscan Class Constructor

```python
Kleenscan(x_auth_token: str,   # API token from https://kleenscan.com/profile (required)
 verbose: bool,                # Enable verbose output (not required and can be omitted, default is True)
 max_minutes: int              # Maximum scan duration in minutes (not required and can be omitted, must be a positive integer)
)
```
Raises:
- `KsInvalidTokenError`: Invalid `x_auth_token`
- `KsApiError`: Low-level API request error
- `ValueError`: Rose when a invalid value is provided to any argument, even though it's the correct type (e.g.: `max_minutes=-1`)
- `TypeError`: Rose when a value of an invalid type is provided to any argument (e.g.: `max_minutes='10'`)

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

- `KsFileTooLargeError`: `file` exceeds size limits
- `KsFileEmptyError`: Empty `file` cannot be scanned
- `KsApiError`: Low-level API request error
- `ValueError`: Rose when a invalid value is provided to any argument, even though it's the correct type (e.g.: `av_list=[1,2,3]` or `out_file=''`)
- `TypeError`: Rose when a value of an invalid type is provided to any argument (e.g.: `output_format=1`)



**scan_urlfile**: Scan a file hosted on a URL
  ```python
Kleenscan.scan_urlfile(url: str,     # URL/server hosting file to be scanned, include scheme, domain and port number if any (required).
   av_list: list,                      # Antivirus list e.g. ['avg', 'avast', 'mirosoftdefender'] (not required and can be omitted).
   output_format: str,                 # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
   out_file: str                       # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str
  ```
Raises:
- `KsRemoteFileTooLargeError`: Remote file exceeds size limits
- `KsGetFileInfoFailedError`: Failed to get information on remote file
- `KsNoFileHostedError`: No file hosted on the provided `url`
- `KsFileDownloadFailedError`: Remote file cannot be downloaded
- `KsDeadLinkError`: Cannot connect to the provided `url`
- `KsApiError`: Low-level API request error
- `ValueError`: Rose when a invalid value is provided to any argument, even though it's the correct type (e.g.: `av_list=[1,2,3]` or `out_file=''`)
- `TypeError`: Rose when a value of an invalid type is provided to any argument (e.g.: `output_format=1`)



  
**scan_url**: Scan a URL
  ```python
Kleenscan.scan_url(url: str,         # URL to be scanned, include scheme, domain and port number if any (required).
   av_list: list,                      # Antivirus list e.g. ['avg', 'avast', 'mirosoftdefender'] (not required and can be omitted).
   output_format: str,                 # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
   out_file: str                       # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str

  ```
Raises:
- `KsApiError`: Low-level API request error.
- `ValueError`: Rose when a invalid value is provided to any argument, even though it's the correct type (e.g.: `av_list=[1,2,3]` or `out_file=''`)
- `TypeError`: Rose when a value of an invalid type is provided to any argument (e.g.: `output_format=1`)

  
**av_list**: List available antivirus engines
  ```python
Kleenscan.av_list(output_format: str # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
   out_file: str                       # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str 
  ```
Raises:
- `KsApiError`: Low-level API request error
- `ValueError`: Rose when a invalid value is provided to any argument, even though it's the correct type (e.g.: `output_format=''` or `out_file=''`)
- `TypeError`: Rose when a value of an invalid type is provided to any argument (e.g.: `output_format=1`)
