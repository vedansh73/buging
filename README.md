# 🐞 Buging - Advanced Recon & Intelligence Suite

**Buging** is a lightweight, fast, and powerful Python-based security auditing and reconnaissance tool designed to extract deep target intelligence from any domain or URL—including public IPs, geolocation, hosting providers, server software, WAF/Cloudflare detection, security header misconfigurations, and common open ports.

---

## ✨ Features

- **IP & Network Intelligence:** Resolves public IP addresses instantly from any domain or URL.
- **Geo-Location & ISP Lookup:** Automatically fetches country, city, organization, and hosting provider details.
- **Web Server & WAF Detection:** Identifies the underlying server software and checks if the site is masked behind Cloudflare or a Web Application Firewall (WAF).
- **Security Headers Analyzer:** Scans for missing HTTP security headers (`X-Frame-Options`, `Content-Security-Policy`, `X-XSS-Protection`).
- **Common Port Scanner:** Quickly checks standard ports (`21`, `22`, `80`, `443`, `8080`, `3306`) to see what services are exposed.
- **Clean Terminal UI:** Built with the `rich` library for a professional, color-coded output.

---

## 🛠️ Installation & Setup (Kali Linux / Termux / Windows)

Open your terminal and run the following commands to clone the repository and set it up:

```bash
# 1. Clone the repository
git clone [https://github.com/vedansh73/buging.git](https://github.com/vedansh73/buging.git)

# 2. Enter the project folder
cd buging

# 3. Create a virtual environment (Recommended for Kali Linux)
python3 -m venv venv
source venv/bin/activate

# 4. Install required dependencies
pip install -r requirements.txt


⚠️ Disclaimer
This tool is created strictly for educational purposes, defensive audits, and authorized penetration testing. Unauthorized scanning of targets without explicit permission is illegal. The developer is not responsible for any misuse.
