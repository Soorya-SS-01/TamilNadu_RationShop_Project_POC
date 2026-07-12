<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=160&section=header&text=Ration%20Shop%20Management%20System&fontSize=32&fontColor=fff&animation=fadeIn&fontAlignY=35&desc=Digitizing%20Ration%20Distribution%20for%20Fair%20Price%20Shops&descAlignY=58&descSize=15" width="100%"/>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=0D6EFD&center=true&vCenter=true&width=650&lines=Flask+%2B+MySQL+Powered+Admin+Panel;Track+Members+%7C+Notify+%7C+Manage+Stock;Built+for+Real+Ration+Shops)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</div>

---

## 📖 About the Project

**Ration Shop Management System** is a lightweight web application built to help a Fair Price Shop (ration shop) admin digitally manage registered members, track who has collected their monthly ration, and broadcast notifications (shop open/close, reminders) to members via email — replacing manual registers and word-of-mouth announcements.

It's a single-admin dashboard: the shop owner logs in, views all registered members, adds or removes members, marks ration as collected, and sends bulk email notifications — all from one page.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 **Admin Login** | Simple username/password gate before the dashboard loads |
| 👥 **Member Management** | Add, view, search, and delete registered ration card holders |
| ✅ **Collection Tracking** | Toggle each member's ration as *Collected* / *Not Collected* |
| 📧 **Bulk Email Notifications** | Notify all members at once when the shop opens |
| ⏰ **Reminder Emails** | Send targeted reminder emails to selected members |
| 🖨️ **Daily Report Printing** | Generate and print a daily distribution report |
| 🔄 **Shop Reset** | Reset all member statuses back to *Not Collected* for the next cycle |

---

## 🏗️ System Architecture

```mermaid
flowchart LR
    subgraph Client["🖥️ Browser (Frontend)"]
        UI["index.html\nHTML + CSS + Vanilla JS"]
    end

    subgraph Server["⚙️ Flask Backend (app.py)"]
        API["REST API Routes"]
    end

    subgraph DB["🗄️ MySQL Database"]
        Members[("members table")]
    end

    subgraph External["📧 External Services"]
        SMTP["Gmail SMTP Server"]
    end

    UI -- "fetch() HTTP requests" --> API
    API -- "SQL queries" --> Members
    Members -- "results" --> API
    API -- "JSON response" --> UI
    API -- "sendmail()" --> SMTP
    SMTP -- "delivers email" --> Members2["👤 Member Inbox"]
```

---

## 🔄 Application Flow

```mermaid
flowchart TD
    A(["🚪 Open App"]) --> B{"Enter Login\nCredentials"}
    B -- "Invalid" --> B
    B -- "Valid" --> C["📋 Dashboard Loads\nGET /members"]
    C --> D{"Choose Action"}

    D --> E["➕ Add Member\nPOST /add-member"]
    D --> F["🗑️ Delete Member\nDELETE /delete-member/:id"]
    D --> G["✅ Toggle Collected\nPUT /toggle-status/:id"]
    D --> H["📧 Notify All Members\nPOST /send-email"]
    D --> I["⏰ Send Reminder\nPOST /send-reminder-email"]
    D --> J["🖨️ Print Daily Report"]
    D --> K["🔄 Close Shop / Reset Status"]

    E --> L["MySQL: INSERT"]
    F --> M["MySQL: DELETE"]
    G --> N["MySQL: UPDATE"]
    H --> O["SMTP: Email All"]
    I --> P["SMTP: Email Selected"]

    L --> C
    M --> C
    N --> C
    O --> Q(["✔️ Members Notified"])
    P --> Q
    J --> R(["🖨️ Report Printed"])
    K --> C
```

---

## 🗂️ Project Structure

```
Rationshop/
├── app.py                  # Flask backend — routes, DB & email logic
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment start command (e.g. Heroku/Render)
├── index.html               # Standalone copy of the frontend
├── templates/
│   └── index.html          # Main frontend served by Flask (Jinja template)
├── static/
│   └── images/
│       └── TNlogo.jpeg      # Branding / background watermark
└── README.md
```

---

## 🧩 Tech Stack

**Backend:** Python, Flask, Flask-CORS
**Database:** MySQL (via `mysql-connector-python`)
**Frontend:** HTML5, CSS3, Vanilla JavaScript (no framework)
**Notifications:** SMTP (Gmail) for email delivery
**Deployment:** Procfile included (Heroku / Render compatible)

---

## 🔌 API Reference

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | Serves the dashboard (`index.html`) |
| `GET` | `/members` | Fetch all registered members |
| `POST` | `/add-member` | Add a new member (`name`, `phone`, `email`) |
| `DELETE` | `/delete-member/<id>` | Remove a member by ID |
| `PUT` | `/toggle-status/<id>` | Toggle a member's ration-collected status |
| `POST` | `/send-email` | Email a message to **all** members |
| `POST` | `/send-reminder-email` | Email a reminder to a **specific list** of members |

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.8+
- MySQL Server running locally
- A Gmail account with an **App Password** enabled (for SMTP)

### 1. Clone the repository
```bash
git clone https://github.com/Soorya-SS-01/Rationshop.git
cd Rationshop
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up the database
Create a MySQL database named `ration_db` with a `members` table:
```sql
CREATE DATABASE ration_db;

USE ration_db;

CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100),
    collected BOOLEAN DEFAULT FALSE
);
```

### 4. Configure database credentials
Update the database connection details in `app.py` to match your local MySQL setup (host, user, password, database name).

### 5. Configure email credentials
Update the sender email and app password in `app.py` with your own Gmail account and an [App Password](https://support.google.com/accounts/answer/185833) for SMTP access.

### 6. Run the app
```bash
python app.py
```
The app will be available at `http://127.0.0.1:5000`

---

## 🚀 Future Improvements

- [ ] SMS notifications via Twilio (dependency already included)
- [ ] Pagination/search optimization for large member lists
- [ ] Monthly auto-reset scheduler for collection status
- [ ] Deploy live demo link

---

## 👤 Author

**Soorya S S**
[GitHub](https://github.com/Soorya-SS-01) · [LinkedIn](https://www.linkedin.com/in/soorya-s-s-364839370)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&animation=fadeIn" width="100%"/>
