def score_bid(row):
    """
    Score bids based on price, delivery, performance, and compliance.
    """
    price_weight = 0.3
    delivery_weight = 0.1
    performance_weight = 0.4
    compliance_weight = 0.2

    price_score = 1 / row['price']
    delivery_score = 1 / row['delivery_days']

    return (price_score * price_weight +
            delivery_score * delivery_weight +
            row['performance'] * performance_weight +
            row['compliance'] * compliance_weight)
