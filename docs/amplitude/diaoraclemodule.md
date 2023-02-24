
# DiaOracleModule

---------
## Calls

---------
### add_currency
#### Attributes
| Name | Type |
| -------- | -------- | 
| blockchain | `Vec<u8>` | 
| symbol | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'DiaOracleModule', 'add_currency', {
    'blockchain': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### authorize_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DiaOracleModule', 'authorize_account', {'account_id': 'AccountId'}
)
```

---------
### deauthorize_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DiaOracleModule', 'deauthorize_account', {'account_id': 'AccountId'}
)
```

---------
### remove_currency
#### Attributes
| Name | Type |
| -------- | -------- | 
| blockchain | `Vec<u8>` | 
| symbol | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'DiaOracleModule', 'remove_currency', {
    'blockchain': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### set_batching_api
#### Attributes
| Name | Type |
| -------- | -------- | 
| api | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'DiaOracleModule', 'set_batching_api', {'api': 'Bytes'}
)
```

---------
### set_updated_coin_infos
#### Attributes
| Name | Type |
| -------- | -------- | 
| coin_infos | `Vec<((Vec<u8>, Vec<u8>), CoinInfo)>` | 

#### Python
```python
call = substrate.compose_call(
    'DiaOracleModule', 'set_updated_coin_infos', {
    'coin_infos': [
        (
            ('Bytes', 'Bytes'),
            {
                'blockchain': 'Bytes',
                'last_update_timestamp': 'u64',
                'name': 'Bytes',
                'price': 'u128',
                'supply': 'u128',
                'symbol': 'Bytes',
            },
        ),
    ],
}
)
```

---------
## Events

---------
### AccountIdAuthorized
Event is triggered when account is authorized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### AccountIdDeauthorized
Event is triggered when account is deauthorized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### BatchingApiRouteSet
Event is triggered when batching api route is set from the list
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

---------
### CurrencyAdded
Event is triggered when currency is added to the list
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```

---------
### CurrencyRemoved
Event is triggered when currency is remove from the list
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```

---------
### UpdatedPrices
Event is triggered when prices are updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<((Vec<u8>, Vec<u8>), CoinInfo)>` | ```[(('Bytes', 'Bytes'), {'symbol': 'Bytes', 'name': 'Bytes', 'blockchain': 'Bytes', 'supply': 'u128', 'last_update_timestamp': 'u64', 'price': 'u128'})]```

---------
## Storage functions

---------
### AuthorizedAccounts
 List of all authorized accounts

#### Python
```python
result = substrate.query(
    'DiaOracleModule', 'AuthorizedAccounts', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### BatchingApi

#### Python
```python
result = substrate.query(
    'DiaOracleModule', 'BatchingApi', []
)
```

#### Return value
```python
'Bytes'
```
---------
### CoinInfosMap
 Map of all the coins names to their respective info and price

#### Python
```python
result = substrate.query(
    'DiaOracleModule', 'CoinInfosMap', [
    {
        'blockchain': 'Bytes',
        'symbol': 'Bytes',
    },
]
)
```

#### Return value
```python
{
    'blockchain': 'Bytes',
    'last_update_timestamp': 'u64',
    'name': 'Bytes',
    'price': 'u128',
    'supply': 'u128',
    'symbol': 'Bytes',
}
```
---------
### SupportedCurrencies
 List of all supported currencies

#### Python
```python
result = substrate.query(
    'DiaOracleModule', 'SupportedCurrencies', [
    {
        'blockchain': 'Bytes',
        'symbol': 'Bytes',
    },
]
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### BadOrigin
BadOrigin

---------
### DeserializeError
Failed Deserializing

---------
### DeserializeStrError
Failed Deserializing to str

---------
### FailedSignedTransaction
Failed to send signed Transaction

---------
### HttpRequestFailed
Http request to Batching Server Failed

---------
### HttpRequestSendFailed
Sending Http request to Batching Server Failed

---------
### NoBatchingApiEndPoint
Batching Api Endpoint not set.

---------
### NoCoinInfoAvailable
Error is returned if no information is available about given coin

---------
### ThisAccountIdIsNotAuthorized
AccountId is not authorized

---------
### UserUnableToDeauthorizeThemself
User cannot deauthorized themself

---------