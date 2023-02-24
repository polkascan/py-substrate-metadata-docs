
# DaoCoreModule

---------
## Calls

---------
### create
An example dispatchable that takes a singles value as a parameter, writes the value to
storage and emits an event. This function must be dispatched by a signed extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| description | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCoreModule', 'create', {'description': 'Bytes'}
)
```

---------
### deregister_app
#### Attributes
| Name | Type |
| -------- | -------- | 
| app_id | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCoreModule', 'deregister_app', {'app_id': 'u8'}
)
```

---------
### invoke
#### Attributes
| Name | Type |
| -------- | -------- | 
| ord_id | `u32` | 
| pallet | `Box<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCoreModule', 'invoke', {'ord_id': 'u32', 'pallet': 'Call'}
)
```

---------
### join
#### Attributes
| Name | Type |
| -------- | -------- | 
| org_id | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCoreModule', 'join', {'org_id': 'u32'}
)
```

---------
### register_app
#### Attributes
| Name | Type |
| -------- | -------- | 
| title | `Vec<u8>` | 
| owner | `T::AccountId` | 
| description | `Vec<u8>` | 
| charge_type | `u32` | 
| price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCoreModule', 'register_app', {
    'charge_type': 'u32',
    'description': 'Bytes',
    'owner': 'AccountId',
    'price': 'u128',
    'title': 'Bytes',
}
)
```

---------
## Events

---------
### AppDeRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `T::AccountId` | ```AccountId```

---------
### AppRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `T::AccountId` | ```AccountId```

---------
### OrgJoined
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
### OrgRegistered
Event documentation should end with an array that provides descriptive names for event
parameters. [ord_id, owner]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### NextAppId

#### Python
```python
result = substrate.query(
    'DaoCoreModule', 'NextAppId', []
)
```

#### Return value
```python
'u8'
```
---------
### NextOrgId

#### Python
```python
result = substrate.query(
    'DaoCoreModule', 'NextOrgId', []
)
```

#### Return value
```python
'u32'
```
---------
### Orgnizations

#### Python
```python
result = substrate.query(
    'DaoCoreModule', 'Orgnizations', ['u32']
)
```

#### Return value
```python
{
    'description': 'Bytes',
    'members': ['AccountId'],
    'org_type': 'u32',
    'owner': 'AccountId',
}
```
---------
### RegisteredApps

#### Python
```python
result = substrate.query(
    'DaoCoreModule', 'RegisteredApps', ['u8']
)
```

#### Return value
```python
{
    'charge_type': 'u32',
    'description': 'Bytes',
    'owner': 'AccountId',
    'price': 'u128',
    'title': 'Bytes',
}
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x70792f64636f7265'
```
#### Python
```python
constant = substrate.get_constant('DaoCoreModule', 'PalletId')
```
---------
## Errors

---------
### AppNotEnable

---------
### AppNotExist

---------
### AppNotFound

---------
### BadOrigin

---------
### NoRepeatJoin

---------
### NoneValue
Error names should be descriptive.

---------
### NotValidOrgMember

---------
### OrgnizationNotExist
Errors should have helpful documentation associated with them.

---------