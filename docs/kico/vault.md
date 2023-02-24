
# Vault

---------
## Calls

---------
### add_guarder
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| guarder | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Vault', 'add_guarder', {
    'dao_id': 'u64',
    'guarder': 'AccountId',
}
)
```

---------
### open_cex_transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| is_open | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Vault', 'open_cex_transfer', {'dao_id': 'u64', 'is_open': 'bool'}
)
```

---------
### remove_guarder
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| guarder | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Vault', 'remove_guarder', {
    'dao_id': 'u64',
    'guarder': 'AccountId',
}
)
```

---------
### set_fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| fee | `Fee<BalanceOf<T>, Permill>` | 

#### Python
```python
call = substrate.compose_call(
    'Vault', 'set_fee', {
    'dao_id': 'u64',
    'fee': {
        'Amount': 'u128',
        'Permill': 'u32',
    },
}
)
```

---------
### set_guarders
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| guarders | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Vault', 'set_guarders', {
    'dao_id': 'u64',
    'guarders': ['AccountId'],
}
)
```

---------
### unreserve
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| asset_id | `AssetId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vault', 'unreserve', {
    'amount': 'u128',
    'asset_id': 'u32',
    'dao_id': 'u64',
}
)
```

---------
## Events

---------
### AddGuarder
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
### BurnOperate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| call | `<T as dao::Config>::Call` | ```Call```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### IcoOperate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| call | `<T as dao::Config>::Call` | ```Call```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### OpenCexTransfer
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `bool` | ```bool```

---------
### RemoveGuard
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
### SetFee
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `Fee<BalanceOf<T>, Permill>` | ```{'Permill': 'u32', 'Amount': 'u128'}```

---------
### SetGuarders
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```

---------
### SomethingStored
Event documentation should end with an array that provides descriptive names for event
parameters. [something, who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
### Unreserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `AssetId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Fees

#### Python
```python
result = substrate.query(
    'Vault', 'Fees', ['u64']
)
```

#### Return value
```python
{'Amount': 'u128', 'Permill': 'u32'}
```
---------
### Guarders

#### Python
```python
result = substrate.query(
    'Vault', 'Guarders', ['u64']
)
```

#### Return value
```python
['AccountId']
```
---------
### IsOpenCexTransfer

#### Python
```python
result = substrate.query(
    'Vault', 'IsOpenCexTransfer', ['u64']
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### BadOrigin

---------
### GuarderIsExists

---------
### HaveNoGurarder

---------
### NotSupprtCall

---------