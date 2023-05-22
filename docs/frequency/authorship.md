
# Authorship

---------
## Calls

---------
### set_uncles
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_uncles | `Vec<T::Header>` | 

#### Python
```python
call = substrate.compose_call(
    'Authorship', 'set_uncles', {
    'new_uncles': [
        {
            'digest': {
                'logs': [
                    {
                        'Consensus': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                        'Other': 'Bytes',
                        None: None,
                        'PreRuntime': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                        'RuntimeEnvironmentUpdated': None,
                        'Seal': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                    },
                ],
            },
            'extrinsics_root': '[u8; 32]',
            'number': 'u32',
            'parent_hash': '[u8; 32]',
            'state_root': '[u8; 32]',
        },
    ],
}
)
```

---------
## Storage functions

---------
### Author

#### Python
```python
result = substrate.query(
    'Authorship', 'Author', []
)
```

#### Return value
```python
'AccountId'
```
---------
### DidSetUncles

#### Python
```python
result = substrate.query(
    'Authorship', 'DidSetUncles', []
)
```

#### Return value
```python
'bool'
```
---------
### Uncles

#### Python
```python
result = substrate.query(
    'Authorship', 'Uncles', []
)
```

#### Return value
```python
[{'InclusionHeight': 'u32', 'Uncle': ('[u8; 32]', (None, 'AccountId'))}]
```
---------
## Constants

---------
### UncleGenerations
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Authorship', 'UncleGenerations')
```
---------
## Errors

---------
### GenesisUncle

---------
### InvalidUncleParent

---------
### OldUncle

---------
### TooHighUncle

---------
### TooManyUncles

---------
### UncleAlreadyIncluded

---------
### UnclesAlreadySet

---------