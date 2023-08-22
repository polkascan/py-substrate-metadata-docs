
# Oracle

---------
## Calls

---------
### set_max_delay
Set the maximum delay (in milliseconds) for a reported value to be used

\# Arguments
* `new_max_delay` - new max delay in milliseconds
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_max_delay | `T::Moment` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'set_max_delay', {'new_max_delay': 'u64'}
)
```

---------
### update_oracle_keys
set oracle keys

\# Arguments
* `oracle_key` - list of oracle keys
#### Attributes
| Name | Type |
| -------- | -------- | 
| oracle_keys | `Vec<OracleKey>` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'update_oracle_keys', {
    'oracle_keys': [
        {
            'ExchangeRate': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': {
                        'code': '[u8; 12]',
                        'issuer': '[u8; 32]',
                    },
                    'AlphaNum4': {
                        'code': '[u8; 4]',
                        'issuer': '[u8; 32]',
                    },
                    'StellarNative': None,
                },
                'XCM': 'u8',
                'ZenlinkLPToken': (
                    'u8',
                    'u8',
                    'u8',
                    'u8',
                ),
            },
        },
    ],
}
)
```

---------
## Events

---------
### AggregateUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| values | `Vec<(OracleKey, T::UnsignedFixedPoint)>` | ```[({'ExchangeRate': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': 'InnerStruct', 'AlphaNum12': 'InnerStruct'}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}, 'u128')]```

---------
### MaxDelayUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| max_delay | `T::Moment` | ```u64```

---------
### OracleKeysUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| oracle_keys | `Vec<OracleKey>` | ```[{'ExchangeRate': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}]```

---------
## Storage functions

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
### OracleKeys

#### Python
```python
result = substrate.query(
    'Oracle', 'OracleKeys', []
)
```

#### Return value
```python
[
    {
        'ExchangeRate': {
            'Native': None,
            'Stellar': {
                'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'},
                'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'},
                'StellarNative': None,
            },
            'XCM': 'u8',
            'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
        },
    },
]
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