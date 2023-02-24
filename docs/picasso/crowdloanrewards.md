
# CrowdloanRewards

---------
## Calls

---------
### add
Adds all accounts in the `additions` vector. Add may be called even if the pallet has
been initialized.
#### Attributes
| Name | Type |
| -------- | -------- | 
| additions | `Vec<(RemoteAccountOf<T>, RewardAmountOf<T>, VestingPeriodOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'add', {
    'additions': [
        (
            {
                'Ethereum': '[u8; 20]',
                'RelayChain': 'AccountId',
            },
            'u128',
            'u64',
        ),
    ],
}
)
```

---------
### associate
Associate a reward account. A valid proof has to be provided.
This call also claim the first reward (a.k.a. the first payment, which is a % of the
vested reward).
If logic gate pass, no fees are applied.

The proof should be:
```haskell
proof = sign (concat prefix (hex reward_account))
```
#### Attributes
| Name | Type |
| -------- | -------- | 
| reward_account | `T::AccountId` | 
| proof | `ProofOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'associate', {
    'proof': {
        'Ethereum': '[u8; 65]',
        'RelayChain': (
            'AccountId',
            {
                'Ecdsa': '[u8; 65]',
                'Ed25519': '[u8; 64]',
                'Sr25519': '[u8; 64]',
            },
        ),
    },
    'reward_account': 'AccountId',
}
)
```

---------
### claim
Claim a reward from the associated reward account.
A previous call to `associate` should have been made.
If logic gate pass, no fees are applied.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'claim', {}
)
```

---------
### initialize
Initialize the pallet at the current timestamp.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'initialize', {}
)
```

---------
### initialize_at
Initialize the pallet at the given timestamp.
#### Attributes
| Name | Type |
| -------- | -------- | 
| at | `MomentOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'initialize_at', {'at': 'u64'}
)
```

---------
### populate
Populate pallet by adding more rewards.

Each index in the rewards vector should contain: `remote_account`, `reward_account`,
`vesting_period`.

Can be called multiple times. If an remote account
already has a reward, it will be replaced by the new reward value.

Can only be called before `initialize`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| rewards | `Vec<(RemoteAccountOf<T>, RewardAmountOf<T>, VestingPeriodOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'populate', {
    'rewards': [
        (
            {
                'Ethereum': '[u8; 20]',
                'RelayChain': 'AccountId',
            },
            'u128',
            'u64',
        ),
    ],
}
)
```

---------
### unlock_rewards_for
#### Attributes
| Name | Type |
| -------- | -------- | 
| reward_accounts | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'unlock_rewards_for', {'reward_accounts': ['AccountId']}
)
```

---------
## Events

---------
### Associated
A remote account has been associated with a reward account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| remote_account | `RemoteAccountOf<T>` | ```{'RelayChain': 'AccountId', 'Ethereum': '[u8; 20]'}```
| reward_account | `T::AccountId` | ```AccountId```

---------
### Claimed
A claim has been made.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| remote_account | `RemoteAccountOf<T>` | ```{'RelayChain': 'AccountId', 'Ethereum': '[u8; 20]'}```
| reward_account | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Initialized
The crowdloan has been initialized or set to initialize at some time.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| at | `MomentOf<T>` | ```u64```

---------
### OverFunded
The crowdloan was successfully initialized, but with excess funds that won&\#x27;t be
claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| excess_funds | `T::Balance` | ```u128```

---------
### RewardsAdded
Called after rewards have been added through the `add` extrinsic.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| additions | `Vec<(RemoteAccountOf<T>, RewardAmountOf<T>, VestingPeriodOf<T>)>` | ```[({'RelayChain': 'AccountId', 'Ethereum': '[u8; 20]'}, 'u128', 'u64')]```

---------
### RewardsDeleted
Called after rewards have been deleted through the `delete` extrinsic.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| deletions | `Vec<RemoteAccountOf<T>>` | ```[{'RelayChain': 'AccountId', 'Ethereum': '[u8; 20]'}]```

---------
### RewardsUnlocked
A portion of rewards have been unlocked and future claims will not have locks
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| at | `MomentOf<T>` | ```u64```

---------
## Storage functions

---------
### Associations
 Associations of reward accounts to remote accounts.

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'Associations', ['AccountId']
)
```

#### Return value
```python
{'Ethereum': '[u8; 20]', 'RelayChain': 'AccountId'}
```
---------
### ClaimedRewards
 The rewards claimed so far.

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'ClaimedRewards', []
)
```

#### Return value
```python
'u128'
```
---------
### RemoveRewardLocks
 If set, new locks will not be added to claims

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'RemoveRewardLocks', []
)
```

#### Return value
```python
()
```
---------
### Rewards

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'Rewards', [
    {
        'Ethereum': '[u8; 20]',
        'RelayChain': 'AccountId',
    },
]
)
```

#### Return value
```python
{'claimed': 'u128', 'total': 'u128', 'vesting_period': 'u64'}
```
---------
### TotalContributors
 The total number of contributors.

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'TotalContributors', []
)
```

#### Return value
```python
'u32'
```
---------
### TotalRewards
 The total amount of rewards to be claimed.

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'TotalRewards', []
)
```

#### Return value
```python
'u128'
```
---------
### VestingTimeStart
 The timestamp at which the users are able to claim their rewards.

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'VestingTimeStart', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### InitialPayment
 The upfront liquidity unlocked at first claim.
#### Value
```python
500000000
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'InitialPayment')
```
---------
### LockByDefault
 If claimed amounts should be locked by the pallet
#### Value
```python
True
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'LockByDefault')
```
---------
### LockId
 The unique identifier for locks maintained by this pallet.
#### Value
```python
'0x636c725f6c6f636b'
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'LockId')
```
---------
### OverFundedThreshold
 The percentage of excess funds required to trigger the `OverFunded` event.
#### Value
```python
10000000
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'OverFundedThreshold')
```
---------
### PalletId
 The unique identifier of this pallet.
#### Value
```python
'0x70616c5f63726f77'
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'PalletId')
```
---------
### Prefix
 The arbitrary prefix used for the proof.
#### Value
```python
'picasso-'
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'Prefix')
```
---------
### VestingStep
 The time you have to wait to unlock another part of your reward.
#### Value
```python
86400000
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'VestingStep')
```
---------
### account_id
 The AccountId of this pallet.
#### Value
```python
'5w3oyasYQg6vkbxZKeMG8Dz2evBw1P7Xr7xhVwk4qwwFkm8u'
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'account_id')
```
---------
## Errors

---------
### AlreadyAssociated

---------
### AlreadyInitialized

---------
### BackToTheFuture

---------
### InvalidClaim

---------
### InvalidProof

---------
### NotAssociated

---------
### NotClaimableYet

---------
### NotInitialized

---------
### NothingToClaim

---------
### RewardsNotFunded

---------
### UnexpectedRewardAmount
Returned by `delete` if the provided expected reward mismatches the actual reward.

---------