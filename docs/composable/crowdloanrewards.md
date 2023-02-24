
# CrowdloanRewards

---------
## Calls

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
            '[u8; 32]',
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
Initialize the pallet at the current transaction block.
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
Initialize the pallet at the given transaction block.
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
Can be called multiple times. If an remote account already has a reward, it will be
replaced by the new reward value.
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
                'RelayChain': '[u8; 32]',
            },
            'u128',
            'u64',
        ),
    ],
}
)
```

---------
## Events

---------
### Associated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| remote_account | `RemoteAccountOf<T>` | ```{'RelayChain': '[u8; 32]', 'Ethereum': '[u8; 20]'}```
| reward_account | `T::AccountId` | ```AccountId```

---------
### Claimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| remote_account | `RemoteAccountOf<T>` | ```{'RelayChain': '[u8; 32]', 'Ethereum': '[u8; 20]'}```
| reward_account | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Initialized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| at | `MomentOf<T>` | ```u64```

---------
## Storage functions

---------
### Associations
 Associate a local account with a remote one.

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'Associations', ['AccountId']
)
```

#### Return value
```python
{'Ethereum': '[u8; 20]', 'RelayChain': '[u8; 32]'}
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
### Rewards

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'Rewards', [
    {
        'Ethereum': '[u8; 20]',
        'RelayChain': '[u8; 32]',
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
 The block at which the users are able to claim their rewards.

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
250000000
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'InitialPayment')
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
 The arbitrary prefix used for the proof
#### Value
```python
'composable-'
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
604800000
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