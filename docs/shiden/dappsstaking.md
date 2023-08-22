
# DappsStaking

---------
## Calls

---------
### bond_and_stake
Lock up and stake balance of the origin account.

`value` must be more than the `minimum_balance` specified by `MinimumStakingAmount`
unless account already has bonded value equal or more than &\#x27;minimum_balance&\#x27;.

The dispatch origin for this call must be _Signed_ by the staker&\#x27;s account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `T::SmartContract` | 
| value | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'bond_and_stake', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'value': 'u128',
}
)
```

---------
### burn_stale_reward
Used to burn unclaimed &amp; stale rewards from an unregistered contract.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `T::SmartContract` | 
| era | `EraIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'burn_stale_reward', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'era': 'u32',
}
)
```

---------
### claim_dapp
Claim earned dapp rewards for the specified era.

Call must ensure that the specified era is eligible for reward payout and that it hasn&\#x27;t already been paid out for the dapp.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `T::SmartContract` | 
| era | `EraIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'claim_dapp', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'era': 'u32',
}
)
```

---------
### claim_staker
Claim earned staker rewards for the oldest unclaimed era.
In order to claim multiple eras, this call has to be called multiple times.

The rewards are always added to the staker&\#x27;s free balance (account) but depending on the reward destination configuration,
they might be immediately re-staked.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'claim_staker', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### force_new_era
Force a new era at the start of the next block.

The dispatch origin must be Root.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'force_new_era', {}
)
```

---------
### maintenance_mode
`true` will disable pallet, enabling maintenance mode. `false` will do the opposite.

The dispatch origin must be Root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| enable_maintenance | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'maintenance_mode', {'enable_maintenance': 'bool'}
)
```

---------
### nomination_transfer
Transfer nomination from one contract to another.

Same rules as for `bond_and_stake` and `unbond_and_unstake` apply.
Minor difference is that there is no unbonding period so this call won&\#x27;t
check whether max number of unbonding chunks is exceeded.

#### Attributes
| Name | Type |
| -------- | -------- | 
| origin_contract_id | `T::SmartContract` | 
| value | `Balance` | 
| target_contract_id | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'nomination_transfer', {
    'origin_contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'target_contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'value': 'u128',
}
)
```

---------
### register
Used to register contract for dapps staking.
The origin account used is treated as the `developer` account.

Depending on the pallet configuration/state it is possible that developer needs to be whitelisted prior to registration.

As part of this call, `RegisterDeposit` will be reserved from devs account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| developer | `T::AccountId` | 
| contract_id | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'register', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'developer': 'AccountId',
}
)
```

---------
### set_contract_stake_info
Used to force set `ContractEraStake` storage values.
The purpose of this call is only for fixing one of the issues detected with dapps-staking.

The dispatch origin must be Root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `T::SmartContract` | 
| era | `EraIndex` | 
| contract_stake_info | `ContractStakeInfo` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'set_contract_stake_info', {
    'contract': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'contract_stake_info': {
        'contract_reward_claimed': 'bool',
        'number_of_stakers': 'u32',
        'total': 'u128',
    },
    'era': 'u32',
}
)
```

---------
### set_reward_destination
Used to set reward destination for staker rewards.

User must be an active staker in order to use this call.
This will apply to all existing unclaimed rewards.
#### Attributes
| Name | Type |
| -------- | -------- | 
| reward_destination | `RewardDestination` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'set_reward_destination', {
    'reward_destination': (
        'FreeBalance',
        'StakeBalance',
    ),
}
)
```

---------
### unbond_and_unstake
Start unbonding process and unstake balance from the contract.

The unstaked amount will no longer be eligible for rewards but still won&\#x27;t be unlocked.
User needs to wait for the unbonding period to finish before being able to withdraw
the funds via `withdraw_unbonded` call.

In case remaining staked balance on contract is below minimum staking amount,
entire stake for that contract will be unstaked.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `T::SmartContract` | 
| value | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'unbond_and_unstake', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'value': 'u128',
}
)
```

---------
### unregister
Unregister existing contract from dapps staking, making it ineligible for rewards from current era onwards.
This must be called by the root (at the moment).

Deposit is returned to the developer but existing stakers should manually call `withdraw_from_unregistered` if they wish to to unstake.

**Warning**: After this action ,contract can not be registered for dapps staking again.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'unregister', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### withdraw_from_unregistered
Withdraw locked funds from a contract that was unregistered.

Funds don&\#x27;t need to undergo the unbonding period - they are returned immediately to the staker&\#x27;s free balance.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `T::SmartContract` | 

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'withdraw_from_unregistered', {
    'contract_id': {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
}
)
```

---------
### withdraw_unbonded
Withdraw all funds that have completed the unbonding process.

If there are unbonding chunks which will be fully unbonded in future eras,
they will remain and can be withdrawn later.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DappsStaking', 'withdraw_unbonded', {}
)
```

