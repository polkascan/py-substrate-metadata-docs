
# EqSessionManager

---------
## Calls

---------
### add_validator
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_id | `<T as pallet::Config>::ValidatorId` | 

#### Python
```python
call = substrate.compose_call(
    'EqSessionManager', 'add_validator', {'validator_id': 'AccountId'}
)
```

---------
### remove_validator
Removes validator. Root authorization required to remove validator.
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_id | `<T as pallet::Config>::ValidatorId` | 

#### Python
```python
call = substrate.compose_call(
    'EqSessionManager', 'remove_validator', {'validator_id': 'AccountId'}
)
```

---------
## Events

---------
### ValidatorAdded
Validator successfully added
\[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as pallet::Config>::ValidatorId` | ```AccountId```

---------
### ValidatorRemoved
Validator successfully removed
\[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as pallet::Config>::ValidatorId` | ```AccountId```

---------
## Storage functions

---------
### IsChanged
 Pallet storage - flag showing that active validators list changed
 during a session

#### Python
```python
result = substrate.query(
    'EqSessionManager', 'IsChanged', []
)
```

#### Return value
```python
'bool'
```
---------
### Validators
 Pallet storage - list of all active validators

#### Python
```python
result = substrate.query(
    'EqSessionManager', 'Validators', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### AlreadyAdded
Validator was not added because he is already active

---------
### AlreadyRemoved
Validator was not removed: there is no active validator with this id

---------
### NotRegistered
Validator was not added because validator is not registered

---------