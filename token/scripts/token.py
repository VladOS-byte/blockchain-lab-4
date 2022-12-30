#!/usr/bin/python3

from brownie import Token, accounts

def main():
	return Token.deploy("Test Token", "TST", 1e21, {'from': accounts[0]})