---------
## Events

---------
### BondAndStake
Account has bonded and staked funds on a smart contract.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| None | `Balance` | ```u128```

---------
### ContractRemoved
Contract removed from dapps staking.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```

---------
### MaintenanceMode
Maintenance mode has been enabled or disabled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
### NewContract
New contract added for staking.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```

---------
### NewDappStakingEra
New dapps staking era. Distribute era rewards to contracts.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EraIndex` | ```u32```

---------
### NominationTransfer
Nomination part has been transfered from one contract to another.

\(staker account, origin smart contract, amount, target smart contract\)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| None | `Balance` | ```u128```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```

---------
### Reward
Reward paid to staker or developer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| None | `EraIndex` | ```u32```
| None | `Balance` | ```u128```

---------
### RewardDestination
Reward handling modified
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `RewardDestination` | ```('FreeBalance', 'StakeBalance')```

---------
### StaleRewardBurned
Stale, unclaimed reward from an unregistered contract has been burned.

\(developer account, smart contract, era, amount burned\)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| None | `EraIndex` | ```u32```
| None | `Balance` | ```u128```

---------
### UnbondAndUnstake
Account has unbonded &amp; unstaked some funds. Unbonding process begins.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| None | `Balance` | ```u128```

---------
### WithdrawFromUnregistered
Account has fully withdrawn all staked amount from an unregistered contract.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::SmartContract` | ```{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}```
| None | `Balance` | ```u128```

---------
### Withdrawn
Account has withdrawn unbonded funds.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### BlockRewardAccumulator
 Accumulator for block rewards during an era. It is reset at every new era

#### Python
```python
result = substrate.query(
    'DappsStaking', 'BlockRewardAccumulator', []
)
```

#### Return value
```python
{'dapps': 'u128', 'stakers': 'u128'}
```
---------
### ContractEraStake
 Staking information about contract in a particular era.

#### Python
```python
result = substrate.query(
    'DappsStaking', 'ContractEraStake', [
    {
        'Evm': '[u8; 20]',
        'Wasm': 'AccountId',
    },
    'u32',
]
)
```

#### Return value
```python
{
    'contract_reward_claimed': 'bool',
    'number_of_stakers': 'u32',
    'total': 'u128',
}
```
---------
### CurrentEra
 The current era index.

#### Python
```python
result = substrate.query(
    'DappsStaking', 'CurrentEra', []
)
```

#### Return value
```python
'u32'
```
---------
### ForceEra
 Mode of era forcing.

#### Python
```python
result = substrate.query(
    'DappsStaking', 'ForceEra', []
)
```

#### Return value
```python
('NotForcing', 'ForceNew')
```
---------
### GeneralEraInfo
 General information about an era like TVL, total staked value, rewards.

#### Python
```python
result = substrate.query(
    'DappsStaking', 'GeneralEraInfo', ['u32']
)
```

#### Return value
```python
{'locked': 'u128', 'rewards': {'dapps': 'u128', 'stakers': 'u128'}, 'staked': 'u128'}
```
---------
### GeneralStakerInfo
 Info about stakers stakes on particular contracts.

#### Python
```python
result = substrate.query(
    'DappsStaking', 'GeneralStakerInfo', [
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
{'stakes': [{'era': 'u32', 'staked': 'u128'}]}
```
---------
### Ledger
 General information about the staker (non-smart-contract specific).

#### Python
```python
result = substrate.query(
    'DappsStaking', 'Ledger', ['AccountId']
)
```

#### Return value
```python
{
    'locked': 'u128',
    'reward_destination': ('FreeBalance', 'StakeBalance'),
    'unbonding_info': {
        'unlocking_chunks': [{'amount': 'u128', 'unlock_era': 'u32'}],
    },
}
```
---------
### NextEraStartingBlock
 Stores the block number of when the next era starts

#### Python
```python
result = substrate.query(
    'DappsStaking', 'NextEraStartingBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### PalletDisabled
 Denotes whether pallet is disabled (in maintenance mode) or not

#### Python
```python
result = substrate.query(
    'DappsStaking', 'PalletDisabled', []
)
```

#### Return value
```python
'bool'
```
---------
### RegisteredDapps
 Simple map where smart contract points to basic info about it (e.g. developer address, state)

#### Python
```python
result = substrate.query(
    'DappsStaking', 'RegisteredDapps', [
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
    'developer': 'AccountId',
    'state': {'Registered': None, 'Unregistered': 'u32'},
}
```
---------
### RegisteredDevelopers
 Simple map where developer account points to their smart contract

#### Python
```python
result = substrate.query(
    'DappsStaking', 'RegisteredDevelopers', ['AccountId']
)
```

#### Return value
```python
{'Evm': '[u8; 20]', 'Wasm': 'AccountId'}
```
---------
### StorageVersion
 Stores the current pallet storage version.

#### Python
```python
result = substrate.query(
    'DappsStaking', 'StorageVersion', []
)
```

#### Return value
```python
('V1_0_0', 'V2_0_0', 'V3_0_0', 'V4_0_0')
```
---------
## Constants

---------
### BlockPerEra
 Number of blocks per era.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'BlockPerEra')
```
---------
### MaxEraStakeValues
 Max number of unique `EraStake` values that can exist for a `(staker, contract)` pairing.
 When stakers claims rewards, they will either keep the number of `EraStake` values the same or they will reduce them by one.
 Stakers cannot add an additional `EraStake` value by calling `bond&amp;stake` or `unbond&amp;unstake` if they&#x27;ve reached the max number of values.

 This ensures that history doesn&#x27;t grow indefinitely - if there are too many chunks, stakers should first claim their former rewards
 before adding additional `EraStake` values.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'MaxEraStakeValues')
```
---------
### MaxNumberOfStakersPerContract
 Maximum number of unique stakers per contract.
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'MaxNumberOfStakersPerContract')
```
---------
### MaxUnlockingChunks
 Max number of unlocking chunks per account Id &lt;-&gt; contract Id pairing.
 If value is zero, unlocking becomes impossible.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'MaxUnlockingChunks')
```
---------
### MinimumRemainingAmount
 Minimum amount that should be left on staker account after staking.
 Serves as a safeguard to prevent users from locking their entire free balance.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'MinimumRemainingAmount')
