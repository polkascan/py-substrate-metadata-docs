
# RevenueIbc

---------
## Calls

---------
### add_allowed
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'add_allowed', {'asset': 'u128'}
)
```

---------
### add_disallowed
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'add_disallowed', {'asset': 'u128'}
)
```

---------
### remove_allowed
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'remove_allowed', {'asset': 'u128'}
)
```

---------
### remove_disallowed
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'remove_disallowed', {'asset': 'u128'}
)
```

---------
### set_address
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `BoundedVec<u8, T::MaxStringSizeAddress>` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'set_address', {'address': 'Bytes'}
)
```

---------
### set_allowed
#### Attributes
| Name | Type |
| -------- | -------- | 
| assets | `Vec<AssetIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'set_allowed', {'assets': ['u128']}
)
```

---------
### set_channel
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'set_channel', {'channel': 'u64'}
)
```

---------
### set_cvm_centauri_address
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| cvm_centauri | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'set_cvm_centauri_address', {
    'asset_id': 'u128',
    'cvm_centauri': 'u128',
}
)
```

---------
### set_cvm_osmo_address
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| cvm_osmo | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'set_cvm_osmo_address', {
    'asset_id': 'u128',
    'cvm_osmo': 'u128',
}
)
```

---------
### set_disallowed
#### Attributes
| Name | Type |
| -------- | -------- | 
| assets | `Vec<AssetIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'set_disallowed', {'assets': ['u128']}
)
```

---------
### set_memo
#### Attributes
| Name | Type |
| -------- | -------- | 
| memo | `BoundedVec<u8, T::MaxStringSizeMemo>` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'set_memo', {'memo': 'Bytes'}
)
```

---------
### set_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'set_period', {'period': 'u32'}
)
```

---------
### trigger_transfer
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'RevenueIbc', 'trigger_transfer', {}
)
```

---------
## Events

---------
### AddAllowed
#### Attributes
No attributes

---------
### AddDisallowed
#### Attributes
No attributes

---------
### CentauriAddressSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `BoundedVec<u8, T::MaxStringSizeAddress>` | ```Bytes```

---------
### CentauriChannelSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| channel | `u64` | ```u64```

---------
### CvmCentauriAddress
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetIdOf<T>` | ```u128```
| cvm_centauri | `u128` | ```u128```

---------
### CvmOsmoAddress
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetIdOf<T>` | ```u128```
| cvm_osmo | `u128` | ```u128```

---------
### IntermediateTransferFail
#### Attributes
No attributes

---------
### Memo
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| memo | `String` | ```Str```

---------
### MemoSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| memo | `BoundedVec<u8, T::MaxStringSizeMemo>` | ```Bytes```

---------
### PeriodSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| period | `T::BlockNumber` | ```u32```

---------
### RemoveAllowed
#### Attributes
No attributes

---------
### RemoveDisallowed
#### Attributes
No attributes

---------
### RevenueCalcutions
#### Attributes
No attributes

---------
### RevenueTransferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `BalanceOf<T>` | ```u128```
| asset_id | `AssetIdOf<T>` | ```u128```
| memo | `BoundedVec<u8, T::MaxStringSizeMemo>` | ```Bytes```

---------
### SetAllowed
#### Attributes
No attributes

---------
### SetDisallowed
#### Attributes
No attributes

---------
### SkipAsset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetIdOf<T>` | ```u128```

---------
### TransferFail
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetIdOf<T>` | ```u128```
| amount | `BalanceOf<T>` | ```u128```

---------
### TransferFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetIdOf<T>` | ```u128```
| amount | `BalanceOf<T>` | ```u128```

---------
### TransferSuccess
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetIdOf<T>` | ```u128```
| amount | `BalanceOf<T>` | ```u128```

---------
### TransferTriggered
#### Attributes
No attributes

---------
## Storage functions

---------
### AllowedAssets

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'AllowedAssets', ['u128']
)
```

#### Return value
```python
()
```
---------
### CentauriAddress

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'CentauriAddress', []
)
```

#### Return value
```python
'Bytes'
```
---------
### CentauriChannel

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'CentauriChannel', []
)
```

#### Return value
```python
'u64'
```
---------
### CvmCentauriAddress

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'CvmCentauriAddress', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### CvmOsmoAddress

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'CvmOsmoAddress', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### DisallowedAssets

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'DisallowedAssets', ['u128']
)
```

#### Return value
```python
()
```
---------
### ForwardMemo

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'ForwardMemo', []
)
```

#### Return value
```python
'Bytes'
```
---------
### Period

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'Period', []
)
```

#### Return value
```python
'u32'
```
---------
### TokenPrevPeriodBalance

#### Python
```python
result = substrate.query(
    'RevenueIbc', 'TokenPrevPeriodBalance', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### FeeAccount
#### Value
```python
'5xMXcPsD9B9xDMvLyNBLmn9uhK7sTXTfubGVTZmXwVJmTVWa'
```
#### Python
```python
constant = substrate.get_constant('RevenueIbc', 'FeeAccount')
```
---------
### IntermediatePalletId
#### Value
```python
'0x726576656e696263'
```
#### Python
```python
constant = substrate.get_constant('RevenueIbc', 'IntermediatePalletId')
```
---------
### MaxStringSizeAddress
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('RevenueIbc', 'MaxStringSizeAddress')
```
---------
### MaxStringSizeMemo
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('RevenueIbc', 'MaxStringSizeMemo')
```
---------
## Errors

---------
### CentauriAddressNotSet

---------
### ChannelNotSet

---------