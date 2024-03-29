
# Configuration

---------
## Calls

---------
### set_app_promotion_configuration_override
See [`Pallet::set_app_promotion_configuration_override`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| configuration | `AppPromotionConfiguration<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_app_promotion_configuration_override', {
    'configuration': {
        'interval_income': (
            None,
            'u32',
        ),
        'max_stakers_per_calculation': (
            None,
            'u8',
        ),
        'pending_interval': (
            None,
            'u32',
        ),
        'recalculation_interval': (
            None,
            'u32',
        ),
    },
}
)
```

---------
### set_collator_selection_desired_collators
See [`Pallet::set_collator_selection_desired_collators`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| max | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_collator_selection_desired_collators', {'max': (None, 'u32')}
)
```

---------
### set_collator_selection_kick_threshold
See [`Pallet::set_collator_selection_kick_threshold`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `Option<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_collator_selection_kick_threshold', {'threshold': (None, 'u32')}
)
```

---------
### set_collator_selection_license_bond
See [`Pallet::set_collator_selection_license_bond`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Option<<T as Config>::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_collator_selection_license_bond', {'amount': (None, 'u128')}
)
```

---------
### set_min_gas_price_override
See [`Pallet::set_min_gas_price_override`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| coeff | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_min_gas_price_override', {'coeff': (None, 'u64')}
)
```

---------
### set_weight_to_fee_coefficient_override
See [`Pallet::set_weight_to_fee_coefficient_override`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| coeff | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_weight_to_fee_coefficient_override', {'coeff': (None, 'u64')}
)
```

---------
## Events

---------
### NewCollatorKickThreshold
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| length_in_blocks | `Option<BlockNumberFor<T>>` | ```(None, 'u32')```

---------
### NewCollatorLicenseBond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bond_cost | `Option<T::Balance>` | ```(None, 'u128')```

---------
### NewDesiredCollators
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| desired_collators | `Option<u32>` | ```(None, 'u32')```

---------
## Storage functions

---------
### AppPromomotionConfigurationOverride

#### Python
```python
result = substrate.query(
    'Configuration', 'AppPromomotionConfigurationOverride', []
)
```

#### Return value
```python
{
    'interval_income': (None, 'u32'),
    'max_stakers_per_calculation': (None, 'u8'),
    'pending_interval': (None, 'u32'),
    'recalculation_interval': (None, 'u32'),
}
```
---------
### CollatorSelectionDesiredCollatorsOverride

#### Python
```python
result = substrate.query(
    'Configuration', 'CollatorSelectionDesiredCollatorsOverride', []
)
```

#### Return value
```python
'u32'
```
---------
### CollatorSelectionKickThresholdOverride

#### Python
```python
result = substrate.query(
    'Configuration', 'CollatorSelectionKickThresholdOverride', []
)
```

#### Return value
```python
'u32'
```
---------
### CollatorSelectionLicenseBondOverride

#### Python
```python
result = substrate.query(
    'Configuration', 'CollatorSelectionLicenseBondOverride', []
)
```

#### Return value
```python
'u128'
```
---------
### MinGasPriceOverride

#### Python
```python
result = substrate.query(
    'Configuration', 'MinGasPriceOverride', []
)
```

#### Return value
```python
'u64'
```
---------
### WeightToFeeCoefficientOverride

#### Python
```python
result = substrate.query(
    'Configuration', 'WeightToFeeCoefficientOverride', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### AppPromotionDailyRate
#### Value
```python
453256
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'AppPromotionDailyRate')
```
---------
### DayRelayBlocks
#### Value
```python
14400
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'DayRelayBlocks')
```
---------
### DefaultCollatorSelectionKickThreshold
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'DefaultCollatorSelectionKickThreshold')
```
---------
### DefaultCollatorSelectionLicenseBond
#### Value
```python
1000000000000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'DefaultCollatorSelectionLicenseBond')
```
---------
### DefaultCollatorSelectionMaxCollators
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'DefaultCollatorSelectionMaxCollators')
```
---------
### DefaultMinGasPrice
#### Value
```python
1873548000299
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'DefaultMinGasPrice')
```
---------
### DefaultWeightToFeeCoefficient
#### Value
```python
74374502416291841
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'DefaultWeightToFeeCoefficient')
```
---------
### MaxXcmAllowedLocations
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'MaxXcmAllowedLocations')
```
---------
## Errors

---------
### InconsistentConfiguration

---------