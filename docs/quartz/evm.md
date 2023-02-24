
# EVM

---------
## Calls

---------
### call
Issue an EVM call operation. This is similar to a message call transaction in Ethereum.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `H160` | 
| target | `H160` | 
| input | `Vec<u8>` | 
| value | `U256` | 
| gas_limit | `u64` | 
| max_fee_per_gas | `U256` | 
| max_priority_fee_per_gas | `Option<U256>` | 
| nonce | `Option<U256>` | 
| access_list | `Vec<(H160, Vec<H256>)>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'call', {
    'access_list': [
        ('[u8; 20]', ['[u8; 32]']),
    ],
    'gas_limit': 'u64',
    'input': 'Bytes',
    'max_fee_per_gas': '[u64; 4]',
    'max_priority_fee_per_gas': (
        None,
        '[u64; 4]',
    ),
    'nonce': (None, '[u64; 4]'),
    'source': '[u8; 20]',
    'target': '[u8; 20]',
    'value': '[u64; 4]',
}
)
```

---------
### create
Issue an EVM create operation. This is similar to a contract creation transaction in
Ethereum.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `H160` | 
| init | `Vec<u8>` | 
| value | `U256` | 
| gas_limit | `u64` | 
| max_fee_per_gas | `U256` | 
| max_priority_fee_per_gas | `Option<U256>` | 
| nonce | `Option<U256>` | 
| access_list | `Vec<(H160, Vec<H256>)>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'create', {
    'access_list': [
        ('[u8; 20]', ['[u8; 32]']),
    ],
    'gas_limit': 'u64',
    'init': 'Bytes',
    'max_fee_per_gas': '[u64; 4]',
    'max_priority_fee_per_gas': (
        None,
        '[u64; 4]',
    ),
    'nonce': (None, '[u64; 4]'),
    'source': '[u8; 20]',
    'value': '[u64; 4]',
}
)
```

---------
### create2
Issue an EVM create2 operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `H160` | 
| init | `Vec<u8>` | 
| salt | `H256` | 
| value | `U256` | 
| gas_limit | `u64` | 
| max_fee_per_gas | `U256` | 
| max_priority_fee_per_gas | `Option<U256>` | 
| nonce | `Option<U256>` | 
| access_list | `Vec<(H160, Vec<H256>)>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'create2', {
    'access_list': [
        ('[u8; 20]', ['[u8; 32]']),
    ],
    'gas_limit': 'u64',
    'init': 'Bytes',
    'max_fee_per_gas': '[u64; 4]',
    'max_priority_fee_per_gas': (
        None,
        '[u64; 4]',
    ),
    'nonce': (None, '[u64; 4]'),
    'salt': '[u8; 32]',
    'source': '[u8; 20]',
    'value': '[u64; 4]',
}
)
```

---------
### withdraw
Withdraw balance from EVM into currency/balances pallet.
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `H160` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'withdraw', {
    'address': '[u8; 20]',
    'value': 'u128',
}
)
```

---------
## Events

---------
### Created
A contract has been created at given address.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `H160` | ```[u8; 20]```

---------
### CreatedFailed
A contract was attempted to be created, but the execution failed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `H160` | ```[u8; 20]```

---------
### Executed
A contract has been executed successfully with states applied.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `H160` | ```[u8; 20]```

---------
### ExecutedFailed
A contract has been executed with errors. States are reverted with only gas fees applied.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `H160` | ```[u8; 20]```

---------
### Log
Ethereum events from contracts.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| log | `Log` | ```{'address': '[u8; 20]', 'topics': ['[u8; 32]'], 'data': 'Bytes'}```

---------
## Storage functions

---------
### AccountCodes

#### Python
```python
result = substrate.query(
    'EVM', 'AccountCodes', ['[u8; 20]']
)
```

#### Return value
```python
'Bytes'
```
---------
### AccountStorages

#### Python
```python
result = substrate.query(
    'EVM', 'AccountStorages', ['[u8; 20]', '[u8; 32]']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### CurrentLogs
 Written on log, reset after transaction
 Should be empty between transactions

#### Python
```python
result = substrate.query(
    'EVM', 'CurrentLogs', []
)
```

#### Return value
```python
[{'address': '[u8; 20]', 'data': 'Bytes', 'topics': ['[u8; 32]']}]
```
---------
## Errors

---------
### BalanceLow
Not enough balance to perform action

---------
### FeeOverflow
Calculating total fee overflowed

---------
### GasLimitTooHigh
Gas limit is too high.

---------
### GasLimitTooLow
Gas limit is too low.

---------
### GasPriceTooLow
Gas price is too low.

---------
### InvalidNonce
Nonce is invalid

---------
### PaymentOverflow
Calculating total payment overflowed

---------
### Reentrancy
EVM reentrancy

---------
### TransactionMustComeFromEOA
EIP-3607,

---------
### Undefined
Undefined error.

---------
### WithdrawFailed
Withdraw fee failed

---------