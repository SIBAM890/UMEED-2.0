# 🌱 UMEED 2.0

**Your Digital Mental Wellness Companion**
A safe, supportive, and interactive platform designed to nurture emotional wellbeing, foster peer support, and connect users with mental health resources.

# 🎯 The Problem
Mental health support is often:
❌ Hard to access
❌ Expensive
❌ Stigmatized
❌ Lacking early intervention tools
People struggle silently without proper outlets, guidance, or awareness — especially students and young adults.

**Before UMEED 2.0:**

* ❌ No safe digital peer-support space
* ❌ No practical early detection tools
* ❌ No centralized mental wellness resources
* ❌ Students unaware of coping strategies or self-care

**With UMEED 2.0:**

* ✅ Anonymous safe space for peer discussion
* ✅ Chatbot for emotional assistance
* ✅ Mood tracking to detect patterns
* ✅ Resource hub with verified mental health information
* ✅ Admin dashboard for management and monitoring
  
# ✨ Features

### 🤖 AI Chatbot (TheraBot)

Your friendly companion for emotional support, basic guidance, and mental wellness conversations.

### 😀 Daily Mood Tracker

Track emotional patterns, receive insights, and observe trends over time.

### 💬 Peer Support Forum

A moderated space where users can share experiences, support peers, and build community.

### 📚 Mental Health Resource Library

Curated PDFs, guides, and trusted resources for better understanding mental wellbeing.

### 🛋 Virtual Lounge

A relaxing digital environment promoting mindfulness and taking mental breaks.

### 🛡 Admin Dashboard

Admins can manage posts, monitor activity, ensure safety, and handle community guidelines.


**(Add link here)**
`https://your-demo-url.com` *(optional)*

### 🖥 Local Development


# Clone the repository
git clone YOUR_REPO_URL_HERE
cd UMEED-2.0

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python run.py


Visit:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)
to view the project locally.

# 🛠️ Tech Stack

**Backend:** Flask (Python)
**Frontend:** HTML, CSS, JavaScript
**Database:** SQLite
**Design:** Minimal, calming theme
**Authentication:** Admin-based control
**Assets:** SVG icons, PDFs, static resources


# 🗂️ Project Structure

UMEED-2.0/
├── app/
│   ├── static/           # CSS, JS, Icons, PDFs
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   ├── routes.py         # Application routes
│   ├── events.py         # Event handlers
│   ├── extensions.py     # DB initialization
│   └── __init__.py       # App factory
│
├── instance/
│   └── umeed.db          # SQLite database
│
├── run.py                # App entry point
├── requirements.txt      # Python dependencies
└── .gitignore

# ⚙️ Environment Variables
Create a `.env` file in the root folder:

```
SECRET_KEY=your_secret_key
DATABASE_URI=sqlite:///umeed.db
DEBUG=True
```
# 🗄️ Database Schema (SQLite)
The database includes:

### **users table**
* id
* username
* password
* role (admin/user)

### **posts table**
* id
* content
* user_id
* created_at

### **mood_logs table**
* id
* mood
* note
* created_at
*(Your actual schema may vary based on your models.)*

# 🤝 Contributing
Contributions are always welcome ❤️
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

# 📝 License
This project is licensed under the **MIT License**.

# 🙏 Acknowledgments
* Built using **Flask**
* Inspired by real-world mental wellness challenges
* Icons from various open-source libraries
* PDFs included for educational purposes


