
# Teeracle

---------
## Calls

---------
### add_to_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| data_source | `DataSource` | 
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
| data_source | `DataSource` | 
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
| data_source | `DataSource` | 
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
### update_oracle
#### Attributes
| Name | Type |
| -------- | -------- | 
| oracle_name | `OracleDataName` | 
| data_source | `DataSource` | 
| new_blob | `OracleDataBlob<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Teeracle', 'update_oracle', {
    'data_source': 'Bytes',
    'new_blob': 'Bytes',
    'oracle_name': 'Bytes',
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
| None | `DataSource` | ```Bytes```
| None | `[u8; 32]` | ```[u8; 32]```

---------
### ExchangeRateDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DataSource` | ```Bytes```
| None | `TradingPairString` | ```Bytes```

---------
### ExchangeRateUpdated
The exchange rate of trading pair was set/updated with value from source.
\[data_source], [trading_pair], [new value\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DataSource` | ```Bytes```
| None | `TradingPairString` | ```Bytes```
| None | `Option<ExchangeRate>` | ```(None, {'bits': 'u64'})```

---------
### OracleUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OracleDataName` | ```Bytes```
| None | `DataSource` | ```Bytes```

---------
### RemovedFromWhitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DataSource` | ```Bytes```
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
### OracleData

#### Python
```python
result = substrate.query(
    'Teeracle', 'OracleData', ['Bytes', 'Bytes']
)
```

#### Return value
```python
'Bytes'
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
### MaxOracleBlobLen
#### Value
```python
4096
```
#### Python
```python
constant = substrate.get_constant('Teeracle', 'MaxOracleBlobLen')
```
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
### DataSourceStringTooLong

---------
### InvalidCurrency

---------
### OracleBlobTooBig

---------
### OracleDataNameStringTooLong

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