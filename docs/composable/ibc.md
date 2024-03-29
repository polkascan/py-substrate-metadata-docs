
# Ibc

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
    'Ibc', 'add_channels_to_feeless_channel_list', {
    'destination_channel': 'u64',
    'source_channel': 'u64',
}
)
```

---------
### deliver
#### Attributes
| Name | Type |
| -------- | -------- | 
| messages | `Vec<Any>` | 

#### Python
```python
call = substrate.compose_call(
    'Ibc', 'deliver', {
    'messages': [
        {
            'type_url': 'Str',
            'value': 'Bytes',
        },
    ],
}
)
```

---------
### freeze_client
Freeze a client at a specific height
#### Attributes
| Name | Type |
| -------- | -------- | 
| client_id | `Vec<u8>` | 
| height | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Ibc', 'freeze_client', {
    'client_id': 'Bytes',
    'height': 'u64',
}
)
```

---------
### increase_counters
Increase all IBC counters by 1. Used only in testing to ensure that
relayer uses proper proper values for source/sink chains.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Ibc', 'increase_counters', {}
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
    'Ibc', 'remove_channels_from_feeless_channel_list', {
    'destination_channel': 'u64',
    'source_channel': 'u64',
}
)
```

---------
### set_child_storage
#### Attributes
| Name | Type |
| -------- | -------- | 
| key | `Vec<u8>` | 
| value | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Ibc', 'set_child_storage', {'key': 'Bytes', 'value': 'Bytes'}
)
```

