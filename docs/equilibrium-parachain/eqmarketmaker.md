
# EqMarketMaker

---------
## Calls

---------
### add_to_whitelist
Add account to whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqMarketMaker', 'add_to_whitelist', {'account_id': 'AccountId'}
)
```

---------
### create_order
Create order. This must be called by whitelisted account
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency | `Asset` | 
| order_type | `OrderType` | 
| side | `OrderSide` | 
| amount | `EqFixedU128` | 

#### Python
```python
call = substrate.compose_call(
    'EqMarketMaker', 'create_order', {
    'amount': 'u128',
    'currency': 'u64',
    'order_type': {
        'Limit': {
            'expiration_time': 'u64',
            'price': 'i64',
        },
        'Market': None,
    },
    'side': ('Buy', 'Sell'),
}
)
```

---------
### delete_order
Delete order. This must be called by whitelisted account
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency | `Asset` | 
| order_id | `OrderId` | 
| price | `FixedI64` | 

#### Python
```python
call = substrate.compose_call(
    'EqMarketMaker', 'delete_order', {
    'currency': 'u64',
    'order_id': 'u64',
    'price': 'i64',
}
)
```

---------
### remove_from_whitelist
Remove account from whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqMarketMaker', 'remove_from_whitelist', {'account_id': 'AccountId'}
)
```

---------
## Events

---------
### AddedToWhitelist
`AccountId` was added to the whitelist. \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### RemovedFromWhitelist
`AccountId` was removed from the whitelist. \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### WhiteList

#### Python
```python
result = substrate.query(
    'EqMarketMaker', 'WhiteList', ['AccountId']
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### NotWhitelistedAccount
Attempt to execute from not whitelisted account

---------