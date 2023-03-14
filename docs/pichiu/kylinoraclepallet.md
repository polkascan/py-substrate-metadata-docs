
# KylinOraclePallet

---------
## Calls

---------
### clear_api
#### Attributes
| Name | Type |
| -------- | -------- | 
| key | `T::OracleKey` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'clear_api', {'key': 'Bytes'}
)
```

---------
### feed_data
Feed the external value.

Require authorized operator.
#### Attributes
| Name | Type |
| -------- | -------- | 
| values | `Vec<(T::OracleKey, T::OracleValue)>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'feed_data', {'values': [('Bytes', 'i64')]}
)
```

---------
### submit_api
#### Attributes
| Name | Type |
| -------- | -------- | 
| key | `T::OracleKey` | 
| url | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'submit_api', {'key': 'Bytes', 'url': 'Bytes'}
)
```

---------
### xcm_evt
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'xcm_evt', {}
)
```

---------
### xcm_evt1
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'xcm_evt1', {}
)
```

---------
### xcm_feed_data
#### Attributes
| Name | Type |
| -------- | -------- | 
| values | `Vec<(T::OracleKey, T::OracleValue)>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'xcm_feed_data', {'values': [('Bytes', 'i64')]}
)
```

---------
### xcm_query_data
#### Attributes
| Name | Type |
| -------- | -------- | 
| key | `T::OracleKey` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'xcm_query_data', {'key': 'Bytes'}
)
```

---------
## Events

---------
### ApiFeedRemoved
Apifeed is removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| key | `T::OracleKey` | ```Bytes```
| feed | `ApiFeed<T::BlockNumber>` | ```{'requested_block_number': 'u32', 'url': (None, 'Bytes')}```

---------
### FeedDataError
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SendError` | ```{'CannotReachDestination': ({'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::55', 'scale_info::55'), 'X3': ('scale_info::55', 'scale_info::55', 'scale_info::55'), 'X4': ('scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55'), 'X5': ('scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55'), 'X6': ('scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55'), 'X7': ('scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55'), 'X8': ('scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55', 'scale_info::55')}}, [{'WithdrawAsset': ['scale_info::69'], 'ReserveAssetDeposited': ['scale_info::69'], 'ReceiveTeleportedAsset': ['scale_info::69'], 'QueryResponse': 'InnerStruct', 'TransferAsset': 'InnerStruct', 'TransferReserveAsset': 'InnerStruct', 'Transact': 'InnerStruct', 'HrmpNewChannelOpenRequest': 'InnerStruct', 'HrmpChannelAccepted': 'InnerStruct', 'HrmpChannelClosing': 'InnerStruct', 'ClearOrigin': None, 'DescendOrigin': 'scale_info::54', 'ReportError': 'InnerStruct', 'DepositAsset': 'InnerStruct', 'DepositReserveAsset': 'InnerStruct', 'ExchangeAsset': 'InnerStruct', 'InitiateReserveWithdraw': 'InnerStruct', 'InitiateTeleport': 'InnerStruct', 'QueryHolding': 'InnerStruct', 'BuyExecution': 'InnerStruct', 'RefundSurplus': None, 'SetErrorHandler': ['scale_info::66'], 'SetAppendix': ['scale_info::66'], 'ClearError': None, 'ClaimAsset': 'InnerStruct', 'Trap': 'u64', 'SubscribeVersion': 'InnerStruct', 'UnsubscribeVersion': None}]), 'Transport': None, 'Unroutable': None, 'DestinationUnsupported': None, 'ExceedsMaxMessageSize': None}```
| None | `ParaId` | ```u32```

---------
### FeedDataSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### NewApiFeed
New feed is submitted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| key | `T::OracleKey` | ```Bytes```
| feed | `ApiFeed<T::BlockNumber>` | ```{'requested_block_number': 'u32', 'url': (None, 'Bytes')}```

---------
### NewFeedData
New feed data is submitted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| values | `Vec<(T::OracleKey, T::OracleValue)>` | ```[('Bytes', 'i64')]```

---------
### NewParaEvt
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```

---------
### NewParaEvt1
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```

---------
### NewParaFeedData
New feed data is submitted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```
| values | `Vec<(T::OracleKey, T::OracleValue)>` | ```[('Bytes', 'i64')]```

---------
## Storage functions

---------
### ApiFeeds

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'ApiFeeds', ['AccountId', 'Bytes']
)
```

#### Return value
```python
{'requested_block_number': 'u32', 'url': (None, 'Bytes')}
```
---------
### HasDispatched
 If an oracle operator has fed a value in this block

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'HasDispatched', []
)
```

#### Return value
```python
['AccountId']
```
---------
### NextUnsignedAt

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'NextUnsignedAt', []
)
```

#### Return value
```python
'u32'
```
---------
### PRawValues

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'PRawValues', ['u32', 'Bytes']
)
```

#### Return value
```python
{'timestamp': 'u128', 'value': 'i64'}
```
---------
### RawValues
 Raw values for each oracle operators

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'RawValues', ['AccountId', 'Bytes']
)
```

#### Return value
```python
{'timestamp': 'u128', 'value': 'i64'}
```
---------
### SystemRunnig

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'SystemRunnig', []
)
```

#### Return value
```python
'bool'
```
---------
### Values
 Up to date combined value from Raw Values

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'Values', ['Bytes']
)
```

#### Return value
```python
{'timestamp': 'u128', 'value': 'i64'}
```
---------
## Constants

---------
### MaxHasDispatchedSize
 Maximum size of HasDispatched
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('KylinOraclePallet', 'MaxHasDispatchedSize')
```
---------
### UnsignedPriority
 A configuration for base priority of unsigned transactions.

 This is exposed so that it can be tuned for particular runtime, when
 multiple pallets send unsigned transactions.
#### Value
```python
1048576
```
#### Python
```python
constant = substrate.get_constant('KylinOraclePallet', 'UnsignedPriority')
```
---------
## Errors

---------
### AlreadyFeeded
Feeder has already feeded at this block

---------
### NoPermission
Sender does not have permission

---------
### TooLarge
DataRequest Fields is too large to store on-chain.

---------