
# DaoDemocracy

---------
## Calls

---------
### cancel_vote
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'cancel_vote', {'dao_id': 'u64', 'index': 'u32'}
)
```

---------
### enact_proposal
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'enact_proposal', {'dao_id': 'u64', 'index': 'u32'}
)
```

---------
### propose
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| proposal | `Box<<T as dao::Config>::Call>` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'propose', {
    'dao_id': 'u64',
    'proposal': 'Call',
    'value': 'u128',
}
)
```

---------
### second
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| proposal | `PropIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'second', {'dao_id': 'u64', 'proposal': 'u32'}
)
```

---------
### set_enactment_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'set_enactment_period', {'dao_id': 'u64', 'period': 'u32'}
)
```

---------
### set_launch_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'set_launch_period', {'dao_id': 'u64', 'period': 'u32'}
)
```

---------
### set_max_public_props
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| max | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'set_max_public_props', {'dao_id': 'u64', 'max': 'u32'}
)
```

---------
### set_min_vote_weight_for_every_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| call | `Box<<T as dao::Config>::Call>` | 
| min_vote_weight | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'set_min_vote_weight_for_every_call', {
    'call': 'Call',
    'dao_id': 'u64',
    'min_vote_weight': 'u128',
}
)
```

---------
### set_minimum_deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| min | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'set_minimum_deposit', {'dao_id': 'u64', 'min': 'u128'}
)
```

---------
### set_rerserve_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'set_rerserve_period', {'dao_id': 'u64', 'period': 'u32'}
)
```

---------
### set_voting_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'set_voting_period', {'dao_id': 'u64', 'period': 'u32'}
)
```

---------
### start_table
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'start_table', {'dao_id': 'u64'}
)
```

---------
### unlock
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'unlock', {}
)
```

---------
### unreserve
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'unreserve', {}
)
```

---------
### vote
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| index | `ReferendumIndex` | 
| vote | `T::Vote` | 
| conviction | `T::Conviction` | 
| attitude | `Attitude` | 

#### Python
```python
call = substrate.compose_call(
    'DaoDemocracy', 'vote', {
    'attitude': ('AYES', 'NAYS'),
    'conviction': (
        'X1',
        'X2',
        'X3',
        'X6',
    ),
    'dao_id': 'u64',
    'index': 'u32',
    'vote': {
        'FungibleAmount': 'u128',
        'NftTokenId': 'u32',
    },
}
)
```

---------
## Events

---------
### CancelVote
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `ReferendumIndex` | ```u32```

---------
### EnactProposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| index | `ReferendumIndex` | ```u32```
| result | `DResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Proposed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `T::Hash` | ```[u8; 32]```

---------
### Second
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### SetEnactmentPeriod
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| period | `T::BlockNumber` | ```u32```

---------
### SetLaunchPeriod
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| period | `T::BlockNumber` | ```u32```

---------
### SetMaxPublicProps
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| max | `u32` | ```u32```

---------
### SetMinVoteWeight
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `T::CallId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### SetMinimumDeposit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| min | `BalanceOf<T>` | ```u128```

---------
### SetReservePeriod
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| period | `T::BlockNumber` | ```u32```

---------
### SetVotingPeriod
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| period | `T::BlockNumber` | ```u32```

---------
### StartTable
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `ReferendumIndex` | ```u32```

---------
### Unlock
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::ConcreteId` | ```{'NftClassId': 'u32', 'FungibleTokenId': 'u32'}```
| None | `T::Vote` | ```{'NftTokenId': 'u32', 'FungibleAmount': 'u128'}```

---------
### Unreserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Vote
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `ReferendumIndex` | ```u32```
| None | `T::Vote` | ```{'NftTokenId': 'u32', 'FungibleAmount': 'u128'}```

---------
## Storage functions

---------
### DepositOf
 Those who have locked a deposit.

 TWOX-NOTE: Safe, as increasing integer keys are safe.

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'DepositOf', ['u64', 'u32']
)
```

#### Return value
```python
(['AccountId'], 'u128')
```
---------
### EnactmentPeriod

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'EnactmentPeriod', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### LaunchPeriod

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'LaunchPeriod', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### LaunchTag

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'LaunchTag', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### MaxPublicProps

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'MaxPublicProps', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### MinVoteWeightOf

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'MinVoteWeightOf', ['u64', 'u32']
)
```

#### Return value
```python
'u128'
```
---------
### MinimumDeposit

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'MinimumDeposit', ['u64']
)
```

#### Return value
```python
'u128'
```
---------
### PublicPropCount

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'PublicPropCount', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### PublicProps
 The public proposals. Unsorted. The second item is the proposal&#x27;s hash.

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'PublicProps', ['u64']
)
```

#### Return value
```python
[('u32', '[u8; 32]', 'Call', 'AccountId')]
```
---------
### ReferendumCount

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'ReferendumCount', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### ReferendumInfoOf

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'ReferendumInfoOf', ['u64', 'u32']
)
```

#### Return value
```python
{
    'Finished': {'approved': 'bool', 'end': 'u32'},
    'Ongoing': {
        'delay': 'u32',
        'end': 'u32',
        'proposal': 'Call',
        'tally': {'ayes': 'u128', 'nays': 'u128'},
    },
}
```
---------
### ReserveOf

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'ReserveOf', ['AccountId']
)
```

#### Return value
```python
[('u128', 'u32')]
```
---------
### ReservePeriod

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'ReservePeriod', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### VotesOf

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'VotesOf', ['AccountId']
)
```

#### Return value
```python
[
    {
        'attitude': ('AYES', 'NAYS'),
        'concrete_id': {'FungibleTokenId': 'u32', 'NftClassId': 'u32'},
        'referendum_index': 'u32',
        'unlock_block': 'u32',
        'vote': {'FungibleAmount': 'u128', 'NftTokenId': 'u32'},
        'vote_weight': 'u128',
    },
]
```
---------
### VotingPeriod

#### Python
```python
result = substrate.query(
    'DaoDemocracy', 'VotingPeriod', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### GetNativeCurrencyId
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('DaoDemocracy', 'GetNativeCurrencyId')
```
---------
## Errors

---------
### InDelayTime

---------
### NoneWaiting

---------
### NotTableTime

---------
### Overflow

---------
### ProposalMissing

---------
### ReferendumFinished

---------
### ReferendumNotExists

---------
### TooManyProposals

---------
### ValueLow

---------
### VoteEnd

---------
### VoteEndButNotPass

---------
### VoteError

---------
### VoteNotEnd

---------
### VoteNotEnough

---------
### VoteNotExists

---------
### VoteWeightTooLow

---------