
# VCManagement

---------
## Calls

---------
### disable_vc
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `VCID` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'disable_vc', {'id': 'u64'}
)
```

---------
### request_vc
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| ruleset | `Ruleset` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'request_vc', {
    'ruleset': {
        'R1': None,
        'R10': ('u128', 'u32'),
        'R11': ('u128', 'u32'),
        'R12': ('u128', 'u32'),
        'R13': 'u32',
        'R2': ('Bytes', 'Bytes'),
        'R3': ('Bytes', 'Bytes'),
        'R4': None,
        'R5': ('Bytes', 'Bytes'),
        'R6': None,
        'R7': ('u128', 'u32'),
        'R8': 'u64',
        'R9': None,
    },
    'shard': '[u8; 32]',
}
)
```

---------
### revoke_vc
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `VCID` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'revoke_vc', {'id': 'u64'}
)
```

---------
### some_error
#### Attributes
| Name | Type |
| -------- | -------- | 
| func | `Vec<u8>` | 
| error | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'some_error', {'error': 'Bytes', 'func': 'Bytes'}
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
| id | `u64` | 
| hash | `H256` | 
| vc | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'VCManagement', 'vc_issued', {
    'account': 'AccountId',
    'hash': '[u8; 32]',
    'id': 'u64',
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
### SomeError
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| func | `Vec<u8>` | ```Bytes```
| error | `Vec<u8>` | ```Bytes```

---------
### VCDisabled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `VCID` | ```u64```

---------
### VCIssued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| id | `VCID` | ```u64```
| vc | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### VCRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```
| ruleset | `Ruleset` | ```{'R1': None, 'R2': ('Bytes', 'Bytes'), 'R3': ('Bytes', 'Bytes'), 'R4': None, 'R5': ('Bytes', 'Bytes'), 'R6': None, 'R7': ('u128', 'u32'), 'R8': 'u64', 'R9': None, 'R10': ('u128', 'u32'), 'R11': ('u128', 'u32'), 'R12': ('u128', 'u32'), 'R13': 'u32'}```

---------
### VCRevoked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `VCID` | ```u64```

---------
## Storage functions

---------
### VCRegistry

#### Python
```python
result = substrate.query(
    'VCManagement', 'VCRegistry', ['u64']
)
```

#### Return value
```python
{'hash': '[u8; 32]', 'status': ('Active', 'Disabled'), 'subject': 'AccountId'}
```
---------
## Errors

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