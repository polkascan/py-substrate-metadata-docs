
# Treasury

---------
## Calls

---------
### buyout
Let user to exchange existed asset to native asset by oracle price plus fee
Parameters:
`asset` - asset to exchange
`amount` - amount of native asset user will get after buyout
           or amount of exchange asset user will give for buyout
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| amount | `Amount<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'buyout', {
    'amount': {
        'Buyout': 'u128',
        'Exchange': 'u128',
    },
    'asset': 'u64',
}
)
```

---------
### update_buyout_limit
Set/unset buyout limit
Parameters:
`limit` - max value of native token user could get with help of buyout for a period(day), None - to disable buyout limits
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `Option<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'update_buyout_limit', {'limit': (None, 'u128')}
)
```

---------
## Events

---------
### Buyout
Buyout event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| buyout_amount | `T::Balance` | ```u128```
| asset | `Asset` | ```u64```
| exchange_amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### BuyoutLimit
 Stores limit amount user could by for a period.
 When `None` - buyouts not limited

#### Python
```python
result = substrate.query(
    'Treasury', 'BuyoutLimit', []
)
```

#### Return value
```python
'u128'
```
---------
### Buyouts
 Stores amount of buyouts (amount, timestamp of last buyout)

#### Python
```python
result = substrate.query(
    'Treasury', 'Buyouts', ['AccountId']
)
```

#### Return value
```python
('u128', 'u64')
```
---------
## Constants

---------
### BuyFee
 Fee from collateral buyouts (any currency that is not basic asset)
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'BuyFee')
```
---------
### MinAmountToBuyout
 Min amount of native token to buyout
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'MinAmountToBuyout')
```
---------
### SellFee
 Fee from the basic asset buyouts
#### Value
```python
150000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'SellFee')
```
---------
## Errors

---------
### BuyoutLimitExceeded
Daily buyout limit exceeded

---------
### InsufficientAccountBalance
The account balance is too low for an operation

---------
### InsufficientTreasuryBalance
The treasury balance is too low for an operation

---------
### NoPrice
One of transacted currencies is missing price information
or the price is outdated

---------
### WrongAssetToBuyout
Attempt to exchange native token to native token

---------