
# AdminUtils

---------
## Calls

---------
### sudo_set_activity_cutoff
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| activity_cutoff | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_activity_cutoff', {
    'activity_cutoff': 'u16',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_adjustment_alpha
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| adjustment_alpha | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_adjustment_alpha', {
    'adjustment_alpha': 'u64',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_adjustment_interval
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| adjustment_interval | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_adjustment_interval', {
    'adjustment_interval': 'u16',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_bonds_moving_average
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| bonds_moving_average | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_bonds_moving_average', {
    'bonds_moving_average': 'u64',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_default_take
#### Attributes
| Name | Type |
| -------- | -------- | 
| default_take | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_default_take', {'default_take': 'u16'}
)
```

---------
### sudo_set_difficulty
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| difficulty | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_difficulty', {'difficulty': 'u64', 'netuid': 'u16'}
)
```

---------
### sudo_set_immunity_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| immunity_period | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_immunity_period', {
    'immunity_period': 'u16',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_kappa
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| kappa | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_kappa', {'kappa': 'u16', 'netuid': 'u16'}
)
```

---------
### sudo_set_lock_reduction_interval
#### Attributes
| Name | Type |
| -------- | -------- | 
| interval | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_lock_reduction_interval', {'interval': 'u64'}
)
```

---------
### sudo_set_max_allowed_uids
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| max_allowed_uids | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_max_allowed_uids', {
    'max_allowed_uids': 'u16',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_max_allowed_validators
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| max_allowed_validators | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_max_allowed_validators', {
    'max_allowed_validators': 'u16',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_max_burn
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| max_burn | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_max_burn', {'max_burn': 'u64', 'netuid': 'u16'}
)
```

---------
### sudo_set_max_difficulty
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| max_difficulty | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_max_difficulty', {
    'max_difficulty': 'u64',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_max_registrations_per_block
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| max_registrations_per_block | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_max_registrations_per_block', {
    'max_registrations_per_block': 'u16',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_max_weight_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| max_weight_limit | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_max_weight_limit', {
    'max_weight_limit': 'u16',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_min_allowed_weights
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| min_allowed_weights | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_min_allowed_weights', {
    'min_allowed_weights': 'u16',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_min_burn
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| min_burn | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_min_burn', {'min_burn': 'u64', 'netuid': 'u16'}
)
```

---------
### sudo_set_min_difficulty
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| min_difficulty | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_min_difficulty', {
    'min_difficulty': 'u64',
    'netuid': 'u16',
}
)
```

---------
### sudo_set_network_immunity_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| immunity_period | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_network_immunity_period', {'immunity_period': 'u64'}
)
```

---------
### sudo_set_network_min_lock_cost
#### Attributes
| Name | Type |
| -------- | -------- | 
| lock_cost | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_network_min_lock_cost', {'lock_cost': 'u64'}
)
```

---------
### sudo_set_network_pow_registration_allowed
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| registration_allowed | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_network_pow_registration_allowed', {
    'netuid': 'u16',
    'registration_allowed': 'bool',
}
)
```

---------
### sudo_set_network_rate_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| rate_limit | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_network_rate_limit', {'rate_limit': 'u64'}
)
```

---------
### sudo_set_network_registration_allowed
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| registration_allowed | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_network_registration_allowed', {
    'netuid': 'u16',
    'registration_allowed': 'bool',
}
)
```

---------
### sudo_set_rao_recycled
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| rao_recycled | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_rao_recycled', {
    'netuid': 'u16',
    'rao_recycled': 'u64',
}
)
```

---------
### sudo_set_rho
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| rho | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_rho', {'netuid': 'u16', 'rho': 'u16'}
)
```

---------
### sudo_set_serving_rate_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| serving_rate_limit | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_serving_rate_limit', {
    'netuid': 'u16',
    'serving_rate_limit': 'u64',
}
)
```

---------
### sudo_set_subnet_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_subnets | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_subnet_limit', {'max_subnets': 'u16'}
)
```

---------
### sudo_set_subnet_owner_cut
#### Attributes
| Name | Type |
| -------- | -------- | 
| subnet_owner_cut | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_subnet_owner_cut', {'subnet_owner_cut': 'u16'}
)
```

---------
### sudo_set_target_registrations_per_interval
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| target_registrations_per_interval | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_target_registrations_per_interval', {
    'netuid': 'u16',
    'target_registrations_per_interval': 'u16',
}
)
```

---------
### sudo_set_tempo
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| tempo | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_tempo', {'netuid': 'u16', 'tempo': 'u16'}
)
```

---------
### sudo_set_total_issuance
#### Attributes
| Name | Type |
| -------- | -------- | 
| total_issuance | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_total_issuance', {'total_issuance': 'u64'}
)
```

---------
### sudo_set_tx_rate_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| tx_rate_limit | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_tx_rate_limit', {'tx_rate_limit': 'u64'}
)
```

---------
### sudo_set_weights_min_stake
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_stake | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_weights_min_stake', {'min_stake': 'u64'}
)
```

---------
### sudo_set_weights_set_rate_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| weights_set_rate_limit | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_weights_set_rate_limit', {
    'netuid': 'u16',
    'weights_set_rate_limit': 'u64',
}
)
```

---------
### sudo_set_weights_version_key
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| weights_version_key | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'sudo_set_weights_version_key', {
    'netuid': 'u16',
    'weights_version_key': 'u64',
}
)
```

---------
### swap_authorities
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_authorities | `BoundedVec<T::AuthorityId, T::MaxAuthorities>` | 

#### Python
```python
call = substrate.compose_call(
    'AdminUtils', 'swap_authorities', {'new_authorities': ['[u8; 32]']}
)
```

---------
## Errors

---------
### MaxAllowedUIdsNotAllowed

---------
### NetworkDoesNotExist

---------
### StorageValueOutOfRange

---------