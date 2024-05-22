import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.stocks = {}

    def add_stock(self, symbol):
        if symbol not in self.stocks:
            self.stocks[symbol] = self.get_stock_data(symbol)
            print(f"Added {symbol} to portfolio.")
        else:
            print(f"{symbol} is already in the portfolio.")

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol} from portfolio.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def get_stock_data(self, symbol):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'Global Quote' in data:
                return data['Global Quote']
            else:
                print("Invalid response from API.")
        else:
            print("Error fetching data from API.")
        return None

    def display_portfolio(self):
        print("Portfolio Summary:")
        for symbol, data in self.stocks.items():
            print(f"Symbol: {symbol}")
            if data:
                print(f"Price: {data['05. price']}")
                print(f"Change: {data['10. change percent']}")
            else:
                print("Data not available.")
            print("------------------")


def main():
    api_key = 'your_alpha_vantage_api_key'
    portfolio = StockPortfolio(api_key)

    while True:
        print("\nStock Portfolio Tracking Tool")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            portfolio.add_stock(symbol)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            portfolio.remove_stock(symbol)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

        
