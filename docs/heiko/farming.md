
# Farming

---------
## Calls

---------
### claim
Claim reward asset from pool

Origin must be Signed.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'claim', {
    'asset': 'u32',
    'lock_duration': 'u32',
    'reward_asset': 'u32',
}
)
```

---------
### create
Create new pool from a privileged origin. Pool can be identified by a pair of asset and reward_asset.

The origin must conform to `UpdateOrigin`.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
- `cool_down_duration`: Lock block number after Withdraw.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 
| cool_down_duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'create', {
    'asset': 'u32',
    'cool_down_duration': 'u32',
    'lock_duration': 'u32',
    'reward_asset': 'u32',
}
)
```

---------
### deposit
Depositing Assets to reward Pool

The origin must be Signed and the sender must have sufficient balance of staking asset.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
- `amount`: the amount of staking asset want to deposit.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'deposit', {
    'amount': 'u128',
    'asset': 'u32',
    'lock_duration': 'u32',
    'reward_asset': 'u32',
}
)
```

---------
### dispatch_reward
Dispatch reward asset with specified amount and duration

The origin must conform to `UpdateOrigin`.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
- `payer`: the payer of reward asset.
- `amount`: the amount of reward asset to dispatch.
- `duration`: the number of block this reward will last for.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 
| payer | `<T::Lookup as StaticLookup>::Source` | 
| amount | `BalanceOf<T>` | 
| reward_duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'dispatch_reward', {
    'amount': 'u128',
    'asset': 'u32',
    'lock_duration': 'u32',
    'payer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'reward_asset': 'u32',
    'reward_duration': 'u32',
}
)
```

---------
### redeem
Redeem unlocked balance of staking asset from Pool

Origin must be Signed.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'redeem', {
    'asset': 'u32',
    'lock_duration': 'u32',
    'reward_asset': 'u32',
}
)
```

---------
### reset_pool_unlock_height
Reset pool unlock height

The origin must conform to `UpdateOrigin`.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'reset_pool_unlock_height', {
    'asset': 'u32',
    'lock_duration': 'u32',
    'reward_asset': 'u32',
}
)
```

---------
### set_pool_cool_down_duration
Set pool cool down duration

The origin must conform to `UpdateOrigin`.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
- `cool_down_duration`: new lock block number after Withdraw.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 
| cool_down_duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'set_pool_cool_down_duration', {
    'asset': 'u32',
    'cool_down_duration': 'u32',
    'lock_duration': 'u32',
    'reward_asset': 'u32',
}
)
```

---------
### set_pool_status
Set pool active status

The origin must conform to `UpdateOrigin`.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
- `is_active`: new active status.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 
| is_active | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'set_pool_status', {
    'asset': 'u32',
    'is_active': 'bool',
    'lock_duration': 'u32',
    'reward_asset': 'u32',
}
)
```

---------
### withdraw
Withdrawing Assets from reward Pool

The origin must be Signed and the sender must have sufficient deposited balance.

- `asset`: The identifier of the staking asset.
- `reward_asset`: The identifier of the reward asset.
- `lock_duration`: Lock block number after Deposit.
- `amount`: the amount of staking asset want to withdraw.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| reward_asset | `AssetIdOf<T>` | 
| lock_duration | `T::BlockNumber` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'withdraw', {
    'amount': 'u128',
    'asset': 'u32',
    'lock_duration': 'u32',
    'reward_asset': 'u32',
}
)
```

---------
## Events

---------
### AssetsDeposited
Deposited Assets in pool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### AssetsRedeem
Redeem Assets from lock pool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### AssetsWithdrew
Withdrew Assets from pool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### PoolAdded
Add new pool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```

---------
### PoolCoolDownDurationChanged
Pool new cool down duration was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `T::BlockNumber` | ```u32```

---------
### PoolStatusChanged
Pool new status was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `bool` | ```bool```

---------
### PoolUnlockHeightReset
Pool unlock height was reset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `T::BlockNumber` | ```u32```

---------
### RewardAdded
Reward added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### RewardPaid
Reward Paid for user
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Pools
 Each pool is associated to a stake asset and reward asset pair

#### Python
```python
result = substrate.query(
    'Farming', 'Pools', ['u32', 'u32', 'u32']
)
```

#### Return value
```python
{
    'cool_down_duration': 'u32',
    'is_active': 'bool',
    'last_update_block': 'u32',
    'period_finish': 'u32',
    'reward_duration': 'u32',
    'reward_per_share_stored': 'u128',
    'reward_rate': 'u128',
    'total_deposited': 'u128',
    'unlock_height': 'u32',
}
```
---------
### Positions
 User position in pool which is associated to a stake asset and reward asset pair

#### Python
```python
result = substrate.query(
    'Farming', 'Positions', ['u32', 'u32', 'u32', 'AccountId']
)
```

#### Return value
```python
{
    'deposit_balance': 'u128',
    'lock_balance_items': [('u128', 'u32')],
    'reward_amount': 'u128',
    'reward_per_share_paid': 'u128',
}
```
---------
## Constants

---------
### CoolDownMaxDuration
 Specifies upper limit of cool down duration for pool
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('Farming', 'CoolDownMaxDuration')
```
---------
### LockPoolMaxDuration
 Specifies upper limit of lock duration for lock pool
#### Value
```python
2628000
```
#### Python
```python
constant = substrate.get_constant('Farming', 'LockPoolMaxDuration')
```
---------
### MaxUserLockItemsCount
 Specifies max amount lock item for a user
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Farming', 'MaxUserLockItemsCount')
```
---------
### PalletId
 Defines the pallet&#x27;s pallet id from which we can define each pool&#x27;s account id
#### Value
```python
'0x7061722f6661726d'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'PalletId')
```
---------
## Errors

---------
### CodecError
Codec error

---------
### DepositBalanceLow
Deposit Balance must be greater than or equal to the withdraw amount

---------
### ExcessMaxCoolDownDuration
Excess max cool down duration for pool

---------
### ExcessMaxLockDuration
Excess max lock duration for lock pool

---------
### ExcessMaxUserLockItemsCount
Excess max user lock item count

---------
### NotAValidAmount
Not a valid amount

---------
### NotAValidDuration
Not a valid duration

---------
### PoolAlreadyExists
Pool associacted with asset already exists

---------
### PoolDoesNotExist
Pool does not exist

---------
### PoolInStatus
Pool is already in desire status

---------
### PoolIsInTargetCoolDownDuration
Pool is in a target cool down duration status

---------
### PoolIsNotActive
Pool is not active

---------
### PoolUnderLock
Pool is in lock status, withdraw is not allowed.

---------
### RewardNotFinish
Last reward is not finish

---------