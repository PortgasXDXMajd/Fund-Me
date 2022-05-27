from brownie import FundMe, accounts, config, network
from scripts.helpful_scripts import get_account, get_PriceFeedAddress, IsPublishable


def depoly_contract():
    account = get_account()
    print(f"account is {account}")

    price_feed_address = get_PriceFeedAddress()
    print(f"price feed  is {price_feed_address}")

    fund_me = FundMe.deploy(
        price_feed_address, {"from": account}, publish_source=IsPublishable()
    )
    return fund_me


def main():
    depoly_contract()
