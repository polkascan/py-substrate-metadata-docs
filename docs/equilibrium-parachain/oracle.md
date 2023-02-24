
# Oracle

---------
## Calls

---------
### set_fin_metrics_recalc_enabled
Enables or disables auto recalculation of financial metrics
#### Attributes
| Name | Type |
| -------- | -------- | 
| enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'set_fin_metrics_recalc_enabled', {'enabled': 'bool'}
)
```

---------
### set_price
Adds and saves a new `DataPoint` containing an asset price information. It
would be used for the `PricePoint` calculation. Only whitelisted
accounts can add `DataPoints`
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| price | `FixedI64` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'set_price', {'asset': 'u64', 'price': 'i64'}
)
```

---------
### set_price_unsigned
Adds new `DataPoint` from an unsigned transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| payload | `PricePayload<T::Public, T::BlockNumber>` | 
| signature | `T::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'set_price_unsigned', {
    'payload': {
        'asset': 'u64',
        'block_number': 'u32',
        'price': 'i64',
        'public': {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
## Events

---------
### NewPrice
A new price added to the storage. The event contains: `Asset` for the price,
`FixedI64` for the price value that was added, `FixedI64` for a new
aggregated price and `AccountId` of the price submitter
\[asset, new_value, aggregated, submitter\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Asset` | ```u64```
| None | `FixedI64` | ```i64```
| None | `FixedI64` | ```i64```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### FinMetricsRecalcEnabled
 Stores flag for the automatic financial metrics recalculation at the start of each block

#### Python
```python
result = substrate.query(
    'Oracle', 'FinMetricsRecalcEnabled', []
)
```

#### Return value
```python
'bool'
```
---------
### PricePoints
 Pallet storage for added price points

#### Python
```python
result = substrate.query(
    'Oracle', 'PricePoints', ['u64']
)
```

#### Return value
```python
{
    'block_number': 'u32',
    'data_points': [
        {
            'account_id': 'AccountId',
            'block_number': 'u32',
            'price': 'i64',
            'timestamp': 'u64',
        },
    ],
    'last_fin_recalc_timestamp': 'u64',
    'price': 'i64',
    'timestamp': 'u64',
}
```
---------
## Constants

---------
### FinancialRecalcPeriodBlocks
 Time between recalculation assets financial data in ms
#### Value
```python
1200
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'FinancialRecalcPeriodBlocks')
```
---------
### MedianPriceTimeout
 Pallet setting representing amount of time for which price median is valid
#### Value
```python
3600
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'MedianPriceTimeout')
```
---------
### PriceTimeout
 Pallet setting representing amount of time for which price point is valid
#### Value
```python
60
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'PriceTimeout')
```
---------
### UnsignedLifetimeInBlocks
 Lifetime in blocks for unsigned transactions
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'UnsignedLifetimeInBlocks')
```
---------
### UnsignedPriority
 For priority calculation of an unsigned transaction
#### Value
```python
(0, 10000)
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'UnsignedPriority')
```
---------
## Errors

---------
### CurrencyNotFound
Incorrect asset

---------
### MethodNotAllowed
This method is not allowed in production

---------
### NotAllowedToSubmitPrice
The account is not allowed to set prices

---------
### PoolNotFound
LP token pool is not found

---------
### PriceAlreadyAdded
The same price data point has been already added

---------
### PriceIsNegative
The price cannot be negative

---------
### PriceIsZero
The price cannot be zero

---------
### PriceTimeout
The price data point is too old and cannot be used

---------
### PrimitiveAssetExpected
A primitive asset is expected

---------
### WrongCurrency
Attempting to submit a new price for constant price currencies

---------