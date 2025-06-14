﻿# python-automation

# PythonProject1 — Automation Scripts Collection

This repository contains various Python automation scripts, each handling a different task. Below is a brief description of each file and the references used while building them.

---

## 📧 autoEmail.py

**Description:**  
Sends automated emails to one or more recipients using `smtplib` for server connection and `MIMEText` for structuring the email content.

**Key Libraries:**
- `smtplib`
- `email.mime`

**References:**
- [smtplib — Official Docs](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail)  
- [email.mime — Official Docs](https://docs.python.org/3/library/email.mime.html)

---

## 🌐 apisdata.py

**Description:**  
Scrapes data from a website using API requests. It uses the `requests` module to fetch the HTML content and `BeautifulSoup` to extract all the links from the page.

**Used on:** `lawlessrp.com`

**Key Libraries:**
- `requests`
- `bs4` (BeautifulSoup)

**References:**
- [Requests Module — W3Schools](https://www.w3schools.com/python/module_requests.asp)  
- [Web Scraping with BeautifulSoup — GeeksForGeeks](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)

---

## 📝 fileRename.py

**Description:**  
Renames all files that contain the word `"copy"` in their filenames, replacing it with `"toBeDeleted"` and appending the current date and time using the `datetime` module.

**Key Libraries:**
- `os`
- `datetime`

**Reference:**
- [os.rename() — Tutorialspoint](https://www.tutorialspoint.com/python/os_rename.htm)

---

## 🗑️ delFile.py

**Description:**  
Deletes files or directories based on specific conditions using the `os` and `datetime` modules.

**Key Libraries:**
- `os`
- `datetime`

**Reference:**
- [Python Delete File — ServerAcademy](https://serveracademy.com/blog/python-delete-file-tutorial/#:~:text=built%2Din%20functions.-,The%20os.,for%20empty%20directories%20and%20shutil.)

---

## ⏰ taskScheduling.py

**Description:**  
Uses the `schedule` module to run functions at specific times or intervals.

**Key Libraries:**
- `schedule`

**Reference:**
- [schedule Module — Docs](https://schedule.readthedocs.io/en/stable/)

---

## 💡 How to Run

1. Clone this repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # For Windows

