
# Configuration

---------
## Calls

---------
### set_async_backing_params
Set the asynchronous backing parameters.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AsyncBackingParams` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_async_backing_params', {
    'new': {
        'allowed_ancestry_len': 'u32',
        'max_candidate_depth': 'u32',
    },
}
)
```

---------
### set_bypass_consistency_check
Setting this to true will disable consistency checks for the configuration setters.
Use with caution.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_bypass_consistency_check', {'new': 'bool'}
)
```

---------
### set_chain_availability_period
Set the availability period for parachains.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_chain_availability_period', {'new': 'u32'}
)
```

---------
### set_code_retention_period
Set the acceptance period for an included candidate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_code_retention_period', {'new': 'u32'}
)
```

---------
### set_dispute_period
Set the dispute period, in number of sessions to keep for disputes.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `SessionIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_dispute_period', {'new': 'u32'}
)
```

---------
### set_dispute_post_conclusion_acceptance_period
Set the dispute post conclusion acceptance period.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_dispute_post_conclusion_acceptance_period', {'new': 'u32'}
)
```

---------
### set_executor_params
Set PVF executor parameters.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `ExecutorParams` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_executor_params', {
    'new': [
        {
            None: None,
            'MaxMemoryPages': 'u32',
            'PrecheckingMaxMemory': 'u64',
            'PvfExecTimeout': (
                (
                    'Backing',
                    'Approval',
                ),
                'u64',
            ),
            'PvfPrepTimeout': (
                (
                    'Precheck',
                    'Lenient',
                ),
                'u64',
            ),
            'StackLogicalMax': 'u32',
            'StackNativeMax': 'u32',
            'WasmExtBulkMemory': None,
        },
    ],
}
)
```

---------
### set_group_rotation_frequency
Set the parachain validator-group rotation frequency
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_group_rotation_frequency', {'new': 'u32'}
)
```

---------
### set_hrmp_channel_max_capacity
Sets the maximum number of messages allowed in an HRMP channel at once.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_channel_max_capacity', {'new': 'u32'}
)
```

---------
### set_hrmp_channel_max_message_size
Sets the maximum size of a message that could ever be put into an HRMP channel.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_channel_max_message_size', {'new': 'u32'}
)
```

---------
### set_hrmp_channel_max_total_size
Sets the maximum total size of messages in bytes allowed in an HRMP channel at once.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_channel_max_total_size', {'new': 'u32'}
)
```

---------
### set_hrmp_max_message_num_per_candidate
Sets the maximum number of outbound HRMP messages can be sent by a candidate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_max_message_num_per_candidate', {'new': 'u32'}
)
```

---------
### set_hrmp_max_parachain_inbound_channels
Sets the maximum number of inbound HRMP channels a parachain is allowed to accept.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_max_parachain_inbound_channels', {'new': 'u32'}
)
```

---------
### set_hrmp_max_parachain_outbound_channels
Sets the maximum number of outbound HRMP channels a parachain is allowed to open.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_max_parachain_outbound_channels', {'new': 'u32'}
)
```

---------
### set_hrmp_max_parathread_inbound_channels
Sets the maximum number of inbound HRMP channels a parathread is allowed to accept.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_max_parathread_inbound_channels', {'new': 'u32'}
)
```

---------
### set_hrmp_max_parathread_outbound_channels
Sets the maximum number of outbound HRMP channels a parathread is allowed to open.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_max_parathread_outbound_channels', {'new': 'u32'}
)
```

---------
### set_hrmp_open_request_ttl
Sets the number of sessions after which an HRMP open channel request expires.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_open_request_ttl', {'new': 'u32'}
)
```

---------
### set_hrmp_recipient_deposit
Sets the amount of funds that the recipient should provide for accepting opening an HRMP
channel.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_recipient_deposit', {'new': 'u128'}
)
```

---------
### set_hrmp_sender_deposit
Sets the amount of funds that the sender should provide for opening an HRMP channel.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_hrmp_sender_deposit', {'new': 'u128'}
)
```

---------
### set_max_code_size
Set the max validation code size for incoming upgrades.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_code_size', {'new': 'u32'}
)
```

---------
### set_max_downward_message_size
Set the critical downward message size.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_downward_message_size', {'new': 'u32'}
)
```

---------
### set_max_head_data_size
Set the max head data size for paras.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_head_data_size', {'new': 'u32'}
)
```

---------
### set_max_pov_size
Set the max POV block size for incoming upgrades.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_pov_size', {'new': 'u32'}
)
```

---------
### set_max_upward_message_num_per_candidate
Sets the maximum number of messages that a candidate can contain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_upward_message_num_per_candidate', {'new': 'u32'}
)
```

