
# ParaSessionInfo

---------
## Storage functions

---------
### AccountKeys
 The validator account keys of the validators actively participating in parachain consensus.

#### Python
```python
result = substrate.query(
    'ParaSessionInfo', 'AccountKeys', ['u32']
)
```

#### Return value
```python
['AccountId']
```
---------
### AssignmentKeysUnsafe
 Assignment keys for the current session.
 Note that this API is private due to it being prone to &#x27;off-by-one&#x27; at session boundaries.
 When in doubt, use `Sessions` API instead.

#### Python
```python
result = substrate.query(
    'ParaSessionInfo', 'AssignmentKeysUnsafe', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### EarliestStoredSession
 The earliest session for which previous session info is stored.

#### Python
```python
result = substrate.query(
    'ParaSessionInfo', 'EarliestStoredSession', []
)
```

#### Return value
```python
'u32'
```
---------
### SessionExecutorParams
 Executor parameter set for a given session index

#### Python
```python
result = substrate.query(
    'ParaSessionInfo', 'SessionExecutorParams', ['u32']
)
```

#### Return value
```python
[
    {
        None: None,
        'MaxMemoryPages': 'u32',
        'PrecheckingMaxMemory': 'u64',
        'PvfExecTimeout': (('Backing', 'Approval'), 'u64'),
        'PvfPrepTimeout': (('Precheck', 'Lenient'), 'u64'),
        'StackLogicalMax': 'u32',
        'StackNativeMax': 'u32',
        'WasmExtBulkMemory': None,
    },
]
```
---------
### Sessions
 Session information in a rolling window.
 Should have an entry in range `EarliestStoredSession..=CurrentSessionIndex`.
 Does not have any entries before the session index in the first session change notification.

#### Python
```python
result = substrate.query(
    'ParaSessionInfo', 'Sessions', ['u32']
)
```

#### Return value
```python
{
    'active_validator_indices': ['u32'],
    'assignment_keys': ['[u8; 32]'],
    'discovery_keys': ['[u8; 32]'],
    'dispute_period': 'u32',
    'n_cores': 'u32',
    'n_delay_tranches': 'u32',
    'needed_approvals': 'u32',
    'no_show_slots': 'u32',
    'random_seed': '[u8; 32]',
    'relay_vrf_modulo_samples': 'u32',
    'validator_groups': [['u32']],
    'validators': ['[u8; 32]'],
    'zeroth_delay_tranche_width': 'u32',
}
```
---------