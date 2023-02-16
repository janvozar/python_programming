def calculate_discounted_price(price, discount_rate):
    discounted_price = price * (1 - discount_rate)
    return discounted_price

def apply_discount(prices, discount_rate):
    discounted_prices = []
    for price in prices:
        discounted_price = calculate_discounted_price(price, discount_rate)
        discounted_prices.append(discounted_price)
    return discounted_prices

def get_total_price(prices):
    total = 0
    for price in prices:
        total += price
    return total

def main():
    prices = [10.0, 20.0, 30.0, 40.0]
    discount_rate = 0.1
    discounted_prices = apply_discount(prices, discount_rate)
    total_discounted_price = get_total_price(prices)
    print("Původní ceny: ", prices)
    print("Ceny po slevě: ", discounted_prices)
    print("Celková cena po slevě: ", total_discounted_price)

if __name__ == "__main__":
    main()