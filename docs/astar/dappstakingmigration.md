
# DappStakingMigration

---------
## Calls

---------
### migrate
See [`Pallet::migrate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| weight_limit | `Option<Weight>` | 

#### Python
```python
call = substrate.compose_call(
    'DappStakingMigration', 'migrate', {
    'weight_limit': (
        None,
        {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
    ),
}
)
```

---------
## Events

---------
### SingularStakingInfoTranslated
Number of staking info entries translated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
## Storage functions

---------
### MigrationStateStorage
 Used to store the current migration state.

#### Python
```python
result = substrate.query(
    'DappStakingMigration', 'MigrationStateStorage', []
)
```

#### Return value
```python
{'Finished': None, 'NotInProgress': None, 'SingularStakingInfo': 'Bytes'}
```
---------