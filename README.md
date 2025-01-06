# Stock Dashboard Flask App

This is a Flask-based web application that allows users to search for stock information using the Alpha Vantage API, manage a list of favorite stocks, and view details about specific stocks.

## Features

- **Dashboard**: Home page of the application.
- **Search Stock**: Search for stock information by symbol.
- **Favorites**: Add or remove stocks to/from your favorites list.
- **View Favorite Stock**: View details about a specific stock in your favorites.

## Prerequisites

Before running this application, ensure you have the following:

- Python 3.7 or higher installed.
- Flask and other dependencies installed.
- An Alpha Vantage API key.
- `.env` file configured with the following variables:

```env
SECRET_KEY=your_secret_key
API_KEY=your_alpha_vantage_api_key
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/stock-dashboard.git
   cd stock-dashboard
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the project directory with the following content:

   ```env
   SECRET_KEY=your_secret_key
   API_KEY=your_alpha_vantage_api_key
   ```

## Usage

1. **Run the application**:

   ```bash
   python app.py
   ```

2. **Access the application**:

   Open your browser and navigate to `http://127.0.0.1:5000`.

## Endpoints

### `/`
- **Method**: GET
- **Description**: Displays the dashboard page.

### `/search`
- **Method**: GET/POST
- **Description**: Search for stock information by symbol. The POST method retrieves stock data.

### `/favorites`
- **Method**: GET
- **Description**: Displays the user's favorite stocks.

### `/add_favorite`
- **Method**: POST
- **Description**: Adds a stock to the favorites list.

### `/remove_favorite`
- **Method**: POST
- **Description**: Removes a stock from the favorites list.

### `/favorites/<symbol>`
- **Method**: GET
- **Description**: Displays details of a specific favorite stock.

### `/favorites/data/<symbol>`
- **Method**: GET
- **Description**: Returns JSON data of a specific favorite stock.

## Folder Structure

```
stock-dashboard/
├── app.py            # Main application file
├── templates/        # HTML templates
│   ├── dashboard.html
│   ├── favorites.html
│   ├── search.html
│   ├── stock.html
├── static/           # Static files (CSS, JS, images)
├── .env              # Environment variables
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## API Reference

This application uses the [Alpha Vantage API](https://www.alphavantage.co/documentation/) for fetching stock data. Ensure you have a valid API key and include it in the `.env` file.


