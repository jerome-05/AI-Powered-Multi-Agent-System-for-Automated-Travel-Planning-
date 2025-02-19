# 🌍 Multi-Agent Travel Planner ✈️🏨🗺️

![Travel Planner](https://source.unsplash.com/800x400/?travel,airplane)

## 📌 Project Overview
The **Multi-Agent Travel Planner** is an intelligent system that assists users in planning their trips by leveraging multiple AI agents. This system helps in:
- **Finding flights** 🛫
- **Booking hotels** 🏨
- **Creating an itinerary** 📍
- **Managing the budget** 💰

Powered by **LangChain**, **Hugging Face**, and **SerpAPI**, the planner provides seamless and automated travel recommendations. 🚀

---

## ⚙️ Features
✅ **Flight Finder**: Searches for flights based on user preferences (origin, destination, and dates).  
✅ **Hotel Finder**: Finds the best hotel deals for your stay.  
✅ **Itinerary Planner**: Suggests top attractions and activities at your destination.  
✅ **Budget Manager**: Helps track travel expenses and manage the budget efficiently.  

---

## 🏗️ Tech Stack
- **Python** 🐍
- **LangChain** 🧠
- **SerpAPI** 🔍
- **Hugging Face** 🤗
- **JSON & Logging** 📜

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
 git clone https://github.com/yourusername/Multi-Agent-Travel-Planner.git
 cd Multi-Agent-Travel-Planner
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys
Create a `.env` file and add your API keys:
```
SERPAPI_API_KEY=your_serpapi_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_key
```

Alternatively, set them as environment variables:
```bash
export SERPAPI_API_KEY='your_serpapi_key'
export HUGGINGFACEHUB_API_TOKEN='your_huggingface_key'
```

### 4️⃣ Run the Travel Planner
```bash
python multi_agent_travel.py
```

---

## 📜 Usage Example
**User Input:**
```
I want to fly from New York to Paris on March 20th and return on March 27th. My budget is $2000. Find me flights, hotels, and an itinerary.
```

**System Response:**
```
✅ Flights Found: New York ✈️ Paris (March 20th), Paris ✈️ New York (March 27th)  
✅ Hotels Suggested: 5 best hotels in Paris 🏨  
✅ Itinerary Created: Top attractions in Paris 📍  
✅ Budget Calculated: Remaining budget after expenses 💰  
```

---

## 📢 Contributing
We welcome contributions! 🚀 To contribute:
1. **Fork** this repository 🍴
2. **Create a new branch** (`feature-branch`) 🌱
3. **Commit your changes** 🔨
4. **Submit a Pull Request** 📩

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👥 Authors
- [Jerome Kenneth Gomes M](https://github.com/jerome-05) 💡

---

