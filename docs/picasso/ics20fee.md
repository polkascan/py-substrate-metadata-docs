
# Ics20Fee

---------
## Calls

---------
### add_channels_to_feeless_channel_list
#### Attributes
| Name | Type |
| -------- | -------- | 
| source_channel | `u64` | 
| destination_channel | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Ics20Fee', 'add_channels_to_feeless_channel_list', {
    'destination_channel': 'u64',
    'source_channel': 'u64',
}
)
```

---------
### remove_channels_from_feeless_channel_list
#### Attributes
| Name | Type |
| -------- | -------- | 
| source_channel | `u64` | 
| destination_channel | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Ics20Fee', 'remove_channels_from_feeless_channel_list', {
    'destination_channel': 'u64',
    'source_channel': 'u64',
}
)
```

---------
### set_charge
#### Attributes
| Name | Type |
| -------- | -------- | 
| charge | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Ics20Fee', 'set_charge', {'charge': 'u32'}
)
```

---------
## Events

---------
### FeeLessChannelIdsAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| source_channel | `u64` | ```u64```
| destination_channel | `u64` | ```u64```

---------
### FeeLessChannelIdsRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| source_channel | `u64` | ```u64```
| destination_channel | `u64` | ```u64```

---------
### IbcTransferFeeCollected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `T::Balance` | ```u128```
| asset_id | `T::AssetId` | ```u128```

---------
## Storage functions

---------
### FeeLessChannelIds
 storage map. key is tuple of (source_channel.sequence(), destination_channel.sequence()) and
 value () that means that this group of channels is feeless

#### Python
```python
result = substrate.query(
    'Ics20Fee', 'FeeLessChannelIds', [('u64', 'u64')]
)
```

#### Return value
```python
()
```
---------
### ServiceChargeIn

#### Python
```python
result = substrate.query(
    'Ics20Fee', 'ServiceChargeIn', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x6963733230666565'
```
#### Python
```python
constant = substrate.get_constant('Ics20Fee', 'PalletId')
```
---------
### ServiceChargeIn
 `ServiceChargeIn` represents the service charge rate applied to assets upon receipt via
 IBC.

 The charge is applied when assets are delivered to the receiving side, on
 deliver(before to mint, send assets to destination account) extrinsic using the
 Inter-Blockchain Communication (IBC) protocol.

 For example, if the service charge rate for incoming assets is 0.04%, `ServiceChargeIn`
 will be configured in rutime as
 parameter_types! { pub IbcIcs20ServiceChargeIn: Perbill = Perbill::from_rational(4_u32,
 1000_u32 ) };
#### Value
```python
4000000
```
#### Python
```python
constant = substrate.get_constant('Ics20Fee', 'ServiceChargeIn')
```
---------