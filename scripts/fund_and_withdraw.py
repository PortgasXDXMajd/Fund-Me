from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    account = get_account()
    fund_me = FundMe[-1]

    entrance_fee = fund_me.getEntranceFee()
    print("funding...")

    fund_me.fund({"from": account, "value": 15 * 10**18})


def wuthdraw():
    account = get_account()
    fund_me = FundMe[-1]
    print("withdraw...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    wuthdraw()
