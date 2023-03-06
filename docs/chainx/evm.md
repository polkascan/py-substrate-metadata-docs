
# Evm

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
    'Evm', 'call', {
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
    'Evm', 'create', {
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
    'Evm', 'create2', {
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
### hotfix_inc_account_sufficients
Increment `sufficients` for existing accounts having a nonzero `nonce` but zero `sufficients` value.
#### Attributes
| Name | Type |
| -------- | -------- | 
| addresses | `Vec<H160>` | 

#### Python
```python
call = substrate.compose_call(
    'Evm', 'hotfix_inc_account_sufficients', {'addresses': ['[u8; 20]']}
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
    'Evm', 'withdraw', {
    'address': '[u8; 20]',
    'value': 'u128',
}
)
```

---------
## Events

---------
### BalanceDeposit
A deposit has been made at a given address. \[sender, address, value\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `H160` | ```[u8; 20]```
| None | `U256` | ```[u64; 4]```

---------
### BalanceWithdraw
A withdrawal has been made from a given address. \[sender, address, value\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `H160` | ```[u8; 20]```
| None | `U256` | ```[u64; 4]```

---------
### Created
A contract has been created at given \[address\].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H160` | ```[u8; 20]```

---------
### CreatedFailed
A \[contract\] was attempted to be created, but the execution failed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H160` | ```[u8; 20]```

---------
### Executed
A \[contract\] has been executed successfully with states applied.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H160` | ```[u8; 20]```

---------
### ExecutedFailed
A \[contract\] has been executed with errors. States are reverted with only gas fees applied.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H160` | ```[u8; 20]```

---------
### Log
Ethereum events from contracts.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Log` | ```{'address': '[u8; 20]', 'topics': ['[u8; 32]'], 'data': 'Bytes'}```

---------
## Storage functions

---------
### AccountCodes

#### Python
```python
result = substrate.query(
    'Evm', 'AccountCodes', ['[u8; 20]']
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
    'Evm', 'AccountStorages', ['[u8; 20]', '[u8; 32]']
)
```

#### Return value
```python
'[u8; 32]'
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
### GasPriceTooLow
Gas price is too low.

---------
### InvalidNonce
Nonce is invalid

---------
### MaxAddressCountExceeded
Maximum address count exceeded

---------
### PaymentOverflow
Calculating total payment overflowed

---------
### WithdrawFailed
Withdraw fee failed

---------