
# Migration

---------
## Calls

---------
### set_migration
Adds new migration, if there is no migration in storage
#### Attributes
| Name | Type |
| -------- | -------- | 
| migration | `Vec<KeyValue>` | 

#### Python
```python
call = substrate.compose_call(
    'Migration', 'set_migration', {'migration': [('Bytes', 'Bytes')]}
)
```

---------
## Events

---------
### Migrated
Migration completed
#### Attributes
No attributes

---------
### MigrationProcessed
Migration processed N items
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```

---------
### MigrationSetted
New migration with N length added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```

---------
## Storage functions

---------
### Migration
 Current migration

#### Python
```python
result = substrate.query(
    'Migration', 'Migration', []
)
```

#### Return value
```python
[('Bytes', 'Bytes')]
```
---------
## Constants

---------
### MigrationsPerBlock
 Set storage calls per block
#### Value
```python
2000
```
#### Python
```python
constant = substrate.get_constant('Migration', 'MigrationsPerBlock')
```
---------
## Errors

---------
### MigrationIsInProgress
We cannot start new migration before current ended

---------