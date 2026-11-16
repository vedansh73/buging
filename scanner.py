import sys
import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from rich.console import Console
from rich.panel import Panel

console = Console()

# कॉमन टेस्ट पेलोड्स (Real Bug Payloads)
XSS_PAYLOAD = "<script>alert(1)</script>"
SQLI_PAYLOAD = "' OR '1'='1"

def banner():
    console.print(Panel("[bold red]REAL BUG HUNTER TOOL[/bold red]\n[cyan]Automated Vulnerability Scanner[/cyan]", border_style="yellow"))

def scan_xss(target_url):
    console.print(f"[yellow][*] Testing for Reflected XSS on: {target_url}[/yellow]")
    parsed_url = urlparse(target_url)
    params = parse_qs(parsed_url.query)
    
    if not params:
        console.print("[red][!] URL me koi parameters nahi mile (jaise ?q=test). XSS test ke liye parameter zaroori hai.[/red]")
        return

    vulnerable = False
    for param in params:
        test_params = params.copy()
        test_params[param] = XSS_PAYLOAD
        new_query = urlencode(test_params, doseq=True)
        new_parts = parsed_url._replace(query=new_query)
        test_url = urlunparse(new_parts)
        
        try:
            response = requests.get(test_url, timeout=5)
            if XSS_PAYLOAD in response.text:
                console.print(f"[bold green][!] VULNERABLE TO XSS![/bold green] Parameter: [cyan]{param}[/cyan]")
                console.print(f"[green]Proof of Concept: {test_url}[/green]")
                vulnerable = True
        except Exception as e:
            pass
            
    if not vulnerable:
        console.print("[red][-] XSS vulnerability nahi mili is URL par.[/red]")

def scan_sqli(target_url):
    console.print(f"[yellow][*] Testing for SQL Injection on: {target_url}[/yellow]")
    parsed_url = urlparse(target_url)
    params = parse_qs(parsed_url.query)
    
    if not params:
        console.print("[red][!] URL me koi parameters nahi mile.[/red]")
        return

    sql_errors = ["sql syntax", "mysql_fetch", "syntax error", "unclosed quotation mark", "odbc_"]
    vulnerable = False

    for param in params:
        test_params = params.copy()
        test_params[param] = SQLI_PAYLOAD
        new_query = urlencode(test_params, doseq=True)
        new_parts = parsed_url._replace(query=new_query)
        test_url = urlunparse(new_parts)
        
        try:
            response = requests.get(test_url, timeout=5)
            for error in sql_errors:
                if error in response.text.lower():
                    console.print(f"[bold green][!] POSSIBLE SQL INJECTION FOUND![/bold green] Parameter: [cyan]{param}[/cyan]")
                    console.print(f"[green]Proof of Concept: {test_url}[/green]")
                    vulnerable = True
                    break
        except Exception as e:
            pass
            
    if not vulnerable:
        console.print("[red][-] SQL Injection ka koi sign nahi mila.[/red]")

def main():
    banner()
    console.print("[1] XSS Vulnerability Scanner")
    console.print("[2] SQL Injection Error Scanner")
    
    choice = console.input("\n[bold cyan]Option chunein (1/2): [/bold cyan]")
    url = console.input("Target URL dalein (jaise http://testphp.vulnweb.com/listproducts.php?cat=1): ")
    
    if choice == "1":
        scan_xss(url)
    elif choice == "2":
        scan_sqli(url)
    else:
        console.print("[red]Galat choice![/red]")

if __name__ == "__main__":
    main()
