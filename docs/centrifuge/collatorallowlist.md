
# CollatorAllowlist

---------
## Calls

---------
### add
Add the given `collator_id` to the allowlist.
Fails if
  - `origin` fails the `ensure_root` check
  - `collator_id` did not yet load their keys into the session
    pallet
  - `collator_id` is already part of the allowlist
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator_id | `T::ValidatorId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorAllowlist', 'add', {'collator_id': 'AccountId'}
)
```

---------
### remove
Remove a `collator_id` from the allowlist.
Fails if
  - `origin` fails the `ensure_root` check
  - `collator_id` is not part of the allowlist
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator_id | `T::ValidatorId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorAllowlist', 'remove', {'collator_id': 'AccountId'}
)
```

---------
## Events

---------
### CollatorAdded
A collator has been added to the allowlist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collator_id | `T::ValidatorId` | ```AccountId```

---------
### CollatorRemoved
A collator has been removed from the allowlist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collator_id | `T::ValidatorId` | ```AccountId```

---------
## Storage functions

---------
### Allowlist
 The collator&#x27;s allowlist.
 Note: We implement it as a close-enough HashSet: Map&lt;ValidatorId, ()&gt;.

#### Python
```python
result = substrate.query(
    'CollatorAllowlist', 'Allowlist', ['AccountId']
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### CollatorAlreadyAllowed
The collator has already been added to the allowlist.

---------
### CollatorNotPresent
The provided collator was not found in the storage.

---------
### CollatorNotReady
The collator is not ready yet following to the underlying
`T::ValidatorRegistration`

---------