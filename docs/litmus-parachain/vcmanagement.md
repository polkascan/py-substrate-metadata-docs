
# VCManagement

---------
## Calls

---------
### activate_schema
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| index | `SchemaIndex` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'activate_schema', {
    'index': 'u64',
    'shard': 'scale_info::11',
}
)
```

---------
### add_schema
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| id | `Vec<u8>` | 
| content | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'add_schema', {
    'content': 'Bytes',
    'id': 'Bytes',
    'shard': 'scale_info::11',
}
)
```

---------
### disable_schema
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| index | `SchemaIndex` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'disable_schema', {
    'index': 'u64',
    'shard': 'scale_info::11',
}
)
```

---------
### disable_vc
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `VCIndex` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'disable_vc', {'index': 'scale_info::11'}
)
```

---------
### request_vc
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| assertion | `Assertion` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'request_vc', {
    'assertion': {
        'A1': None,
        'A10': 'u128',
        'A11': 'u128',
        'A13': 'u32',
        'A2': 'Bytes',
        'A3': (
            'Bytes',
            'Bytes',
            'Bytes',
        ),
        'A4': 'u128',
        'A5': ('Bytes', 'Bytes'),
        'A6': None,
        'A7': 'u128',
        'A8': None,
        'A9': None,
    },
    'shard': 'scale_info::11',
}
)
```

---------
### revoke_schema
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| index | `SchemaIndex` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'revoke_schema', {
    'index': 'u64',
    'shard': 'scale_info::11',
}
)
```

---------
### revoke_vc
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `VCIndex` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'revoke_vc', {'index': 'scale_info::11'}
)
```

---------
### set_schema_admin
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'set_schema_admin', {'new': 'AccountId'}
)
```

---------
### some_error
#### Attributes
| Name | Type |
| -------- | -------- | 
| error | `VCMPError` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'some_error', {
    'error': {
        'Assertion10Failed': None,
        'Assertion11Failed': None,
        'Assertion1Failed': None,
        'Assertion2Failed': None,
        'Assertion3Failed': None,
        'Assertion4Failed': None,
        'Assertion5Failed': None,
        'Assertion6Failed': None,
        'Assertion7Failed': None,
        'Assertion8Failed': None,
        'HttpRequestFailed': 'Bytes',
        'ParseError': None,
        'RequestVCHandlingFailed': None,
    },
}
)
```

---------
### vc_issued
---------------------------------------------------
The following extrinsics are supposed to be called by TEE only
---------------------------------------------------
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 
| index | `H256` | 
| hash | `H256` | 
| vc | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'vc_issued', {
    'account': 'AccountId',
    'hash': 'scale_info::11',
    'index': 'scale_info::11',
    'vc': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
}
)
```

---------
## Events

---------
### Assertion10Failed
#### Attributes
No attributes

---------
### Assertion11Failed
#### Attributes
No attributes

---------
### Assertion1Failed
#### Attributes
No attributes

---------
### Assertion2Failed
#### Attributes
No attributes

---------
### Assertion3Failed
#### Attributes
No attributes

---------
### Assertion4Failed
#### Attributes
No attributes

---------
### Assertion5Failed
#### Attributes
No attributes

---------
### Assertion6Failed
#### Attributes
No attributes

---------
### Assertion7Failed
#### Attributes
No attributes

---------
### Assertion8Failed
#### Attributes
No attributes

---------
### HttpRequestFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reason | `ErrorString` | ```Bytes```

---------
### ParseError
#### Attributes
No attributes

---------
### RequestVCHandlingFailed
#### Attributes
No attributes

---------
### SchemaActivated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| shard | `ShardIdentifier` | ```scale_info::11```
| index | `SchemaIndex` | ```u64```

---------
### SchemaAdminChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_admin | `Option<T::AccountId>` | ```(None, 'AccountId')```
| new_admin | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### SchemaDisabled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| shard | `ShardIdentifier` | ```scale_info::11```
| index | `SchemaIndex` | ```u64```

---------
### SchemaIssued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| shard | `ShardIdentifier` | ```scale_info::11```
| index | `SchemaIndex` | ```u64```

---------
### SchemaRevoked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| shard | `ShardIdentifier` | ```scale_info::11```
| index | `SchemaIndex` | ```u64```

---------
### VCDisabled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `VCIndex` | ```scale_info::11```

---------
### VCIssued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| index | `VCIndex` | ```scale_info::11```
| vc | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### VCNotExist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `VCIndex` | ```scale_info::11```

---------
### VCRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::11```
| assertion | `Assertion` | ```{'A1': None, 'A2': 'Bytes', 'A3': ('Bytes', 'Bytes', 'Bytes'), 'A4': 'u128', 'A5': ('Bytes', 'Bytes'), 'A6': None, 'A7': 'u128', 'A8': None, 'A9': None, 'A10': 'u128', 'A11': 'u128', 'A13': 'u32'}```

---------
### VCRevoked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `VCIndex` | ```scale_info::11```

---------
## Storage functions

---------
### SchemaAdmin

#### Python
```python
result = substrate.query(
    'VCManagement', 'SchemaAdmin', []
)
```

#### Return value
```python
'AccountId'
```
---------
### SchemaRegistry

#### Python
```python
result = substrate.query(
    'VCManagement', 'SchemaRegistry', ['u64']
)
```

#### Return value
```python
{
    'author': 'AccountId',
    'content': 'Bytes',
    'id': 'Bytes',
    'status': ('Active', 'Disabled'),
}
```
---------
### SchemaRegistryIndex

#### Python
```python
result = substrate.query(
    'VCManagement', 'SchemaRegistryIndex', []
)
```

#### Return value
```python
'u64'
```
---------
### VCRegistry

#### Python
```python
result = substrate.query(
    'VCManagement', 'VCRegistry', ['scale_info::11']
)
```

#### Return value
```python
{'hash': 'scale_info::11', 'status': ('Active', 'Disabled'), 'subject': 'AccountId'}
```
---------
## Errors

---------
### LengthMismatch

---------
### RequireSchemaAdmin
Error when the caller account is not the admin

---------
### SchemaAlreadyActivated
Schema is active

---------
### SchemaAlreadyDisabled
Schema is already disabled

---------
### SchemaIndexOverFlow

---------
### SchemaNotExists
Schema not exists

---------
### VCAlreadyDisabled
The VC is already disabled

---------
### VCAlreadyExists
the VC already exists

---------
### VCNotExist
the ID doesn&\#x27;t exist

---------
### VCSubjectMismatch
The requester doesn&\#x27;t have the permission (because of subject mismatch)

---------