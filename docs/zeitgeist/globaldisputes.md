
# GlobalDisputes

---------
## Calls

---------
### add_vote_outcome
Add voting outcome to a global dispute in exchange for a constant fee.
Errors if the voting outcome already exists or
if the global dispute has not started or has already finished.

\# Arguments

- `market_id`: The id of the market.
- `outcome`: The outcome report to add.

\# Weight

Complexity: `O(n)`, where `n` is the number of owner(s) of the winner outcome
in the case that this gets called for an already finished global dispute.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| outcome | `OutcomeReport` | 

#### Python
```python
call = substrate.compose_call(
    'GlobalDisputes', 'add_vote_outcome', {
    'market_id': 'u128',
    'outcome': {
        'Categorical': 'u16',
        'Scalar': 'u128',
    },
}
)
```

---------
### purge_outcomes
Purge all outcomes to allow the winning outcome owner(s) to get their reward.
Fails if the global dispute is not concluded yet.

\# Arguments

- `market_id`: The id of the market.

\# Weight

Complexity: `O(n)`,
where `n` is the number of all existing outcomes for a global dispute.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'GlobalDisputes', 'purge_outcomes', {'market_id': 'u128'}
)
```

---------
### refund_vote_fees
Return the voting outcome fees in case the global dispute was destroyed.

\# Arguments

- `market_id`: The id of the market.

\# Weight

Complexity: `O(n)`,
where `n` is the number of all existing outcomes for a global dispute.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'GlobalDisputes', 'refund_vote_fees', {'market_id': 'u128'}
)
```

---------
### reward_outcome_owner
Reward the collected fees to the owner(s) of a voting outcome.
Fails if outcomes is not already purged.

\# Arguments

- `market_id`: The id of the market.

\# Weight

Complexity: `O(n)`, where `n` is the number of owners for the winning outcome.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'GlobalDisputes', 'reward_outcome_owner', {'market_id': 'u128'}
)
```

---------
### unlock_vote_balance
Return all locked native tokens from a finished or destroyed global dispute.
Fails if the global dispute is not concluded yet.

\# Arguments

- `voter`: The account id lookup to unlock funds for.

\# Weight

Complexity: `O(n + m)`, where `n` is the number of all current votes on global disputes,
and `m` is the number of owners for the winning outcome.
#### Attributes
| Name | Type |
| -------- | -------- | 
| voter | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'GlobalDisputes', 'unlock_vote_balance', {
    'voter': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### vote_on_outcome
Vote on existing voting outcomes by locking native tokens.
Fails if the global dispute has not started or has already finished.

\# Arguments

- `market_id`: The id of the market.
- `outcome`: The existing outcome report to vote on.
- `amount`: The amount to vote with.

\# Weight

Complexity: `O(n + m)`, where `n` is the number of all current votes on global disputes,
and `m` is the number of owners for the specified outcome.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| outcome | `OutcomeReport` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'GlobalDisputes', 'vote_on_outcome', {
    'amount': 'u128',
    'market_id': 'u128',
    'outcome': {
        'Categorical': 'u16',
        'Scalar': 'u128',
    },
}
)
```

---------
## Events

---------
### AddedVotingOutcome
A new voting outcome has been added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```
| owner | `AccountIdOf<T>` | ```AccountId```
| outcome | `OutcomeReport` | ```{'Categorical': 'u16', 'Scalar': 'u128'}```

---------
### GlobalDisputeWinnerDetermined
The winner of the global dispute system is determined.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```

---------
### OutcomeOwnerRewarded
The outcome owner has been rewarded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```
| owner | `AccountIdOf<T>` | ```AccountId```

---------
### OutcomeOwnersRewarded
The outcome owners have been rewarded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```
| owners | `Vec<AccountIdOf<T>>` | ```['AccountId']```

---------
### OutcomesFullyCleaned
The outcomes storage item is fully cleaned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```

---------
### OutcomesPartiallyCleaned
The outcomes storage item is partially cleaned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```

---------
### VotedOnOutcome
A vote happened on an outcome.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| voter | `AccountIdOf<T>` | ```AccountId```
| market_id | `MarketIdOf<T>` | ```u128```
| outcome | `OutcomeReport` | ```{'Categorical': 'u16', 'Scalar': 'u128'}```
| vote_amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### GlobalDisputesInfo
 Maps the market id to all information
 about the global dispute.

#### Python
```python
result = substrate.query(
    'GlobalDisputes', 'GlobalDisputesInfo', ['u128']
)
```

