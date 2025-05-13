# 📈 Stock Monitoring & Alert System

A full-stack application that monitors price changes, dividends, trends, and other market data for selected securities. It provides customizable alerts for various market events such as **trend changes**, **breakouts**, **volume spikes**, and **upcoming dividends**. It also enables **historical performance analysis** and **AI-assisted insights**.

---

## 🚀 Features

- 🔔 **Real-Time Alerts**  
  Get notified about trend shifts, price breakouts, volume surges, and dividend announcements.

- 📊 **Historical Data Analysis**  
  Study stock performance over time to identify patterns and trends.

- 🧪 **Custom Filters**  
  Set up your own alert criteria — no noise, just what matters to you.

- 🤖 **AI Integration**  
  Receive basic AI-powered summaries of stock behavior and key metrics.

- 🌐 **Multiple Data Sources**  
  Pulls data from **TMX**, **AlphaVantage**, and other providers.

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)  
- **Database**: MySQL + SQLAlchemy ORM  
- **AI/ML**: Basic trend detection (planned enhancement)  
- **Alerts**: Real-time email/SMS (planned enhancement)  
- **Frontend**: React (planned)

---

## 🧪 Getting Started

### 📋 Prerequisites

- Python `3.8+`  
- MySQL (MySQL Workbench is useful too)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stock-monitoring-app.git
cd stock-monitoring-app
```

### 2. Set up MySQL Database:

- Create a MySQL database and user for the app.


### 3. Run Database Migrations:

- The app uses SQLAlchemy for ORM-based database management. Run migrations to create tables in MySQL.

- You can manually create the database or let the app create it on startup.


### 4. Start the Application:

```bash
uvicorn main:app --reload
```

or (use any convenient port)
```bash
uvicorn main:app --host 127.0.0.1 --port 8080
```


### 5. Testing the API:

- This will start the FastAPI application locally. Open the browser and go to http://127.0.0.1:8000 to access the API.

- Visiting http://127.0.0.1:8000/docs will open the testing environment for FastAPI backend (no Postman here)

- You can also visit the http://127.0.0.1:8080/stocks/html_summary to see the stocks stored in the database along with their records' first and last, it looks like this:
![image](https://github.com/user-attachments/assets/a01f62a3-ca37-4197-8d34-7f7aeb77b738)



## Future Enhancements

- Front-End Dashboard: A React-based front-end for visualizing stocks and their performance.

- More Complex AI/ML Models: Integration of advanced stock prediction or anomaly detection models.

- Notification Services: Expand alerting systems to include email, SMS, or push notifications.

- Performance Optimization: Investigate database partitioning and indexing strategies to improve query performance with large datasets.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
