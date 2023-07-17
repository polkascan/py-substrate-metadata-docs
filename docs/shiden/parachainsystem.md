
# ParachainSystem

---------
## Calls

---------
### authorize_upgrade
#### Attributes
| Name | Type |
| -------- | -------- | 
| code_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'authorize_upgrade', {'code_hash': '[u8; 32]'}
)
```

---------
### enact_authorized_upgrade
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'enact_authorized_upgrade', {'code': 'Bytes'}
)
```

---------
### set_validation_data
Set the current validation data.

This should be invoked exactly once per block. It will panic at the finalization
phase if the call was not invoked.

The dispatch origin for this call must be `Inherent`

As a side effect, this function upgrades the current validation function
if the appropriate time has come.
#### Attributes
| Name | Type |
| -------- | -------- | 
| data | `ParachainInherentData` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'set_validation_data', {
    'data': {
        'downward_messages': [
            {
                'msg': 'Bytes',
                'sent_at': 'u32',
            },
        ],
        'horizontal_messages': 'scale_info::220',
        'relay_chain_state': {
            'trie_nodes': 'scale_info::217',
        },
        'validation_data': {
            'max_pov_size': 'u32',
            'parent_head': 'Bytes',
            'relay_parent_number': 'u32',
            'relay_parent_storage_root': '[u8; 32]',
        },
    },
}
)
```

---------
### sudo_send_upward_message
#### Attributes
| Name | Type |
| -------- | -------- | 
| message | `UpwardMessage` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'sudo_send_upward_message', {'message': 'Bytes'}
)
```

---------
## Events

---------
### DownwardMessagesProcessed
Downward messages were processed using the given weight.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| weight_used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| dmq_head | `relay_chain::Hash` | ```[u8; 32]```

---------
### DownwardMessagesReceived
Some downward messages have been received and will be processed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| count | `u32` | ```u32```

---------
### UpgradeAuthorized
An upgrade has been authorized.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```[u8; 32]```

---------
### UpwardMessageSent
An upward message was sent to the relay chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<XcmHash>` | ```(None, '[u8; 32]')```

---------
### ValidationFunctionApplied
The validation function was applied as of the contained relay chain block number.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| relay_chain_block_num | `RelayChainBlockNumber` | ```u32```

---------
### ValidationFunctionDiscarded
The relay-chain aborted the upgrade process.
#### Attributes
No attributes

---------
### ValidationFunctionStored
The validation function has been scheduled to apply.
#### Attributes
No attributes

---------
## Storage functions

---------
### AnnouncedHrmpMessagesPerCandidate
 The number of HRMP messages we observed in `on_initialize` and thus used that number for
 announcing the weight of `on_initialize` and `on_finalize`.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'AnnouncedHrmpMessagesPerCandidate', []
)
```

#### Return value
```python
'u32'
```
---------
### AuthorizedUpgrade
 The next authorized upgrade, if there is one.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'AuthorizedUpgrade', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### CustomValidationHeadData
 A custom head data that should be returned as result of `validate_block`.

 See [`Pallet::set_custom_validation_head_data`] for more information.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'CustomValidationHeadData', []
)
```

#### Return value
```python
'Bytes'
```
---------
### DidSetValidationCode
 Were the validation data set to notify the relay chain?

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'DidSetValidationCode', []
)
```

#### Return value
```python
'bool'
```
---------
### HostConfiguration
 The parachain host configuration that was obtained from the relay parent.

 This field is meant to be updated each block with the validation data inherent. Therefore,
 before processing of the inherent, e.g. in `on_initialize` this data may be stale.

 This data is also absent from the genesis.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'HostConfiguration', []
)
```

#### Return value
```python
{
    'hrmp_max_message_num_per_candidate': 'u32',
    'max_code_size': 'u32',
    'max_head_data_size': 'u32',
    'max_upward_message_num_per_candidate': 'u32',
    'max_upward_message_size': 'u32',
    'max_upward_queue_count': 'u32',
    'max_upward_queue_size': 'u32',
    'validation_upgrade_cooldown': 'u32',
    'validation_upgrade_delay': 'u32',
}
```
---------
### HrmpOutboundMessages
 HRMP messages that were sent in a block.

 This will be cleared in `on_initialize` of each new block.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'HrmpOutboundMessages', []
)
```

#### Return value
```python
[{'data': 'Bytes', 'recipient': 'u32'}]
```
---------
### HrmpWatermark
 HRMP watermark that was set in a block.

 This will be cleared in `on_initialize` of each new block.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'HrmpWatermark', []
)
```

#### Return value
```python
'u32'
```
---------
### LastDmqMqcHead
 The last downward message queue chain head we have observed.

 This value is loaded before and saved after processing inbound downward messages carried
 by the system inherent.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'LastDmqMqcHead', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### LastHrmpMqcHeads
 The message queue chain heads we have observed per each channel incoming channel.

 This value is loaded before and saved after processing inbound downward messages carried
 by the system inherent.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'LastHrmpMqcHeads', []
)
```

