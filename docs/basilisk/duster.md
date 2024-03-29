
# Duster

---------
## Calls

---------
### add_nondustable_account
See [`Pallet::add_nondustable_account`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Duster', 'add_nondustable_account', {'account': 'AccountId'}
)
```

---------
### dust_account
See [`Pallet::dust_account`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'Duster', 'dust_account', {
    'account': 'AccountId',
    'currency_id': 'u32',
}
)
```

---------
### remove_nondustable_account
See [`Pallet::remove_nondustable_account`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Duster', 'remove_nondustable_account', {'account': 'AccountId'}
)
```

---------
## Events

---------
### Added
Account added to non-dustable list.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### Dusted
Account dusted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Removed
Account removed from non-dustable list.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### AccountBlacklist
 Accounts excluded from dusting.

#### Python
```python
result = substrate.query(
    'Duster', 'AccountBlacklist', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### DustAccount
 Account to send dust to.

#### Python
```python
result = substrate.query(
    'Duster', 'DustAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### RewardAccount
 Account to take reward from.

#### Python
```python
result = substrate.query(
    'Duster', 'RewardAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### NativeCurrencyId
 Native Asset Id
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Duster', 'NativeCurrencyId')
```
---------
### Reward
 Reward amount
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Duster', 'Reward')
```
---------
## Errors

---------
### AccountBlacklisted
Account is excluded from dusting.

---------
### AccountNotBlacklisted
Account is not present in the non-dustable list.

---------
### BalanceSufficient
The balance is sufficient to keep account open.

---------
### DustAccountNotSet
Dust account is not set.

---------
### ReserveAccountNotSet
Reserve account is not set.

---------
### ZeroBalance
The balance is zero.

---------