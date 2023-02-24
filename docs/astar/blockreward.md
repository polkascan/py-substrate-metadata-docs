
# BlockReward

---------
## Calls

---------
### set_configuration
Sets the reward distribution configuration parameters which will be used from next block reward distribution.

It is mandatory that all components of configuration sum up to one whole (**100%**),
otherwise an error `InvalidDistributionConfiguration` will be raised.

- `reward_distro_params` - reward distribution params

Emits `DistributionConfigurationChanged` with config embeded into event itself.

#### Attributes
| Name | Type |
| -------- | -------- | 
| reward_distro_params | `RewardDistributionConfig` | 

#### Python
```python
call = substrate.compose_call(
    'BlockReward', 'set_configuration', {
    'reward_distro_params': {
        'adjustable_percent': 'u32',
        'base_staker_percent': 'u32',
        'base_treasury_percent': 'u32',
        'collators_percent': 'u32',
        'dapps_percent': 'u32',
        'ideal_dapps_staking_tvl': 'u32',
    },
}
)
```

---------
## Events

---------
### DistributionConfigurationChanged
Distribution configuration has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RewardDistributionConfig` | ```{'base_treasury_percent': 'u32', 'base_staker_percent': 'u32', 'dapps_percent': 'u32', 'collators_percent': 'u32', 'adjustable_percent': 'u32', 'ideal_dapps_staking_tvl': 'u32'}```

---------
## Storage functions

---------
### RewardDistributionConfigStorage

#### Python
```python
result = substrate.query(
    'BlockReward', 'RewardDistributionConfigStorage', []
)
```

#### Return value
```python
{
    'adjustable_percent': 'u32',
    'base_staker_percent': 'u32',
    'base_treasury_percent': 'u32',
    'collators_percent': 'u32',
    'dapps_percent': 'u32',
    'ideal_dapps_staking_tvl': 'u32',
}
```
---------
## Constants

---------
### RewardAmount
 The amount of issuance for each block.
#### Value
```python
253080000000000000000
```
#### Python
```python
constant = substrate.get_constant('BlockReward', 'RewardAmount')
```
---------
## Errors

---------
### InvalidDistributionConfiguration
Sum of all rations must be one whole (100%)

---------