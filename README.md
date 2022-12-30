# blockchain-lab-4
## Requirements
- python3
- eth-brownie
## Pre-usage
- install brownie
- [create](https://eth-brownie.readthedocs.io/en/stable/network-management.html?highlight=network#using-a-forked-development-network) fork mainnet network in brownie
## Usage
- For test swapping use
```
brownie test tests/test_swap.py -s --disable-warnings --network mainnet-fork
```
- For test Token use
```
brownie test -s --disable-warnings --network mainnet-fork
```
## Output
- For test swapping
```
MBP-Vlad-2:token vlad$ brownie test tests/test_swap.py -s --disable-warnings --network mainnet-fork
Brownie v1.19.2 - Python development framework for Ethereum

===================================================== test session starts =====================================================
platform darwin -- Python 3.8.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
hypothesis profile 'brownie-verbose' -> verbosity=2, deadline=None, max_examples=50, stateful_step_count=10, report_multiple_bugs=False, database=DirectoryBasedExampleDatabase(PosixPath('/Users/vlad/.brownie/hypothesis'))
rootdir: /Users/vlad/GitHub/alchemy-ethereum-api/blockchain-lab-4/token
plugins: eth-brownie-1.19.2, anyio-3.6.1, forked-1.4.0, web3-5.31.1, xdist-1.34.0, hypothesis-6.27.3
collected 1 item                                                                                                              

Launching 'ganache-cli --accounts 10 --hardfork istanbul --fork https://eth-mainnet.alchemyapi.io/v2/<API> --gasLimit 12000000 --mnemonic brownie --port 8545 --chainId 1'...

tests/test_swap.py::test_custom_token_swap RUNNING
Tokens deploying
Deployed token: Vlad Token by address: 0x9E4c14403d7d9A8A782044E86a93CAE09D7B2ac9
Account balance: 100000000000000000000000
Deployed token: Alice Token by address: 0xcCB53c9429d32594F404d01fbe9E65ED1DCda8D9
Account balance: 100000000000000000000000
Load factory contract...
Fetching source of 0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f from api.etherscan.io...
Created pair 0xE1332C07cF36b11B120c12B9A5cfd5b4CA4dFa61 of tokens: (0x9E4c14403d7d9A8A782044E86a93CAE09D7B2ac9, 0xcCB53c9429d32594F404d01fbe9E65ED1DCda8D9)
Initial reserves: (0, 0, 0)
Add liquidity 1e18 for both tokens
Syncing...
Updated reserves: (1000000000000000000, 1000000000000000000, 1672401258)
Transfer to pair
Token Vlad Token. Account balance: 99998999999999999800000
Token Alice Token. Account balance: 99999000000000000000000
Swap 1e5 Vlad Token to Alice Token
Swapped
Token Vlad Token. Account balance: 99998999999999999800000
Token Alice Token. Account balance: 99999000000000000100000
Syncing...
Updated reserves: (1000000000000200000, 999999999999900000, 1672401259)
tests/test_swap.py::test_custom_token_swap PASSED

===================================================== 1 passed in 16.00s ======================================================
Terminating local RPC client...
```
