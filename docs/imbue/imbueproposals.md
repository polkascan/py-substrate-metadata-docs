
# ImbueProposals

---------
## Calls

---------
### add_project_whitelist
Step 1.5 (INITATOR)
Add whitelist to a project
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 
| new_whitelist_spots | `BoundedWhitelistSpots<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'add_project_whitelist', {
    'new_whitelist_spots': 'scale_info::280',
    'project_key': 'u32',
}
)
```

---------
### approve
Step 4 (ADMIN)
Approve project
If the project is approved, the project initator can withdraw funds for approved milestones
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_key | `Option<RoundKey>` | 
| project_key | `ProjectKey` | 
| milestone_keys | `Option<BoundedMilestoneKeys>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'approve', {
    'milestone_keys': (None, ['u32']),
    'project_key': 'u32',
    'round_key': (None, 'u32'),
}
)
```

---------
### cancel_round
Step 2.5 (ADMIN)
Cancel a round
This round must have not started yet
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_key | `RoundKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'cancel_round', {'round_key': 'u32'}
)
```

---------
### contribute
Step 3 (CONTRIBUTOR/FUNDER)
Contribute to a project
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_key | `Option<RoundKey>` | 
| project_key | `ProjectKey` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'contribute', {
    'project_key': 'u32',
    'round_key': (None, 'u32'),
    'value': 'u128',
}
)
```

---------
### create_project
Step 1 (INITATOR)
Create project.
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `BoundedStringField` | 
| logo | `BoundedStringField` | 
| description | `BoundedDescriptionField` | 
| website | `BoundedDescriptionField` | 
| proposed_milestones | `BoundedProposedMilestones` | 
| required_funds | `BalanceOf<T>` | 
| currency_id | `common_types::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'create_project', {
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'description': 'Bytes',
    'logo': 'Bytes',
    'name': 'Bytes',
    'proposed_milestones': [
        {
            'name': 'Bytes',
            'percentage_to_unlock': 'u32',
        },
    ],
    'required_funds': 'u128',
    'website': 'Bytes',
}
)
```

---------
### finalise_milestone_voting
Step 7 (INITATOR)
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 
| milestone_key | `MilestoneKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'finalise_milestone_voting', {
    'milestone_key': 'u32',
    'project_key': 'u32',
}
)
```

---------
### finalise_no_confidence_round
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_key | `Option<RoundKey>` | 
| project_key | `ProjectKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'finalise_no_confidence_round', {
    'project_key': 'u32',
    'round_key': (None, 'u32'),
}
)
```

---------
### raise_vote_of_no_confidence
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
### refund
Ad Hoc Step (ADMIN)
Refund
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
### remove_project_whitelist
Step 1.5 (INITATOR)
Remove a whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'remove_project_whitelist', {'project_key': 'u32'}
)
```

---------
### schedule_round
Step 2 (ADMIN)
Schedule a round
project_keys: the projects were selected for this round
#### Attributes
| Name | Type |
| -------- | -------- | 
| start | `T::BlockNumber` | 
| end | `T::BlockNumber` | 
| project_keys | `BoundedProjectKeys` | 
| round_type | `RoundType` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'schedule_round', {
    'end': 'u32',
    'project_keys': ['u32'],
    'round_type': (
        'ContributionRound',
        'VotingRound',
        'VoteOfNoConfidence',
    ),
    'start': 'u32',
}
)
```

---------
### set_is_identity_required
set is_identity_required
#### Attributes
| Name | Type |
| -------- | -------- | 
| is_identity_required | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'set_is_identity_required', {'is_identity_required': 'bool'}
)
```

---------
### set_max_project_count_per_round
Set max project count per round
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_project_count_per_round | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'set_max_project_count_per_round', {'max_project_count_per_round': 'u32'}
)
```

---------
### set_milestone_voting_window
Set milestone voting window
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_milestone_voting_window | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'set_milestone_voting_window', {'new_milestone_voting_window': 'u32'}
)
```

