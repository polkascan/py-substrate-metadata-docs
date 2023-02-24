
# KylinOraclePallet

---------
## Calls

---------
### clear_api_queue_unsigned
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_number | `T::BlockNumber` | 
| processed_requests | `Vec<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'clear_api_queue_unsigned', {
    'block_number': 'u32',
    'processed_requests': ['u64'],
}
)
```

---------
### clear_processed_requests_unsigned
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_number | `T::BlockNumber` | 
| processed_requests | `Vec<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'clear_processed_requests_unsigned', {
    'block_number': 'u32',
    'processed_requests': ['u64'],
}
)
```

---------
### query_data
#### Attributes
| Name | Type |
| -------- | -------- | 
| para_id | `Option<ParaId>` | 
| feed_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'query_data', {
    'feed_name': 'Bytes',
    'para_id': (None, 'u32'),
}
)
```

---------
### receive_response_from_parachain
#### Attributes
| Name | Type |
| -------- | -------- | 
| feed_name | `Vec<u8>` | 
| response | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'receive_response_from_parachain', {
    'feed_name': 'Bytes',
    'response': 'Bytes',
}
)
```

---------
### submit_data_signed
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_number | `T::BlockNumber` | 
| key | `u64` | 
| data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'submit_data_signed', {
    'block_number': 'u32',
    'data': 'Bytes',
    'key': 'u64',
}
)
```

---------
### submit_data_unsigned
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_number | `T::BlockNumber` | 
| key | `u64` | 
| data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'submit_data_unsigned', {
    'block_number': 'u32',
    'data': 'Bytes',
    'key': 'u64',
}
)
```

---------
### submit_data_via_api
#### Attributes
| Name | Type |
| -------- | -------- | 
| para_id | `Option<ParaId>` | 
| url | `Vec<u8>` | 
| feed_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'submit_data_via_api', {
    'feed_name': 'Bytes',
    'para_id': (None, 'u32'),
    'url': 'Bytes',
}
)
```

---------
### submit_price_feed
#### Attributes
| Name | Type |
| -------- | -------- | 
| para_id | `Option<ParaId>` | 
| requested_currencies | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'submit_price_feed', {
    'para_id': (None, 'u32'),
    'requested_currencies': 'Bytes',
}
)
```

---------
### sudo_remove_feed_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| feed_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'sudo_remove_feed_account', {'feed_name': 'Bytes'}
)
```

---------
### write_data_onchain
#### Attributes
| Name | Type |
| -------- | -------- | 
| feed_name | `Vec<u8>` | 
| data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'write_data_onchain', {
    'data': 'Bytes',
    'feed_name': 'Bytes',
}
)
```

---------
### xcm_submit_data_via_api
#### Attributes
| Name | Type |
| -------- | -------- | 
| url | `Vec<u8>` | 
| feed_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinOraclePallet', 'xcm_submit_data_via_api', {'feed_name': 'Bytes', 'url': 'Bytes'}
)
```

---------
## Events

---------
### ErrorSendingResponse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SendError` | ```{'CannotReachDestination': ({'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::54', 'scale_info::54'), 'X3': ('scale_info::54', 'scale_info::54', 'scale_info::54'), 'X4': ('scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54'), 'X5': ('scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54'), 'X6': ('scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54'), 'X7': ('scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54'), 'X8': ('scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54', 'scale_info::54')}}, [{'WithdrawAsset': ['scale_info::67'], 'ReserveAssetDeposited': ['scale_info::67'], 'ReceiveTeleportedAsset': ['scale_info::67'], 'QueryResponse': 'InnerStruct', 'TransferAsset': 'InnerStruct', 'TransferReserveAsset': 'InnerStruct', 'Transact': 'InnerStruct', 'HrmpNewChannelOpenRequest': 'InnerStruct', 'HrmpChannelAccepted': 'InnerStruct', 'HrmpChannelClosing': 'InnerStruct', 'ClearOrigin': None, 'DescendOrigin': 'scale_info::53', 'ReportError': 'InnerStruct', 'DepositAsset': 'InnerStruct', 'DepositReserveAsset': 'InnerStruct', 'ExchangeAsset': 'InnerStruct', 'InitiateReserveWithdraw': 'InnerStruct', 'InitiateTeleport': 'InnerStruct', 'QueryHolding': 'InnerStruct', 'BuyExecution': 'InnerStruct', 'RefundSurplus': None, 'SetErrorHandler': ['scale_info::64'], 'SetAppendix': ['scale_info::64'], 'ClearError': None, 'ClaimAsset': 'InnerStruct', 'Trap': 'u64', 'SubscribeVersion': 'InnerStruct', 'UnsubscribeVersion': None}]), 'Transport': None, 'Unroutable': None, 'DestinationUnsupported': None, 'ExceedsMaxMessageSize': None}```
| None | `ParaId` | ```u32```
| None | `DataRequest<ParaId, T::BlockNumber, T::AccountId>` | ```{'para_id': (None, 'u32'), 'account_id': (None, 'AccountId'), 'requested_block_number': 'u32', 'processed_block_number': (None, 'u32'), 'requested_timestamp': 'u128', 'processed_timestamp': (None, 'u128'), 'payload': 'Bytes', 'feed_name': 'Bytes', 'is_query': 'bool', 'url': (None, 'Bytes')}```

