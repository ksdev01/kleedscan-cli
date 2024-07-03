# Kleenscan

Kleenscan is a Python library and command-line tool for scanning files and URLs with various antivirus engines provided by [Kleenscan](https://kleenscan.com).
<img width="1549" alt="image" src="https://github.com/ksdev01/kleenscan-cli/assets/174640881/c1996843-8292-454f-a989-396161537a4b">

## Installation

You can install Kleenscan using pip3/pip:

```
pip install kleenscan
```

## Command line usage

```
# Help command:
kleenscan -h

# Simple file scan (max scan wait 1 minute):
kleenscan -t <api_token> -f binary.exe --minutes 1

# Simple url scan (max scan wait 1 minute):
kleenscan -t <api_token> -u https://example.com --minutes 1

# List available antivirus:
kleenscan --token <api_token> -l

# Simple file scan using a list of antivirus:
kleenscan -t <api_token> -f binary.exe --minutes 1 --antiviruses avg microsoftdefender avast --minutes 1

# Simple url scan using a list of antivirus:
kleenscan -t <api_token> -u https://google.com --minutes 1 --antiviruses avg microsoftdefender avast --minutes 1

# File scan and output to YAML and only output the YAML results to standard output (--silent/-s excludes real-time verbosity):
kleenscan -t <api_token> -f binary.exe --format yaml --silent --show --minutes 1

# File scan and output to TOML and store results to a file and standard output (--show/-sh outputs the formatted results):
kleenscan -t <api_token> -f binary.exe --format toml --show --outfile results.toml --minutes 1

# Url scan and output to JSON and store results to a file:
kleenscan -t <api_token> -u https://example.com --format json --outfile results.json --minutes 1

```

## Python library/module usage
```python
from kleenscan.kleenscan import Kleenscan
'''

# Kleenscan class constructor args:

Kleenscan(x_auth_token: str,         # XAuth token generated at https://kleenscan.com/profile (required)
  verbose: bool,                     # Verbose, default is True, if set to false the library only returns results from called methods (not required and can be omitted).
  max_minutes: int                   # Max scan in minutes, is AV vendors are delaying executing this can be used to decrease overall scantime (not required and can be omitted).
)


# Kleenscan methods, all return the string results of the format provided (default is JSON):

Kleenscan.scan(file: str,            # Absolute path to file on local disk to be scanned.
  av_list: list,                     # Antivirus list e.g. ['avg', 'avast', 'mirosoftdefender'] (not required and can be omitted).
  output_format: str,                # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
  out_file: str                      # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str

Kleenscan.scan_url(url: str,         # URL to be scanned, include scheme, domain and port number if any (required).
  av_list: list,                     # Antivirus list e.g. ['avg', 'avast', 'mirosoftdefender'] (not required and can be omitted).
  output_format: str,                # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
  out_file: str                      # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str

Kleenscan.av_list(output_format: str # Output format, e.g. 'toml', 'yaml', 'json' (not required and can be omitted).
  out_file: str                      # Output file to store results to e.g. "results.json" (not required and can be omitted).
) -> str 


Kleenscan errors (from kleenscan.lib.errors import *):

kleenscan.lib.errors.KsInvalidTokenError   # Rose when an invalid API token is provided.
kleenscan.lib.errors.KsApiError            # Low level API errors which occur with HTTP requests.
kleenscan.lib.errors.KsNoFileError         # No file string provided to the Kleenscan.scan method.
kleenscan.lib.errors.KsNoUrlError          # No URL string provided to the Kleenscan.scan_url method.
kleenscan.lib.errors.KsFileTooLargeError   # File provided to the Kleenscan.scan method is too large and exceeds Kleenscan API fize size limits.
kleenscan.lib.errors.KsFileEmptyError      # File provided to the Kleenscan.scan method is empty and cannot be scanned.
'''


# Code examples:

# Set API token and instantiate a Kleenscan instance:
ks = Kleenscan('<api_token>', verbose=False)

# Simple file scan (default output is JSON):
result = ks.scan('binary.exe')
print(result)

# Simple url scan (default output is JSON):
result = ks.scan_url('http://example.com')
print(result)

# Simple list antivirus (default output is JSON):
result = ks.av_list()
print(result)

result = ks.scan('binary.exe', av_list=['avg', 'avast'])
print(result)

result = ks.scan('binary.exe', output_format='yaml')
print(result)

result = ks.scan('binary.exe', out_file='result.yaml', output_format='yaml')
print(result)

result = ks.scan_url('http://example.com', output_format='yaml')
print(result)

result = ks.scan_url('http://example.com', out_file='result.yaml', output_format='yaml')
print(result)

result = ks.av_list(output_format='yaml')
print(result)

result = ks.av_list(out_file='result.yaml', output_format='yaml')
print(result)
```


