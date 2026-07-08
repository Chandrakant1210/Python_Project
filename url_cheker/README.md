# 🛡️ Google Safe Browsing URL Threat Analyzer

A Python-based cybersecurity tool that checks whether a website URL is safe or potentially malicious using the **Google Safe Browsing API**.

The application sends a URL to Google's threat intelligence service, analyzes the response, displays the scan result, and saves a report locally.

---

## 🚀 Features

- 🔍 Scan any website URL
- 🛡️ Detect malicious websites using Google Safe Browsing API
- 📊 Display Safe/Unsafe status
- ⚠️ Show detected threat types
- 📝 Save scan history to `report.txt`
- 🌐 Uses REST API with JSON requests
- 📡 Handles API responses and network errors

---

## 🛠️ Technologies Used

- Python 3
- Requests Library
- Google Safe Browsing API
- JSON
- File Handling
- Datetime Module

---

## 📂 Project Structure

```
Google-Safe-Browsing/

│── main.py             # Main application
│── config.py           # API Key
│── report.txt          # Scan history
│── requirements.txt    # Project dependencies
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/google-safe-browsing-url-checker.git
```

Move into the project

```bash
cd google-safe-browsing-url-checker
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Google Safe Browsing API Setup

1. Create a project in Google Cloud Console.
2. Enable **Safe Browsing API**.
3. Create an API Key.
4. Open `config.py`.
5. Add your API key.

Example

```python
API_KEY = "YOUR_API_KEY"
```

---

## ▶️ Run the Project

```bash
python main.py
```

Example

```
Enter Website URL:
https://google.com
```

---

## ✅ Example Output (Safe Website)

```
Status Code : 200

====================================
✅ SAFE WEBSITE
Threats NOT Found
====================================

Report saved successfully.
```

---

## ⚠️ Example Output (Unsafe Website)

```
Status Code : 200

====================================
⚠️ UNSAFE WEBSITE
Threats Found

Threat Type : MALWARE
Platform    : ANY_PLATFORM
====================================

Report saved successfully.
```

---

## 📄 Report File

Each scan is automatically stored inside

```
report.txt
```

Example

```
2026-07-08 22:30:11

URL :
https://google.com

Status :
SAFE

--------------------------------------------------
```

---

## 📚 Concepts Learned

- REST API
- HTTP POST Requests
- JSON Request & Response
- Google Safe Browsing API
- Exception Handling
- File Handling
- Python Dictionaries
- Python Functions
- Cybersecurity Threat Intelligence

---

## 🔮 Future Improvements

- Read multiple URLs from a text file
- Export scan results to CSV using Pandas
- Generate PDF security reports
- Build a GUI using Tkinter
- Create a Flask Web Application
- Add URL validation
- Threat statistics dashboard
- Support Domain and IP scanning

---

## 🎯 Learning Outcome

This project demonstrates practical knowledge of:

- Python Programming
- API Integration
- Cybersecurity Fundamentals
- Threat Intelligence
- Google Cloud APIs
- Secure Coding Practices

---

## 👨‍💻 Author

**Chandrakant Kumar**

B.Tech CSE Student | Python Developer | AI & Cybersecurity Enthusiast

GitHub:
https://github.com/chandrakant1210



---

## ⭐ If you found this project useful, don't forget to Star the repository.