---------
### QueryFeeAwarded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `<<T as pallet::Config>::Currency as Currency<<T as frame_system::
Config>::AccountId,>>::Balance` | ```u128```
| None | `Vec<u8>` | ```Bytes```

---------
### ReadFromDWH
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<ParaId>` | ```(None, 'u32')```
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```
| None | `DataRequest<ParaId, T::BlockNumber, T::AccountId>` | ```{'para_id': (None, 'u32'), 'account_id': (None, 'AccountId'), 'requested_block_number': 'u32', 'processed_block_number': (None, 'u32'), 'requested_timestamp': 'u128', 'processed_timestamp': (None, 'u128'), 'payload': 'Bytes', 'feed_name': 'Bytes', 'is_query': 'bool', 'url': (None, 'Bytes')}```
| None | `T::BlockNumber` | ```u32```

---------
### RemovedFeedAccount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

---------
### ResponseReceived
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```
| None | `T::BlockNumber` | ```u32```

---------
### ResponseSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `DataRequest<ParaId, T::BlockNumber, T::AccountId>` | ```{'para_id': (None, 'u32'), 'account_id': (None, 'AccountId'), 'requested_block_number': 'u32', 'processed_block_number': (None, 'u32'), 'requested_timestamp': 'u128', 'processed_timestamp': (None, 'u128'), 'payload': 'Bytes', 'feed_name': 'Bytes', 'is_query': 'bool', 'url': (None, 'Bytes')}```
| None | `T::BlockNumber` | ```u32```

---------
### SavedToDWH
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<ParaId>` | ```(None, 'u32')```
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```
| None | `DataRequest<ParaId, T::BlockNumber, T::AccountId>` | ```{'para_id': (None, 'u32'), 'account_id': (None, 'AccountId'), 'requested_block_number': 'u32', 'processed_block_number': (None, 'u32'), 'requested_timestamp': 'u128', 'processed_timestamp': (None, 'u128'), 'payload': 'Bytes', 'feed_name': 'Bytes', 'is_query': 'bool', 'url': (None, 'Bytes')}```
| None | `T::BlockNumber` | ```u32```

---------
### SubmitNewData
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<ParaId>` | ```(None, 'u32')```
| None | `Vec<u8>` | ```Bytes```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```
| None | `Option<T::AccountId>` | ```(None, 'AccountId')```
| None | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### ApiQueue

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'ApiQueue', ['u64']
)
```

#### Return value
```python
{
    'account_id': (None, 'AccountId'),
    'feed_name': 'Bytes',
    'is_query': 'bool',
    'para_id': (None, 'u32'),
    'payload': 'Bytes',
    'processed_block_number': (None, 'u32'),
    'processed_timestamp': (None, 'u128'),
    'requested_block_number': 'u32',
    'requested_timestamp': 'u128',
    'url': (None, 'Bytes'),
}
```
---------
### DataId

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'DataId', []
)
```

#### Return value
```python
'u64'
```
---------
### DataRequests

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'DataRequests', ['u64']
)
```

#### Return value
```python
{
    'account_id': (None, 'AccountId'),
    'feed_name': 'Bytes',
    'is_query': 'bool',
    'para_id': (None, 'u32'),
    'payload': 'Bytes',
    'processed_block_number': (None, 'u32'),
    'processed_timestamp': (None, 'u128'),
    'requested_block_number': 'u32',
    'requested_timestamp': 'u128',
    'url': (None, 'Bytes'),
}
```
---------
### FeedAccountLookup

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'FeedAccountLookup', ['Bytes']
)
```

#### Return value
```python
('AccountId', 'Bytes')
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
### SavedRequests

#### Python
```python
result = substrate.query(
    'KylinOraclePallet', 'SavedRequests', ['u64']
)
```

#### Return value
```python
{
    'account_id': (None, 'AccountId'),
    'feed_name': 'Bytes',
    'is_query': 'bool',
    'para_id': (None, 'u32'),
    'payload': 'Bytes',
    'processed_block_number': (None, 'u32'),
    'processed_timestamp': (None, 'u128'),
    'requested_block_number': 'u32',
    'requested_timestamp': 'u128',
    'url': (None, 'Bytes'),
}
```
---------
## Constants

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
### TooLarge
DataRequest Fields is too large to store on-chain.

---------