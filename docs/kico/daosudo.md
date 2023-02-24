
# DaoSudo

---------
## Calls

---------
### close_sudo
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| is_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'DaoSudo', 'close_sudo', {'dao_id': 'u64', 'is_close': 'bool'}
)
```

---------
### set_sudo_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| sudo_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DaoSudo', 'set_sudo_account', {
    'dao_id': 'u64',
    'sudo_account': 'AccountId',
}
)
```

---------
### sudo
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| call | `Box<<T as dao::Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoSudo', 'sudo', {'call': 'Call', 'dao_id': 'u64'}
)
```

---------
## Events

---------
### CloseSudo
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| is_close | `bool` | ```bool```

---------
### SetSudoAccount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| sudo_account | `T::AccountId` | ```AccountId```

---------
### SudoDone
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo | `T::AccountId` | ```AccountId```
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
## Storage functions

---------
### IsMustDemocracy

#### Python
```python
result = substrate.query(
    'DaoSudo', 'IsMustDemocracy', ['u64']
)
```

#### Return value
```python
'bool'
```
---------
### SudoAccount

#### Python
```python
result = substrate.query(
    'DaoSudo', 'SudoAccount', ['u64']
)
```

#### Return value
```python
'AccountId'
```
---------
## Errors

---------
### NotSudo

---------