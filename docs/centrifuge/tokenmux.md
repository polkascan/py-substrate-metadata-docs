
# TokenMux

---------
## Calls

---------
### burn
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_out | `T::CurrencyId` | 
| amount_out | `T::BalanceOut` | 

#### Python
```python
call = substrate.compose_call(
    'TokenMux', 'burn', {
    'amount_out': 'u128',
    'currency_out': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
}
)
```

---------
### deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_out | `T::CurrencyId` | 
| amount_out | `T::BalanceOut` | 

#### Python
```python
call = substrate.compose_call(
    'TokenMux', 'deposit', {
    'amount_out': 'u128',
    'currency_out': {
        'Native': None,
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
}
)
```

---------
### match_swap
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `T::OrderId` | 
| amount | `T::BalanceOut` | 

#### Python
```python
call = substrate.compose_call(
    'TokenMux', 'match_swap', {'amount': 'u128', 'order_id': 'u64'}
)
```

---------
## Events

---------
### Burned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| currency_out | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}```
| currency_in | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}```
| amount | `T::BalanceOut` | ```u128```

---------
### Deposited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| currency_out | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}```
| currency_in | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}```
| amount | `T::BalanceOut` | ```u128```

---------
### SwapMatched
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `T::OrderId` | ```u64```
| amount | `T::BalanceOut` | ```u128```

---------
## Storage functions

---------
## Constants

---------
### PalletId
#### Value
```python
'0x6366672f746d7578'
```
#### Python
```python
constant = substrate.get_constant('TokenMux', 'PalletId')
```
---------
## Errors

---------
### DecimalMismatch
Variant and local representation have mismatching decimals in their
metadata. A conversion between the two is not possible

---------
### InvalidSwapCurrencies
This means the swap is either not a local to variant or not a
variant to local swap

---------
### MetadataNotFound
The given currency has no metadata set.

---------
### NoLocalRepresentation
The given currency has no local representation and can hence not be
deposited to receive a local representation.

---------
### NotIdenticalSwap
Matching orders does only work if there is a one-to-one conversion

---------
### SwapNotFound
Swap could not be found by id

---------