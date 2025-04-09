# 🎥 Snap2Reel — Image to Video Creator

Snap2Reel is a Django-based web application that allows users to upload multiple images, select background music and transition styles, and convert them into a stylish video slideshow with animations and sound.

---

## 🚀 Features

- 📤 Upload multiple images (drag-and-drop or file input)
- 🎵 Choose or upload background music
- 🎨 Select transition styles (fade, slide, zoom, etc.)
- 🎬 Animated video generation with themes (birthday, travel, wedding)
- 🎧 Music overlay and video export in MP4
- 🔍 In-browser video preview
- 📩 Optional: Send video to email
- 🧾 Optional: User login and saved projects

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript (vanilla or jQuery)
- **Media Processing:** `moviepy`, `ffmpeg`, `pydub`, `Pillow`
- **File Handling:** Django FileSystem or `django-storages`
- **Database:** SQLite (default), PostgreSQL (optional for production)

---

## 📂 Project Structure

```
snap2reel/
│
├── media/                  # Uploaded files (images, music, generated videos)
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS)
├── video_generator/        # App handling media logic
│   ├── views.py            # Core logic for upload, video creation
│   ├── utils.py            # Helper functions for transitions, video rendering
│   └── models.py           # Media file models
│
├── snap2reel/              # Django project settings
│   ├── settings.py
│   └── urls.py
│
├── requirements.txt
└── manage.py
```

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/obaidullah72/snap2reel.git
cd snap2reel
```

2. **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Run the server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📦 Dependencies

```
Django
moviepy
ffmpeg-python
pillow
pydub
django-storages
```

Install manually if needed:

```bash
pip install django moviepy ffmpeg-python pillow pydub django-storages
```

> ⚠️ Make sure **FFmpeg** is installed and added to your system PATH.

---

## 🧪 How It Works

1. User uploads images and selects music/theme
2. Django stores the files and triggers the video generation
3. `moviepy` + `ffmpeg` adds transitions, animations, music
4. Final video is saved and returned to the user as MP4

---

## ✅ To-Do (Optional Improvements)

- [ ] Add login/signup and project saving
- [ ] More themes and transition styles
- [ ] Voice-over support
- [ ] Cloud storage integration (S3, Google Drive)
- [ ] Mobile-friendly UI

---

## 🧑‍💻 Author

Built with ❤️ by [Your Name]  
GitHub: [@obaidullah72](https://github.com/obaidullah72)

---

## 🤝 Contributions

Contributions are welcome!  
Fork the repo and submit a PR with your improvements.

---

## 📜 License

Licensed under the [MIT License](LICENSE).

---

## 📬 Contact Me

Feel free to reach out for any questions or suggestions:  

- **GitHub**: [obaidullah72](https://github.com/obaidullah72)  
- **LinkedIn**: [obaidullah72](https://www.linkedin.com/in/obaidullah72/)  

[![Visitor Count](https://visitcount.itsvg.in/api?id=obaidullah72&label=Profile%20Views&color=0&icon=0&pretty=true)](https://visitcount.itsvg.in)
