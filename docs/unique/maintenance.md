
# Maintenance

---------
## Calls

---------
### disable
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'disable', {}
)
```

---------
### enable
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'enable', {}
)
```

---------
### execute_preimage
Execute a runtime call stored as a preimage.

`weight_bound` is the maximum weight that the caller is willing
to allow the extrinsic to be executed with.
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `H256` | 
| weight_bound | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'execute_preimage', {
    'hash': '[u8; 32]',
    'weight_bound': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
## Events

---------
### MaintenanceDisabled
#### Attributes
No attributes

---------
### MaintenanceEnabled
#### Attributes
No attributes

---------
## Storage functions

---------
### Enabled

#### Python
```python
result = substrate.query(
    'Maintenance', 'Enabled', []
)
```

#### Return value
```python
'bool'
```
---------