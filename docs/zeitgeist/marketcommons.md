
# MarketCommons

---------
## Storage functions

---------
### MarketCounter
 The number of markets that have been created (including removed markets) and the next
 identifier for a created market.

#### Python
```python
result = substrate.query(
    'MarketCommons', 'MarketCounter', []
)
```

#### Return value
```python
'u128'
```
---------
### MarketPool
 Maps a market id to a related pool id. It is up to the caller to keep and sync valid
 existent markets with valid existent pools.

#### Python
```python
result = substrate.query(
    'MarketCommons', 'MarketPool', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### Markets
 Holds all markets

#### Python
```python
result = substrate.query(
    'MarketCommons', 'Markets', ['u128']
)
```

#### Return value
```python
{
    'base_asset': {
        'CategoricalOutcome': ('u128', 'u16'),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': ('u128', ('Long', 'Short')),
        'Ztg': None,
    },
    'bonds': {
        'creation': (
            None,
            {'is_settled': 'bool', 'value': 'u128', 'who': 'AccountId'},
        ),
        'oracle': (
            None,
            {'is_settled': 'bool', 'value': 'u128', 'who': 'AccountId'},
        ),
        'outsider': (
            None,
            {'is_settled': 'bool', 'value': 'u128', 'who': 'AccountId'},
        ),
    },
    'creation': ('Permissionless', 'Advised'),
    'creator': 'AccountId',
    'creator_fee': 'u8',
    'deadlines': {
        'dispute_duration': 'u64',
        'grace_period': 'u64',
        'oracle_duration': 'u64',
    },
    'dispute_mechanism': ('Authorized', 'Court', 'SimpleDisputes'),
    'market_type': {
        'Categorical': 'u16',
        'Scalar': {'end': 'u128', 'start': 'u128'},
    },
    'metadata': 'Bytes',
    'oracle': 'AccountId',
    'period': {
        'Block': {'end': 'u64', 'start': 'u64'},
        'Timestamp': {'end': 'u64', 'start': 'u64'},
    },
    'report': (
        None,
        {
            'at': 'u64',
            'by': 'AccountId',
            'outcome': {'Categorical': 'u16', 'Scalar': 'u128'},
        },
    ),
    'resolved_outcome': (None, {'Categorical': 'u16', 'Scalar': 'u128'}),
    'scoring_rule': ('CPMM', 'RikiddoSigmoidFeeMarketEma'),
    'status': (
        'Proposed',
        'Active',
        'Suspended',
        'Closed',
        'CollectingSubsidy',
        'InsufficientSubsidy',
        'Reported',
        'Disputed',
        'Resolved',
    ),
}
```
---------
## Constants

---------
### PredictionMarketsPalletId
 The prefix used to calculate the prize pool accounts.
#### Value
```python
'0x7a67652f70726564'
```
#### Python
```python
constant = substrate.get_constant('MarketCommons', 'PredictionMarketsPalletId')
```
---------
## Errors

---------
### MarketDoesNotExist
A market with the provided ID does not exist.

---------
### MarketPoolDoesNotExist
Market does not have an stored associated pool id.

---------
### NoMarketHasBeenCreated
It is not possible to fetch the latest market ID when
no market has been created.

---------
### NoReport
Market does not have a report

---------
### PoolAlreadyExists
There&\#x27;s a pool registered for this market already.

---------