---------
### set_withdrawal_expiration
Set withdrawal expiration
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdrawal_expiration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'set_withdrawal_expiration', {'withdrawal_expiration': 'u32'}
)
```

---------
### submit_milestone
Step 5 (INITATOR)
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
Step 6 (CONTRIBUTOR/FUNDER)
Vote on a milestone
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_key | `ProjectKey` | 
| milestone_key | `MilestoneKey` | 
| round_key | `Option<RoundKey>` | 
| approve_milestone | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'vote_on_milestone', {
    'approve_milestone': 'bool',
    'milestone_key': 'u32',
    'project_key': 'u32',
    'round_key': (None, 'u32'),
}
)
```

---------
### vote_on_no_confidence_round
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_key | `Option<RoundKey>` | 
| project_key | `ProjectKey` | 
| is_yay | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueProposals', 'vote_on_no_confidence_round', {
    'is_yay': 'bool',
    'project_key': 'u32',
    'round_key': (None, 'u32'),
}
)
```

---------
### withdraw
Step 8 (INITATOR)
Withdraw
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
### ContributeSucceeded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `common_types::CurrencyId` | ```{'Native': None, 'KSM': None, 'AUSD': None, 'KAR': None, 'MGX': None, 'ForeignAsset': 'u32'}```
| None | `T::BlockNumber` | ```u32```

---------
### FundingRoundCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundKey` | ```u32```
| None | `Vec<ProjectKey>` | ```['u32']```

---------
### MilestoneApproved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```
| None | `MilestoneKey` | ```u32```
| None | `T::BlockNumber` | ```u32```

---------
### MilestoneSubmitted
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
| None | `RoundKey` | ```u32```
| None | `ProjectKey` | ```u32```

---------
### NoConfidenceRoundFinalised
You have finalised a vote of no confidence.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundKey` | ```u32```
| None | `ProjectKey` | ```u32```

---------
### NoConfidenceRoundVotedUpon
You have voted upon a round of no confidence.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundKey` | ```u32```
| None | `ProjectKey` | ```u32```

---------
### ProjectApproved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundKey` | ```u32```
| None | `ProjectKey` | ```u32```

---------
### ProjectCancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundKey` | ```u32```
| None | `ProjectKey` | ```u32```

---------
### ProjectCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<u8>` | ```Bytes```
| None | `ProjectKey` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `common_types::CurrencyId` | ```{'Native': None, 'KSM': None, 'AUSD': None, 'KAR': None, 'MGX': None, 'ForeignAsset': 'u32'}```

---------
### ProjectFundsWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProjectKey` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `CurrencyId` | ```{'Native': None, 'KSM': None, 'AUSD': None, 'KAR': None, 'MGX': None, 'ForeignAsset': 'u32'}```

---------
### ProjectLockedFundsRefunded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProjectKey` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### RoundCancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundKey` | ```u32```

---------
### VoteComplete
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
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundKey` | ```u32```
| None | `Vec<ProjectKey>` | ```['u32']```

---------
### WhitelistAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProjectKey` | ```u32```
| None | `T::BlockNumber` | ```u32```

---------
### WhitelistRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProjectKey` | ```u32```
| None | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### IsIdentityRequired

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'IsIdentityRequired', []
)
```

#### Return value
```python
'bool'
```
---------
### MaxProjectCountPerRound

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'MaxProjectCountPerRound', []
)
```

#### Return value
```python
'u32'
```
---------
### MilestoneVotes

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'MilestoneVotes', [('u32', 'u32')]
)
```

#### Return value
```python
{'is_approved': 'bool', 'nay': 'u128', 'yay': 'u128'}
```
---------
### MilestoneVotingWindow

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'MilestoneVotingWindow', []
)
```

