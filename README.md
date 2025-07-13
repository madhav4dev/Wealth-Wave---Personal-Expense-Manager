
# 🌊 Wealth Wave — Budget Tracker

**Wealth Wave** is a Django-based web application designed to help users efficiently manage their income and expenses. It offers a sleek and intuitive interface packed with essential tools like advanced filtering, visual analytics, and CSV export to help you take control of your finances.

---

## 🚀 Features

- 🔐 **User Authentication** – Secure login/logout system
- 💸 **Transaction Management** – Add, edit, and delete incomes and expenses
- 🗂️ **Smart Filtering** – Filter transactions by date range, category, and type
- 📊 **Analytics Dashboard** – Visualize spending patterns and income trends
- 🌗 **Dark Mode Toggle** – Easily switch between light and dark themes
- 📤 **Export to CSV** – Download your transaction history
- 🛠️ **Admin Panel** – Manage users and data using Django’s built-in admin
- 🌐 **Responsive Design** – Works seamlessly across all screen sizes

---

## 🛠️ Tech Stack

- **Framework:** Django (Python 3)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** MySQL
- **Analytics:** Chart.js (or similar library)

---

## 📁 Project Structure

```
wealth_wave/
├── tracker/              # Main app: models, views, templates, static files
├── budget_tracker/       # Project configuration and URLs
├── static/               # Global static files (CSS, JS)
├── templates/            # HTML templates
├── requirements.txt
├── manage.py
└── README.md
```

---

## ⚙️ Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/wealth-wave.git
cd wealth-wave

# Set up virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations and start the server
python manage.py migrate
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## ✅ Highlights

- Dark mode toggle  
- Transaction filtering by category, type, and date  
- Export to CSV  
- Mobile-friendly and responsive design  

---

## 🔭 Future Enhancements

- Add budgeting goals and spending limits
- PDF export option
- Monthly summary reports

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Madhav**  
Crafted as a personal project to explore full-stack development using Django.  
⭐ If you found this useful, consider giving it a star on [GitHub](https://github.com/yourusername/wealth-wave)!
