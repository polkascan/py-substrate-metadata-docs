
# DappStaking

---------
## Calls

---------
### claim_bonus_reward
See [`Pallet::claim_bonus_reward`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| smart_contract | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'claim_bonus_reward', {
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### claim_dapp_reward
See [`Pallet::claim_dapp_reward`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| smart_contract | `T::SmartContract` | 
| era | `EraNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'claim_dapp_reward', {
    'era': 'u32',
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### claim_staker_rewards
See [`Pallet::claim_staker_rewards`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'claim_staker_rewards', {}
)
```

---------
### claim_unlocked
See [`Pallet::claim_unlocked`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'claim_unlocked', {}
)
```

---------
### cleanup_expired_entries
See [`Pallet::cleanup_expired_entries`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'cleanup_expired_entries', {}
)
```

---------
### force
See [`Pallet::force`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| forcing_type | `ForcingType` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'force', {'forcing_type': ('Era', 'Subperiod')}
)
```

---------
### lock
See [`Pallet::lock`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'lock', {'amount': 'u128'}
)
```

---------
### maintenance_mode
See [`Pallet::maintenance_mode`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'maintenance_mode', {'enabled': 'bool'}
)
```

---------
### register
See [`Pallet::register`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `T::AccountId` | 
| smart_contract | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'register', {
    'owner': 'AccountId',
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### relock_unlocking
See [`Pallet::relock_unlocking`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'relock_unlocking', {}
)
```

---------
### set_dapp_owner
See [`Pallet::set_dapp_owner`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| smart_contract | `T::SmartContract` | 
| new_owner | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'set_dapp_owner', {
    'new_owner': 'AccountId',
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### set_dapp_reward_beneficiary
See [`Pallet::set_dapp_reward_beneficiary`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| smart_contract | `T::SmartContract` | 
| beneficiary | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'set_dapp_reward_beneficiary', {
    'beneficiary': (None, 'AccountId'),
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### stake
See [`Pallet::stake`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| smart_contract | `T::SmartContract` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'stake', {
    'amount': 'u128',
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### unbond_and_unstake
See [`Pallet::unbond_and_unstake`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `T::SmartContract` | 
| value | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'unbond_and_unstake', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'value': 'u128',
}
)
```

---------
### unlock
See [`Pallet::unlock`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'unlock', {'amount': 'u128'}
)
```

---------
### unregister
See [`Pallet::unregister`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| smart_contract | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'unregister', {
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### unstake
See [`Pallet::unstake`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| smart_contract | `T::SmartContract` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'unstake', {
    'amount': 'u128',
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### unstake_from_unregistered
See [`Pallet::unstake_from_unregistered`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| smart_contract | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'unstake_from_unregistered', {
    'smart_contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### withdraw_unbonded
See [`Pallet::withdraw_unbonded`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DappStaking', 'withdraw_unbonded', {}
)
```

---------
## Events

---------
### BonusReward
Bonus reward has been paid out to a loyal staker.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| period | `PeriodNumber` | ```u32```
| amount | `Balance` | ```u128```

---------
### ClaimedUnlocked
Account has claimed unlocked amount, removing the lock from it.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### DAppOwnerChanged
dApp owner has been changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| new_owner | `T::AccountId` | ```AccountId```

---------
### DAppRegistered
A smart contract has been registered for dApp staking
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| dapp_id | `DAppId` | ```u16```

---------
### DAppReward
dApp reward has been paid out to a beneficiary.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| beneficiary | `T::AccountId` | ```AccountId```
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| tier_id | `TierId` | ```u8```
| era | `EraNumber` | ```u32```
| amount | `Balance` | ```u128```

---------
### DAppRewardDestinationUpdated
dApp reward destination has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| beneficiary | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### DAppUnregistered
dApp has been unregistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| era | `EraNumber` | ```u32```

---------
### ExpiredEntriesRemoved
Some expired stake entries have been removed from storage.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| count | `u16` | ```u16```

---------
### Force
Privileged origin has forced a new era and possibly a subperiod to start from next block.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| forcing_type | `ForcingType` | ```('Era', 'Subperiod')```

---------
### Locked
Account has locked some amount into dApp staking.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### MaintenanceMode
Maintenance mode has been either enabled or disabled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| enabled | `bool` | ```bool```

---------
### NewEra
New era has started.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| era | `EraNumber` | ```u32```

---------
### NewSubperiod
New subperiod has started.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| subperiod | `Subperiod` | ```('Voting', 'BuildAndEarn')```
| number | `PeriodNumber` | ```u32```

---------
### Relock
Account has relocked all of the unlocking chunks.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### Reward
Account has claimed some stake rewards.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| era | `EraNumber` | ```u32```
| amount | `Balance` | ```u128```

---------
### Stake
Account has staked some amount on a smart contract.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| amount | `Balance` | ```u128```

---------
### Unlocking
Account has started the unlocking process for some amount.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### Unstake
Account has unstaked some amount from a smart contract.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| amount | `Balance` | ```u128```

---------
### UnstakeFromUnregistered
Account has unstaked funds from an unregistered smart contract
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| smart_contract | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| amount | `Balance` | ```u128```

---------
## Storage functions

---------
### ActiveProtocolState
 General information about dApp staking protocol state.

#### Python
```python
result = substrate.query(
    'DappStaking', 'ActiveProtocolState', []
)
```

#### Return value
```python
{
    'era': 'u32',
    'maintenance': 'bool',
    'next_era_start': 'u32',
    'period_info': {
        'next_subperiod_start_era': 'u32',
        'number': 'u32',
        'subperiod': ('Voting', 'BuildAndEarn'),
    },
}
```
---------
### ContractStake
 Information about how much has been staked on a smart contract in some era or period.

#### Python
```python
result = substrate.query(
    'DappStaking', 'ContractStake', ['u16']
)
```

#### Return value
```python
{
    'staked': {
        'build_and_earn': 'u128',
        'era': 'u32',
        'period': 'u32',
        'voting': 'u128',
    },
    'staked_future': (
        None,
        {
            'build_and_earn': 'u128',
            'era': 'u32',
            'period': 'u32',
            'voting': 'u128',
        },
    ),
}
```
---------
### CounterForIntegratedDApps
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'DappStaking', 'CounterForIntegratedDApps', []
)
```

#### Return value
```python
'u32'
```
---------
### CurrentEraInfo
 General information about the current era.

#### Python
```python
result = substrate.query(
    'DappStaking', 'CurrentEraInfo', []
)
```

#### Return value
```python
{
    'current_stake_amount': {
        'build_and_earn': 'u128',
        'era': 'u32',
        'period': 'u32',
        'voting': 'u128',
    },
    'next_stake_amount': {
        'build_and_earn': 'u128',
        'era': 'u32',
        'period': 'u32',
        'voting': 'u128',
    },
    'total_locked': 'u128',
    'unlocking': 'u128',
}
```
---------
### DAppTiers
 Information about which tier a dApp belonged to in a specific era.

#### Python
```python
result = substrate.query(
    'DappStaking', 'DAppTiers', ['u32']
)
```

#### Return value
```python
{'dapps': 'scale_info::406', 'period': 'u32', 'rewards': ['u128']}
```
---------
### EraRewards
 Information about rewards for each era.

 Since each entry is a &#x27;span&#x27;, covering up to `T::EraRewardSpanLength` entries, only certain era value keys can exist in storage.
 For the sake of simplicity, valid `era` keys are calculated as:

 era_key = era - (era % T::EraRewardSpanLength)

 This means that e.g. in case `EraRewardSpanLength = 8`, only era values 0, 8, 16, 24, etc. can exist in storage.
 Eras 1-7 will be stored in the same entry as era 0, eras 9-15 will be stored in the same entry as era 8, etc.

#### Python
```python
result = substrate.query(
    'DappStaking', 'EraRewards', ['u32']
)
```

#### Return value
```python
{
    'first_era': 'u32',
    'last_era': 'u32',
    'span': [
        {
            'dapp_reward_pool': 'u128',
            'staked': 'u128',
            'staker_reward_pool': 'u128',
        },
    ],
}
```
---------
### HistoryCleanupMarker
 History cleanup marker - holds information about which DB entries should be cleaned up next, when applicable.

#### Python
```python
result = substrate.query(
    'DappStaking', 'HistoryCleanupMarker', []
)
```

#### Return value
```python
{
    'dapp_tiers_index': 'u32',
    'era_reward_index': 'u32',
    'oldest_valid_era': 'u32',
}
```
---------
### IntegratedDApps
 Map of all dApps integrated into dApp staking protocol.

 Even though dApp is integrated, it does not mean it&#x27;s still actively participating in dApp staking.
 It might have been unregistered at some point in history.

#### Python
```python
result = substrate.query(
    'DappStaking', 'IntegratedDApps', [
    {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
]
)
```

#### Return value
```python
{'id': 'u16', 'owner': 'AccountId', 'reward_beneficiary': (None, 'AccountId')}
```
---------
### Ledger
 General locked/staked information for each account.

#### Python
```python
result = substrate.query(
    'DappStaking', 'Ledger', ['AccountId']
)
```

#### Return value
```python
{
    'contract_stake_count': 'u32',
    'locked': 'u128',
    'staked': {
        'build_and_earn': 'u128',
        'era': 'u32',
        'period': 'u32',
        'voting': 'u128',
    },
    'staked_future': (
        None,
        {
            'build_and_earn': 'u128',
            'era': 'u32',
            'period': 'u32',
            'voting': 'u128',
        },
    ),
    'unlocking': [{'amount': 'u128', 'unlock_block': 'u32'}],
}
```
---------
### NextDAppId
 Counter for unique dApp identifiers.

#### Python
```python
result = substrate.query(
    'DappStaking', 'NextDAppId', []
)
```

#### Return value
```python
'u16'
```
---------
### PeriodEnd
 Information about period&#x27;s end.

#### Python
```python
result = substrate.query(
    'DappStaking', 'PeriodEnd', ['u32']
)
```

#### Return value
```python
{'bonus_reward_pool': 'u128', 'final_era': 'u32', 'total_vp_stake': 'u128'}
```
---------
### Safeguard
 Safeguard to prevent unwanted operations in production.
 Kept as a storage without extrinsic setter, so we can still enable it for some
 chain-fork debugging if required.

#### Python
```python
result = substrate.query(
    'DappStaking', 'Safeguard', []
)
```

#### Return value
```python
'bool'
```
---------
### StakerInfo
 Information about how much each staker has staked for each smart contract in some period.

#### Python
```python
result = substrate.query(
    'DappStaking', 'StakerInfo', [
    'AccountId',
    {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
]
)
```

#### Return value
```python
{
    'loyal_staker': 'bool',
    'previous_staked': {
        'build_and_earn': 'u128',
        'era': 'u32',
        'period': 'u32',
        'voting': 'u128',
    },
    'staked': {
        'build_and_earn': 'u128',
        'era': 'u32',
        'period': 'u32',
        'voting': 'u128',
    },
}
```
---------
### StaticTierParams
 Static tier parameters used to calculate tier configuration.

#### Python
```python
result = substrate.query(
    'DappStaking', 'StaticTierParams', []
)
```

#### Return value
```python
{
    'reward_portion': ['u32'],
    'slot_distribution': ['u32'],
    'tier_thresholds': [
        {
            'DynamicTvlAmount': {'amount': 'u128', 'minimum_amount': 'u128'},
            'FixedTvlAmount': {'amount': 'u128'},
        },
    ],
}
```
---------
### TierConfig
 Tier configuration user for current &amp; preceding eras.

#### Python
```python
result = substrate.query(
    'DappStaking', 'TierConfig', []
)
```

#### Return value
```python
{
    'number_of_slots': 'u16',
    'reward_portion': ['u32'],
    'slots_per_tier': ['u16'],
    'tier_thresholds': [
        {
            'DynamicTvlAmount': {'amount': 'u128', 'minimum_amount': 'u128'},
            'FixedTvlAmount': {'amount': 'u128'},
        },
    ],
}
```
---------
## Constants

---------
### EraRewardSpanLength
 Maximum length of a single era reward span length entry.
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'EraRewardSpanLength')
```
---------
### MaxNumberOfContracts
 Maximum number of contracts that can be integrated into dApp staking at once.
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'MaxNumberOfContracts')
```
---------
### MaxNumberOfStakedContracts
 Maximum amount of stake contract entries an account is allowed to have at once.
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'MaxNumberOfStakedContracts')
```
---------
### MaxUnlockingChunks
 Maximum number of unlocking chunks that can exist per account at a time.
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'MaxUnlockingChunks')
```
---------
### MinimumLockedAmount
 Minimum amount an account has to lock in dApp staking in order to participate.
#### Value
```python
500000000000000000000
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'MinimumLockedAmount')
```
---------
### MinimumStakeAmount
 Minimum amount staker can stake on a contract.
#### Value
```python
500000000000000000000
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'MinimumStakeAmount')
```
---------
### NumberOfTiers
 Number of different tiers.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'NumberOfTiers')
```
---------
### RewardRetentionInPeriods
 Number of periods for which we keep rewards available for claiming.
 After that period, they are no longer claimable.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'RewardRetentionInPeriods')
```
---------
### UnlockingPeriod
 Number of standard eras that need to pass before unlocking chunk can be claimed.
 Even though it&#x27;s expressed in &#x27;eras&#x27;, it&#x27;s actually measured in number of blocks.
#### Value
```python
9
```
#### Python
```python
constant = substrate.get_constant('DappStaking', 'UnlockingPeriod')
```
---------
## Errors

---------
### AccountNotAvailableForDappStaking
Account is not allowed to participate in dApp staking due to some external reason (e.g. account is already a collator).

---------
### ContractAlreadyExists
Smart contract already exists within dApp staking protocol.

---------
### ContractNotFound
Specified smart contract does not exist in dApp staking.

---------
### ContractStillActive
Contract is still active, not unregistered.

---------
### Disabled
Pallet is disabled/in maintenance mode.

---------
### ExceededMaxNumberOfContracts
Maximum number of smart contracts has been reached.

---------
### ForceNotAllowed
Force call is not allowed in production.

---------
### InsufficientStakeAmount
Total staked amount on contract is below the minimum required value.

---------
### InternalClaimBonusError
An unexpected error occurred while trying to claim bonus reward.

---------
### InternalClaimDAppError
An unexpected error occurred while trying to claim dApp reward.

---------
### InternalClaimStakerError
An unexpected error occurred while trying to claim staker rewards.

---------
### InternalStakeError
An unexpected error occurred while trying to stake.

---------
### InternalUnstakeError
An unexpected error occurred while trying to unstake.

---------
### InvalidClaimEra
Claim era is invalid - it must be in history, and rewards must exist for it.

---------
### LockedAmountBelowThreshold
Total locked amount for staker is below minimum threshold.

---------
### NewDAppIdUnavailable
Not possible to assign a new dApp Id.
This should never happen since current type can support up to 65536 - 1 unique dApps.

---------
### NoClaimableRewards
There are no claimable rewards.

---------
### NoDAppTierInfo
No dApp tier info exists for the specified era. This can be because era has expired
or because during the specified era there were no eligible rewards or protocol wasn&\#x27;t active.

---------
### NoExpiredEntries
There are no expired entries to cleanup for the account.

---------
### NoStakingInfo
Account has no staking information for the contract.

---------
### NoUnlockedChunksToClaim
There are no eligible unlocked chunks to claim. This can happen either if no eligible chunks exist, or if user has no chunks at all.

---------
### NoUnlockingChunks
There are no unlocking chunks available to relock.

---------
### NotEligibleForBonusReward
Account is has no eligible stake amount for bonus reward.

---------
### OriginNotOwner
Call origin is not dApp owner.

---------
### PeriodEndsInNextEra
Stake operation is rejected since period ends in the next era.

---------
### RemainingStakePreventsFullUnlock
Remaining stake prevents entire balance of starting the unlocking process.

---------
### RewardExpired
Rewards are no longer claimable since they are too old.

---------
### RewardPayoutFailed
Reward payout has failed due to an unexpected reason.

---------
### TooManyStakedContracts
There are too many contract stake entries for the account. This can be cleaned up by either unstaking or cleaning expired entries.

---------
### TooManyUnlockingChunks
Cannot add additional unlocking chunks due to capacity limit.

---------
### UnavailableStakeFunds
The amount being staked is too large compared to what&\#x27;s available for staking.

---------
### UnclaimedRewards
There are unclaimed rewards remaining from past eras or periods. They should be claimed before attempting any stake modification again.

---------
### UnstakeAmountTooLarge
Unstake amount is greater than the staked amount.

---------
### UnstakeFromPastPeriod
Unstaking is rejected since the period in which past stake was active has passed.

---------
### ZeroAmount
Performing locking or staking with 0 amount.

---------