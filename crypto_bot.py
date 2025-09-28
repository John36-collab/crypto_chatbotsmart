"""
CryptoBuddy - AI-Powered Cryptocurrency Advisor Chatbot
Author: [John36_collab]
Date: [2025-09-28]
"""

# Cryptocurrency database with predefined data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3,   # out of 10
        "risk_level": "medium"
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6,
        "risk_level": "medium"
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8,
        "risk_level": "low"
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "risk_level": "medium"
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "risk_level": "low"
    },
    "Algorand": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 9,
        "risk_level": "low"
    }
}

class CryptoAdvisorBot:
    def __init__(self, name="CryptoBuddy"):
        self.name = name  
        self.greeting = "Hey there! Let's find you a green and growing crypto!"
        self.disclaimer = "⚠ Remember: Crypto is risky—always do your own research!"
        self.conversation_history = []

    def greet_user(self):
        """Display welcome message and instructions"""
        print(f"\n{'='*60}")
        print(f" {self.name}: {self.greeting}")
        print(f"{'='*60}")
        print(f" {self.name}: {self.disclaimer}")
        print(f"\n{self.name}: How can I help you today?")
        print("\nYou can ask me about:")
        print("  - Trending cryptocurrencies")
        print("  - Sustainable/eco-friendly coins") 
        print("  - Best long-term investments")
        print("ℹ   - Specific crypto information")
        print("  - Risk analysis")
        print("  - Type 'help' for options")
        print("  - Type 'quit' to exit")
        print("-" * 50)

    def log_conversation(self, user_input, bot_response):
        """Keep track of conversation history"""
        self.conversation_history.append({
            "user": user_input,
            "bot": bot_response,
            "timestamp": "2025"  # placeholder timestamp
        })

    # --- ANALYSIS METHODS ---
    def analyze_profitability(self):
        profitable_coins = []
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]:
                profitable_coins.append((coin, data))
        profitable_coins.sort(
            key=lambda x: (x[1]["market_cap"] == "high", x[1]["sustainability_score"]),
            reverse=True
        )
        return profitable_coins

    def analyze_sustainability(self):
        sustainable_coins = []
        for coin, data in crypto_db.items():
            if data["energy_use"] == "low" and data["sustainability_score"] >= 7:
                sustainable_coins.append((coin, data))
        sustainable_coins.sort(key=lambda x: x[1]["sustainability_score"], reverse=True)
        return sustainable_coins

    def find_balanced_investment(self):
        balanced_coins = []
        for coin, data in crypto_db.items():
            score = 0
            if data["price_trend"] == "rising": score += 3
            if data["market_cap"] == "high": score += 2
            elif data["market_cap"] == "medium": score += 1
            if data["energy_use"] == "low": score += 3
            elif data["energy_use"] == "medium": score += 1
            score += data["sustainability_score"] * 2
            balanced_coins.append((coin, data, score))
        balanced_coins.sort(key=lambda x: x[2], reverse=True)
        return balanced_coins

    def get_coin_info(self, coin_name):
        coin_name = coin_name.lower()
        for coin in crypto_db.keys():
            if coin_name in coin.lower():
                return crypto_db[coin]
        return None

    def assess_risk(self, coin_name):
        coin_data = self.get_coin_info(coin_name)
        if not coin_data:
            return None
        return coin_data["risk_level"]

    # --- QUERY HANDLER ---
    def process_query(self, user_input):
        user_input_lower = user_input.lower()
        
        if any(word in user_input_lower for word in ["hello", "hi", "hey", "greetings"]):
            return f"{self.name}: Hello! Ready to explore smart crypto investments?"

        elif any(word in user_input_lower for word in ["trend", "profit", "rising", "growing", "best investment", "make money"]):
            profitable_coins = self.analyze_profitability()
            if profitable_coins:
                best_coin = profitable_coins[0]
                return f"{self.name}: For profitability, consider {best_coin[0]}! It's {best_coin[1]['price_trend']} with a {best_coin[1]['market_cap']} market cap and sustainability score {best_coin[1]['sustainability_score']}/10."
            else:
                return f"{self.name}: Currently no strongly trending coins meet my profitability criteria."

        elif any(word in user_input_lower for word in ["sustainable", "eco", "green", "environment", "energy", "planet"]):
            sustainable_coins = self.analyze_sustainability()
            if sustainable_coins:
                best_coin = sustainable_coins[0]
                return f"{self.name}: Top sustainable choice: {best_coin[0]}! Energy: {best_coin[1]['energy_use']}, Sustainability: {best_coin[1]['sustainability_score']}/10, Risk: {best_coin[1]['risk_level']}."
            else:
                return f"{self.name}: No highly sustainable coins available in my database."

        elif any(word in user_input_lower for word in ["long term", "long-term", "future", "hold", "balanced"]):
            balanced_coins = self.find_balanced_investment()
            if balanced_coins:
                best_coin = balanced_coins[0]
                return f"{self.name}: For long-term growth, I recommend {best_coin[0]}! It balances profitability and sustainability perfectly. Score: {best_coin[2]}/10"
            else:
                return f"{self.name}: No ideal long-term options found in current market conditions."

        elif any(word in user_input_lower for word in ["risk", "safe", "danger", "volatile"]):
            for coin in crypto_db.keys():
                if coin.lower() in user_input_lower:
                    risk_level = self.assess_risk(coin)
                    if risk_level:
                        return f"{self.name}: {coin} has {risk_level} risk level."
            return f"{self.name}: Ask about risk for specific coins like Bitcoin, Ethereum, or Cardano."

        elif any(word in user_input_lower for word in [coin.lower() for coin in crypto_db.keys()]):
            for coin in crypto_db.keys():
                if coin.lower() in user_input_lower:
                    data = crypto_db[coin]
                    return f"""ℹ  {coin} Analysis:
 Price Trend: {data['price_trend']} 
 Market Cap: {data['market_cap']}
 Energy Use: {data['energy_use']}
 Sustainability: {data['sustainability_score']}/10
 Risk Level: {data['risk_level']}
 Recommendation: {'Good for long-term' if data['sustainability_score'] >= 7 else 'Monitor trends'}"""

        elif "list" in user_input_lower or "all" in user_input_lower or "coins" in user_input_lower:
            coins_list = "\n".join([f"• {coin}" for coin in crypto_db.keys()])
            return f"{self.name}: Available cryptocurrencies:\n{coins_list}"

        elif "help" in user_input_lower:
            return f"""{self.name}: I can help you with:

 Trending Cryptos - "What's trending?"
 Sustainable Coins - "Show me eco-friendly coins"  
 Long-term Investments - "Best long-term crypto?"
ℹ  Coin Info - "Tell me about Bitcoin"
 Risk Analysis - "Is Ethereum risky?"
 List All - "Show all cryptocurrencies"

Try these examples!"""

        else:
            return f"{self.name}: I'm not sure I understand. Try asking about crypto trends, sustainability, or type 'help' for options!"

# --- MAIN ---
def main():
    bot = CryptoAdvisorBot()
    bot.greet_user()
    conversation_count = 0
    while True:
        try:
            user_input = input("\n You: ").strip()
            if not user_input:
                print(f"{bot.name}: Please type a question or 'help' for options!")
                continue
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye', 'q']:
                print(f"\n{'='*60}")
                print(f"{bot.name}: Thanks for chatting! We had {conversation_count} conversations.")
                print(f"{bot.name}: Remember to diversify your investments!")
                print(f"{bot.name}: Happy investing!")
                print(f"{'='*60}")
                break
            response = bot.process_query(user_input)
            print(f"\n{response}")
            bot.log_conversation(user_input, response)
            conversation_count += 1
        except KeyboardInterrupt:
            print(f"\n\n{bot.name}: Session ended by user. Stay crypto-savvy!")
            break
        except Exception as e:
            print(f"\n{bot.name}: Oops! Something went wrong. Let's try again.")
            print(f"Debug: {e}")

if __name__ == "__main__":
    print("Starting CryptoBuddy Chatbot...")
    main()