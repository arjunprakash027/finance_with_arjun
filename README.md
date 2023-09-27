
## Streamlit Project Documentation

### Introduction

This Streamlit project is designed to provide users with financial information and stock market news for Indian companies. It consists of three main components: a dashboard for exploring stock prices and historical trends, a section for displaying top stock headlines, and a common footer.

### Files

1. **app.py**

   - This is the main application file that manages the user interface and navigation.
   - It imports functions from `explore.py`, `news.py`, and `footsy.py`.
   - It allows users to choose between two pages: "news" and "explore."

2. **explore.py**

   - This file contains functions related to exploring stock prices and historical trends.
   - It uses libraries like `streamlit`, `matplotlib`, `seaborn`, `pandas`, `numpy`, `datetime`, `yahoofinancials`, and `altair`.
   - Users can select an Indian company, choose a start date, and set a time interval (monthly, weekly, or daily) to view historical stock data.
   - Various financial metrics like current price, revenue, profit, moving averages, and net income are displayed in the sidebar.
   - Users can also visualize stock price trends through line charts.
   - Additional statistics can be displayed by clicking the "show more stats" button.

3. **news.py**

   - This file contains functions for displaying top stock headlines.
   - It uses libraries like `streamlit`, `requests`, and `BeautifulSoup` for web scraping.
   - It fetches stock market news headlines from [Economic Times](https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms).
   - Users can expand each headline to view the associated link.

4. **footsy.py** 

   - HTML for footer

### How to Use

1. **Select a Page**

   - Upon running the application, users can choose between two pages: "news" and "explore."

2. **News Page**

   - In the "news" page, users can explore top stock headlines for the day.
   - Clicking on the headlines expands to reveal the associated link.

3. **Explore Page**

   - In the "explore" page, users can analyze historical stock data for Indian companies.
   - Choose a company, start date, and time interval to fetch historical data.
   - Various financial metrics are displayed in the sidebar.
   - Users can visualize historical price trends using line charts.
   - Additional statistics can be viewed by clicking the "show more stats" button.

### Dependencies

The project relies on several Python libraries, including `streamlit`, `matplotlib`, `seaborn`, `pandas`, `numpy`, `datetime`, `yahoofinancials`, `altair`, `requests`, and `BeautifulSoup`.

### Notes

- Please ensure that you have the necessary dependencies installed to run the application successfully.
- The `footsy.py` file is assumed to exist and provide common footer functionality for the application.

This documentation provides an overview of the Streamlit project's structure, features, and how to use it. It should help users navigate and utilize the application effectively.