#### Return value
```python
{
    'outcome_info': {
        'outcome_sum': 'u128',
        'possession': {
            'Paid': {'fee': 'u128', 'owner': 'AccountId'},
            'Shared': {'owners': ['AccountId']},
        },
    },
    'status': {'Active': {'add_outcome_end': 'u64', 'vote_end': 'u64'}, 'Destroyed': None, 'Finished': None},
    'winner_outcome': {'Categorical': 'u16', 'Scalar': 'u128'},
}
```
---------
### Locks
 All highest lock information (vote id, outcome index and locked balance)
 for a particular voter.

 TWOX-NOTE: SAFE as `AccountId`s are crypto hashes anyway.

#### Python
```python
result = substrate.query(
    'GlobalDisputes', 'Locks', ['AccountId']
)
```

#### Return value
```python
[('u128', 'u128')]
```
---------
### Outcomes
 Maps the market id to the outcome and providing information about the outcome.

#### Python
```python
result = substrate.query(
    'GlobalDisputes', 'Outcomes', [
    'u128',
    {
        'Categorical': 'u16',
        'Scalar': 'u128',
    },
]
)
```

#### Return value
```python
{
    'outcome_sum': 'u128',
    'possession': {
        'Paid': {'fee': 'u128', 'owner': 'AccountId'},
        'Shared': {'owners': ['AccountId']},
    },
}
```
---------
### Winners

#### Python
```python
result = substrate.query(
    'GlobalDisputes', 'Winners', ['u128']
)
```

#### Return value
```python
{
    'is_finished': 'bool',
    'outcome': {'Categorical': 'u16', 'Scalar': 'u128'},
    'outcome_info': {'outcome_sum': 'u128', 'owners': ['AccountId']},
}
```
---------
## Constants

---------
### AddOutcomePeriod
 The time period in which the addition of new outcomes are allowed.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'AddOutcomePeriod')
```
---------
### GdVotingPeriod
 The time period in which votes are allowed.
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'GdVotingPeriod')
```
---------
### GlobalDisputeLockId
 The vote lock identifier.
#### Value
```python
'0x7a67652f67646c6b'
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'GlobalDisputeLockId')
```
---------
### GlobalDisputesPalletId
 The pallet identifier.
#### Value
```python
'0x7a67652f676c6470'
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'GlobalDisputesPalletId')
```
---------
### MaxGlobalDisputeVotes
 The maximum numbers of distinct markets
 on which one account can simultaneously vote on outcomes.
 When the user unlocks, the user has again `MaxGlobalDisputeVotes` number of votes.
 This constant is useful to limit the number of for-loop iterations (weight constraints).
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'MaxGlobalDisputeVotes')
```
---------
### MaxOwners
 The maximum number of owners
 for a voting outcome for private API calls of `push_vote_outcome`.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'MaxOwners')
```
---------
### MinOutcomeVoteAmount
 The minimum required amount to vote on an outcome.
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'MinOutcomeVoteAmount')
```
---------
### RemoveKeysLimit
 The maximum number of keys to remove from a storage map.
#### Value
```python
250
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'RemoveKeysLimit')
```
---------
### VotingOutcomeFee
 The fee required to add a voting outcome.
#### Value
```python
2000000000000
```
#### Python
```python
constant = substrate.get_constant('GlobalDisputes', 'VotingOutcomeFee')
```
---------
## Errors

---------
### AddOutcomePeriodIsOver
The period in which outcomes can be added is over.

---------
### AmountTooLow
Sender tried to vote with an amount below a defined minimum.

---------
### GlobalDisputeAlreadyExists
The global dispute was already started.

---------
### GlobalDisputeNotDestroyed
The operation requires a global dispute in a destroyed state.

---------
### GlobalDisputeNotFound
No global dispute present at the moment.

---------
### InsufficientAmount
Sender does not have enough funds for the vote on an outcome.

---------
### InvalidGlobalDisputeStatus
The global dispute status is invalid for this operation.

---------
### MaxOwnersReached
The maximum amount of owners is reached.

---------
### MaxVotesReached
The maximum number of votes for this account is reached.

---------
### NoFundsToReward
The amount in the reward pot is zero.

---------
### NotInGdVotingPeriod
It is not inside the period in which votes are allowed.

---------
### OutcomeAlreadyExists
The voting outcome has been already added.

---------
### OutcomeDoesNotExist
The outcome specified is not present in the voting outcomes.

---------
### OutcomeMismatch
Submitted outcome does not match market type.

---------
### OutcomesNotFullyCleaned
The outcomes are not fully cleaned yet.

---------
### SharedPossessionRequired
Only a shared possession is allowed.

---------
### UnfinishedGlobalDispute
The global dispute period is not over yet. The winner is not yet determined.

---------