
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
        'horizontal_messages': 'scale_info::111',
        'relay_chain_state': {
            'trie_nodes': 'scale_info::93',
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
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| weight_used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| dmq_head | `relay_chain::Hash` | ```[u8; 32]```

---------
### DownwardMessagesReceived
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| count | `u32` | ```u32```

---------
### UpgradeAuthorized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```[u8; 32]```

---------
### ValidationFunctionApplied
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| relay_chain_block_num | `RelayChainBlockNumber` | ```u32```

---------
### ValidationFunctionDiscarded
#### Attributes
No attributes

---------
### ValidationFunctionStored
#### Attributes
No attributes

---------
## Storage functions

---------
### AnnouncedHrmpMessagesPerCandidate

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

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'LastHrmpMqcHeads', []
)
```

#### Return value
```python
'scale_info::102'
```
---------
### LastRelayChainBlockNumber

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

#### Python
```python
result = substrate.query(
    'ParachainSystem', 'RelayStateProof', []
)
```

#### Return value
```python
{'trie_nodes': 'scale_info::93'}
```
---------
### RelevantMessagingState

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

---------
### NotScheduled

---------
### NothingAuthorized

---------
### OverlappingUpgrades

---------
### ProhibitedByPolkadot

---------
### TooBig

---------
### Unauthorized

---------
### ValidationDataNotAvailable

---------