def risk_score(amount, usual_amount, new_country=False):
    score = 2 * (amount / usual_amount)
    if new_country:
        score += 30
    return min(100, score)
