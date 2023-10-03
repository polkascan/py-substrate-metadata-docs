
# NFT

---------
## Calls

---------
### burn
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(ClassIdOf<T>, TokenIdOf<T>)` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'burn', {'token': ('u32', 'u64')}
)
```

---------
### burn_with_remark
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(ClassIdOf<T>, TokenIdOf<T>)` | 
| remark | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'burn_with_remark', {
    'remark': 'Bytes',
    'token': ('u32', 'u64'),
}
)
```

---------
### create_class
#### Attributes
| Name | Type |
| -------- | -------- | 
| metadata | `CID` | 
| properties | `Properties` | 
| attributes | `Attributes` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'create_class', {
    'attributes': 'scale_info::345',
    'metadata': 'Bytes',
    'properties': 'u8',
}
)
```

---------
### destroy_class
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'destroy_class', {
    'class_id': 'u32',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### mint
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `<T::Lookup as StaticLookup>::Source` | 
| class_id | `ClassIdOf<T>` | 
| metadata | `CID` | 
| attributes | `Attributes` | 
| quantity | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'mint', {
    'attributes': 'scale_info::345',
    'class_id': 'u32',
    'metadata': 'Bytes',
    'quantity': 'u32',
    'to': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `<T::Lookup as StaticLookup>::Source` | 
| token | `(ClassIdOf<T>, TokenIdOf<T>)` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'transfer', {
    'to': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'token': ('u32', 'u64'),
}
)
```

---------
### update_class_properties
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 
| properties | `Properties` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'update_class_properties', {
    'class_id': 'u32',
    'properties': 'u8',
}
)
```

---------
## Events

---------
### BurnedToken
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| class_id | `ClassIdOf<T>` | ```u32```
| token_id | `TokenIdOf<T>` | ```u64```

---------
### BurnedTokenWithRemark
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| class_id | `ClassIdOf<T>` | ```u32```
| token_id | `TokenIdOf<T>` | ```u64```
| remark_hash | `T::Hash` | ```[u8; 32]```

---------
### CreatedClass
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| class_id | `ClassIdOf<T>` | ```u32```

---------
### DestroyedClass
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| class_id | `ClassIdOf<T>` | ```u32```

---------
### MintedToken
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| class_id | `ClassIdOf<T>` | ```u32```
| quantity | `u32` | ```u32```

---------
### TransferredToken
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| class_id | `ClassIdOf<T>` | ```u32```
| token_id | `TokenIdOf<T>` | ```u64```

---------
## Constants

---------
### CreateClassDeposit
#### Value
```python
50000000000000
```
#### Python
```python
constant = substrate.get_constant('NFT', 'CreateClassDeposit')
```
---------
### CreateTokenDeposit
#### Value
```python
200000000000
```
#### Python
```python
constant = substrate.get_constant('NFT', 'CreateTokenDeposit')
```
---------
### DataDepositPerByte
#### Value
```python
600000000
```
#### Python
```python
constant = substrate.get_constant('NFT', 'DataDepositPerByte')
```
---------
### MaxAttributesBytes
#### Value
```python
2048
```
#### Python
```python
constant = substrate.get_constant('NFT', 'MaxAttributesBytes')
```
---------
### PalletId
#### Value
```python
'0x6163612f614e4654'
```
#### Python
```python
constant = substrate.get_constant('NFT', 'PalletId')
```
---------
## Errors

---------
### AttributesTooLarge

---------
### CannotDestroyClass

---------
### ClassIdNotFound

---------
### Immutable

---------
### IncorrectTokenId

---------
### InvalidQuantity

---------
### NoPermission

---------
### NonBurnable

---------
### NonMintable

---------
### NonTransferable

---------
### TokenIdNotFound

---------