#### Return value
```python
'scale_info::336'
```
---------
### LastRelayChainBlockNumber
 The relay chain block number associated with the last parachain block.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'LastRelayChainBlockNumber', []
)
```

#### Return value
```python
'u32'
```
---------
### NewValidationCode
 Validation code that is set by the parachain and is to be communicated to collator and
 consequently the relay-chain.

 This will be cleared in `on_initialize` of each new block if no other pallet already set
 the value.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'NewValidationCode', []
)
```

#### Return value
```python
'Bytes'
```
---------
### PendingUpwardMessages
 Upward messages that are still pending and not yet send to the relay chain.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'PendingUpwardMessages', []
)
```

#### Return value
```python
['Bytes']
```
---------
### PendingValidationCode
 In case of a scheduled upgrade, this storage field contains the validation code to be applied.

 As soon as the relay chain gives us the go-ahead signal, we will overwrite the [`:code`][well_known_keys::CODE]
 which will result the next block process with the new validation code. This concludes the upgrade process.

 [well_known_keys::CODE]: sp_core::storage::well_known_keys::CODE

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'PendingValidationCode', []
)
```

#### Return value
```python
'Bytes'
```
---------
### ProcessedDownwardMessages
 Number of downward messages processed in a block.

 This will be cleared in `on_initialize` of each new block.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'ProcessedDownwardMessages', []
)
```

#### Return value
```python
'u32'
```
---------
### RelayStateProof
 The state proof for the last relay parent block.

 This field is meant to be updated each block with the validation data inherent. Therefore,
 before processing of the inherent, e.g. in `on_initialize` this data may be stale.

 This data is also absent from the genesis.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'RelayStateProof', []
)
```

#### Return value
```python
{'trie_nodes': 'scale_info::217'}
```
---------
### RelevantMessagingState
 The snapshot of some state related to messaging relevant to the current parachain as per
 the relay parent.

 This field is meant to be updated each block with the validation data inherent. Therefore,
 before processing of the inherent, e.g. in `on_initialize` this data may be stale.

 This data is also absent from the genesis.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'RelevantMessagingState', []
)
```

#### Return value
```python
{
    'dmq_mqc_head': '[u8; 32]',
    'egress_channels': [
        (
            'u32',
            {
                'max_capacity': 'u32',
                'max_message_size': 'u32',
                'max_total_size': 'u32',
                'mqc_head': (None, '[u8; 32]'),
                'msg_count': 'u32',
                'total_size': 'u32',
            },
        ),
    ],
    'ingress_channels': [
        (
            'u32',
            {
                'max_capacity': 'u32',
                'max_message_size': 'u32',
                'max_total_size': 'u32',
                'mqc_head': (None, '[u8; 32]'),
                'msg_count': 'u32',
                'total_size': 'u32',
            },
        ),
    ],
    'relay_dispatch_queue_size': ('u32', 'u32'),
}
```
---------
### ReservedDmpWeightOverride
 The weight we reserve at the beginning of the block for processing DMP messages. This
 overrides the amount set in the Config trait.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'ReservedDmpWeightOverride', []
)
```

#### Return value
```python
{'proof_size': 'u64', 'ref_time': 'u64'}
```
---------
### ReservedXcmpWeightOverride
 The weight we reserve at the beginning of the block for processing XCMP messages. This
 overrides the amount set in the Config trait.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'ReservedXcmpWeightOverride', []
)
```

#### Return value
```python
{'proof_size': 'u64', 'ref_time': 'u64'}
```
---------
### UpgradeRestrictionSignal
 An option which indicates if the relay-chain restricts signalling a validation code upgrade.
 In other words, if this is `Some` and [`NewValidationCode`] is `Some` then the produced
 candidate will be invalid.

 This storage item is a mirror of the corresponding value for the current parachain from the
 relay-chain. This value is ephemeral which means it doesn&#x27;t hit the storage. This value is
 set after the inherent.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'UpgradeRestrictionSignal', []
)
```

#### Return value
```python
(None, ('Present', ))
```
---------
### UpwardMessages
 Upward messages that were sent in a block.

 This will be cleared in `on_initialize` of each new block.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'UpwardMessages', []
)
```

#### Return value
```python
['Bytes']
```
---------
### ValidationData
 The [`PersistedValidationData`] set for this block.
 This value is expected to be set only once per block and it&#x27;s never stored
 in the trie.

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'ValidationData', []
)
```

#### Return value
```python
{
    'max_pov_size': 'u32',
    'parent_head': 'Bytes',
    'relay_parent_number': 'u32',
    'relay_parent_storage_root': '[u8; 32]',
}
```
---------
## Errors

---------
### HostConfigurationNotAvailable
The inherent which supplies the host configuration did not run this block

---------
### NotScheduled
No validation function upgrade is currently scheduled.

---------
### NothingAuthorized
No code upgrade has been authorized.

---------
### OverlappingUpgrades
Attempt to upgrade validation function while existing upgrade pending

---------
### ProhibitedByPolkadot
Polkadot currently prohibits this parachain from upgrading its validation function

---------
### TooBig
The supplied validation function has compiled into a blob larger than Polkadot is
willing to run

---------
### Unauthorized
The given code upgrade has not been authorized.

---------
### ValidationDataNotAvailable
The inherent which supplies the validation data did not run this block

---------