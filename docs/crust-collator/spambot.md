
# Spambot

---------
## Calls

---------
### ping
#### Attributes
| Name | Type |
| -------- | -------- | 
| seq | `u32` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'ping', {'payload': 'Bytes', 'seq': 'u32'}
)
```

---------
### pong
#### Attributes
| Name | Type |
| -------- | -------- | 
| seq | `u32` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'pong', {'payload': 'Bytes', 'seq': 'u32'}
)
```

---------
### start
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'start', {'para': 'u32', 'payload': 'Bytes'}
)
```

---------
### start_many
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| count | `u32` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'start_many', {
    'count': 'u32',
    'para': 'u32',
    'payload': 'Bytes',
}
)
```

---------
### stop
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'stop', {'para': 'u32'}
)
```

---------
### stop_all
#### Attributes
| Name | Type |
| -------- | -------- | 
| maybe_para | `Option<ParaId>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'stop_all', {'maybe_para': (None, 'u32')}
)
```

---------
## Events

---------
### ErrorSendingPing
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SendError` | ```{'CannotReachDestination': ({'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::49', 'scale_info::49'), 'X3': ('scale_info::49', 'scale_info::49', 'scale_info::49'), 'X4': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49'), 'X5': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49'), 'X6': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49'), 'X7': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49'), 'X8': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49')}}, [{'WithdrawAsset': ['scale_info::63'], 'ReserveAssetDeposited': ['scale_info::63'], 'ReceiveTeleportedAsset': ['scale_info::63'], 'QueryResponse': 'InnerStruct', 'TransferAsset': 'InnerStruct', 'TransferReserveAsset': 'InnerStruct', 'Transact': 'InnerStruct', 'HrmpNewChannelOpenRequest': 'InnerStruct', 'HrmpChannelAccepted': 'InnerStruct', 'HrmpChannelClosing': 'InnerStruct', 'ClearOrigin': None, 'DescendOrigin': 'scale_info::48', 'ReportError': 'InnerStruct', 'DepositAsset': 'InnerStruct', 'DepositReserveAsset': 'InnerStruct', 'ExchangeAsset': 'InnerStruct', 'InitiateReserveWithdraw': 'InnerStruct', 'InitiateTeleport': 'InnerStruct', 'QueryHolding': 'InnerStruct', 'BuyExecution': 'InnerStruct', 'RefundSurplus': None, 'SetErrorHandler': ['scale_info::60'], 'SetAppendix': ['scale_info::60'], 'ClearError': None, 'ClaimAsset': 'InnerStruct', 'Trap': 'u64', 'SubscribeVersion': 'InnerStruct', 'UnsubscribeVersion': None}]), 'Transport': None, 'Unroutable': None, 'DestinationUnsupported': None, 'ExceedsMaxMessageSize': None}```
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### ErrorSendingPong
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SendError` | ```{'CannotReachDestination': ({'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::49', 'scale_info::49'), 'X3': ('scale_info::49', 'scale_info::49', 'scale_info::49'), 'X4': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49'), 'X5': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49'), 'X6': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49'), 'X7': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49'), 'X8': ('scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49', 'scale_info::49')}}, [{'WithdrawAsset': ['scale_info::63'], 'ReserveAssetDeposited': ['scale_info::63'], 'ReceiveTeleportedAsset': ['scale_info::63'], 'QueryResponse': 'InnerStruct', 'TransferAsset': 'InnerStruct', 'TransferReserveAsset': 'InnerStruct', 'Transact': 'InnerStruct', 'HrmpNewChannelOpenRequest': 'InnerStruct', 'HrmpChannelAccepted': 'InnerStruct', 'HrmpChannelClosing': 'InnerStruct', 'ClearOrigin': None, 'DescendOrigin': 'scale_info::48', 'ReportError': 'InnerStruct', 'DepositAsset': 'InnerStruct', 'DepositReserveAsset': 'InnerStruct', 'ExchangeAsset': 'InnerStruct', 'InitiateReserveWithdraw': 'InnerStruct', 'InitiateTeleport': 'InnerStruct', 'QueryHolding': 'InnerStruct', 'BuyExecution': 'InnerStruct', 'RefundSurplus': None, 'SetErrorHandler': ['scale_info::60'], 'SetAppendix': ['scale_info::60'], 'ClearError': None, 'ClaimAsset': 'InnerStruct', 'Trap': 'u64', 'SubscribeVersion': 'InnerStruct', 'UnsubscribeVersion': None}]), 'Transport': None, 'Unroutable': None, 'DestinationUnsupported': None, 'ExceedsMaxMessageSize': None}```
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### PingSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### Pinged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### PongSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### Ponged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```
| None | `T::BlockNumber` | ```u32```

---------
### UnknownPong
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### PingCount
 The total number of pings sent.

#### Python
```python
result = substrate.query(
    'Spambot', 'PingCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Pings
 The sent pings.

#### Python
```python
result = substrate.query(
    'Spambot', 'Pings', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### Targets
 The target parachains to ping.

#### Python
```python
result = substrate.query(
    'Spambot', 'Targets', []
)
```

#### Return value
```python
[('u32', 'Bytes')]
```
---------
## Errors

---------
### PayloadTooLarge
The payload provided is too large, limit is 1024 bytes.

---------
### TooManyTargets
Too many parachains have been added as a target.

---------