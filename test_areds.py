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

# tally points for LE
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


def total(right, left):
    add = (right + left)
    # final = sum(add)
    print(f"Total Score = {sum(add)}")
    return add


def risk_score(score):
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
    amd = sum(score)
    return amd