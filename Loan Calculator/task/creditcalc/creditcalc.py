import argparse
from math import ceil, floor, log


def print_results(
        mode, payment=None, principal=None, periods=None, interest=None
):
    if mode == "annuity":
        if not payment:
            payment = ceil(
                principal * (interest * pow(1 + interest, periods)
                             / (pow(1 + interest, periods) - 1))
            )
            print("Your annuity payment =", payment)
        elif not principal:
            principal = floor(
                payment * (pow(1 + interest, periods) - 1)
                / (interest * pow(1 + interest, periods))
            )
            print("Your loan principal =", principal)
        elif not periods:
            periods = ceil(
                log(payment / (payment - interest * principal),
                    1 + interest)
            )
            print_years_months(periods)
        print()
        print("Overpayment =", payment * periods - principal)
    elif mode == "diff":
        payments_sum = 0
        for m in range(1, periods + 1):
            mth_payment = ceil(
                principal / periods +
                interest * (principal - principal * (m - 1) / periods)
            )
            payments_sum += mth_payment
            print(f"Month {m}: payment is {mth_payment}")
        print()
        print("Overpayment =", payments_sum - principal)


def print_years_months(periods):
    if periods < 12:
        print(f"It will take {periods} months to repay this loan!")
    elif periods % 12 == 0:
        print(f"It will take {periods // 12} years to repay this loan!")
    else:
        print(f"It will take {periods // 12} years "
              f"and {periods % 12} months to repay this loan!")


parser = argparse.ArgumentParser(description="Behold: a loan calculator!!!")

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()
if args.interest:
    args.interest /= 1200
if not (args.type and args.interest) \
        or (args.type == "diff" and args.payment) \
        or [args.type, args.payment, args.principal,
            args.periods, args.interest].count(None) != 1:
    print("Incorrect parameters, use -h or --help")
else:
    print_results(args.type,
                  payment=args.payment, principal=args.principal,
                  periods=args.periods, interest=args.interest)
