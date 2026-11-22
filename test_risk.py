from risk import risk_score
def test_normal_is_low(): assert risk_score(100, 100) < 30
def test_huge_is_capped_at_100(): assert risk_score(1000, 100) == 100
def test_new_country_adds_risk(): assert risk_score(100, 100, True) > risk_score(100, 100, False)
