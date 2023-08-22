
# EmaOracle

---------
## Storage functions

---------
### Accumulator
 Accumulator for oracle data in current block that will be recorded at the end of the block.

#### Python
```python
result = substrate.query(
    'EmaOracle', 'Accumulator', []
)
```

#### Return value
```python
'scale_info::556'
```
---------
### Oracles
 Orace storage keyed by data source, involved asset ids and the period length of the oracle.

 Stores the data entry as well as the block number when the oracle was first initialized.

#### Python
```python
result = substrate.query(
    'EmaOracle', 'Oracles', [
    '[u8; 8]',
    ('u32', 'u32'),
    (
        'LastBlock',
        'Short',
        'TenMinutes',
        'Hour',
        'Day',
        'Week',
    ),
]
)
```

#### Return value
```python
(
    {
        'liquidity': {'a': 'u128', 'b': 'u128'},
        'price': {'d': 'u128', 'n': 'u128'},
        'updated_at': 'u32',
        'volume': {
            'a_in': 'u128',
            'a_out': 'u128',
            'b_in': 'u128',
            'b_out': 'u128',
        },
    },
    'u32',
)
```
---------
## Constants

---------
### MaxUniqueEntries
 Maximum number of unique oracle entries expected in one block.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('EmaOracle', 'MaxUniqueEntries')
```
---------
## Errors

---------
### OnTradeValueZero

---------
### TooManyUniqueEntries

---------