#### Return value
```python
'u32'
```
---------
### NoConfidenceVotes

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
    'approved_for_funding': 'bool',
    'cancelled': 'bool',
    'contributions': 'scale_info::428',
    'create_block_number': 'u32',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'description': 'Bytes',
    'funding_threshold_met': 'bool',
    'initiator': 'AccountId',
    'logo': 'Bytes',
    'milestones': 'scale_info::424',
    'name': 'Bytes',
    'raised_funds': 'u128',
    'required_funds': 'u128',
    'website': 'Bytes',
    'withdrawn_funds': 'u128',
}
```
---------
### RoundCount

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'RoundCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Rounds

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'Rounds', ['u32']
)
```

#### Return value
```python
(
    None,
    {
        'end': 'u32',
        'is_canceled': 'bool',
        'project_keys': ['u32'],
        'round_type': (
            'ContributionRound',
            'VotingRound',
            'VoteOfNoConfidence',
        ),
        'start': 'u32',
    },
)
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
('V0', 'V1', 'V2')
```
---------
### UserVotes

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'UserVotes', [('AccountId', 'u32', 'u32', 'u32')]
)
```

#### Return value
```python
'bool'
```
---------
### WhitelistSpots

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'WhitelistSpots', ['u32']
)
```

#### Return value
```python
'scale_info::280'
```
---------
### WithdrawalExpiration

#### Python
```python
result = substrate.query(
    'ImbueProposals', 'WithdrawalExpiration', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### ContributionMustBeLowerThanMaxCap
Contribution has exceeded the maximum capacity of the project.

---------
### EndBlockNumberInvalid
This block number must be later than the current.

---------
### EndTooEarly
The starting block number must be before the ending block number.

---------
### IdentityNeeded
Required identity not found.

---------
### InvalidAccount
Your account does not have the correct authority.

---------
### InvalidParam
Input parameter is invalid

---------
### KeyNotFound
The given key must exist in storage.

---------
### LengthMustExceedZero
The input vector must exceed length zero.

---------
### LogoIsMandatory
Project logo is a mandatory field.

---------
### MilestoneDoesNotExist

---------
### MilestoneVotingNotComplete
The voting threshhold has not been met.

---------
### MilestonesTotalPercentageMustEqual100
Milestones totals do not add up to 100%.

---------
### NoActiveProject

---------
### NoActiveRound
Currently no active round to participate in.

---------
### NoAvailableFundsToWithdraw
There are no avaliable funds to withdraw.

---------
### OnlyApprovedProjectsCanSubmitMilestones
A project must be approved before the submission of milestones.

---------
### OnlyContributorsCanVote
Only contributors can vote.

---------
### OnlyInitiatorOrAdminCanApproveMilestone
You do not have permission to do this.

---------
### OnlyWhitelistedAccountsCanContribute
You do not have permission to do this.

---------
### Overflow
There was an overflow.

---------
### ParamLimitExceed
Parameter limit exceeded.

---------
### ProjectAmountExceed

---------
### ProjectApprovalRequired
The project must be approved.

---------
### ProjectApproved

---------
### ProjectDescriptionIsMandatory
Project description is a mandatory field.

---------
### ProjectDoesNotExist
Project does not exist.

---------
### ProjectNameIsMandatory
Project name is a mandatory field.

---------
### ProjectNotInRound
The selected project does not exist in the round.

---------
### ProjectWithdrawn

---------
### RoundCanceled
Round has been cancelled.

---------
### RoundNotEnded
Round stll in progress.

---------
### RoundNotProcessing
There was a processing error when finding the round.

---------
### RoundStarted
Round has already started and cannot be modified.

---------
### StartBlockNumberTooSmall

---------
### UserIsNotInitator
You do not have permission to do this.

---------
### VoteAlreadyExists
You have already voted on this round.

---------
### VoteThresholdNotMet
The voting threshold has not been met.

---------
### WebsiteURLIsMandatory
Website url is a mandatory field.

---------
### WithdrawalExpirationExceed

---------