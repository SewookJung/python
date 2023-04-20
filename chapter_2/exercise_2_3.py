"""
Question
 - Which is cheaper to buy a laptop in dollar or euro?

Purpose
 - Find the exchange rate uero and dollar


"""

dollar_exchange_rate = 1386
euro_exchange_rate = 1388

labtop_price_by_dollar = 750
laptap_price_by_euro = 650

laptop_with_dollar = dollar_exchange_rate * labtop_price_by_dollar
laptop_with_euro = euro_exchange_rate * laptap_price_by_euro

if laptop_with_dollar > laptop_with_euro:
    print("Buy laptop with euro")
else:
    print("Buy laptop with dollar")