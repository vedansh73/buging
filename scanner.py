cat << 'EOF' > scanner.py
import sys
import socket
import requests
from urllib.parse import urlparse
from rich.console import Console
from rich.panel import Panel

console = Console()

def banner():
    console.print(Panel("[bold red]BUGING - ADVANCED RECON & INTELLIGENCE SUITE[/bold red]\n[cyan]Full Target Intelligence & Security Auditor[/cyan]", border_style="yellow"))

def full_recon(target):
    if "http://" in target or "https://" in target:
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

    # 2. Geo-Location & Hosting Info
    try:
        res = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5).json()
        console.print(f"[green][+] Country / City    :[/green] {res.get('country_name')} / {res.get('city')}")
        console.print(f"[green][+] ISP / Organization  :[/green] {res.get('org')} ({res.get('asn')})")
        console.print(f"[green][+] Hosting Provider  :[/green] {res.get('network', 'Unknown')}")
    except Exception:
        console.print("[red][-] Geo-Location fetch failed.[/red]")

    # 3. HTTP Headers & WAF / Cloudflare Check
    try:
        target_url = f"https://{domain}" if not target.startswith("http") else target
        response = requests.get(target_url, timeout=5)
        console.print(f"\n[bold yellow][*] Web Server & Security Headers Analysis:[/bold yellow]")
        console.print(f"[green][+] HTTP Status Code    :[/green] {response.status_code}")
        
        server = response.headers.get("Server", "Hidden/Unknown")
        console.print(f"[green][+] Server Software     :[/green] {server}")
        
        if "cloudflare" in server.lower() or "cf-ray" in response.headers:
            console.print("[bold red][!] WAF Detected:[/bold red] Site is protected by Cloudflare (Real IP might be masked!).")
        else:
            console.print("[green][+] WAF/CDN             :[/green] Direct Server (No Cloudflare mask detected).")

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
    console.print("[1] Full Recon & IP/Hosting Intelligence")
    console.print("[2] Exit")
    
    choice = console.input("\n[bold cyan]Select an option (1/2): [/bold cyan]")
    if choice == "1":
        target = console.input("Enter target domain or URL (e.g., rocketbhaiya.in): ")
        full_recon(target)
    elif choice == "2":
        console.print("[bold red]Exiting... Stay safe and ethical![/bold red]")
        sys.exit()
    else:
        console.print("[red]Invalid choice![/red]")

if __name__ == "__main__":
    main()
EOF
