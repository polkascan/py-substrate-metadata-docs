
# Whitelists

---------
## Calls

---------
### add_to_whitelist
Adds a `who_to_add` account to whitelist. Requires root authorization
#### Attributes
| Name | Type |
| -------- | -------- | 
| who_to_add | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Whitelists', 'add_to_whitelist', {'who_to_add': 'AccountId'}
)
```

---------
### remove_from_whitelist
Removes an account `who_to_remove` from whitelist. Requires sudo authorization
#### Attributes
| Name | Type |
| -------- | -------- | 
| who_to_remove | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Whitelists', 'remove_from_whitelist', {'who_to_remove': 'AccountId'}
)
```

---------
## Events

---------
### AddedToWhitelist
`AccountId` was added to the whitelist. \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### RemovedFromWhitelist
`AccountId` was removed from the whitelist. \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### WhiteList
 Storage of all whitelisted `AccountId`s

#### Python
```python
result = substrate.query(
    'Whitelists', 'WhiteList', []
)
```

#### Return value
```python
['AccountId']
```
---------
## Errors

---------
### AlreadyAdded
Account was not added to whitelist: already in whitelist

---------
### AlreadyRemoved
Account was not removed from whitelist: not in whitelist

---------