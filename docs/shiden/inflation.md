
# Inflation

---------
## Calls

---------
### force_inflation_recalculation
See [`Pallet::force_inflation_recalculation`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| next_era | `EraNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Inflation', 'force_inflation_recalculation', {'next_era': 'u32'}
)
```

---------
### force_set_inflation_params
See [`Pallet::force_set_inflation_params`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `InflationParameters` | 

#### Python
```python
call = substrate.compose_call(
    'Inflation', 'force_set_inflation_params', {
    'params': {
        'adjustable_stakers_part': 'u64',
        'base_stakers_part': 'u64',
        'bonus_part': 'u64',
        'collators_part': 'u64',
        'dapps_part': 'u64',
        'ideal_staking_rate': 'u64',
        'max_inflation_rate': 'u64',
        'treasury_part': 'u64',
    },
}
)
```

---------
## Events

---------
### ForcedInflationRecalculation
Inflation recalculation has been forced.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| config | `InflationConfiguration` | ```{'recalculation_era': 'u32', 'issuance_safety_cap': 'u128', 'collator_reward_per_block': 'u128', 'treasury_reward_per_block': 'u128', 'dapp_reward_pool_per_era': 'u128', 'base_staker_reward_pool_per_era': 'u128', 'adjustable_staker_reward_pool_per_era': 'u128', 'bonus_reward_pool_per_period': 'u128', 'ideal_staking_rate': 'u64'}```

---------
### InflationConfigurationForceChanged
Inflation configuration has been force changed. This will have an immediate effect from this block.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| config | `InflationConfiguration` | ```{'recalculation_era': 'u32', 'issuance_safety_cap': 'u128', 'collator_reward_per_block': 'u128', 'treasury_reward_per_block': 'u128', 'dapp_reward_pool_per_era': 'u128', 'base_staker_reward_pool_per_era': 'u128', 'adjustable_staker_reward_pool_per_era': 'u128', 'bonus_reward_pool_per_period': 'u128', 'ideal_staking_rate': 'u64'}```

---------
### InflationParametersForceChanged
Inflation parameters have been force changed. This will have effect on the next inflation recalculation.
#### Attributes
No attributes

---------
### NewInflationConfiguration
New inflation configuration has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| config | `InflationConfiguration` | ```{'recalculation_era': 'u32', 'issuance_safety_cap': 'u128', 'collator_reward_per_block': 'u128', 'treasury_reward_per_block': 'u128', 'dapp_reward_pool_per_era': 'u128', 'base_staker_reward_pool_per_era': 'u128', 'adjustable_staker_reward_pool_per_era': 'u128', 'bonus_reward_pool_per_period': 'u128', 'ideal_staking_rate': 'u64'}```

---------
## Storage functions

---------
### ActiveInflationConfig
 Active inflation configuration parameters.
 They describe current rewards, when inflation needs to be recalculated, etc.

#### Python
```python
result = substrate.query(
    'Inflation', 'ActiveInflationConfig', []
)
```

#### Return value
```python
{
    'adjustable_staker_reward_pool_per_era': 'u128',
    'base_staker_reward_pool_per_era': 'u128',
    'bonus_reward_pool_per_period': 'u128',
    'collator_reward_per_block': 'u128',
    'dapp_reward_pool_per_era': 'u128',
    'ideal_staking_rate': 'u64',
    'issuance_safety_cap': 'u128',
    'recalculation_era': 'u32',
    'treasury_reward_per_block': 'u128',
}
```
---------
### DoRecalculation
 Flag indicating whether on the first possible opportunity, recalculation of the inflation config should be done.

#### Python
```python
result = substrate.query(
    'Inflation', 'DoRecalculation', []
)
```

#### Return value
```python
'u32'
```
---------
### InflationParams
 Static inflation parameters - used to calculate active inflation configuration at certain points in time.

#### Python
```python
result = substrate.query(
    'Inflation', 'InflationParams', []
)
```

#### Return value
```python
{
    'adjustable_stakers_part': 'u64',
    'base_stakers_part': 'u64',
    'bonus_part': 'u64',
    'collators_part': 'u64',
    'dapps_part': 'u64',
    'ideal_staking_rate': 'u64',
    'max_inflation_rate': 'u64',
    'treasury_part': 'u64',
}
```
---------
## Errors

---------
### InvalidInflationParameters
Sum of all parts must be one whole (100%).

---------