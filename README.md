# 🧠 বিজ্ঞানমেলা – Science Made Fun, Friendly & Fact-Based (in Bangla)

A Bengali-first interactive web app where users can chat with legendary scientists, bust myths, verify claims, and learn scientific thinking — all through AI-powered conversations and simulations.

👥 Built for the **SN Bose National Science Festival 2025 – IT Hackathon** by **Team Alpha (SNIH202544)**

---

## 🌟 Features

- 👨‍🔬 **Chat with Scientists**  
  Talk to 20 legendary science icons like Einstein, Satyendra Nath Bose, Curie, and more — all in Bangla.

- ✅ **Bust Myths with Fact Checks**  
  Submit any scientific claim and get AI-generated trust score, verdict, sources, and explanation — in Bangla.

- 🧪 **Scientific Method Simulations**  
  Gamified case studies (e.g., “Why are fish dying in a river?”) that teach hypothesis, testing, and reasoning.

- 🧠 **Critical Thinking Playground**  
  Interactive logic games and story-based reasoning tasks to build scientific mindset.

- 🌐 **Bangla-Only UI**  
  100% localized interface and content in Bengali — accessible to all learners.

---

## 🧰 Tech Stack

| Layer           | Technology                         |
|----------------|-------------------------------------|
| Frontend        | HTML, Tailwind CSS, JavaScript     |
| Backend         | Django (REST API)                  |
| AI Integration  | Google Gemini 2.0 Flash API        |
| Local LLM (extra) | Ollama + Mistral 7B (on VM)      |
| Hosting         | Deployed on custom server (VPS)    |

---

## 📁 Repository Structure

```

📦 scientistbuddy/
├── frontend/                 # HTML + Tailwind components
├── backend/                 # Django project
│   ├── views.py             # Handles chat, fact-check, simulation APIs
│   └── urls.py
├── static/                  # Assets (CSS, images)
├── templates/               # Django templates
├── README.md
├── requirements.txt
└── manage.py

````

---

## 🚀 Getting Started (Local Setup)

```bash
# 1. Clone the repo
git clone https://github.com/yourteam/scientistbuddy.git && cd scientistbuddy

# 2. Create virtual environment
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key in views.py or as an env variable

# 5. Run the server
python manage.py runserver
````

---

## 🎬 Demo Links

* 🔴 **Live App**: [http://203.190.9.175:7090/](http://203.190.9.175:7090/)
* 📽️ **Demo Video**: [Watch here](https://drive.google.com/drive/folders/1laPPgO6kMwXADEwv5BJElVmyazQ_fkWn?usp=sharing)
* 📑 **Presentation Slides**: `বিজ্ঞানমেলা_ Science Made Fun, Friendly & Fact-Based.pptx` (Included in submission ZIP)
* 📝 **2-page Project Document**: Included in submission ZIP

---

## 🛠️ Authors – Team Alpha (SNIH202544)

| Name              | Role                |
| ----------------- | ------------------- |
| Md Mobashir Hasan | AI Engineer         |
| Abdullah Al Mamun | Backend Developer   |
| Simanta Kumar Roy | DevOps / Deployment |

---

## 📌 License

This project is built for educational & demonstration purposes for the SN Bose Science Festival 2025 Hackathon.

---

## 🙏 Acknowledgements

* Google Gemini API
* Mistral 7B via Ollama
* Tailwind CSS
* Django & Python Community
* BRAC-Biggan Adda & SN Bose Science Festival organizers

---

> “Encouraging young minds to question, explore, and trust science — one conversation at a time.” – Team Alpha
