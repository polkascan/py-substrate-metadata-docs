
# PriceDao

---------
## Calls

---------
### del_feed_account
Council slash accounts
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'PriceDao', 'del_feed_account', {'accounts': ['AccountId']}
)
```

---------
### exit_feed
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PriceDao', 'exit_feed', {}
)
```

---------
### insert_feed_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'PriceDao', 'insert_feed_account', {'accounts': ['AccountId']}
)
```

---------
### unlock_price
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'PriceDao', 'unlock_price', {'currency_id': 'u32'}
)
```

---------
### withdraw
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PriceDao', 'withdraw', {}
)
```

---------
## Events

---------
### DepositAccounts
Some accounts deposit successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<T::AccountId>` | ```['AccountId']```
| None | `BalanceOf<T>` | ```u128```

---------
### GetOraclePrice
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `Price` | ```u128```

---------
### GetPrice

#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `Price` | ```u128```

---------
### GetSwapPrice
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `Price` | ```u128```

---------
### LockPrice
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `Price` | ```u128```

---------
### SlashAccounts
slash some accounts and transfer balance to treasury
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<T::AccountId>` | ```['AccountId']```

---------
### UnlockPrice
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```

---------
### WhoLock
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### DepositBalance

#### Python
```python
result = substrate.query(
    'PriceDao', 'DepositBalance', ['AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'expiration': 'u32'}
```
---------
### LockedPrice

#### Python
```python
result = substrate.query(
    'PriceDao', 'LockedPrice', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### Members

#### Python
```python
result = substrate.query(
    'PriceDao', 'Members', []
)
```

#### Return value
```python
['AccountId']
```
---------
## Constants

---------
### DicoTreasuryModuleId
#### Value
```python
'0x6469636f2f747273'
```
#### Python
```python
constant = substrate.get_constant('PriceDao', 'DicoTreasuryModuleId')
```
---------
### PledgedBalance
#### Value
```python
500000000000000000
```
#### Python
```python
constant = substrate.get_constant('PriceDao', 'PledgedBalance')
```
---------
### WithdrawExpirationPeriod
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('PriceDao', 'WithdrawExpirationPeriod')
```
---------
## Errors

---------
### ExpirationEmpty
Expiration time is empty

---------
### ExpirationNotEmpty

---------
### NoneValue
Error names should be descriptive.

---------
### NotExpired
Not expired

---------
### Overflow


---------
### StorageOverflow
Errors should have helpful documentation associated with them.

---------