---------
### set_max_upward_message_size
Sets the maximum size of an upward message that can be sent by a candidate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_upward_message_size', {'new': 'u32'}
)
```

---------
### set_max_upward_queue_count
Sets the maximum items that can present in a upward dispatch queue at once.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_upward_queue_count', {'new': 'u32'}
)
```

---------
### set_max_upward_queue_size
Sets the maximum total size of items that can present in a upward dispatch queue at once.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_upward_queue_size', {'new': 'u32'}
)
```

---------
### set_max_validators
Set the maximum number of validators to use in parachain consensus.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_validators', {'new': (None, 'u32')}
)
```

---------
### set_max_validators_per_core
Set the maximum number of validators to assign to any core.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_max_validators_per_core', {'new': (None, 'u32')}
)
```

---------
### set_minimum_validation_upgrade_delay
Sets the minimum delay between announcing the upgrade block for a parachain until the
upgrade taking place.

See the field documentation for information and constraints for the new value.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_minimum_validation_upgrade_delay', {'new': 'u32'}
)
```

---------
### set_n_delay_tranches
Set the total number of delay tranches.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_n_delay_tranches', {'new': 'u32'}
)
```

---------
### set_needed_approvals
Set the number of validators needed to approve a block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_needed_approvals', {'new': 'u32'}
)
```

---------
### set_no_show_slots
Set the no show slots, in number of number of consensus slots.
Must be at least 1.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_no_show_slots', {'new': 'u32'}
)
```

---------
### set_parathread_cores
Set the number of parathread execution cores.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_parathread_cores', {'new': 'u32'}
)
```

---------
### set_parathread_retries
Set the number of retries for a particular parathread.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_parathread_retries', {'new': 'u32'}
)
```

---------
### set_pvf_checking_enabled
Enable or disable PVF pre-checking. Consult the field documentation prior executing.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_pvf_checking_enabled', {'new': 'bool'}
)
```

---------
### set_pvf_voting_ttl
Set the number of session changes after which a PVF pre-checking voting is rejected.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `SessionIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_pvf_voting_ttl', {'new': 'u32'}
)
```

---------
### set_relay_vrf_modulo_samples
Set the number of samples to do of the `RelayVRFModulo` approval assignment criterion.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_relay_vrf_modulo_samples', {'new': 'u32'}
)
```

---------
### set_scheduling_lookahead
Set the scheduling lookahead, in expected number of blocks at peak throughput.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_scheduling_lookahead', {'new': 'u32'}
)
```

---------
### set_thread_availability_period
Set the availability period for parathreads.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_thread_availability_period', {'new': 'u32'}
)
```

---------
### set_ump_max_individual_weight
Sets the maximum amount of weight any individual upward message may consume.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_ump_max_individual_weight', {
    'new': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### set_ump_service_total_weight
Sets the soft limit for the phase of dispatching dispatchable upward messages.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_ump_service_total_weight', {
    'new': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### set_validation_upgrade_cooldown
Set the validation upgrade cooldown.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_validation_upgrade_cooldown', {'new': 'u32'}
)
```

---------
### set_validation_upgrade_delay
Set the validation upgrade delay.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_validation_upgrade_delay', {'new': 'u32'}
)
```

---------
### set_zeroth_delay_tranche_width
Set the zeroth delay tranche width.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_zeroth_delay_tranche_width', {'new': 'u32'}
)
```

---------
## Storage functions

---------
### ActiveConfig
 The active configuration for the current session.

#### Python
```python
result = substrate.query(
    'Configuration', 'ActiveConfig', []
)
```

