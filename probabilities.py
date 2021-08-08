def pot_odds(pot, bet):
    """Pot sized bet gives you 2:1 on your money, or 33%+ equity needed to continue."""
    return (float(bet) + float(pot)) / (float(pot) + 2.0 * float(bet))

def fold_frequency(pot, bet):
    """Pot sized bet gives you a 50% fold frequency."""
    return float(bet) / (float(pot) + float(bet))

def should_call(equity, pot_odds):
    """Basic function that uses only the expected value to calculate whether to call or not."""
    return equity > pot_odds