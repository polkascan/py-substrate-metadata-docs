
# Migration

---------
## Calls

---------
### update_balance
See [`Pallet::update_balance`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| requested_migrations | `EntriesToMigrate<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Migration', 'update_balance', {
    'requested_migrations': {
        'attestation': [
            'scale_info::12',
        ],
        'delegation': [
            'scale_info::12',
        ],
        'did': ['AccountId'],
        'lookup': [
            {
                'AccountId20': '[u8; 20]',
                'AccountId32': 'AccountId',
            },
        ],
        'public_credentials': [
            (
                {
                    'asset_id': 'scale_info::89',
                    'chain_id': 'scale_info::79',
                },
                'scale_info::12',
            ),
        ],
        'w3n': ['Bytes'],
    },
}
)
```

---------
## Events

---------
### EntriesUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EntriesToMigrate<T>` | ```{'attestation': ['scale_info::12'], 'delegation': ['scale_info::12'], 'did': ['AccountId'], 'lookup': [{'AccountId20': '[u8; 20]', 'AccountId32': 'AccountId'}], 'w3n': ['Bytes'], 'public_credentials': [('scale_info::78', 'scale_info::12')]}```

---------
## Storage functions

---------
### MigratedKeys

#### Python
```python
result = substrate.query(
    'Migration', 'MigratedKeys', ['scale_info::12']
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### MaxMigrationsPerPallet
 The max amount on migrations for each pallet
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Migration', 'MaxMigrationsPerPallet')
```
---------
## Errors

---------
### KeyParse

---------