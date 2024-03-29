
# Authorship

---------
## Calls

---------
### set_uncles
Provide a set of uncles.
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
                        'Other': 'Bytes',
                        None: None,
                        'Consensus': (
                            '[u8; 4]',
                            'Bytes',
                        ),
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
            'extrinsics_root': 'scale_info::11',
            'number': 'u32',
            'parent_hash': 'scale_info::11',
            'state_root': 'scale_info::11',
        },
    ],
}
)
```

---------
## Storage functions

---------
### Author
 Author of current block.

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
 Whether uncles were already set in this block.

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
 Uncles

#### Python
```python
result = substrate.query(
    'Authorship', 'Uncles', []
)
```

#### Return value
```python
[{'InclusionHeight': 'u32', 'Uncle': ('scale_info::11', (None, 'AccountId'))}]
```
---------
## Constants

---------
### UncleGenerations
 The number of blocks back we should accept uncles.
 This means that we will deal with uncle-parents that are
 `UncleGenerations + 1` before `now`.
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
The uncle is genesis.

---------
### InvalidUncleParent
The uncle parent not in the chain.

---------
### OldUncle
The uncle isn&\#x27;t recent enough to be included.

---------
### TooHighUncle
The uncle is too high in chain.

---------
### TooManyUncles
Too many uncles.

---------
### UncleAlreadyIncluded
The uncle is already included.

---------
### UnclesAlreadySet
Uncles already set in the block.

---------