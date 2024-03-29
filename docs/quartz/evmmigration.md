
# EvmMigration

---------
## Calls

---------
### begin
See [`Pallet::begin`].
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
See [`Pallet::finish`].
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
See [`Pallet::insert_eth_logs`].
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
            'topics': [
                'scale_info::12',
            ],
        },
    ],
}
)
```

---------
### insert_events
See [`Pallet::insert_events`].
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
### remove_rmrk_data
See [`Pallet::remove_rmrk_data`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EvmMigration', 'remove_rmrk_data', {}
)
```

---------
### set_data
See [`Pallet::set_data`].
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
    'data': [
        (
            'scale_info::12',
            'scale_info::12',
        ),
    ],
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