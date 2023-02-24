
# GovernanceRegistry

---------
## Calls

---------
### grant_root
Sets the value of an `asset_id` to root. Only callable by root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'GovernanceRegistry', 'grant_root', {'asset_id': 'u128'}
)
```

---------
### remove
Removes mapping of an `asset_id`. Only callable by root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'GovernanceRegistry', 'remove', {'asset_id': 'u128'}
)
```

---------
### set
Sets the value of an `asset_id` to the signed account id. Only callable by root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| value | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'GovernanceRegistry', 'set', {
    'asset_id': 'u128',
    'value': 'AccountId',
}
)
```

---------
## Events

---------
### GrantRoot
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```

---------
### Remove
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```

---------
### Set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| value | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### OriginsByAssetId

#### Python
```python
result = substrate.query(
    'GovernanceRegistry', 'OriginsByAssetId', ['u128']
)
```

#### Return value
```python
{'Root': None, 'Signed': 'AccountId'}
```
---------
## Errors

---------
### NoneError
Not found

---------