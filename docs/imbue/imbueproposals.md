
# ImbueProposals

---------
## Calls

---------
### raise_vote_of_no_confidence
In case of contributors losing confidence in the initiator a &quot;Vote of no confidence&quot; can be called.
This will start a round which each contributor can vote on.
The round will last as long as set in the Config.
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'raise_vote_of_no_confidence', {'project_key': 'u32'}
)
```

---------
### submit_milestone
Submit a milestones to be voted on.
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 
| milestone_key | `MilestoneKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'submit_milestone', {
    'milestone_key': 'u32',
    'project_key': 'u32',
}
)
```

---------
### vote_on_milestone
The contributors call this to vote on a milestone submission.
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 
| milestone_key | `MilestoneKey` | 
| approve_milestone | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'vote_on_milestone', {
    'approve_milestone': 'bool',
    'milestone_key': 'u32',
    'project_key': 'u32',
}
)
```

---------
### vote_on_no_confidence_round
pallet-disputes?
Vote on an already existing &quot;Vote of no condidence&quot; round.
is_yay is FOR the project&\#x27;s continuation.
so is_yay == false == against the project from continuing.
This autofinalises like in the milestone voting.
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 
| is_yay | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'vote_on_no_confidence_round', {
    'is_yay': 'bool',
    'project_key': 'u32',
}
)
```

---------
### withdraw
Withdraw some avaliable funds from the project.
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'withdraw', {'project_key': 'u32'}
)
```

---------
## Events

---------
### MilestoneApproved
A milestone has been approved.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```
| None | `MilestoneKey` | ```u32```
| None | `T::BlockNumber` | ```u32```

---------
### MilestoneSubmitted
You have submitted a milestone.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```
| None | `MilestoneKey` | ```u32```

---------
### NoConfidenceRoundCreated
You have created a vote of no confidence.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```

---------
### NoConfidenceRoundFinalised
You have finalised a vote of no confidence.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```

---------
### NoConfidenceRoundVotedUpon
You have voted upon a round of no confidence.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```

---------
### ProjectCancelled
A project has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProjectKey` | ```u32```

---------
### ProjectCreated
You have created a project.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `H256` | ```[u8; 32]```
| None | `ProjectKey` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `common_types::CurrencyId` | ```{'Native': None, 'KSM': None, 'AUSD': None, 'KAR': None, 'MGX': None, 'ForeignAsset': 'u32'}```
| None | `T::AccountId` | ```AccountId```

---------
### ProjectFundsWithdrawn
Successfully withdrawn funds from the project.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `CurrencyId` | ```{'Native': None, 'KSM': None, 'AUSD': None, 'KAR': None, 'MGX': None, 'ForeignAsset': 'u32'}```

---------
### VoteSubmitted
Vote submited successfully.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```
| None | `MilestoneKey` | ```u32```
| None | `bool` | ```bool```
| None | `T::BlockNumber` | ```u32```

---------
### VotingRoundCreated
A voting round has been created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProjectKey` | ```u32```

---------
## Storage functions

---------
### CompletedProjects

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'CompletedProjects', ['AccountId']
)
```

#### Return value
```python
['u32']
```
---------
### MilestoneVotes

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'MilestoneVotes', ['u32', 'u32']
)
```

#### Return value
```python
{'is_approved': 'bool', 'nay': 'u128', 'yay': 'u128'}
```
---------
### NoConfidenceVotes
 This holds the votes when a no confidence round is raised.

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'NoConfidenceVotes', ['u32']
)
```

#### Return value
```python
{'is_approved': 'bool', 'nay': 'u128', 'yay': 'u128'}
```
---------
### ProjectCount

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'ProjectCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Projects

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'Projects', ['u32']
)
```

#### Return value
```python
{
    'agreement_hash': '[u8; 32]',
    'cancelled': 'bool',
    'contributions': 'scale_info::459',
    'created_on': 'u32',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'deposit_id': 'u64',
    'funding_type': {'Brief': None, 'Grant': ('Kusama', 'Imbue', 'Karura'), 'Proposal': None},
    'initiator': 'AccountId',
    'milestones': 'scale_info::454',
    'raised_funds': 'u128',
    'withdrawn_funds': 'u128',
}
```
---------
### Rounds
 Stores the ending block of the project key and round.

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'Rounds', [
    'u32',
    (
        'VotingRound',
        'VoteOfNoConfidence',
    ),
]
)
```

#### Return value
```python
'u32'
```
---------
### RoundsExpiring
 Stores the project keys and round types ending on a given block

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'RoundsExpiring', ['u32']
)
```

#### Return value
```python
[('u32', ('VotingRound', 'VoteOfNoConfidence'), 'u32')]
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'StorageVersion', []
)
```

#### Return value
```python
('V0', 'V1', 'V2', 'V3', 'V4')
```
---------
### UserHasVoted

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'UserHasVoted', [
    (
        'u32',
        (
            'VotingRound',
            'VoteOfNoConfidence',
        ),
        'u32',
    ),
]
)
```

#### Return value
```python
'scale_info::466'
```
---------
## Errors

---------
### ImbueRequiredForStorageDep
You dont have enough IMBU for the project storage deposit.

---------
### InvalidAccount
Your account doenst have the privilage.

---------
### InvalidParam
Input parameter is invalid

---------
### KeyNotFound
The given key must exist in storage.

---------
### MathError
Error with a mathematical operation

---------
### MilestoneAlreadyApproved
The milestone has already been approved.

---------
### MilestoneDoesNotExist
The milestone does not exist.

---------
### MilestoneVotingNotComplete
The voting threshhold has not been met.

---------
### NoActiveRound
Currently no active round to participate in.

---------
### NoAvailableFundsToWithdraw
There are no avaliable funds to withdraw.

---------
### OnlyContributorsCanVote
Only contributors can vote.

---------
### Overflow
There was an internal overflow prevented in pallet_proposals.

---------
### ProjectDoesNotExist
Project does not exist.

---------
### ProjectNotInRound
The selected project does not exist in the round.

---------
### ProjectWithdrawn
The project has been cancelled.

---------
### RoundCanceled
Round has been cancelled.

---------
### RoundStarted
Round has already started and cannot be modified.

---------
### TooManyContributions
There are too many contributions.

---------
### TooManyMilestones
There are too many milestones.

---------
### TooManyProjects
There are too many projects for a given account

---------
### UserIsNotInitiator
You do not have permission to do this.

---------
### VoteAlreadyExists
You have already voted on this round.

---------
### VoteThresholdNotMet
The voting threshold has not been met.

---------
### VotesAreImmutable
you have already voted and cannot change your vote.

---------
### VotingRoundNotStarted
The voting round has not started yet.

---------