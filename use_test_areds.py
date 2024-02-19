import test_areds

RE = test_areds.risk_factors_RE()
LE = test_areds.risk_factors_LE()
print("-" * 50)
points = test_areds.total(RE, LE)
print("-" * 50)
risk = test_areds.risk_score(points)

# call function returning points for each eye in turn
# pass the returned values from those functions into the function that adds them together
# pass the returned value into the function that converts points into % risk

# passing values = like a game of netball :)