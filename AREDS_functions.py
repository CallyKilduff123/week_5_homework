
# AREDS trial looked at 5 year risk of developing advanced AMD based on fundus appearance
# risk factors = large drusen and pigment changes

def risk_factors_RE():
    drusen_re = 0
    pigment_re = 0
    right_eye1 = input("Right eye: Large drusen present? Y/N: ").upper()
    if right_eye1 == "Y":
        drusen_re += 1
        print("1 point")
    else:
        print("0 points")
    right_eye2 = input("Right eye: Pigment changes present? Y/N: ").upper()
    if right_eye2 == "Y":
        pigment_re += 1
        print("1 point")
    else:
        print("0 points")
    return drusen_re, pigment_re


def risk_factors_LE():
    drusen_le = 0
    pigment_le = 0
    left_eye1 = input("Left eye: Large drusen present? Y/N: ").upper()
    if left_eye1 == "Y":
        drusen_le += 1
        print("1 point")
    else:
        print("0 points")
    left_eye2 = input("Left eye: Pigment changes present? Y/N: ").upper()
    if left_eye2 == "Y":
        pigment_le += 1
        print("1 point")
    else:
        print("0 points")
    return drusen_le, pigment_le

def risk_score(score):
    # right = risk_factors_RE()
    # left = risk_factors_LE()
    # score = right + left
    # print("-" * 50)
    # print(f"Total Score = {sum(score)}")
    # print("-" * 50)
    if sum(score) == 0:
        print("5 year risk of developing advanced AMD = 0.5%")
    elif sum(score) == 1:
        print("5 year risk of developing advanced AMD = 3%")
    elif sum(score) == 2:
        print("5 year risk of developing advanced AMD = 12%")
    elif sum(score) == 3:
        print("5 year risk of developing advanced AMD = 25%")
    else:
        print("5 year risk of developing advanced AMD = 50%")
    return sum(score)


# if __name__ == "__main__":
# RE = risk_factors_RE()
# LE = risk_factors_LE()
# score = RE + LE
# print("-" * 50)
# print(f"Total Score = {sum(score)}")
# print("-" * 50)
# risk = risk_score(score)




