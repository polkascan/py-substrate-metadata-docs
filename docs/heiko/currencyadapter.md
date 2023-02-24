
# CurrencyAdapter

---------
## Calls

---------
### force_remove_lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CurrencyAdapter', 'force_remove_lock', {'asset': 'u32', 'who': 'AccountId'}
)
```

---------
### force_set_lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| who | `T::AccountId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CurrencyAdapter', 'force_set_lock', {
    'amount': 'u128',
    'asset': 'u32',
    'who': 'AccountId',
}
)
```

---------
## Constants

---------
### GetNativeCurrencyId
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('CurrencyAdapter', 'GetNativeCurrencyId')
```
---------
## Errors

---------
### NotANativeToken
Not a native token

---------