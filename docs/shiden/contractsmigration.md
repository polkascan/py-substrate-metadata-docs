
# ContractsMigration

---------
## Calls

---------
### migrate
#### Attributes
| Name | Type |
| -------- | -------- | 
| weight_limit | `Option<Weight>` | 

#### Python
```python
call = substrate.compose_call(
    'ContractsMigration', 'migrate', {
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
### ContractsMigrated
Number of contracts that were migrated in the migration call
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
## Storage functions

---------
### MigrationStateStorage

#### Python
```python
result = substrate.query(
    'ContractsMigration', 'MigrationStateStorage', []
)
```

#### Return value
```python
{'CodeStorage': (None, 'Bytes'), 'NotInProgress': None}
```
---------