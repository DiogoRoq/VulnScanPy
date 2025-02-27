# Web Security Scanner

## Overview

The Web Security Scanner is a Python-based tool designed to crawl a target website and identify potential security vulnerabilities. It supports scanning for SQL Injection, Cross-Site Scripting (XSS), and sensitive information exposure (e.g., emails, phone numbers, API keys). The tool uses multi-threading to speed up the scanning process and provides a detailed report of any vulnerabilities found.

## Features

- **Crawling**: Recursively crawls the target website up to a specified depth.
- **SQL Injection Detection**: Tests for SQL Injection vulnerabilities using common payloads.
- **XSS Detection**: Tests for Cross-Site Scripting (XSS) vulnerabilities using common payloads.
- **Sensitive Information Detection**: Scans for sensitive information such as emails, phone numbers, and API keys.
- **Multi-threading**: Utilizes multi-threading to speed up the scanning process.
- **Detailed Reporting**: Provides a detailed report of vulnerabilities found, including the type, URL, parameter, and payload.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/web-security-scanner.git
   cd web-security-scanner
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Web Security Scanner, use the following command:

```bash
python scanner.py <target_url>
```

### Example

```bash
python scanner.py https://example.com
```

### Output

The tool will output the following information:

- **Vulnerabilities Found**: Details of any vulnerabilities detected, including the type, URL, parameter, and payload.
- **Scan Summary**: Total number of URLs scanned and total vulnerabilities found.

## Code Structure

- **WebScanner Class**: The main class responsible for crawling the website and performing security checks.
  - `__init__`: Initializes the scanner with the target URL and maximum depth.
  - `normalize_url`: Normalizes the URL to ensure consistency.
  - `crawl`: Recursively crawls the website.
  - `check_sql_injection`: Tests for SQL Injection vulnerabilities.
  - `check_xss`: Tests for XSS vulnerabilities.
  - `check_sensitive_info`: Scans for sensitive information.
  - `scan`: Initiates the scanning process.
  - `report_vulnerability`: Reports any vulnerabilities found.

## Dependencies

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML content.
- `colorama`: For colored console output.
- `concurrent.futures`: For multi-threading support.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational and ethical testing purposes only. Do not use it on any website without explicit permission from the owner. The authors are not responsible for any misuse or damage caused by this tool.

---
