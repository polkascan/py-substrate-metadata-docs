
# QSwap

---------
## Calls

---------
### set_config
#### Attributes
| Name | Type |
| -------- | -------- | 
| mb_max_q_amount | `Option<T::Balance>` | 
| mb_q_swap_configurations | `Option<Vec<
(Asset, SwapConfigurationInput<T::Balance, T::BlockNumber>)>,>` | 

#### Python
```python
call = substrate.compose_call(
    'QSwap', 'set_config', {
    'mb_max_q_amount': (None, 'u128'),
    'mb_q_swap_configurations': (
        None,
        [
            (
                'u64',
                {
                    'mb_enabled': (
                        None,
                        'bool',
                    ),
                    'mb_instant_swap_share': (
                        None,
                        'u8',
                    ),
                    'mb_main_asset_q_discounted_price': (
                        None,
                        'u128',
                    ),
                    'mb_main_asset_q_price': (
                        None,
                        'u128',
                    ),
                    'mb_main_vesting_duration_blocks': (
                        None,
                        'u128',
                    ),
                    'mb_main_vesting_number': (
                        None,
                        'u8',
                    ),
                    'mb_main_vesting_starting_block': (
                        None,
                        'u32',
                    ),
                    'mb_min_amount': (
                        None,
                        'u128',
                    ),
                    'mb_secondary_asset': (
                        None,
                        'u64',
                    ),
                    'mb_secondary_asset_q_discounted_price': (
                        None,
                        'u128',
                    ),
                    'mb_secondary_asset_q_price': (
                        None,
                        'u128',
                    ),
                    'mb_secondary_vesting_duration_blocks': (
                        None,
                        'u128',
                    ),
                    'mb_secondary_vesting_number': (
                        None,
                        'u8',
                    ),
                    'mb_secondary_vesting_starting_block': (
                        None,
                        'u32',
                    ),
                },
            ),
        ],
    ),
}
)
```

---------
### swap
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'QSwap', 'swap', {'amount': 'u128', 'asset': 'u64'}
)
```

---------
## Events

---------
### QSwap
Transfer event. Included values are:
- from `AccountId`
- requested amount (asset \#1)
- requested amount (asset \#2)
- Q received amount
- Q vested amount \#1
- Q vested amount \#2
\[from, amount_1, amount_2, amount_3, amount_4, amount_5 \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
## Storage functions

---------
### QReceivedAmounts
 Stores Q amount transferred to users

#### Python
```python
result = substrate.query(
    'QSwap', 'QReceivedAmounts', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### QReceivingThreshold
 Max amount of Q to receive by each user.

#### Python
```python
result = substrate.query(
    'QSwap', 'QReceivingThreshold', []
)
```

#### Return value
```python
'u128'
```
---------
### QSwapConfigurations
 Stores Q swap configuration

#### Python
```python
result = substrate.query(
    'QSwap', 'QSwapConfigurations', ['u64']
)
```

#### Return value
```python
{
    'enabled': 'bool',
    'instant_swap_share': 'u8',
    'main_asset_q_discounted_price': 'u128',
    'main_asset_q_price': 'u128',
    'main_vesting_duration_blocks': 'u128',
    'main_vesting_number': 'u8',
    'main_vesting_starting_block': 'u32',
    'min_amount': 'u128',
    'secondary_asset': 'u64',
    'secondary_asset_q_discounted_price': 'u128',
    'secondary_asset_q_price': 'u128',
    'secondary_vesting_duration_blocks': 'u128',
    'secondary_vesting_number': 'u8',
    'secondary_vesting_starting_block': 'u32',
}
```
---------
## Errors

---------
### AmountTooSmall
Specified amount is too small to perform swap

---------
### InvalidConfiguration
Configuration is invalid

---------
### NotEnoughBalance
Available balance is not enough to perform swap

---------
### SwapsAreDisabled
Swaps are disabled

---------