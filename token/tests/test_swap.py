#!/usr/bin/python3

import pytest
from brownie import Contract, UniswapV2Pair


def test_custom_token_swap(Token, accounts):
    print('Tokens deploying')
    token1 = accounts[0].deploy(Token, "Vlad Token", "VST", 1e23)
    token2 = accounts[0].deploy(Token, "Alice Token", "AST", 1e23)

    for token in [token1, token2]:
        print('Deployed token: ' + str(token.name()) + ' by address: ' + str(token))
        print('Account balance: ' + str(token.balanceOf(accounts[0])))

    print('Load factory contract...')
    factory = Contract.from_explorer('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f')
    factory.createPair(token1, token2, {'from': accounts[0]})

    pair = Contract.from_abi("UniswapV2Pair", factory.getPair(token1, token2), UniswapV2Pair.abi)
    print('Created pair ' + str(pair) + ' of tokens: (' + pair.token0() + ', ' + pair.token1() + ')')

    assert str(token1) == str(pair.token0()) and str(token2) == str(pair.token1())

    print('Initial reserves: ' + str(pair.getReserves()))

    print('Add liquidity 1e18 for both tokens')
    token1.transfer(pair.address, 1e18)
    token2.transfer(pair.address, 1e18)

    print('Syncing...')
    pair.sync({'from': accounts[0]})

    print('Updated reserves: ' + str(pair.getReserves()))

    print('Transfer to pair')
    token1.transfer(pair.address, 2e5)

    for token in [token1, token2]:
        print('Token ' + str(token.name()) + '. Account balance: ' + str(token.balanceOf(accounts[0])))

    print('Swap 1e5 ' + str(token1.name()) + ' to ' + str(token2.name()))
    pair.swap(0, 1e5, accounts[0], bytes(), {'from': accounts[0]})

    print('Swapped')
    for token in [token1, token2]:
        print('Token ' + str(token.name()) + '. Account balance: ' + str(token.balanceOf(accounts[0])))

    print('Syncing...')
    pair.sync({'from': accounts[0]})
    print('Updated reserves: ' + str(pair.getReserves()))




