
# Xstorage

---------
## Calls

---------
### place_storage_order
#### Attributes
| Name | Type |
| -------- | -------- | 
| cid | `Vec<u8>` | 
| size | `u64` | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'Xstorage', 'place_storage_order', {
    'cid': 'Bytes',
    'currency_id': {
        'OtherReserve': 'u128',
        'SelfReserve': None,
    },
    'size': 'u64',
}
)
```

---------
### place_storage_order_through_parachain
#### Attributes
| Name | Type |
| -------- | -------- | 
| cid | `Vec<u8>` | 
| size | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Xstorage', 'place_storage_order_through_parachain', {'cid': 'Bytes', 'size': 'u64'}
)
```

---------
### register_storage_fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| amount | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Xstorage', 'register_storage_fee', {
    'amount': 'u128',
    'currency_id': {
        'OtherReserve': 'u128',
        'SelfReserve': None,
    },
}
)
```

---------
## Events

---------
### FileSuccess
New asset with the asset manager is registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| cid | `Vec<u8>` | ```Bytes```
| size | `u64` | ```u64```

---------
### StorageFeeRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'SelfReserve': None, 'OtherReserve': 'u128'}```
| amount | `u128` | ```u128```

---------
## Storage functions

---------
### StorageFeePerCurrency

#### Python
```python
result = substrate.query(
    'Xstorage', 'StorageFeePerCurrency', [
    {
        'OtherReserve': 'u128',
        'SelfReserve': None,
    },
]
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### NotCrossChainTransferableCurrency

---------
### NotSupportedCurrency

---------
### UnableToTransferStorageFee

---------