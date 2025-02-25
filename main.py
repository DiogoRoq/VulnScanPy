import requests
from bs4 import BeautifulSoup
import urllib.parse
import colorama
import re
from concurrent.futures import ThreadPoolExecutor
import sys
from typing import List, Dict, Set

class WebScanner:
    def __init__(self, target_url: str, max_depth: int = 3):
        self.target_url = target_url
        self.max_depth = max_depth
        self.visited_urls: Set[str] = set()
        self.vulnerabilities: List[Dict] = []
        self.session = requests.Session()

        colorama.init()
        
    def normaizel_url(self, url:str) -> str:

        parsed = urllib.parse.urlparse(url)
        return f'{parsed.scheme}://{parsed.netloc}{parsed.path}'


    def crawl(self, url: str, depth: int = 0) -> None:
        if depth > self.max_depth or url in self.visited_urls:
            return

        try:
            self.visited_urls.add(url)
            response = self.session.get(url, verify = False)
            soup = BeautifulSoup(response.text, 'html.parser')


            links = soup.find_all('a', href =True)
            for link in links:
                next_url = urllib.parse.urljoin(url, link['href'])
                if next_url.startswith(self.target_url):
                    self.crawl(next_url, depth + 1)

        except Exception as e:
            print(f'Error crawling {url}: {str(e)}')


    def check_sql_injection(self, url: str) -> None:

        sql_payloads = ["'", "1' OR '1'='1", "' OR 1=1--", "UNION SELECT NULL--"]

        for payload in sql_payloads:
            try:
                parsed = urllib.parse.urlparse(url)
                params = urllib.parse.parse_qs(parsed.query)

                for param in params:
                    test_url = url.replace(f"{param} = {params[param][0]}",
                                           f"{param} = {payload}")
                    response = self.session.get(test_url)

                    if any(error in response.text.lower() for error in ['sql', 'mysql', 'sqlite', 'postgresql', 'oracle']):
                        self.report_vulnerability({
                            'type': 'SQL Injection',
                            'url': url,
                            'parameter':param,
                            'payload': payload 

                        })
            except Exception as e:
                print(f'Error testing SQL Injection on {url}: {str(e)}')          

        def check_xss(self, url: str) -> None:
            xss_payloads = [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "javascript:alert('XSS)"
                            ]

            for payload in xss_payloads:
                try:
                    parsed = urllib.parse.urlparse(url)
                    params = urllib.parse.parse_qs(parsed.query)

                    for param in params:
                        test_url = url.replace(f"{param}={params[param][0]}",
                                               f"{param}={urllib.parse.quote(payload)}")
                        response = self.session.get(test_url)

                        if payload in response.text:
                            self.report_vulnerability({
                                'type': 'Cross-Site Scripting (XSS)',
                                'url': url,
                                'parameter': param,
                                'payload': payload
                            })  
                except Exception as e:
                    print(f"Error testing XSS on {url}: {str(e)}")