```
---------
### MinimumStakingAmount
 Minimum amount user must have staked on contract.
 User can stake less if they already have the minimum staking amount staked on that particular contract.
#### Value
```python
50000000000000000000
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'MinimumStakingAmount')
```
---------
### PalletId
 Dapps staking pallet Id
#### Value
```python
'0x70792f6470737374'
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'PalletId')
```
---------
### RegisterDeposit
 Deposit that will be reserved as part of new contract registration.
#### Value
```python
100000000000000000000
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'RegisterDeposit')
```
---------
### UnbondingPeriod
 Number of eras that need to pass until unstaked value can be withdrawn.
 Current era is always counted as full era (regardless how much blocks are remaining).
 When set to `0`, it&#x27;s equal to having no unbonding period.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'UnbondingPeriod')
```
---------
### UnregisteredDappRewardRetention
 Number of eras that need to pass until dApp rewards for the unregistered contracts can be burned.
 Developer can still claim rewards after this period has passed, iff it hasn&#x27;t been burned yet.

 For example, if retention is set to `2` and current era is `10`, it means that all unclaimed rewards bellow era `8` can be burned.
#### Value
```python
7
```
#### Python
```python
constant = substrate.get_constant('DappsStaking', 'UnregisteredDappRewardRetention')
```
---------
## Errors

---------
### AlreadyClaimedInThisEra
Contract already claimed in this era and reward is distributed

---------
### AlreadyRegisteredContract
The contract is already registered by other account

---------
### AlreadyUsedDeveloperAccount
This account was already used to register contract

---------
### Disabled
Disabled

---------
### EraOutOfBounds
Era parameter is out of bounds

---------
### InsufficientValue
Can not stake with value less than minimum staking value

---------
### MaxNumberOfStakersExceeded
Number of stakers per contract exceeded.

---------
### NoMaintenanceModeChange
No change in maintenance mode

---------
### NominationTransferToSameContract
Transfering nomination to the same contract

---------
### NotActiveStaker
Account is not actively staking

---------
### NotOperatedContract
Targets must be operated contracts

---------
### NotOwnedContract
Smart contract not owned by the account id.

---------
### NotStakedContract
Contract isn&\#x27;t staked.

---------
### NotUnregisteredContract
Contract isn&\#x27;t unregistered.

---------
### NothingToWithdraw
There are no previously unbonded funds that can be unstaked and withdrawn.

---------
### StakingWithNoValue
Can not stake with zero value.

---------
### TooManyEraStakeValues
Too many active `EraStake` values for (staker, contract) pairing.
Claim existing rewards to fix this problem.

---------
### TooManyUnlockingChunks
Contract has too many unlocking chunks. Withdraw the existing chunks if possible
or wait for current chunks to complete unlocking process to withdraw them.

---------
### UnclaimedRewardsRemaining
Unclaimed rewards should be claimed before withdrawing stake.

---------
### UnexpectedStakeInfoEra
Report issue on github if this is ever emitted

---------
### UnknownEraReward
Report issue on github if this is ever emitted

---------
### UnstakingWithNoValue
Unstaking a contract with zero value

---------
### UpgradeTooHeavy
Upgrade is too heavy, reduce the weight parameter.

---------