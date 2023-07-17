
# XBtcLedger

---------
## Calls

---------
### force_transfer
Exactly as `transfer`, except the origin must be root and
the source account may be specified.
The dispatch origin for this call is `root`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'XBtcLedger', 'force_transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'source': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
### set_balance
Set the balances of a given account.

This will alter `FreeBalance` in storage. it will
also alter the total issuance of the system (`TotalInComing`) appropriately.
The dispatch origin for this call is `root`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| new_free | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'XBtcLedger', 'set_balance', {
    'new_free': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### transfer
Transfer some liquid free balance to another account.

`transfer` will set the `FreeBalance` of the sender and receiver.
The dispatch origin for this call must be `Signed` by the transactor.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'XBtcLedger', 'transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
## Events

---------
### BalanceSet
A balance was set by root.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```

---------
### Deposit
Some amount was deposited (e.g. for transaction fees).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Endowed
An account was created with some free balance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| free_balance | `T::Balance` | ```u128```

---------
### Transfer
Transfer succeeded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Withdraw
Some amount was withdrawn from the account (e.g. for transaction fees).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### AccountStore
 The Balances pallet example of storing the balance of an account.

#### Python
```python
result = substrate.query(
    'XBtcLedger', 'AccountStore', ['AccountId']
)
```

#### Return value
```python
{'free': 'u128'}
```
---------
### StorageVersion
 Storage version of the pallet.


#### Python
```python
result = substrate.query(
    'XBtcLedger', 'StorageVersion', []
)
```

#### Return value
```python
('V1_0_0', )
```
---------
### TotalInComing
 The total units issued in the system.

#### Python
```python
result = substrate.query(
    'XBtcLedger', 'TotalInComing', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### PalletId
 The btc-ledger&#x27;s pallet id, used for deriving its sovereign account ID.
#### Value
```python
'0x7063782f74727379'
```
#### Python
```python
constant = substrate.get_constant('XBtcLedger', 'PalletId')
```
---------
## Errors

---------
### DeadAccount
Beneficiary account must pre-exist

---------
### InsufficientBalance
Balance too low to send value

---------