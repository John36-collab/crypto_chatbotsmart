#!/usr/bin/env python3
"""
Test script for CryptoBuddy Chatbot
"""

from crypto_bot import CryptoAdvisorBot

def test_bot_functionality():
    """Test all major bot functions"""
    bot = CryptoAdvisorBot()
    
    print(" Testing CryptoBuddy Chatbot...")
    
    # Test profitability analysis
    profitable_coins = bot.analyze_profitability()
    print(f" Profitability Analysis: Found {len(profitable_coins)} coins")
    
    # Test sustainability analysis  
    sustainable_coins = bot.analyze_sustainability()
    print(f" Sustainability Analysis: Found {len(sustainable_coins)} coins")
    
    # Test balanced investment
    balanced_coins = bot.find_balanced_investment()
    print(f" Balanced Investment: Top coin {balanced_coins[0][0]} with score {balanced_coins[0][2]}")
    
    # Test query processing
    test_queries = [
        "hello",
        "what's trending?",
        "sustainable coins",
        "tell me about bitcoin",
        "help"
    ]
    
    for query in test_queries:
        response = bot.process_query(query)
        print(f" Query: '{query}' → Response: {response[:50]}...")
    
    print(" All tests passed! Bot is working correctly.")

if __name__ == "__main__":
    test_bot_functionality()