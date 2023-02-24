
# RikiddoSigmoidFeeMarketEma

---------
## Storage functions

---------
### RikiddoPerPool
 Storage that maps pool ids to Rikiddo instances.

#### Python
```python
result = substrate.query(
    'RikiddoSigmoidFeeMarketEma', 'RikiddoPerPool', ['u128']
)
```

#### Return value
```python
{
    'config': {'initial_fee': {'bits': 'i128'}, 'log2_e': {'bits': 'i128'}},
    'fees': {
        'config': {
            'initial_fee': {'bits': 'i128'},
            'm': {'bits': 'i128'},
            'min_revenue': {'bits': 'i128'},
            'n': {'bits': 'i128'},
            'p': {'bits': 'i128'},
        },
    },
    'ma_long': {
        'config': {
            'ema_period': {
                'Days': 'u16',
                'Hours': 'u32',
                'Minutes': 'u32',
                'Seconds': 'u32',
                'Weeks': 'u16',
            },
            'ema_period_estimate_after': (
                None,
                {
                    'Days': 'u16',
                    'Hours': 'u32',
                    'Minutes': 'u32',
                    'Seconds': 'u32',
                    'Weeks': 'u16',
                },
            ),
            'smoothing': {'bits': 'u128'},
        },
        'ema': {'bits': 'u128'},
        'last_time': 'u64',
        'multiplier': {'bits': 'u128'},
        'start_time': 'u64',
        'state': ('Uninitialized', 'DataCollectionStarted', 'DataCollected'),
        'volumes_per_period': {'bits': 'u128'},
    },
    'ma_short': {
        'config': {
            'ema_period': {
                'Days': 'u16',
                'Hours': 'u32',
                'Minutes': 'u32',
                'Seconds': 'u32',
                'Weeks': 'u16',
            },
            'ema_period_estimate_after': (
                None,
                {
                    'Days': 'u16',
                    'Hours': 'u32',
                    'Minutes': 'u32',
                    'Seconds': 'u32',
                    'Weeks': 'u16',
                },
            ),
            'smoothing': {'bits': 'u128'},
        },
        'ema': {'bits': 'u128'},
        'last_time': 'u64',
        'multiplier': {'bits': 'u128'},
        'start_time': 'u64',
        'state': ('Uninitialized', 'DataCollectionStarted', 'DataCollected'),
        'volumes_per_period': {'bits': 'u128'},
    },
}
```
---------
## Constants

---------
### BalanceFractionalDecimals
 Number of fractional decimal places for one unit of currency.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('RikiddoSigmoidFeeMarketEma', 'BalanceFractionalDecimals')
```
---------
## Errors

---------
### FixedConversionImpossible
Conversion between the `Balance` and the internal Rikiddo core type failed.

---------
### RikiddoAlreadyExistsForPool
Trying to create a Rikiddo instance for a `poolid` that already has a Rikiddo instance.

---------
### RikiddoNotFoundForPool
For a given `poolid`, no Rikiddo instance could be found.

---------