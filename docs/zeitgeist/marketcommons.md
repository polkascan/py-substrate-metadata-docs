
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
 Maps a market ID to a related pool ID. It is up to the caller to keep and sync valid
 existent markets with valid existent pools.

 Beware! DEPRECATED as of v0.5.0.

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
        'ParimutuelShare': ('u128', 'u16'),
        'PoolShare': 'u128',
        'ScalarOutcome': ('u128', ('Long', 'Short')),
        'Ztg': None,
    },
    'bonds': {
        'close_dispute': (
            None,
            {'is_settled': 'bool', 'value': 'u128', 'who': 'AccountId'},
        ),
        'close_request': (
            None,
            {'is_settled': 'bool', 'value': 'u128', 'who': 'AccountId'},
        ),
        'creation': (
            None,
            {'is_settled': 'bool', 'value': 'u128', 'who': 'AccountId'},
        ),
        'dispute': (
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
    'creator_fee': 'u32',
    'deadlines': {
        'dispute_duration': 'u64',
        'grace_period': 'u64',
        'oracle_duration': 'u64',
    },
    'dispute_mechanism': (None, ('Authorized', 'Court', 'SimpleDisputes')),
    'early_close': (
        None,
        {
            'new': {
                'Block': {'end': 'u64', 'start': 'u64'},
                'Timestamp': {'end': 'u64', 'start': 'u64'},
            },
            'old': {
                'Block': {'end': 'u64', 'start': 'u64'},
                'Timestamp': {'end': 'u64', 'start': 'u64'},
            },
            'state': (
                'ScheduledAsMarketCreator',
                'ScheduledAsOther',
                'Disputed',
                'Rejected',
            ),
        },
    ),
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
    'scoring_rule': ('Lmsr', 'Orderbook', 'Parimutuel'),
    'status': (
        'Proposed',
        'Active',
        'Closed',
        'Reported',
        'Disputed',
        'Resolved',
    ),
}
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