
# ImbueProposals

---------
## Calls

---------
### mint_offchain_assets
See [`Pallet::mint_offchain_assets`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `AccountIdOf<T>` | 
| currency_id | `CurrencyId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'mint_offchain_assets', {
    'amount': 'u128',
    'beneficiary': 'AccountId',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': (
            'ETH',
            'USDT',
        ),
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
}
)
```

---------
### raise_dispute
See [`Pallet::raise_dispute`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 
| milestone_keys | `BoundedVec<MilestoneKey, T::MaxMilestonesPerProject>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'raise_dispute', {
    'milestone_keys': ['u32'],
    'project_key': 'u32',
}
)
```

---------
### refund
See [`Pallet::refund`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'refund', {'project_key': 'u32'}
)
```

---------
### set_foreign_asset_signer
See [`Pallet::set_foreign_asset_signer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'set_foreign_asset_signer', {'new': 'AccountId'}
)
```

---------
### submit_milestone
See [`Pallet::submit_milestone`].
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
See [`Pallet::vote_on_milestone`].
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
### withdraw
See [`Pallet::withdraw`].
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
### ForeignAssetMinted
Foreign Asset Signer Changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `CurrencyId` | ```{'Native': None, 'KSM': None, 'AUSD': None, 'KAR': None, 'MGX': None, 'ForeignAsset': ('ETH', 'USDT')}```
| None | `BalanceOf<T>` | ```u128```

---------
### ForeignAssetSignerChanged
Foreign Asset Signer Changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### MilestoneApproved
A milestone has been approved.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```
| None | `MilestoneKey` | ```u32```
| None | `BlockNumberFor<T>` | ```u32```

---------
### MilestoneRejected
This milestone has been rejected.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProjectKey` | ```u32```
| None | `MilestoneKey` | ```u32```

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
| None | `H256` | ```scale_info::12```
| None | `ProjectKey` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `common_types::CurrencyId` | ```{'Native': None, 'KSM': None, 'AUSD': None, 'KAR': None, 'MGX': None, 'ForeignAsset': ('ETH', 'USDT')}```
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
| None | `CurrencyId` | ```{'Native': None, 'KSM': None, 'AUSD': None, 'KAR': None, 'MGX': None, 'ForeignAsset': ('ETH', 'USDT')}```

---------
### ProjectRefunded
A project has been refunded either partially or completely.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_key | `ProjectKey` | ```u32```
| total_amount | `BalanceOf<T>` | ```u128```

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
| None | `BlockNumberFor<T>` | ```u32```

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
 Stores the completed project by a given initiator.

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
### ForeignCurrencySigner
 The `AccountId` of the multichain signer

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'ForeignCurrencySigner', []
)
```

#### Return value
```python
'AccountId'
```
---------
### IndividualVoteStore
 Stores the individuals votes on a given milestone key

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'IndividualVoteStore', ['u32']
)
```

#### Return value
```python
{'votes': 'scale_info::508'}
```
---------
### MilestoneVotes

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'MilestoneVotes', ['u32']
)
```

#### Return value
```python
'scale_info::513'
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
### ProjectInVoting
 Projects in Voting round.
 A helper for the runtime api so we dont have to iterate over the Rounds Double map.

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'ProjectInVoting', ['u32', 'u32']
)
```

#### Return value
```python
()
```
---------
### Projects
 Stores the projects of the pallet.

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'Projects', ['u32']
)
```

#### Return value
```python
{
    'agreement_hash': 'scale_info::12',
    'cancelled': 'bool',
    'contributions': 'scale_info::491',
    'created_on': 'u32',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': ('ETH', 'USDT'),
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'deposit_id': 'u64',
    'external_owned_address': (None, {'ETH': '[u8; 20]', 'TRON': '[u8; 22]'}),
    'initiator': 'AccountId',
    'jury': ['AccountId'],
    'milestones': 'scale_info::486',
    'on_creation_funding': ('TakeFromReserved', 'WaitForFunding'),
    'raised_funds': 'u128',
    'refund_locations': [
        ({'Foreign': 'scale_info::66', 'Local': 'AccountId'}, 'u8'),
    ],
    'refunded_funds': 'u128',
    'withdrawn_funds': 'u128',
}
```
---------
### ProjectsInDispute
 A helper to find what projects / milestones are in a dispute.

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'ProjectsInDispute', ['u32']
)
```

#### Return value
```python
['u32']
```
---------
### Rounds
 Stores the ending block of the project key and round.

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'Rounds', [
    ('u32', 'u32'),
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
'scale_info::503'
```
---------
## Errors

---------
### CannotRaiseDisputeOnApprovedMilestone
You cannot raise a dispute on an approved milestone.

---------
### ImbueRequiredForStorageDep
You dont have enough IMBU for the project storage deposit.

---------
### IndividualVoteNotFound
An internal error, a collection of votes for a milestone has been lost.s

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
### MilestoneConversionFailed
Conversion failed due to an error in milestone conversion (probably a bound has been abused).

---------
### MilestoneDoesNotExist
The milestone does not exist.

---------
### MilestoneVotingNotComplete
The voting threshhold has not been met.

---------
### MilestonesAlreadyInDispute
One of these milestones is already in a dispute.

---------
### NoActiveRound
Currently no active round to participate in.

---------
### NoAvailableFundsToWithdraw
There are no avaliable funds to withdraw.

---------
### NotEnoughFundsForFees
Not enough funds in project account to distribute fees.

---------
### OnlyContributorsCanInitiateRefund
Only a contributor can initiate a refund.

---------
### OnlyContributorsCanRaiseDispute
Only a contributor can raise a dispute.

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
### ProjectFundingFailed
Conversion failed due to an error while funding the Project.

---------
### ProjectNotInRound
The selected project does not exist in the round.

---------
### ProjectWithdrawn
The project has been cancelled.

---------
### RequireForeignAssetSigner
Only the ForeignAssetSigner can mint tokens

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
### TooManyJuryMembers
This project has too many jury members.

---------
### TooManyMilestoneVotes
There are too many milestone votes, this generally shouldnt be hit.

---------
### TooManyMilestones
There are too many milestones.

---------
### TooManyProjects
There are too many projects for a given account

---------
### TooManyRefundLocations
This project has too many refund locations.

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