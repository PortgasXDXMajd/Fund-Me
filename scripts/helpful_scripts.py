from brownie import MockV3Aggregator, accounts, network, config


FORKED_LOCAL_ENV = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIR = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIR
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        print(network.show_active())
        return accounts[0]

    elif network.show_active() == "rinkeby":
        print("Rinkeby network")
        return accounts.add(config["wallets"]["test_private_key"])

    elif network.show_active() == "mainnet":
        print("Mainnet network")
        return accounts.load("MyAccount")


def get_PriceFeedAddress():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIR:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]

    else:
        # deploy mock aggregator
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        # latest mocks we've deployed
        return MockV3Aggregator[-1].address


def IsPublishable():
    return config["networks"][network.show_active()].get("verify")
