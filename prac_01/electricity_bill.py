print("Please enter inputs to calculate your electricity bill.")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
cost = int(input("Which tariff are you on, 11 or 31? "))
usage = float(input("How many kWh are used per day? "))
bill_period = int(input("How many days are in the billing period? "))
if cost == 11:
    bill = (TARIFF_11 * usage) * bill_period
else:
    bill = (TARIFF_31 * usage) * bill_period
print("Estimated bill: $""%.2f" % bill, end=' ')
