
# Oracle

---------
## Calls

---------
### feed_values
Feeds data from the oracles, e.g., the exchange rates. This function
is intended to be API-compatible with orml-oracle.

\# Arguments

* `values` - a vector of (key, value) pairs to submit
#### Attributes
| Name | Type |
| -------- | -------- | 
| values | `Vec<(OracleKey, T::UnsignedFixedPoint)>` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'feed_values', {
    'values': [
        (
            {
                'ExchangeRate': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                    ),
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                'FeeEstimation': None,
            },
            'u128',
        ),
    ],
}
)
```

---------
### insert_authorized_oracle
Adds an authorized oracle account (only executable by the Root account)

\# Arguments
* `account_id` - the account Id of the oracle
* `name` - a descriptive name for the oracle
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 
| name | `NameOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'insert_authorized_oracle', {
    'account_id': 'AccountId',
    'name': 'Bytes',
}
)
```

---------
### remove_authorized_oracle
Removes an authorized oracle account (only executable by the Root account)

\# Arguments
* `account_id` - the account Id of the oracle
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'remove_authorized_oracle', {'account_id': 'AccountId'}
)
```

---------
## Events

---------
### AggregateUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| values | `Vec<(OracleKey, Option<T::UnsignedFixedPoint>)>` | ```[({'ExchangeRate': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ('scale_info::52', 'scale_info::52'), 'StableLpToken': 'u32'}, 'FeeEstimation': None}, (None, 'u128'))]```

---------
### FeedValues
Event emitted when exchange rate is set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| oracle_id | `T::AccountId` | ```AccountId```
| values | `Vec<(OracleKey, T::UnsignedFixedPoint)>` | ```[({'ExchangeRate': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ('scale_info::52', 'scale_info::52'), 'StableLpToken': 'u32'}, 'FeeEstimation': None}, 'u128')]```

---------
### OracleAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| oracle_id | `T::AccountId` | ```AccountId```
| name | `NameOf<T>` | ```Bytes```

---------
### OracleRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| oracle_id | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Aggregate
 Current medianized value for the given key

#### Python
```python
result = substrate.query(
    'Oracle', 'Aggregate', [
    {
        'ExchangeRate': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'FeeEstimation': None,
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### AuthorizedOracles

#### Python
```python
result = substrate.query(
    'Oracle', 'AuthorizedOracles', ['AccountId']
)
```

#### Return value
```python
'Bytes'
```
---------
### MaxDelay
 Maximum delay (milliseconds) for a reported value to be used

#### Python
```python
result = substrate.query(
    'Oracle', 'MaxDelay', []
)
```

#### Return value
```python
'u64'
```
---------
### RawValues

#### Python
```python
result = substrate.query(
    'Oracle', 'RawValues', [
    {
        'ExchangeRate': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'FeeEstimation': None,
    },
    'AccountId',
]
)
```

#### Return value
```python
{'timestamp': 'u64', 'value': 'u128'}
```
---------
### RawValuesUpdated
 if a key is present, it means the values have been updated

#### Python
```python
result = substrate.query(
    'Oracle', 'RawValuesUpdated', [
    {
        'ExchangeRate': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'FeeEstimation': None,
    },
]
)
```

#### Return value
```python
'bool'
```
---------
### StorageVersion
 Build storage at V1 (requires default 0).

#### Python
```python
result = substrate.query(
    'Oracle', 'StorageVersion', []
)
```

#### Return value
```python
('V0', )
```
---------
### ValidUntil
 Time until which the aggregate is valid

#### Python
```python
result = substrate.query(
    'Oracle', 'ValidUntil', [
    {
        'ExchangeRate': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'FeeEstimation': None,
    },
]
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### MaxNameLength
 The maximum length of an oracle name.
#### Value
```python
255
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'MaxNameLength')
```
---------
## Errors

---------
### InvalidOracleSource
Not authorized to set exchange rate

---------
### MissingExchangeRate
Exchange rate not specified or has expired

---------
### TryIntoIntError
Unable to convert value

---------