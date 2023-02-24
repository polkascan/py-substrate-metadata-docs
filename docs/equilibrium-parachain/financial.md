
# Financial

---------
## Calls

---------
### recalc
Recalculates financial metrics for all known assets.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Financial', 'recalc', {}
)
```

---------
### recalc_asset
Recalculates financial metrics for a given asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `T::Asset` | 

#### Python
```python
call = substrate.compose_call(
    'Financial', 'recalc_asset', {'asset': 'u64'}
)
```

---------
### recalc_portfolio
Recalculates financial metrics for a given portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 
| z_score | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Financial', 'recalc_portfolio', {
    'account_id': 'AccountId',
    'z_score': 'u32',
}
)
```

---------
### set_metrics
Test utility function for setting metrics, not allowed in production
#### Attributes
| Name | Type |
| -------- | -------- | 
| metrics | `FinancialMetrics<T::Asset, T::Price>` | 

#### Python
```python
call = substrate.compose_call(
    'Financial', 'set_metrics', {
    'metrics': {
        'assets': ['u64'],
        'correlations': [
            {'bits': 'i128'},
        ],
        'covariances': [
            {'bits': 'i128'},
        ],
        'mean_returns': [
            {'bits': 'i128'},
        ],
        'period_end': {
            'nanos': 'u32',
            'secs': 'u64',
        },
        'period_start': {
            'nanos': 'u32',
            'secs': 'u64',
        },
        'volatilities': [
            {'bits': 'i128'},
        ],
    },
}
)
```

---------
### set_per_asset_metrics
Test utility function for setting asset metrics, not allowed in production
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `T::Asset` | 
| metrics | `AssetMetrics<T::Asset, T::Price>` | 

#### Python
```python
call = substrate.compose_call(
    'Financial', 'set_per_asset_metrics', {
    'asset': 'u64',
    'metrics': {
        'correlations': [
            ('u64', {'bits': 'i128'}),
        ],
        'period_end': {
            'nanos': 'u32',
            'secs': 'u64',
        },
        'period_start': {
            'nanos': 'u32',
            'secs': 'u64',
        },
        'returns': [{'bits': 'i128'}],
        'volatility': {'bits': 'i128'},
    },
}
)
```

---------
## Events

---------
### AssetMetricsRecalculated
Financial metrics for the specified asset have been recalculated
\[asset\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Asset` | ```u64```

---------
### MetricsRecalculated
Financial metrics for all assets have been recalculated
#### Attributes
No attributes

---------
### PortfolioMetricsRecalculated
Financial metrics for the specified portfolio have been recalculated
\[portfolio\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```

---------
## Storage functions

---------
### Metrics
 Financial metrics for all known assets.

#### Python
```python
result = substrate.query(
    'Financial', 'Metrics', []
)
```

#### Return value
```python
{
    'assets': ['u64'],
    'correlations': [{'bits': 'i128'}],
    'covariances': [{'bits': 'i128'}],
    'mean_returns': [{'bits': 'i128'}],
    'period_end': {'nanos': 'u32', 'secs': 'u64'},
    'period_start': {'nanos': 'u32', 'secs': 'u64'},
    'volatilities': [{'bits': 'i128'}],
}
```
---------
### PerAssetMetrics
 Financial metrics on per asset basis.

#### Python
```python
result = substrate.query(
    'Financial', 'PerAssetMetrics', ['u64']
)
```

#### Return value
```python
{
    'correlations': [('u64', {'bits': 'i128'})],
    'period_end': {'nanos': 'u32', 'secs': 'u64'},
    'period_start': {'nanos': 'u32', 'secs': 'u64'},
    'returns': [{'bits': 'i128'}],
    'volatility': {'bits': 'i128'},
}
```
---------
### PerPortfolioMetrics
 Financial metrics on per portfolio basis.

#### Python
```python
result = substrate.query(
    'Financial', 'PerPortfolioMetrics', ['AccountId']
)
```

#### Return value
```python
{
    'period_end': {'nanos': 'u32', 'secs': 'u64'},
    'period_start': {'nanos': 'u32', 'secs': 'u64'},
    'value_at_risk': {'bits': 'i128'},
    'volatility': {'bits': 'i128'},
    'z_score': 'u32',
}
```
---------
### PriceLogs
 Price log on per asset basis.

#### Python
```python
result = substrate.query(
    'Financial', 'PriceLogs', ['u64']
)
```

#### Return value
```python
{
    'latest_timestamp': {'nanos': 'u32', 'secs': 'u64'},
    'prices': {'head_index': 'u32', 'items': [{'bits': 'i128'}], 'len_cap': 'u32'},
}
```
---------
### Updates
 Latest price updates on per asset basis.

#### Python
```python
result = substrate.query(
    'Financial', 'Updates', ['u64']
)
```

#### Return value
```python
{
    'period_start': {'nanos': 'u32', 'secs': 'u64'},
    'price': {'bits': 'i128'},
    'time': {'nanos': 'u32', 'secs': 'u64'},
}
```
---------
## Constants

---------
### PriceCount
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('Financial', 'PriceCount')
```
---------
### PricePeriod
#### Value
```python
1440
```
#### Python
```python
constant = substrate.get_constant('Financial', 'PricePeriod')
```
---------
## Errors

---------
### DivisionByZero
Division by zero occurred during financial calculation process.

---------
### InvalidArgument
An invalid argument passed to the function.

---------
### InvalidConstant
Default return type or default correlation type is initialized with a value that can
not be converted to type `CalcReturnType` or `CalcVolatilityType` respectively.

---------
### InvalidPeriodStart
Specified period start timestamp is invalid for current
[`PricePeriod`](./trait.Config.html\#associatedtype.PricePeriod) value.

---------
### InvalidStorage
Storage of the pallet is in an unexpected state.

---------
### MethodNotAllowed
This method is not allowed in production. Method is used in testing only

---------
### NotEnoughPoints
Price log is not long enough to calculate required value.

---------
### NotImplemented
Required functionality is not implemented.

---------
### Overflow
Overflow occurred during financial calculation process.

---------
### PeriodIsInThePast
Timestamp of the received price is in the past.

---------
### Transcendental
An invalid argument passed to the transcendental function (i.e. log, sqrt, etc.)
during financial calculation process.

---------