---------
### substitute_client_state
#### Attributes
| Name | Type |
| -------- | -------- | 
| client_id | `String` | 
| height | `Height` | 
| client_state_bytes | `Vec<u8>` | 
| consensus_state_bytes | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Ibc', 'substitute_client_state', {
    'client_id': 'Str',
    'client_state_bytes': 'Bytes',
    'consensus_state_bytes': 'Bytes',
    'height': {
        'revision_height': 'u64',
        'revision_number': 'u64',
    },
}
)
```

---------
### transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `TransferParams<<T as frame_system::Config>::AccountId>` | 
| asset_id | `T::AssetId` | 
| amount | `T::Balance` | 
| memo | `Option<T::MemoMessage>` | 

#### Python
```python
call = substrate.compose_call(
    'Ibc', 'transfer', {
    'amount': 'u128',
    'asset_id': 'u128',
    'memo': (None, 'Str'),
    'params': {
        'source_channel': 'u64',
        'timeout': {
            'Absolute': {
                'height': (
                    None,
                    'u64',
                ),
                'timestamp': (
                    None,
                    'u64',
                ),
            },
            'Offset': {
                'height': (
                    None,
                    'u64',
                ),
                'timestamp': (
                    None,
                    'u64',
                ),
            },
        },
        'to': {
            'Id': 'AccountId',
            'Raw': 'Bytes',
        },
    },
}
)
```

---------
### upgrade_client
We write the consensus &amp; client state under these predefined paths so that
we can produce state proofs of the values to connected chains
in order to execute client upgrades.
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `UpgradeParams` | 

#### Python
```python
call = substrate.compose_call(
    'Ibc', 'upgrade_client', {
    'params': {
        'client_state': 'Bytes',
        'consensus_state': 'Bytes',
    },
}
)
```

---------
## Events

---------
### AssetAdminUpdated
Asset Admin Account Updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| admin_account | `<T as frame_system::Config>::AccountId` | ```AccountId```

---------
### ChannelOpened
A channel has been opened
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| channel_id | `Vec<u8>` | ```Bytes```
| port_id | `Vec<u8>` | ```Bytes```

---------
### ChargingFeeConfirmed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sequence | `u64` | ```u64```

---------
### ChargingFeeFailedAcknowledgement
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sequence | `u64` | ```u64```

---------
### ChargingFeeOnTransferInitiated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sequence | `u64` | ```u64```
| from | `Vec<u8>` | ```Bytes```
| to | `Vec<u8>` | ```Bytes```
| ibc_denom | `Vec<u8>` | ```Bytes```
| local_asset_id | `Option<T::AssetId>` | ```(None, 'u128')```
| amount | `T::Balance` | ```u128```
| is_flat_fee | `bool` | ```bool```
| source_channel | `Vec<u8>` | ```Bytes```
| destination_channel | `Vec<u8>` | ```Bytes```

---------
### ChargingFeeTimeout
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sequence | `u64` | ```u64```

---------
### ChildStateUpdated
#### Attributes
No attributes

---------
### ClientFrozen
Client has been frozen
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| client_id | `Vec<u8>` | ```Bytes```
| height | `u64` | ```u64```
| revision_number | `u64` | ```u64```

---------
### ClientStateSubstituted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| client_id | `String` | ```Str```
| height | `Height` | ```{'revision_number': 'u64', 'revision_height': 'u64'}```

---------
### ClientUpgradeSet
Client upgrade path has been set
#### Attributes
No attributes

---------
### Events
Events emitted by the ibc subsystem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| events | `Vec<Result<events::IbcEvent, errors::IbcError>>` | ```[{'Ok': {'NewBlock': {'revision_height': 'u64', 'revision_number': 'u64'}, 'CreateClient': {'client_id': 'Bytes', 'client_type': 'Bytes', 'revision_height': 'u64', 'revision_number': 'u64', 'consensus_height': 'u64', 'consensus_revision_number': 'u64'}, 'UpdateClient': {'client_id': 'Bytes', 'client_type': 'Bytes', 'revision_height': 'u64', 'revision_number': 'u64', 'consensus_height': 'u64', 'consensus_revision_number': 'u64'}, 'UpgradeClient': {'client_id': 'Bytes', 'client_type': 'Bytes', 'revision_height': 'u64', 'revision_number': 'u64', 'consensus_height': 'u64', 'consensus_revision_number': 'u64'}, 'ClientMisbehaviour': {'client_id': 'Bytes', 'client_type': 'Bytes', 'revision_height': 'u64', 'revision_number': 'u64', 'consensus_height': 'u64', 'consensus_revision_number': 'u64'}, 'OpenInitConnection': {'revision_height': 'u64', 'revision_number': 'u64', 'connection_id': (None, 'Bytes'), 'client_id': 'Bytes', 'counterparty_connection_id': (None, 'Bytes'), 'counterparty_client_id': 'Bytes'}, 'OpenConfirmConnection': {'revision_height': 'u64', 'revision_number': 'u64', 'connection_id': (None, 'Bytes'), 'client_id': 'Bytes', 'counterparty_connection_id': (None, 'Bytes'), 'counterparty_client_id': 'Bytes'}, 'OpenTryConnection': {'revision_height': 'u64', 'revision_number': 'u64', 'connection_id': (None, 'Bytes'), 'client_id': 'Bytes', 'counterparty_connection_id': (None, 'Bytes'), 'counterparty_client_id': 'Bytes'}, 'OpenAckConnection': {'revision_height': 'u64', 'revision_number': 'u64', 'connection_id': (None, 'Bytes'), 'client_id': 'Bytes', 'counterparty_connection_id': (None, 'Bytes'), 'counterparty_client_id': 'Bytes'}, 'OpenInitChannel': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': (None, 'Bytes'), 'connection_id': 'Bytes', 'counterparty_port_id': 'Bytes', 'counterparty_channel_id': (None, 'Bytes')}, 'OpenConfirmChannel': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': (None, 'Bytes'), 'connection_id': 'Bytes', 'counterparty_port_id': 'Bytes', 'counterparty_channel_id': (None, 'Bytes')}, 'OpenTryChannel': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': (None, 'Bytes'), 'connection_id': 'Bytes', 'counterparty_port_id': 'Bytes', 'counterparty_channel_id': (None, 'Bytes')}, 'OpenAckChannel': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': (None, 'Bytes'), 'connection_id': 'Bytes', 'counterparty_port_id': 'Bytes', 'counterparty_channel_id': (None, 'Bytes')}, 'CloseInitChannel': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': 'Bytes', 'connection_id': 'Bytes', 'counterparty_port_id': 'Bytes', 'counterparty_channel_id': (None, 'Bytes')}, 'CloseConfirmChannel': {'revision_height': 'u64', 'revision_number': 'u64', 'channel_id': (None, 'Bytes'), 'port_id': 'Bytes', 'connection_id': 'Bytes', 'counterparty_port_id': 'Bytes', 'counterparty_channel_id': (None, 'Bytes')}, 'ReceivePacket': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': 'Bytes', 'dest_port': 'Bytes', 'dest_channel': 'Bytes', 'sequence': 'u64'}, 'SendPacket': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': 'Bytes', 'dest_port': 'Bytes', 'dest_channel': 'Bytes', 'sequence': 'u64'}, 'AcknowledgePacket': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': 'Bytes', 'sequence': 'u64'}, 'WriteAcknowledgement': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': 'Bytes', 'dest_port': 'Bytes', 'dest_channel': 'Bytes', 'sequence': 'u64'}, 'TimeoutPacket': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': 'Bytes', 'sequence': 'u64'}, 'TimeoutOnClosePacket': {'revision_height': 'u64', 'revision_number': 'u64', 'port_id': 'Bytes', 'channel_id': 'Bytes', 'sequence': 'u64'}, 'Empty': None, 'ChainError': None, 'AppModule': {'kind': 'Bytes', 'module_id': 'Bytes'}, 'PushWasmCode': {'wasm_code_id': 'Bytes'}}, 'Err': {'Ics02Client': {'message': 'Bytes'}, 'Ics03Connection': {'message': 'Bytes'}, 'Ics04Channel': {'message': 'Bytes'}, 'Ics20FungibleTokenTransfer': {'message': 'Bytes'}, 'UnknownMessageTypeUrl': {'message': 'Bytes'}, 'MalformedMessageBytes': {'message': 'Bytes'}}}]```

---------
### ExecuteMemoIbcTokenTransferFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `Vec<u8>` | ```Bytes```
| asset_id | `T::AssetId` | ```u128```
| amount | `T::Balance` | ```u128```
| channel | `u64` | ```u64```
| next_memo | `Option<T::MemoMessage>` | ```(None, 'Str')```

---------
### ExecuteMemoIbcTokenTransferFailedWithReason
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| memo | `String` | ```Str```
| reason | `u8` | ```u8```

---------
### ExecuteMemoIbcTokenTransferSuccess
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `Vec<u8>` | ```Bytes```
| asset_id | `T::AssetId` | ```u128```
| amount | `T::Balance` | ```u128```
| channel | `u64` | ```u64```
| next_memo | `Option<T::MemoMessage>` | ```(None, 'Str')```

---------
### ExecuteMemoStarted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| memo | `Option<String>` | ```(None, 'Str')```

---------
### ExecuteMemoXcmFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `u128` | ```u128```
| asset_id | `T::AssetId` | ```u128```
| para_id | `Option<u32>` | ```(None, 'u32')```

---------
### ExecuteMemoXcmSuccess
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `u128` | ```u128```
| asset_id | `T::AssetId` | ```u128```
| para_id | `Option<u32>` | ```(None, 'u32')```

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
### OnRecvPacketError
On recv packet was not processed successfully processes
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msg | `Vec<u8>` | ```Bytes```

---------
### ParamsUpdated
Pallet params updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| send_enabled | `bool` | ```bool```
| receive_enabled | `bool` | ```bool```

---------
### TokenReceived
Ibc tokens have been received and minted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `Signer` | ```Str```
| to | `Signer` | ```Str```
| ibc_denom | `Vec<u8>` | ```Bytes```
| local_asset_id | `Option<T::AssetId>` | ```(None, 'u128')```
| amount | `T::Balance` | ```u128```
| is_receiver_source | `bool` | ```bool```
| source_channel | `Vec<u8>` | ```Bytes```
| destination_channel | `Vec<u8>` | ```Bytes```

---------
### TokenTransferCompleted
An outgoing Ibc token transfer has been completed and burnt
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `Signer` | ```Str```
| to | `Signer` | ```Str```
| ibc_denom | `Vec<u8>` | ```Bytes```
| local_asset_id | `Option<T::AssetId>` | ```(None, 'u128')```
| amount | `T::Balance` | ```u128```
| is_sender_source | `bool` | ```bool```
| source_channel | `Vec<u8>` | ```Bytes```
| destination_channel | `Vec<u8>` | ```Bytes```

---------
### TokenTransferFailed
Ibc transfer failed, received an acknowledgement error, tokens have been refunded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `Signer` | ```Str```
| to | `Signer` | ```Str```
| ibc_denom | `Vec<u8>` | ```Bytes```
| local_asset_id | `Option<T::AssetId>` | ```(None, 'u128')```
| amount | `T::Balance` | ```u128```
| is_sender_source | `bool` | ```bool```
| source_channel | `Vec<u8>` | ```Bytes```
| destination_channel | `Vec<u8>` | ```Bytes```

---------
### TokenTransferInitiated
An Ibc token transfer has been started
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `Vec<u8>` | ```Bytes```
| to | `Vec<u8>` | ```Bytes```
| ibc_denom | `Vec<u8>` | ```Bytes```
| local_asset_id | `Option<T::AssetId>` | ```(None, 'u128')```
| amount | `T::Balance` | ```u128```
| is_sender_source | `bool` | ```bool```
| source_channel | `Vec<u8>` | ```Bytes```
| destination_channel | `Vec<u8>` | ```Bytes```

---------
### TokenTransferTimeout
Happens when token transfer timeouts, tokens have been refunded. expected
`TokenTransferFailed` does not happen in this case.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `Signer` | ```Str```
| to | `Signer` | ```Str```
| ibc_denom | `Vec<u8>` | ```Bytes```
| local_asset_id | `Option<T::AssetId>` | ```(None, 'u128')```
| amount | `T::Balance` | ```u128```
| is_sender_source | `bool` | ```bool```
| source_channel | `Vec<u8>` | ```Bytes```
| destination_channel | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### AcknowledgementCounter
 counter for acknowledgments

#### Python
```python
result = substrate.query(
    'Ibc', 'AcknowledgementCounter', []
)
```

#### Return value
```python
'u32'
```
---------
### Acks
 Acks info

#### Python
```python
result = substrate.query(
    'Ibc', 'Acks', ['Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
### ChannelCounter

#### Python
```python
result = substrate.query(
    'Ibc', 'ChannelCounter', []
)
```

#### Return value
```python
'u32'
```
---------
### ChannelIds
 ChannelIds open from this module

#### Python
```python
result = substrate.query(
    'Ibc', 'ChannelIds', []
)
```

#### Return value
```python
['Bytes']
```
---------
### ChannelsConnection
 connection_identifier =&gt; Vec&lt;(port_id, channel_id)&gt;

#### Python
```python
result = substrate.query(
    'Ibc', 'ChannelsConnection', ['Bytes']
)
```

#### Return value
```python
[('Bytes', 'Bytes')]
```
---------
### ClientCounter
 counter for clients

#### Python
```python
result = substrate.query(
    'Ibc', 'ClientCounter', []
)
```

#### Return value
```python
'u32'
```
---------
### ClientUpdateHeight
 client_id , Height =&gt; Height

#### Python
```python
result = substrate.query(
    'Ibc', 'ClientUpdateHeight', ['Bytes', 'Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
### ClientUpdateTime
 client_id , Height =&gt; Timestamp

#### Python
```python
result = substrate.query(
    'Ibc', 'ClientUpdateTime', ['Bytes', 'Bytes']
)
```

#### Return value
```python
'u64'
```
---------
### ConnectionClient
 client_id =&gt; Vec&lt;Connection_id&gt;

#### Python
```python
result = substrate.query(
    'Ibc', 'ConnectionClient', ['Bytes']
)
```

#### Return value
```python
['Bytes']
```
---------
### ConnectionCounter
 counter for clients

#### Python
```python
result = substrate.query(
    'Ibc', 'ConnectionCounter', []
)
```

#### Return value
```python
'u32'
```
---------
### ConsensusHeights
 Consensus heights
 Stored as a tuple of (revision_number, revision_height)

#### Python
```python
result = substrate.query(
    'Ibc', 'ConsensusHeights', ['Bytes']
)
```

#### Return value
```python
'scale_info::549'
```
---------
### CounterForIbcAssetIds
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'Ibc', 'CounterForIbcAssetIds', []
)
```

#### Return value
```python
'u32'
```
---------
### CounterForIbcDenoms
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'Ibc', 'CounterForIbcDenoms', []
)
```

#### Return value
```python
'u32'
```
---------
### EscrowAddresses
 Active Escrow addresses

#### Python
```python
result = substrate.query(
    'Ibc', 'EscrowAddresses', []
)
```

#### Return value
```python
'scale_info::547'
```
---------
### FeeLessChannelIds
 storage map. key is tuple of (source_channel.sequence(), destination_channel.sequence()) and
 value () that means that this group of channels is feeless

#### Python
```python
result = substrate.query(
    'Ibc', 'FeeLessChannelIds', [('u64', 'u64')]
)
```

#### Return value
```python
()
```
---------
### IbcAssetIds
 Map of asset id to ibc denom pairs (T::AssetId, Vec&lt;u8&gt;)
 ibc denoms represented as utf8 string bytes

#### Python
```python
result = substrate.query(
    'Ibc', 'IbcAssetIds', ['u128']
)
```

#### Return value
```python
'Bytes'
```
---------
### IbcDenoms
 Map of asset id to ibc denom pairs (Vec&lt;u8&gt;, T::AssetId)
 ibc denoms represented as utf8 string bytes

#### Python
```python
result = substrate.query(
    'Ibc', 'IbcDenoms', ['Bytes']
)
```

#### Return value
```python
'u128'
```
---------
### PacketCounter

#### Python
```python
result = substrate.query(
    'Ibc', 'PacketCounter', []
)
```

#### Return value
```python
'u32'
```
---------
### PacketReceiptCounter
 counter for packet receipts

#### Python
```python
result = substrate.query(
    'Ibc', 'PacketReceiptCounter', []
)
```

#### Return value
```python
'u32'
```
---------
### PendingRecvPacketSeqs
 Pending recv packet sequences. Used in `packet_cleanup` procedure.

#### Python
```python
result = substrate.query(
    'Ibc', 'PendingRecvPacketSeqs', [('Bytes', 'Bytes')]
)
```

#### Return value
```python
('scale_info::552', 'u64')
```
---------
### PendingSendPacketSeqs
 Pending send packet sequences. Used in `packet_cleanup` procedure.

#### Python
```python
result = substrate.query(
    'Ibc', 'PendingSendPacketSeqs', [('Bytes', 'Bytes')]
)
```

#### Return value
```python
('scale_info::552', 'u64')
```
---------
### RecvPackets
 RecvPackets info

#### Python
```python
result = substrate.query(
    'Ibc', 'RecvPackets', ['Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
### SendPackets
 SendPackets info

#### Python
```python
result = substrate.query(
    'Ibc', 'SendPackets', ['Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
### SequenceFee
 storage map where key is transfer sequence number and value calculated fee for that sequence
 number

#### Python
```python
result = substrate.query(
    'Ibc', 'SequenceFee', ['u64']
)
```

#### Return value
```python
'u128'
```
---------
### ServiceChargeOut

#### Python
```python
result = substrate.query(
    'Ibc', 'ServiceChargeOut', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### CleanUpPacketsPeriod
 Cleanup packets period (in blocks)
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Ibc', 'CleanUpPacketsPeriod')
```
---------
### ExpectedBlockTime
 Expected block time in milliseconds
#### Value
```python
12000
```
#### Python
```python
constant = substrate.get_constant('Ibc', 'ExpectedBlockTime')
```
---------
### LightClientProtocol
 Light client protocol this chain is operating
#### Value
```python
'Grandpa'
```
#### Python
```python
constant = substrate.get_constant('Ibc', 'LightClientProtocol')
```
---------
### MinimumConnectionDelay
 Minimum connection delay period in seconds for ibc connections that can be created or
 accepted. Ensure that this is non-zero in production as it&#x27;s a critical vulnerability.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Ibc', 'MinimumConnectionDelay')
```
---------
### NativeAssetId
 The native asset id, this will use the `NativeCurrency` for all operations.
#### Value
```python
79228162514264337593543950338
```
#### Python
```python
constant = substrate.get_constant('Ibc', 'NativeAssetId')
```
---------
### PalletPrefix
 Prefix for events stored in the Off-chain DB via Indexing API, child trie and connection
#### Value
```python
'ibc/'
```
#### Python
```python
constant = substrate.get_constant('Ibc', 'PalletPrefix')
```
---------
### ServiceChargeOut
 `ServiceChargeOut` represents the service charge rate applied to assets that will be
 sent via IBC.

 The charge is applied before assets are transffered from the sender side, during
 transfer extrinsic (before to burn or send assets to escrow account) before the packet
 send via IBC Inter-Blockchain Communication (IBC) protocol.

 For example, if the service charge rate for incoming assets is 0.04%, `ServiceChargeIn`
 will be configured in rutime as
 parameter_types! { pub IbcIcs20ServiceChargeOut: Perbill = Perbill::from_rational(4_u32,
 1000_u32 ) };
#### Value
```python
5000000
```
#### Python
```python
constant = substrate.get_constant('Ibc', 'ServiceChargeOut')
```
---------
### SpamProtectionDeposit
 Amount to be reserved for client and connection creation
#### Value
```python
1000000000000000
```
#### Python
```python
constant = substrate.get_constant('Ibc', 'SpamProtectionDeposit')
```
---------
## Errors

---------
### AccessDenied
Access denied

---------
### ChannelEscrowAddress
Failed to derive channel escrow address

---------
### ChannelInitError
Error opening channel

---------
### ChannelNotFound
Channel not found

---------
### ClientFreezeFailed
Error Freezing client

---------
### ClientStateNotFound
Client state not found

---------
### ClientUpdateNotFound
Client update time and height not found

---------
### ConnectionNotFound
Connection not found

---------
### ConsensusStateNotFound
Client consensus state not found for height

---------
### DecodingError
Error decoding some type

---------
### EncodingError
Error encoding some type

---------
### FailedSendFeeToAccount
Fee errors

---------
### FailedToGetRevisionNumber
Unable to get client revision number

---------
### InvalidAmount
Invalid amount

---------
### InvalidAssetId
Invalid asset id

---------
### InvalidChannelId
Invalid channel id

---------
### InvalidMemo
The memo hasn&\#x27;t passed the validation. Potential reasons:
- The memo is too long.
- The memo is in invalid format
- The memo contains unsupported middlewares

---------
### InvalidMessageType
Invalid message for extrinsic

---------
### InvalidParams
Invalid params passed

---------
### InvalidPortId
Invalid port id

---------
### InvalidRoute
Invalid route

---------
### InvalidTimestamp
Invalid timestamp

---------
### OriginAddress
Failed to derive origin sender address.

---------
### Other
Other forms of errors

---------
### PacketAcknowledgmentNotFound
Packet Acknowledgment wasn&\#x27;t found

---------
### PacketCommitmentNotFound
Packet commitment wasn&\#x27;t found

---------
### PacketReceiptNotFound
Packet receipt wasn&\#x27;t found

---------
### PrefixedDenomParse
Invalid Ibc denom

---------
### ProcessingError
Error processing ibc messages

---------
### ProofGenerationError
Error generating trie proof

---------
### RateLimiter

---------
### SendPacketError
Error constructing packet

---------
### TimestampAndHeightNotFound
Latest height and timestamp for a client not found

---------
### TransferInternals
The interchain token transfer was not successfully initiated

---------
### TransferOther

---------
### TransferProtocol

---------
### TransferSend

---------
### TransferSerde

---------
### Utf8Error
Error Decoding utf8 bytes

---------
### WriteAckError
Error writing acknowledgement to storage

---------