#### Return value
```python
{
    'async_backing_params': {
        'allowed_ancestry_len': 'u32',
        'max_candidate_depth': 'u32',
    },
    'chain_availability_period': 'u32',
    'code_retention_period': 'u32',
    'dispute_period': 'u32',
    'dispute_post_conclusion_acceptance_period': 'u32',
    'executor_params': [
        {
            None: None,
            'MaxMemoryPages': 'u32',
            'PrecheckingMaxMemory': 'u64',
            'PvfExecTimeout': ('scale_info::324', 'u64'),
            'PvfPrepTimeout': ('scale_info::323', 'u64'),
            'StackLogicalMax': 'u32',
            'StackNativeMax': 'u32',
            'WasmExtBulkMemory': None,
        },
    ],
    'group_rotation_frequency': 'u32',
    'hrmp_channel_max_capacity': 'u32',
    'hrmp_channel_max_message_size': 'u32',
    'hrmp_channel_max_total_size': 'u32',
    'hrmp_max_message_num_per_candidate': 'u32',
    'hrmp_max_parachain_inbound_channels': 'u32',
    'hrmp_max_parachain_outbound_channels': 'u32',
    'hrmp_max_parathread_inbound_channels': 'u32',
    'hrmp_max_parathread_outbound_channels': 'u32',
    'hrmp_recipient_deposit': 'u128',
    'hrmp_sender_deposit': 'u128',
    'max_code_size': 'u32',
    'max_downward_message_size': 'u32',
    'max_head_data_size': 'u32',
    'max_pov_size': 'u32',
    'max_upward_message_num_per_candidate': 'u32',
    'max_upward_message_size': 'u32',
    'max_upward_queue_count': 'u32',
    'max_upward_queue_size': 'u32',
    'max_validators': (None, 'u32'),
    'max_validators_per_core': (None, 'u32'),
    'minimum_validation_upgrade_delay': 'u32',
    'n_delay_tranches': 'u32',
    'needed_approvals': 'u32',
    'no_show_slots': 'u32',
    'parathread_cores': 'u32',
    'parathread_retries': 'u32',
    'pvf_checking_enabled': 'bool',
    'pvf_voting_ttl': 'u32',
    'relay_vrf_modulo_samples': 'u32',
    'scheduling_lookahead': 'u32',
    'thread_availability_period': 'u32',
    'ump_max_individual_weight': {'proof_size': 'u64', 'ref_time': 'u64'},
    'ump_service_total_weight': {'proof_size': 'u64', 'ref_time': 'u64'},
    'validation_upgrade_cooldown': 'u32',
    'validation_upgrade_delay': 'u32',
    'zeroth_delay_tranche_width': 'u32',
}
```
---------
### BypassConsistencyCheck
 If this is set, then the configuration setters will bypass the consistency checks. This
 is meant to be used only as the last resort.

#### Python
```python
result = substrate.query(
    'Configuration', 'BypassConsistencyCheck', []
)
```

#### Return value
```python
'bool'
```
---------
### PendingConfigs
 Pending configuration changes.

 This is a list of configuration changes, each with a session index at which it should
 be applied.

 The list is sorted ascending by session index. Also, this list can only contain at most
 2 items: for the next session and for the `scheduled_session`.

#### Python
```python
result = substrate.query(
    'Configuration', 'PendingConfigs', []
)
```

#### Return value
```python
[
    (
        'u32',
        {
            'async_backing_params': {
                'allowed_ancestry_len': 'u32',
                'max_candidate_depth': 'u32',
            },
            'chain_availability_period': 'u32',
            'code_retention_period': 'u32',
            'dispute_period': 'u32',
            'dispute_post_conclusion_acceptance_period': 'u32',
            'executor_params': ['scale_info::322'],
            'group_rotation_frequency': 'u32',
            'hrmp_channel_max_capacity': 'u32',
            'hrmp_channel_max_message_size': 'u32',
            'hrmp_channel_max_total_size': 'u32',
            'hrmp_max_message_num_per_candidate': 'u32',
            'hrmp_max_parachain_inbound_channels': 'u32',
            'hrmp_max_parachain_outbound_channels': 'u32',
            'hrmp_max_parathread_inbound_channels': 'u32',
            'hrmp_max_parathread_outbound_channels': 'u32',
            'hrmp_recipient_deposit': 'u128',
            'hrmp_sender_deposit': 'u128',
            'max_code_size': 'u32',
            'max_downward_message_size': 'u32',
            'max_head_data_size': 'u32',
            'max_pov_size': 'u32',
            'max_upward_message_num_per_candidate': 'u32',
            'max_upward_message_size': 'u32',
            'max_upward_queue_count': 'u32',
            'max_upward_queue_size': 'u32',
            'max_validators': (None, 'u32'),
            'max_validators_per_core': (None, 'u32'),
            'minimum_validation_upgrade_delay': 'u32',
            'n_delay_tranches': 'u32',
            'needed_approvals': 'u32',
            'no_show_slots': 'u32',
            'parathread_cores': 'u32',
            'parathread_retries': 'u32',
            'pvf_checking_enabled': 'bool',
            'pvf_voting_ttl': 'u32',
            'relay_vrf_modulo_samples': 'u32',
            'scheduling_lookahead': 'u32',
            'thread_availability_period': 'u32',
            'ump_max_individual_weight': {
                'proof_size': 'u64',
                'ref_time': 'u64',
            },
            'ump_service_total_weight': {
                'proof_size': 'u64',
                'ref_time': 'u64',
            },
            'validation_upgrade_cooldown': 'u32',
            'validation_upgrade_delay': 'u32',
            'zeroth_delay_tranche_width': 'u32',
        },
    ),
]
```
---------
## Errors

---------
### InvalidNewValue
The new value for a configuration parameter is invalid.

---------