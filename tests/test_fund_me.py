from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIR
from scripts.deploy import depoly_contract
from brownie import network, accounts, exceptions
import pytest


def test_fund_and_withdraw():
    account = get_account()
    fund_me = depoly_contract()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_onlyOwnerCanWithdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIR:
        pytest.skip("only for local testing")

    fund_me = depoly_contract()
    bad_account = accounts.add()

    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_account})
