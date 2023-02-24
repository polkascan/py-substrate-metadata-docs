
# CreateDao

---------
## Calls

---------
### create_dao
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| concrete_id | `T::ConcreteId` | 

#### Python
```python
call = substrate.compose_call(
    'CreateDao', 'create_dao', {
    'concrete_id': {
        'FungibleTokenId': 'u32',
        'NftClassId': 'u32',
    },
    'dao_id': 'u64',
}
)
```

---------
### dao_remark
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| remark | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'CreateDao', 'dao_remark', {'dao_id': 'u64', 'remark': 'Bytes'}
)
```

---------
## Events

---------
### CreatedDao
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::DaoId` | ```u64```
| None | `T::ConcreteId` | ```{'NftClassId': 'u32', 'FungibleTokenId': 'u32'}```

---------
### SomethingStored
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Daos

#### Python
```python
result = substrate.query(
    'CreateDao', 'Daos', ['u64']
)
```

#### Return value
```python
{'creator': 'AccountId', 'id': {'FungibleTokenId': 'u32', 'NftClassId': 'u32'}, 'start_block': 'u32'}
```
---------
## Errors

---------
### BadOrigin

---------
### DaoExists

---------
### DaoNotExists

---------
### HaveNoCallId

---------
### HaveNoCreatePermission

---------
### InVailCall

---------
### InVailCallId

---------
### InVailDaoId

---------
### NotDaoId

---------
### NotDaoSupportCall

---------