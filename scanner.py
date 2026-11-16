import sys
import socket
import requests
from urllib.parse import urlparse
from rich.console import Console
from rich.panel import Panel

console = Console()

def banner():
    console.print(Panel("[bold red]BUGING - ADVANCED RECON & BUG SUITE[/bold red]\n[cyan]Full Target Intelligence & Vulnerability Scanner[/cyan]", border_style="yellow"))

def full_recon(target):
    # URL से सिर्फ डोमेन निकालना (जैसे https://example.com/xyz -> example.com)
    if "http://" in target or "https://://" in target or "https://" in target:
        parsed_url = urlparse(target)
        domain = parsed_url.netloc
    else:
        domain = target.split("/")[0]

    console.print(f"\n[bold yellow][*] Gathering Full Intelligence for: {domain}[/bold yellow]\n")

    # 1. IP Address Lookup
    try:
        ip = socket.gethostbyname(domain)
        console.print(f"[green][+] Public IP Address :[/green] {ip}")
    except Exception as e:
        console.print(f"[red][-] IP Resolve Failed: {e}[/red]")
        return

    # 2. Geo-Location & Hosting Info (Using ipapi.co free API)
    try:
        res = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5).json()
        console.print(f"[green][+] Country / City    :[/green] {res.get('country_name')} / {res.get('city')}")
        console.print(f"[green][+] ISP / Organization  :[/green] {res.get('org')} ({res.get('asn')})")
        console.print(f"[green][+] Hosting Provider  :[/green] {res.get('network', 'Unknown')}")
    except Exception:
        console.print("[red][-] Geo-Location fetch nahi ho paya.[/red]")

    # 3. HTTP Headers & WAF / Cloudflare Check (Fake/Hidden Protection Check)
    try:
        target_url = f"https://{domain}" if not target.startswith("http") else target
        response = requests.get(target_url, timeout=5)
        console.print(f"\n[bold yellow][*] Web Server & Security Headers Analysis:[/bold yellow]")
        console.print(f"[green][+] HTTP Status Code    :[/green] {response.status_code}")
        
        server = response.headers.get("Server", "Hidden/Unknown")
        console.print(f"[green][+] Server Software     :[/green] {server}")
        
        # Check for Cloudflare / WAF (Fake IP hiding real backend)
        if "cloudflare" in server.lower() or "cf-ray" in response.headers:
            console.print("[bold red][!] WAF Detected:[/bold red] Yeh site Cloudflare ke peeche chhupi hai (Real IP masked hai!).")
        else:
            console.print("[green][+] WAF/CDN             :[/green] Direct Server (No Cloudflare mask detected).")

        # Check important security headers
        headers_to_check = ["X-Frame-Options", "Content-Security-Policy", "X-XSS-Protection"]
        for h in headers_to_check:
            if h in response.headers:
                console.print(f"    [green]✔ {h}: Present[/green]")
            else:
                console.print(f"    [red]✘ {h}: Missing (Vulnerable to misconfig)[/red]")

    except Exception as e:
        console.print(f"[red][-] HTTP Header check error: {e}[/red]")

    # 4. Port Scanner (Common Ports)
    console.print(f"\n[bold yellow][*] Scanning Common Ports on {ip}...[/bold yellow]")
    common_ports = [21, 22, 80, 443, 8080, 3306]
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            console.print(f"    [bold green]✔ Port {port} is OPEN[/bold green]")
        else:
            console.print(f"    [dim red]✘ Port {port} is closed[/dim red]")
        s.close()

def main():
    banner()
    console.print("[1] Full Recon & IP/Hosting Intelligence (Works on any website)")
    console.print("[2] Exit")
    
    choice = console.input("\n[bold cyan]Option chunein (1/2): [/bold cyan]")
    if choice == "1":
        target = console.input("Target Domain ya URL dalein (jaise rocketbhai
