
# Teeracle

---------
## Calls

---------
### add_to_whitelist
See [`Pallet::add_to_whitelist`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| data_source | `DataSource` | 
| enclave_fingerprint | `EnclaveFingerprint` | 

#### Python
```python
call = substrate.compose_call(
    'Teeracle', 'add_to_whitelist', {
    'data_source': 'Bytes',
    'enclave_fingerprint': 'scale_info::12',
}
)
```

---------
### remove_from_whitelist
See [`Pallet::remove_from_whitelist`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| data_source | `DataSource` | 
| enclave_fingerprint | `EnclaveFingerprint` | 

#### Python
```python
call = substrate.compose_call(
    'Teeracle', 'remove_from_whitelist', {
    'data_source': 'Bytes',
    'enclave_fingerprint': 'scale_info::12',
}
)
```

---------
### update_exchange_rate
See [`Pallet::update_exchange_rate`].
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
See [`Pallet::update_oracle`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| oracle_data_name | `OracleDataName` | 
| data_source | `DataSource` | 
| new_blob | `OracleDataBlob<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Teeracle', 'update_oracle', {
    'data_source': 'Bytes',
    'new_blob': 'Bytes',
    'oracle_data_name': 'Bytes',
}
)
```

---------
## Events

---------
### AddedToWhitelist
an oracle fingerprint has been added to the whitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| data_source | `DataSource` | ```Bytes```
| enclave_fingerprint | `EnclaveFingerprint` | ```scale_info::12```

---------
### ExchangeRateDeleted
The exchange rate of trading pair was deleted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| data_source | `DataSource` | ```Bytes```
| trading_pair | `TradingPairString` | ```Bytes```

---------
### ExchangeRateUpdated
The exchange rate of trading pair was set/updated with value from source.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| data_source | `DataSource` | ```Bytes```
| trading_pair | `TradingPairString` | ```Bytes```
| exchange_rate | `ExchangeRate` | ```{'bits': 'u64'}```

---------
### OracleUpdated
a generic named oracle has updated its data blob
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| oracle_data_name | `OracleDataName` | ```Bytes```
| data_source | `DataSource` | ```Bytes```

---------
### RemovedFromWhitelist
an oracle fingerprint has been removed from the whitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| data_source | `DataSource` | ```Bytes```
| enclave_fingerprint | `EnclaveFingerprint` | ```scale_info::12```

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
['scale_info::12']
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
data source string too long

---------
### FingerprintAlreadyWhitelisted
enclave fingerprint already whitelisted for this data source.

---------
### FingerprintNotWhitelisted
calling enclave fingerprint not whitelisted for this data source.

---------
### FingerprintWhitelistOverflow
Too many enclave fingerprints in the whitelist for this data source.

---------
### OracleBlobTooBig
generic oracle blob too big

---------
### OracleDataNameStringTooLong
generic oracle data name string too long

---------
### TradingPairStringTooLong
trading pair string too long

---------