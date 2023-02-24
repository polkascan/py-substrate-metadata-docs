
# CrowdloanRewards

---------
## Calls

---------
### associate_native_identity
Associate a native rewards_destination identity with a crowdloan contribution.

The caller needs to provide the unassociated relay account and a proof to succeed
with the association
The proof is nothing but a signature over the reward_address using the relay keys
#### Attributes
| Name | Type |
| -------- | -------- | 
| reward_account | `T::AccountId` | 
| relay_account | `T::RelayChainAccountId` | 
| proof | `MultiSignature` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'associate_native_identity', {
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'relay_account': '[u8; 32]',
    'reward_account': '[u8; 20]',
}
)
```

---------
### change_association_with_relay_keys
Change reward account by submitting proofs from relay accounts

The number of valid proofs needs to be bigger than &\#x27;RewardAddressRelayVoteThreshold&\#x27;
The account to be changed needs to be submitted as &\#x27;previous_account&\#x27;
Origin must be RewardAddressChangeOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| reward_account | `T::AccountId` | 
| previous_account | `T::AccountId` | 
| proofs | `Vec<(T::RelayChainAccountId, MultiSignature)>` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'change_association_with_relay_keys', {
    'previous_account': '[u8; 20]',
    'proofs': [
        (
            '[u8; 32]',
            {
                'Ecdsa': '[u8; 65]',
                'Ed25519': '[u8; 64]',
                'Sr25519': '[u8; 64]',
            },
        ),
    ],
    'reward_account': '[u8; 20]',
}
)
```

---------
### claim
Collect whatever portion of your reward are currently vested.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'claim', {}
)
```

---------
### complete_initialization
This extrinsic completes the initialization if some checks are fullfiled. These checks are:
 -The reward contribution money matches the crowdloan pot
 -The end vesting block is higher than the init vesting block
 -The initialization has not complete yet
#### Attributes
| Name | Type |
| -------- | -------- | 
| lease_ending_block | `T::VestingBlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'complete_initialization', {'lease_ending_block': 'u32'}
)
```

---------
### initialize_reward_vec
Initialize the reward distribution storage. It shortcuts whenever an error is found
This does not enforce any checks other than making sure we dont go over funds
complete_initialization should perform any additional
#### Attributes
| Name | Type |
| -------- | -------- | 
| rewards | `Vec<(T::RelayChainAccountId, Option<T::AccountId>, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'initialize_reward_vec', {
    'rewards': [
        (
            '[u8; 32]',
            (None, '[u8; 20]'),
            'u128',
        ),
    ],
}
)
```

---------
### update_reward_address
Update reward address, proving that the caller owns the current native key
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_reward_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanRewards', 'update_reward_address', {'new_reward_account': '[u8; 20]'}
)
```

---------
## Events

---------
### InitialPaymentMade
The initial payment of InitializationPayment % was paid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### InitializedAccountWithNotEnoughContribution
When initializing the reward vec an already initialized account was found
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::RelayChainAccountId` | ```[u8; 32]```
| None | `Option<T::AccountId>` | ```(None, '[u8; 20]')```
| None | `BalanceOf<T>` | ```u128```

---------
### InitializedAlreadyInitializedAccount
When initializing the reward vec an already initialized account was found
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::RelayChainAccountId` | ```[u8; 32]```
| None | `Option<T::AccountId>` | ```(None, '[u8; 20]')```
| None | `BalanceOf<T>` | ```u128```

---------
### NativeIdentityAssociated
Someone has proven they made a contribution and associated a native identity with it.
Data is the relay account,  native account and the total amount of _rewards_ that will be paid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::RelayChainAccountId` | ```[u8; 32]```
| None | `T::AccountId` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### RewardAddressUpdated
A contributor has updated the reward address.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```[u8; 20]```
| None | `T::AccountId` | ```[u8; 20]```

---------
### RewardsPaid
A contributor has claimed some rewards.
Data is the account getting paid and the amount of rewards paid.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AccountsPayable

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'AccountsPayable', ['[u8; 20]']
)
```

#### Return value
```python
{
    'claimed_reward': 'u128',
    'contributed_relay_addresses': ['[u8; 32]'],
    'total_reward': 'u128',
}
```
---------
### ClaimedRelayChainIds

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'ClaimedRelayChainIds', ['[u8; 32]']
)
```

#### Return value
```python
()
```
---------
### EndRelayBlock
 Vesting block height at the initialization of the pallet

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'EndRelayBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### InitRelayBlock
 Vesting block height at the initialization of the pallet

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'InitRelayBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### Initialized

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'Initialized', []
)
```

#### Return value
```python
'bool'
```
---------
### InitializedRewardAmount
 Total initialized amount so far. We store this to make pallet funds == contributors reward
 check easier and more efficient

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'InitializedRewardAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalContributors
 Total number of contributors to aid hinting benchmarking

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
### UnassociatedContributions

#### Python
```python
result = substrate.query(
    'CrowdloanRewards', 'UnassociatedContributions', ['[u8; 32]']
)
```

#### Return value
```python
{
    'claimed_reward': 'u128',
    'contributed_relay_addresses': ['[u8; 32]'],
    'total_reward': 'u128',
}
```
---------
## Constants

---------
### InitializationPayment
 Percentage to be payed at initialization
#### Value
```python
300000000
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'InitializationPayment')
```
---------
### MaxInitContributors
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'MaxInitContributors')
```
---------
### RewardAddressRelayVoteThreshold
 A fraction representing the percentage of proofs
 that need to be presented to change a reward address through the relay keys
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'RewardAddressRelayVoteThreshold')
```
---------
### SignatureNetworkIdentifier
 Network Identifier to be appended into the signatures for reward address change/association
 Prevents replay attacks from one network to the other
#### Value
```python
'moonbeam-'
```
#### Python
```python
constant = substrate.get_constant('CrowdloanRewards', 'SignatureNetworkIdentifier')
```
---------
## Errors

---------
### AlreadyAssociated
User trying to associate a native identity with a relay chain identity for posterior
reward claiming provided an already associated relay chain identity

---------
### BatchBeyondFundPot
Trying to introduce a batch that goes beyond the limits of the funds

---------
### FirstClaimAlreadyDone
First claim already done

---------
### InsufficientNumberOfValidProofs
User submitted an unsifficient number of proofs to change the reward address

---------
### InvalidClaimSignature
User trying to associate a native identity with a relay chain identity for posterior
reward claiming provided a wrong signature

---------
### InvalidFreeClaimSignature
User trying to claim the first free reward provided the wrong signature

---------
### NoAssociatedClaim
User trying to claim an award did not have an claim associated with it. This may mean
they did not contribute to the crowdloan, or they have not yet associated a native id
with their contribution

---------
### NonContributedAddressProvided
User provided a signature from a non-contributor relay account

---------
### RewardNotHighEnough
The contribution is not high enough to be eligible for rewards

---------
### RewardVecAlreadyInitialized
Reward vec has already been initialized

---------
### RewardVecNotFullyInitializedYet
Reward vec has not yet been fully initialized

---------
### RewardsAlreadyClaimed
User trying to claim rewards has already claimed all rewards associated with its
identity and contribution

---------
### RewardsDoNotMatchFund
Rewards should match funds of the pallet

---------
### TooManyContributors
Initialize_reward_vec received too many contributors

---------
### VestingPeriodNonValid
Provided vesting period is not valid

---------