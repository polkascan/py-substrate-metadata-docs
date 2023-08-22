
# PalletMultihopXcmIbc

---------
## Calls

---------
### add_route
#### Attributes
| Name | Type |
| -------- | -------- | 
| route_id | `u128` | 
| route | `RouteBoundedVec<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PalletMultihopXcmIbc', 'add_route', {
    'route': [
        (
            {
                'chain_hop': (
                    'SubstrateIbc',
                    'CosmosIbc',
                    'Xcm',
                ),
                'chain_id': 'u32',
                'channel_id': 'u64',
                'height': (
                    None,
                    'u64',
                ),
                'order': 'u8',
                'para_id': (
                    None,
                    'u32',
                ),
                'retries': (
                    None,
                    'u8',
                ),
                'timeout': (
                    None,
                    'u64',
                ),
                'timestamp': (
                    None,
                    'u64',
                ),
            },
            'Bytes',
        ),
    ],
    'route_id': 'u128',
}
)
```

---------
## Events

---------
### FailedCallback
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin_address | `[u8; 32]` | ```[u8; 32]```
| route_id | `u128` | ```u128```
| reason | `MultihopEventReason` | ```('FailedToConvertAddressToBytes', 'XcmTransferInitiated', 'IncorrectPalletId', 'MultiHopRouteDoesNotExist', 'MultiHopRouteExistButNotConfigured', 'IncorrectCountOfAddresses', 'FailedToDeriveCosmosAddressFromBytes', 'FailedToDeriveChainNameFromUtf8', 'FailedToEncodeBech32Address', 'FailedToDecodeDestAccountId', 'FailedToDecodeSenderAccountId', 'DoesNotSupportNonFungible', 'FailedCreateMemo', 'FailedToConvertMemoIntoPalletIbcMemoMessageType')```

---------
### FailedMatchLocation
#### Attributes
No attributes

---------
### FailedXcmToIbc
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin_address | `T::AccountId` | ```AccountId```
| to | `[u8; 32]` | ```[u8; 32]```
| amount | `u128` | ```u128```
| asset_id | `T::AssetId` | ```u128```
| memo | `Option<T::MemoMessage>` | ```(None, 'Str')```

---------
### MultihopXcmMemo
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reason | `MultihopEventReason` | ```('FailedToConvertAddressToBytes', 'XcmTransferInitiated', 'IncorrectPalletId', 'MultiHopRouteDoesNotExist', 'MultiHopRouteExistButNotConfigured', 'IncorrectCountOfAddresses', 'FailedToDeriveCosmosAddressFromBytes', 'FailedToDeriveChainNameFromUtf8', 'FailedToEncodeBech32Address', 'FailedToDecodeDestAccountId', 'FailedToDecodeSenderAccountId', 'DoesNotSupportNonFungible', 'FailedCreateMemo', 'FailedToConvertMemoIntoPalletIbcMemoMessageType')```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `u128` | ```u128```
| asset_id | `u128` | ```u128```
| is_error | `bool` | ```bool```

---------
### SuccessXcmToIbc
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin_address | `T::AccountId` | ```AccountId```
| to | `[u8; 32]` | ```[u8; 32]```
| amount | `u128` | ```u128```
| asset_id | `T::AssetId` | ```u128```
| memo | `Option<T::MemoMessage>` | ```(None, 'Str')```

---------
## Storage functions

---------
### RouteIdToRoutePath

#### Python
```python
result = substrate.query(
    'PalletMultihopXcmIbc', 'RouteIdToRoutePath', ['u128']
)
```

#### Return value
```python
[
    (
        {
            'chain_hop': ('SubstrateIbc', 'CosmosIbc', 'Xcm'),
            'chain_id': 'u32',
            'channel_id': 'u64',
            'height': (None, 'u64'),
            'order': 'u8',
            'para_id': (None, 'u32'),
            'retries': (None, 'u8'),
            'timeout': (None, 'u64'),
            'timestamp': (None, 'u64'),
        },
        'Bytes',
    ),
]
```
---------
## Constants

---------
### ChainNameVecLimit
 The maximum length of chain name
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('PalletMultihopXcmIbc', 'ChainNameVecLimit')
```
---------
### MaxMultihopCount
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('PalletMultihopXcmIbc', 'MaxMultihopCount')
```
---------
### PalletInstanceId
#### Value
```python
192
```
#### Python
```python
constant = substrate.get_constant('PalletMultihopXcmIbc', 'PalletInstanceId')
```
---------
## Errors

---------
### DoesNotSupportNonFungible

---------
### FailedToConstructMemo

---------
### FailedToDecodeAccountId

---------
### FailedToEncodeBech32Address

---------
### IncorrectAddress

---------
### IncorrectChainName

---------
### IncorrectCountOfAddresses

---------
### IncorrectMultiLocation

---------
### MultiHopRouteDoesNotExist

---------
### XcmDepositFailed

---------