# 🕵️ LOL Party Tools – Spy Drawer

A lightweight web tool to randomly assign a "spy" among 5 League of Legends players before a game.  
Perfect for custom games with friends where a bit of mystery makes things more fun.

---

## 🔧 Tech Stack

- 🐍 Python 3
- 🎈 Streamlit (web UI)
- 📊 Pandas (CSV handling)
- 🎲 Random (spy selection logic)

---

## 🚀 How to Use

### ▶️ Run Locally (for developers)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then visit:  
```
http://localhost:8501
```

---

### 🌍 Public Deployment (Streamlit Cloud)

If deployed via [Streamlit Cloud](https://streamlit.io/cloud), you can access it from anywhere:

```
[https://your-username.streamlit.app](https://league-of-legends-funprojects.streamlit.app/)
```

No installation required — just upload a CSV and click a button.

---

## 📥 Input Format

Upload a `.csv` file with exactly 5 players. The file must contain one column named `player_name`:

```csv
player_name
A
B
C
D
E
```

> ⚠️ Current version supports **exactly** 5 players.

---

## 🎯 How It Works

1. Upload your player list CSV
2. Click the 🎲 “Draw Spy” button
3. The result will be revealed directly on the page

---

## 🧪 Screenshot (Optional)

_Add a screenshot of your Streamlit app here for visual reference:_

![image](https://github.com/user-attachments/assets/5fadb4ce-a4f9-46f8-88be-156a237b8525)


---

## 🛠 Future Enhancements

| Feature            | Description                                    |
|--------------------|------------------------------------------------|
| No-CSV input       | Replace file upload with on-page text input   |
| Private role view  | One player at a time reveals their identity   |
| More game modes    | Add Undercover / Captain / Role shuffle modes |
| Export option      | Download role assignment as ZIP or TXT        |
| UI/Theming         | Add background, emoji roles, and sound effects|

---

## 📁 Project Structure

```bash
League-of-Legends-FunProjects/
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation (this file)
├── .gitignore
└── sample_players.csv   # Example input file
```

---

## 🤝 Author

Made with ❤️ by [Allen](https://github.com/allensayyes)  
Powered by [Streamlit](https://streamlit.io)

---

## 🪪 License

MIT License. Free to use, share, and modify.  
But don't ruin your friendships over this 😎
