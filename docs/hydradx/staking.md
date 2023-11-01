
# Staking

---------
## Calls

---------
### claim
Claim rewards accumulated for specific staking position.

Function calculates amount of rewards to pay for specified staking position based on
the amount of points position accumulated. Function also unlocks all the rewards locked
from `increase_stake` based on the amount of the points.

This action is penalized by removing all the points and returning allocated unpaid rewards
for redistribution.

Parameters:
- `position_id`: The identifier of the position to claim rewards for.

Emits `RewardsClaimed` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| position_id | `T::PositionItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'claim', {'position_id': 'u128'}
)
```

---------
### increase_stake
Extrinsic to increase staked amount of existing staking position by specified `amount`.

`increase_stake` increases staked amount of position specified by `postion_id` by the
`amount` specified by the user.
Staking position must exist and `origin` has to be the owner of the position.
Users can stake tokens which are not vested or already staked.
Position&\#x27;s params e.g points are updated to offset stake increase and rewards
accumulated until this point are paid and locked to the user.

Parameters:
- `position_id`: The identifier of the position which stake will be increased.
- `amount`: Amount of native asset to be added to staked amount. `amount` can&\#x27;t be vested or
already staked

Emits `StakeAdded` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| position_id | `T::PositionItemId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'increase_stake', {
    'amount': 'u128',
    'position_id': 'u128',
}
)
```

---------
### initialize_staking
Staking pallet initialization. This call will reserved `pot`&\#x27;s balance to prevent
account dusting and start collecting fees from trades as rewards.

`pot`’s account has to have a balance which will be reserved to prevent account dusting.

Emits `StakingInitialized` event when successful.

#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Staking', 'initialize_staking', {}
)
```

---------
### stake
Stake `amount` into a new staking position.

`stake` locks specified `amount` into staking and creates new NFT representing staking
position.
Users can stake `NativeAssetId` balance which is not vested or already staked.

Staking pallet must be initialized otherwise extrinsic will fail with error.

Parameters:
- `amount`: Amount of native asset to be staked. `amount` can&\#x27;t be vested or already
staked

Emits `PositionCreated` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'stake', {'amount': 'u128'}
)
```

---------
### unstake
Function pays rewards, unlocks all the staked assets and destroys staking position
specified by `position_id`.

Function calculates and pays latest rewards, unlocks all the locked rewards and staked
tokens for staking position and burns NFT representing staking position.
Unpaid allocated rewards are returned to the Staking for redistribution.

Parameters:
- `position_id`: The identifier of the position to be destroyed.

Emits `RewardsClaimed` and `Unstaked` events when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| position_id | `T::PositionItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'unstake', {'position_id': 'u128'}
)
```

---------
## Events

---------
### AccumulatedRpsUpdated
Staking&\#x27;s `accumulated_reward_per_stake` was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| accumulated_rps | `FixedU128` | ```u128```
| total_stake | `Balance` | ```u128```

---------
### PositionCreated
New staking position was created and NFT was minted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| position_id | `T::PositionItemId` | ```u128```
| stake | `Balance` | ```u128```

---------
### RewardsClaimed
Rewards were claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| position_id | `T::PositionItemId` | ```u128```
| paid_rewards | `Balance` | ```u128```
| unlocked_rewards | `Balance` | ```u128```
| slashed_points | `Point` | ```u128```
| slashed_unpaid_rewards | `Balance` | ```u128```
| payable_percentage | `FixedU128` | ```u128```

---------
### StakeAdded
Staked amount for existing position was increased.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| position_id | `T::PositionItemId` | ```u128```
| stake | `Balance` | ```u128```
| total_stake | `Balance` | ```u128```
| locked_rewards | `Balance` | ```u128```
| slashed_points | `Point` | ```u128```
| payable_percentage | `FixedU128` | ```u128```

---------
### StakingInitialized
Staking was initialized.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| non_dustable_balance | `Balance` | ```u128```

---------
### Unstaked
Staked amount was withdrawn and NFT was burned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| position_id | `T::PositionItemId` | ```u128```
| unlocked_stake | `Balance` | ```u128```

