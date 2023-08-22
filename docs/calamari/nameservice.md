
# NameService

---------
## Calls

---------
### accept_register
After Pending Register has passed its block wait time, finish regiser
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `UserName` | 
| registrant | `ZkAddressType` | 

#### Python
```python
call = substrate.compose_call(
    'NameService', 'accept_register', {
    'registrant': '[u8; 32]',
    'username': 'Bytes',
}
)
```

---------
### cancel_pending_register
Cancel pending name for register
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `UserName` | 
| registrant | `ZkAddressType` | 

#### Python
```python
call = substrate.compose_call(
    'NameService', 'cancel_pending_register', {
    'registrant': '[u8; 32]',
    'username': 'Bytes',
}
)
```

---------
### register
Queue Username for Register if it has not been registered or queued yet
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `UserName` | 
| registrant | `ZkAddressType` | 

#### Python
```python
call = substrate.compose_call(
    'NameService', 'register', {
    'registrant': '[u8; 32]',
    'username': 'Bytes',
}
)
```

---------
### remove_register
Remove Already Registered Name
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `UserName` | 
| registrant | `ZkAddressType` | 

#### Python
```python
call = substrate.compose_call(
    'NameService', 'remove_register', {
    'registrant': '[u8; 32]',
    'username': 'Bytes',
}
)
```

---------
### set_primary_name
Set a registered and owned username as Primary
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `UserName` | 
| registrant | `ZkAddressType` | 

#### Python
```python
call = substrate.compose_call(
    'NameService', 'set_primary_name', {
    'registrant': '[u8; 32]',
    'username': 'Bytes',
}
)
```

---------
## Events

---------
### NameQueuedForRegister
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash_username | `T::Hash` | ```[u8; 32]```
| hash_owner | `T::Hash` | ```[u8; 32]```

---------
### NameRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| username | `UserName` | ```Bytes```
| owner | `ZkAddressType` | ```[u8; 32]```

---------
### NameSetAsPrimary
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `ZkAddressType` | ```[u8; 32]```
| username | `UserName` | ```Bytes```

---------
### RegisterCanceled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash_username | `T::Hash` | ```[u8; 32]```
| hash_owner | `T::Hash` | ```[u8; 32]```

---------
### RegisterRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| username | `UserName` | ```Bytes```
| owner | `ZkAddressType` | ```[u8; 32]```

---------
## Storage functions

---------
### PendingRegister
 Names pending to be registered with the given blocknumber(wait time) [username,(registrant,blocknumber)]

#### Python
```python
result = substrate.query(
    'NameService', 'PendingRegister', ['[u8; 32]']
)
```

#### Return value
```python
('[u8; 32]', 'u32')
```
---------
### PrimaryRecords
 Primary Records, 1 AccountID may have only one primary name

#### Python
```python
result = substrate.query(
    'NameService', 'PrimaryRecords', ['[u8; 32]']
)
```

#### Return value
```python
'Bytes'
```
---------
### UsernameRecords
 All registered Names

#### Python
```python
result = substrate.query(
    'NameService', 'UsernameRecords', ['Bytes']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
## Constants

---------
### RegisterPrice
#### Value
```python
3300000000000000
```
#### Python
```python
constant = substrate.get_constant('NameService', 'RegisterPrice')
```
---------
### RegisterWaitingPeriod
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('NameService', 'RegisterWaitingPeriod')
```
---------
## Errors

---------
### AlreadyPendingRegister
Already pending Register

---------
### InsufficientBalance
Not enough balance for Register payment

---------
### InvalidUsernameFormat
Username invalid

---------
### NameAlreadyRegistered
Username exists

---------
### NotOwned
Username not owned

---------
### NotRegistered
Username not registered

---------
### RegisterTimeNotReached
The Registration time not reached

---------
### UsernameNotFound
Not Found (used in cases of canceling)

---------
### UsernameNotPrimary
Username registered but is not primary (transfers)

---------