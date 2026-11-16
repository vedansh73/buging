# 🐞 Buging - Web Vulnerability Scanner

**Buging** एक हल्का और तेज़ Python-आधारित सिक्योरिटी ऑडिटिंग टूल है, जिसे वेबसाइट के URL पैरामीटर्स में संभावित **Reflected XSS** और **SQL Injection** गलतियों की जांच करने के लिए बनाया गया है।

---

## ✨ Features (खासियत)
- **Reflected XSS Scanner:** URL क्वेरी पैरामीटर्स में इनपुट रिफ्लेक्शन चेक करता है।
- **SQL Injection Error Scanner:** सामान्य डेटाबेस सिंटैक्स एरर रिस्पॉन्स की पहचान करता है।
- **Clean Terminal UI:** `rich` लाइब्रेरी की मदद से कलरफुल और पढ़ने में आसान आउटपुट।
- **Cross-Platform:** Kali Linux, Termux (Android), और Windows पर आसानी से चलता है।

---

## 🛠️ Installation (इंस्टॉल कैसे करें)

अपने टर्मिनल (Kali Linux / Termux / CMD) में नीचे दिए गए कमांड्स चलाएं:

```bash
# 1. Repository को क्लोन करें
git clone [https://github.com/vedansh73/buging.git](https://github.com/vedansh73/buging.git)

# 2. फोल्डर के अंदर जाएं
cd buging

# 3. ज़रूरी लाइब्रेरी इंस्टॉल करें
pip install -r requirements.txt