---------
## Storage functions

---------
### NextPositionId
 Position ids sequencer.

#### Python
```python
result = substrate.query(
    'Staking', 'NextPositionId', []
)
```

#### Return value
```python
'u128'
```
---------
### PositionVotes
 List of position votes.

#### Python
```python
result = substrate.query(
    'Staking', 'PositionVotes', ['u128']
)
```

#### Return value
```python
{
    'votes': [
        (
            'u32',
            {
                'amount': 'u128',
                'conviction': (
                    'None',
                    'Locked1x',
                    'Locked2x',
                    'Locked3x',
                    'Locked4x',
                    'Locked5x',
                    'Locked6x',
                ),
            },
        ),
    ],
}
```
---------
### Positions
 User&#x27;s position state.

#### Python
```python
result = substrate.query(
    'Staking', 'Positions', ['u128']
)
```

#### Return value
```python
{
    'accumulated_locked_rewards': 'u128',
    'accumulated_slash_points': 'u128',
    'accumulated_unpaid_rewards': 'u128',
    'action_points': 'u128',
    'created_at': 'u32',
    'reward_per_stake': 'u128',
    'stake': 'u128',
}
```
---------
### Staking
 Global staking state.

#### Python
```python
result = substrate.query(
    'Staking', 'Staking', []
)
```

#### Return value
```python
{
    'accumulated_reward_per_stake': 'u128',
    'pot_reserved_balance': 'u128',
    'total_stake': 'u128',
}
```
---------
## Constants

---------
### ActionPointsWeight
 Weight of the action points in total points calculations.
#### Value
```python
200000000
```
#### Python
```python
constant = substrate.get_constant('Staking', 'ActionPointsWeight')
```
---------
### CurrentStakeWeight
 Weight of the actual stake in slash points calculation. Bigger the value lower the calculated slash points.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('Staking', 'CurrentStakeWeight')
```
---------
### MaxVotes
 Max amount of votes the user can have at any time.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MaxVotes')
```
---------
### MinStake
 Min amount user must stake.
#### Value
```python
1000000000000000
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MinStake')
```
---------
### NFTCollectionId
 NFT collection id.
#### Value
```python
2222
```
#### Python
```python
constant = substrate.get_constant('Staking', 'NFTCollectionId')
```
---------
### NativeAssetId
 Native Asset ID.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Staking', 'NativeAssetId')
```
---------
### PalletId
 Pallet id.
#### Value
```python
'0x7374616b696e6723'
```
#### Python
```python
constant = substrate.get_constant('Staking', 'PalletId')
```
---------
### PeriodLength
 Staking period length in blocks.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Staking', 'PeriodLength')
```
---------
### TimePointsPerPeriod
 Number of time points users receive for each period.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Staking', 'TimePointsPerPeriod')
```
---------
### TimePointsWeight
 Weight of the time points in total points calculations.
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('Staking', 'TimePointsWeight')
```
---------
### UnclaimablePeriods
 Number of periods user can&#x27;t claim rewards for. User can exit but won&#x27;t receive any rewards.
 If he stay longer than `UnclaimablePeriods` he will receive rewards also for these periods.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Staking', 'UnclaimablePeriods')
```
---------
## Errors

---------
### AlreadyInitialized
Staking is already initialized.

---------
### Arithmetic
Arithmetic error.

---------
### Forbidden
Signer is not an owner of the staking position.

---------
### InconsistentState
Action cannot be completed because unexpected error has occurred. This should be reported
to protocol maintainers.

---------
### InsufficientBalance
Balance is too low.

---------
### InsufficientStake
Staked amount is too low.

---------
### MaxVotesReached
Maximum amount of votes were reached for staking position.

---------
### MissingPotBalance
Pot&\#x27;s balance is zero.

---------
### NotInitialized
Staking is not initialized.

---------
### PositionAlreadyExists
Account&\#x27;s position already exists.

---------
### PositionNotFound
Staking position has not been found.

---------