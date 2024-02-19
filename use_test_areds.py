import test_areds

RE = test_areds.risk_factors_RE()
LE = test_areds.risk_factors_LE()
print("-" * 50)
points = test_areds.total(RE, LE)
print("-" * 50)
risk = test_areds.risk_score(points)