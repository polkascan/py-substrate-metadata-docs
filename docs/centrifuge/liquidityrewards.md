
# LiquidityRewards

---------
## Calls

---------
### claim_reward
Claims the reward the associated to a currency.
The reward will be transferred to the origin&\#x27;s account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityRewards', 'claim_reward', {
    'currency_id': {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
}
)
```

---------
### set_currency_group
Admin method to set the group used for a currency in the next
epochs. Current epoch is not affected by this call.

This method will do the currency available for using it in
stake/unstake/claim calls.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| group_id | `T::GroupId` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityRewards', 'set_currency_group', {
    'currency_id': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'group_id': 'u32',
}
)
```

---------
### set_distributed_reward
Admin method to set the reward amount used for the next epochs.
Current epoch is not affected by this call.
#### Attributes
| Name | Type |
| -------- | -------- | 
| balance | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityRewards', 'set_distributed_reward', {'balance': 'u128'}
)
```

---------
### set_epoch_duration
Admin method to set the duration used for the next epochs.
Current epoch is not affected by this call.
#### Attributes
| Name | Type |
| -------- | -------- | 
| duration | `MomentOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityRewards', 'set_epoch_duration', {'duration': 'u64'}
)
```

---------
### set_group_weight
Admin method to set the group weights used for the next epochs.
Current epoch is not affected by this call.
#### Attributes
| Name | Type |
| -------- | -------- | 
| group_id | `T::GroupId` | 
| weight | `T::Weight` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityRewards', 'set_group_weight', {'group_id': 'u32', 'weight': 'u64'}
)
```

---------
### stake
Deposit a stake amount associated to a currency for the origin&\#x27;s
account. The account must have enough currency to make the deposit,
if not, an Err will be returned.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityRewards', 'stake', {
    'amount': 'u128',
    'currency_id': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
}
)
```

---------
### unstake
Withdraw a stake amount associated to a currency for the origin&\#x27;s
account. The account must have enough currency staked to make the
withdraw, if not, an Err will be returned.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityRewards', 'unstake', {
    'amount': 'u128',
    'currency_id': {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
}
)
```

---------
## Events

---------
### NewEpoch
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ends_on | `MomentOf<T>` | ```u64```
| reward | `T::Balance` | ```u128```
| last_changes | `EpochChanges<T>` | ```{'duration': (None, 'u64'), 'reward': (None, 'u128'), 'weights': 'scale_info::93', 'currencies': 'scale_info::97'}```

---------
## Storage functions

---------
### ActiveEpochData
 Data associated to the current epoch.

#### Python
```python
result = substrate.query(
    'LiquidityRewards', 'ActiveEpochData', []
)
```

#### Return value
```python
{'duration': 'u64', 'reward': 'u128', 'weights': 'scale_info::93'}
```
---------
### EndOfEpoch
 Contains the timestamp when the current epoch is finalized.

#### Python
```python
result = substrate.query(
    'LiquidityRewards', 'EndOfEpoch', []
)
```

#### Return value
```python
'u64'
```
---------
### NextEpochChanges
 Pending update data used when the current epoch finalizes.
 Once it&#x27;s used for the update, it&#x27;s reset.

#### Python
```python
result = substrate.query(
    'LiquidityRewards', 'NextEpochChanges', []
)
```

#### Return value
```python
{
    'currencies': 'scale_info::97',
    'duration': (None, 'u64'),
    'reward': (None, 'u128'),
    'weights': 'scale_info::93',
}
```
---------
## Constants

---------
### InitialEpochDuration
 Initial epoch duration.
 This value can be updated later using
 [`Pallet::set_epoch_duration()`]`.
#### Value
```python
60000
```
#### Python
```python
constant = substrate.get_constant('LiquidityRewards', 'InitialEpochDuration')
```
---------
### MaxChangesPerEpoch
 Max number of changes of the same type enqueued to apply in the next
 epoch. Max calls to [`Pallet::set_group_weight()`] or to
 [`Pallet::set_currency_group()`] with the same id.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('LiquidityRewards', 'MaxChangesPerEpoch')
```
---------
### MaxGroups
 Max groups used by this pallet.
 If this limit is reached, the exceeded groups are either not
 computed and not stored.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('LiquidityRewards', 'MaxGroups')
```
---------
## Errors

---------
### MaxChangesPerEpochReached
Limit of max calls with same id to [`Pallet::set_group_weight()`] or
[`Pallet::set_currency_group()`] reached.

---------