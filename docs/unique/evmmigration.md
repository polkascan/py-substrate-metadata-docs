
# EvmMigration

---------
## Calls

---------
### begin
Start contract migration, inserts contract stub at target address,
and marks account as pending, allowing to insert storage
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `H160` | 

#### Python
```python
call = substrate.compose_call(
    'EvmMigration', 'begin', {'address': '[u8; 20]'}
)
```

---------
### finish
Finish contract migration, allows it to be called.
It is not possible to alter contract storage via [`Self::set_data`]
after this call.
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `H160` | 
| code | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'EvmMigration', 'finish', {
    'address': '[u8; 20]',
    'code': 'Bytes',
}
)
```

---------
### insert_eth_logs
Create ethereum events attached to the fake transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| logs | `Vec<ethereum::Log>` | 

#### Python
```python
call = substrate.compose_call(
    'EvmMigration', 'insert_eth_logs', {
    'logs': [
        {
            'address': '[u8; 20]',
            'data': 'Bytes',
            'topics': ['[u8; 32]'],
        },
    ],
}
)
```

---------
### insert_events
Create substrate events
#### Attributes
| Name | Type |
| -------- | -------- | 
| events | `Vec<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'EvmMigration', 'insert_events', {'events': ['Bytes']}
)
```

---------
### set_data
Insert items into contract storage, this method can be called
multiple times
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `H160` | 
| data | `Vec<(H256, H256)>` | 

#### Python
```python
call = substrate.compose_call(
    'EvmMigration', 'set_data', {
    'address': '[u8; 20]',
    'data': [('[u8; 32]', '[u8; 32]')],
}
)
```

---------
## Events

---------
### TestEvent
This event is used in benchmarking and can be used for tests
#### Attributes
No attributes

---------
## Storage functions

---------
### MigrationPending

#### Python
```python
result = substrate.query(
    'EvmMigration', 'MigrationPending', ['[u8; 20]']
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### AccountIsNotMigrating
Migration of this account is not yet started, or already finished.

---------
### AccountNotEmpty
Can only migrate to empty address.

---------
### BadEvent
Failed to decode event bytes

---------