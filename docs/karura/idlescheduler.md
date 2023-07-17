
# IdleScheduler

---------
## Calls

---------
### schedule_task
#### Attributes
| Name | Type |
| -------- | -------- | 
| task | `T::Task` | 

#### Python
```python
call = substrate.compose_call(
    'IdleScheduler', 'schedule_task', {
    'task': {
        'EvmTask': {
            'Remove': {
                'caller': '[u8; 20]',
                'contract': '[u8; 20]',
                'maintainer': '[u8; 20]',
            },
            'Schedule': {
                'from': '[u8; 20]',
                'gas_limit': 'u64',
                'input': 'Bytes',
                'storage_limit': 'u32',
                'target': '[u8; 20]',
                'value': 'u128',
            },
        },
    },
}
)
```

---------
## Events

---------
### TaskAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `Nonce` | ```u32```
| task | `T::Task` | ```{'EvmTask': {'Schedule': {'from': '[u8; 20]', 'target': '[u8; 20]', 'input': 'Bytes', 'value': 'u128', 'gas_limit': 'u64', 'storage_limit': 'u32'}, 'Remove': {'caller': '[u8; 20]', 'contract': '[u8; 20]', 'maintainer': '[u8; 20]'}}}```

---------
### TaskDispatched
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `Nonce` | ```u32```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
## Storage functions

---------
### NextTaskId

#### Python
```python
result = substrate.query(
    'IdleScheduler', 'NextTaskId', []
)
```

#### Return value
```python
'u32'
```
---------
### PreviousRelayBlockNumber

#### Python
```python
result = substrate.query(
    'IdleScheduler', 'PreviousRelayBlockNumber', []
)
```

#### Return value
```python
'u32'
```
---------
### Tasks

#### Python
```python
result = substrate.query(
    'IdleScheduler', 'Tasks', ['u32']
)
```

#### Return value
```python
{
    'EvmTask': {
        'Remove': {
            'caller': '[u8; 20]',
            'contract': '[u8; 20]',
            'maintainer': '[u8; 20]',
        },
        'Schedule': {
            'from': '[u8; 20]',
            'gas_limit': 'u64',
            'input': 'Bytes',
            'storage_limit': 'u32',
            'target': '[u8; 20]',
            'value': 'u128',
        },
    },
}
```
---------
## Constants

---------
### DisableBlockThreshold
#### Value
```python
6
```
#### Python
```python
constant = substrate.get_constant('IdleScheduler', 'DisableBlockThreshold')
```
---------
### MinimumWeightRemainInBlock
#### Value
```python
{'proof_size': 1048576, 'ref_time': 10000000000}
```
#### Python
```python
constant = substrate.get_constant('IdleScheduler', 'MinimumWeightRemainInBlock')
```
---------