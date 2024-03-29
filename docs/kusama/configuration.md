
# Configuration

---------
## Calls

---------
### set_async_backing_params
See [`Pallet::set_async_backing_params`].
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
See [`Pallet::set_bypass_consistency_check`].
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
### set_code_retention_period
See [`Pallet::set_code_retention_period`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_code_retention_period', {'new': 'u32'}
)
```

---------
### set_dispute_period
See [`Pallet::set_dispute_period`].
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
See [`Pallet::set_dispute_post_conclusion_acceptance_period`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_dispute_post_conclusion_acceptance_period', {'new': 'u32'}
)
```

---------
### set_executor_params
See [`Pallet::set_executor_params`].
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
See [`Pallet::set_group_rotation_frequency`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_group_rotation_frequency', {'new': 'u32'}
)
```

---------
### set_hrmp_channel_max_capacity
See [`Pallet::set_hrmp_channel_max_capacity`].
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
See [`Pallet::set_hrmp_channel_max_message_size`].
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
See [`Pallet::set_hrmp_channel_max_total_size`].
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
See [`Pallet::set_hrmp_max_message_num_per_candidate`].
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
See [`Pallet::set_hrmp_max_parachain_inbound_channels`].
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
See [`Pallet::set_hrmp_max_parachain_outbound_channels`].
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
### set_hrmp_open_request_ttl
See [`Pallet::set_hrmp_open_request_ttl`].
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
See [`Pallet::set_hrmp_recipient_deposit`].
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
See [`Pallet::set_hrmp_sender_deposit`].
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
See [`Pallet::set_max_code_size`].
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
See [`Pallet::set_max_downward_message_size`].
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
See [`Pallet::set_max_head_data_size`].
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
See [`Pallet::set_max_pov_size`].
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
See [`Pallet::set_max_upward_message_num_per_candidate`].
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
See [`Pallet::set_max_upward_message_size`].
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
See [`Pallet::set_max_upward_queue_count`].
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
See [`Pallet::set_max_upward_queue_size`].
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
See [`Pallet::set_max_validators`].
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
See [`Pallet::set_max_validators_per_core`].
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
### set_minimum_backing_votes
See [`Pallet::set_minimum_backing_votes`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_minimum_backing_votes', {'new': 'u32'}
)
```

---------
### set_minimum_validation_upgrade_delay
See [`Pallet::set_minimum_validation_upgrade_delay`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_minimum_validation_upgrade_delay', {'new': 'u32'}
)
```

---------
### set_n_delay_tranches
See [`Pallet::set_n_delay_tranches`].
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
See [`Pallet::set_needed_approvals`].
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
See [`Pallet::set_no_show_slots`].
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
### set_on_demand_base_fee
See [`Pallet::set_on_demand_base_fee`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_on_demand_base_fee', {'new': 'u128'}
)
```

---------
### set_on_demand_cores
See [`Pallet::set_on_demand_cores`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_on_demand_cores', {'new': 'u32'}
)
```

---------
### set_on_demand_fee_variability
See [`Pallet::set_on_demand_fee_variability`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_on_demand_fee_variability', {'new': 'u32'}
)
```

---------
### set_on_demand_queue_max_size
See [`Pallet::set_on_demand_queue_max_size`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_on_demand_queue_max_size', {'new': 'u32'}
)
```

---------
### set_on_demand_retries
See [`Pallet::set_on_demand_retries`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_on_demand_retries', {'new': 'u32'}
)
```

---------
### set_on_demand_target_queue_utilization
See [`Pallet::set_on_demand_target_queue_utilization`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_on_demand_target_queue_utilization', {'new': 'u32'}
)
```

---------
### set_on_demand_ttl
See [`Pallet::set_on_demand_ttl`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_on_demand_ttl', {'new': 'u32'}
)
```

---------
### set_paras_availability_period
See [`Pallet::set_paras_availability_period`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_paras_availability_period', {'new': 'u32'}
)
```

---------
### set_pvf_voting_ttl
See [`Pallet::set_pvf_voting_ttl`].
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
See [`Pallet::set_relay_vrf_modulo_samples`].
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
See [`Pallet::set_scheduling_lookahead`].
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
### set_validation_upgrade_cooldown
See [`Pallet::set_validation_upgrade_cooldown`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_validation_upgrade_cooldown', {'new': 'u32'}
)
```

---------
### set_validation_upgrade_delay
See [`Pallet::set_validation_upgrade_delay`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_validation_upgrade_delay', {'new': 'u32'}
)
```

---------
### set_zeroth_delay_tranche_width
See [`Pallet::set_zeroth_delay_tranche_width`].
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
    'code_retention_period': 'u32',
    'dispute_period': 'u32',
    'dispute_post_conclusion_acceptance_period': 'u32',
    'executor_params': [
        {
            None: None,
            'MaxMemoryPages': 'u32',
            'PrecheckingMaxMemory': 'u64',
            'PvfExecTimeout': ('scale_info::332', 'u64'),
            'PvfPrepTimeout': ('scale_info::331', 'u64'),
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
    'minimum_backing_votes': 'u32',
    'minimum_validation_upgrade_delay': 'u32',
    'n_delay_tranches': 'u32',
    'needed_approvals': 'u32',
    'no_show_slots': 'u32',
    'on_demand_base_fee': 'u128',
    'on_demand_cores': 'u32',
    'on_demand_fee_variability': 'u32',
    'on_demand_queue_max_size': 'u32',
    'on_demand_retries': 'u32',
    'on_demand_target_queue_utilization': 'u32',
    'on_demand_ttl': 'u32',
    'paras_availability_period': 'u32',
    'pvf_voting_ttl': 'u32',
    'relay_vrf_modulo_samples': 'u32',
    'scheduling_lookahead': 'u32',
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
            'code_retention_period': 'u32',
            'dispute_period': 'u32',
            'dispute_post_conclusion_acceptance_period': 'u32',
            'executor_params': ['scale_info::330'],
            'group_rotation_frequency': 'u32',
            'hrmp_channel_max_capacity': 'u32',
            'hrmp_channel_max_message_size': 'u32',
            'hrmp_channel_max_total_size': 'u32',
            'hrmp_max_message_num_per_candidate': 'u32',
            'hrmp_max_parachain_inbound_channels': 'u32',
            'hrmp_max_parachain_outbound_channels': 'u32',
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
            'minimum_backing_votes': 'u32',
            'minimum_validation_upgrade_delay': 'u32',
            'n_delay_tranches': 'u32',
            'needed_approvals': 'u32',
            'no_show_slots': 'u32',
            'on_demand_base_fee': 'u128',
            'on_demand_cores': 'u32',
            'on_demand_fee_variability': 'u32',
            'on_demand_queue_max_size': 'u32',
            'on_demand_retries': 'u32',
            'on_demand_target_queue_utilization': 'u32',
            'on_demand_ttl': 'u32',
            'paras_availability_period': 'u32',
            'pvf_voting_ttl': 'u32',
            'relay_vrf_modulo_samples': 'u32',
            'scheduling_lookahead': 'u32',
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