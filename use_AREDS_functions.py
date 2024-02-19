import AREDS_functions

# Calculate 5 year risk of developing advanced AMD based on fundus findings:

RE = AREDS_functions.risk_factors_RE()
LE = AREDS_functions.risk_factors_LE()
score = RE + LE
print("-" * 50)
print(f"Total Score = {sum(score)}")
print("-" * 50)
risk = AREDS_functions.risk_score(score)


