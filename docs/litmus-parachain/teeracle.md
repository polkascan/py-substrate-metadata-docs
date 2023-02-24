
# Teeracle

---------
## Calls

---------
### add_to_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| data_source | `MarketDataSourceString` | 
| mrenclave | `[u8; 32]` | 

#### Python
```python
call = substrate.compose_call(
    'Teeracle', 'add_to_whitelist', {
    'data_source': 'Bytes',
    'mrenclave': '[u8; 32]',
}
)
```

---------
### remove_from_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| data_source | `MarketDataSourceString` | 
| mrenclave | `[u8; 32]` | 

#### Python
```python
call = substrate.compose_call(
    'Teeracle', 'remove_from_whitelist', {
    'data_source': 'Bytes',
    'mrenclave': '[u8; 32]',
}
)
```

---------
### update_exchange_rate
#### Attributes
| Name | Type |
| -------- | -------- | 
| data_source | `MarketDataSourceString` | 
| trading_pair | `TradingPairString` | 
| new_value | `Option<ExchangeRate>` | 

#### Python
```python
call = substrate.compose_call(
    'Teeracle', 'update_exchange_rate', {
    'data_source': 'Bytes',
    'new_value': (
        None,
        {'bits': 'u64'},
    ),
    'trading_pair': 'Bytes',
}
)
```

---------
## Events

---------
### AddedToWhitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MarketDataSourceString` | ```Bytes```
| None | `[u8; 32]` | ```[u8; 32]```

---------
### ExchangeRateDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MarketDataSourceString` | ```Bytes```
| None | `TradingPairString` | ```Bytes```

---------
### ExchangeRateUpdated
The exchange rate of trading pair was set/updated with value from source. \[data_source], [trading_pair], [new value\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MarketDataSourceString` | ```Bytes```
| None | `TradingPairString` | ```Bytes```
| None | `Option<ExchangeRate>` | ```(None, {'bits': 'u64'})```

---------
### RemovedFromWhitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MarketDataSourceString` | ```Bytes```
| None | `[u8; 32]` | ```[u8; 32]```

---------
## Storage functions

---------
### ExchangeRates
 Exchange rates chain&#x27;s cryptocurrency/currency (trading pair) from different sources

#### Python
```python
result = substrate.query(
    'Teeracle', 'ExchangeRates', ['Bytes', 'Bytes']
)
```

#### Return value
```python
{'bits': 'u64'}
```
---------
### Whitelists
 whitelist of trusted oracle&#x27;s releases for different data sources

#### Python
```python
result = substrate.query(
    'Teeracle', 'Whitelists', ['Bytes']
)
```

#### Return value
```python
['[u8; 32]']
```
---------
## Constants

---------
### MaxWhitelistedReleases
 Max number of whitelisted oracle&#x27;s releases allowed
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Teeracle', 'MaxWhitelistedReleases')
```
---------
## Errors

---------
### InvalidCurrency

---------
### MarketDataSourceStringTooLong

---------
### ReleaseAlreadyWhitelisted

---------
### ReleaseNotWhitelisted

---------
### ReleaseWhitelistOverflow
Too many MrEnclave in the whitelist.

---------
### TradingPairStringTooLong

---------