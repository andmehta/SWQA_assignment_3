def retire(age, salary, pct_saved, goal):
    if age > 100 or age <= 0:
        print("Invalid age")
        raise SystemExit

    if salary <= 0:
        print("Invalid salary")
        raise SystemExit

    if pct_saved > 1 or pct_saved <= 0:
        print("Invalid percent saved")
        raise SystemExit

    if goal < 0:
        print("Invalid goal")
        raise SystemExit

    total = 0
    while total*1.35 < goal:
        total += salary*pct_saved
        age += 1

    if age > 100.0:
        return -1

    else:
        return age


