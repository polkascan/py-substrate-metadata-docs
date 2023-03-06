
# UpgradeCommittee

---------
## Calls

---------
### set_expires_after
Changes the time after which a proposal expires.

\# Arguments
* `expiry` - The new expiry time.
#### Attributes
| Name | Type |
| -------- | -------- | 
| expiry | `MaybeBlock<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'UpgradeCommittee', 'set_expires_after', {
    'expiry': {
        'None': None,
        'Some': 'u32',
    },
}
)
```

---------
### set_release_coordinator
Changes the release coordinator.

\# Arguments
* `id` - The DID of the new release coordinator.

\# Errors
* `NotAMember`, If the new coordinator `id` is not part of the committee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'UpgradeCommittee', 'set_release_coordinator', {'id': '[u8; 32]'}
)
```

---------
### set_vote_threshold
Change the vote threshold the determines the winning proposal.
For e.g., for a simple majority use (1, 2) which represents the in-equation &quot;&gt;= 1/2&quot;.

\# Arguments
* `n` - Numerator of the fraction representing vote threshold.
* `d` - Denominator of the fraction representing vote threshold.
#### Attributes
| Name | Type |
| -------- | -------- | 
| n | `u32` | 
| d | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'UpgradeCommittee', 'set_vote_threshold', {'d': 'u32', 'n': 'u32'}
)
```

---------
### vote
Votes `approve`ingly (or not, if `false`)
on an existing `proposal` given by its hash, `index`.

\# Arguments
* `proposal` - A hash of the proposal to be voted on.
* `index` - The proposal index.
* `approve` - If `true` than this is a `for` vote, and `against` otherwise.

\# Errors
* `NotAMember`, if the `origin` is not a member of this committee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'UpgradeCommittee', 'vote', {
    'approve': 'bool',
    'index': 'u32',
    'proposal': '[u8; 32]',
}
)
```

---------
### vote_or_propose
Proposes to the committee that `call` should be executed in its name.
Alternatively, if the hash of `call` has already been recorded, i.e., already proposed,
then this call counts as a vote, i.e., as if `vote_by_hash` was called.

\# Weight

The weight of this dispatchable is that of `call` as well as the complexity
for recording the vote itself.

\# Arguments
* `approve` - is this an approving vote?
  If the proposal doesn&\#x27;t exist, passing `false` will result in error `FirstVoteReject`.
* `call` - the call to propose for execution.

\# Errors
* `FirstVoteReject`, if `call` hasn&\#x27;t been proposed and `approve == false`.
* `NotAMember`, if the `origin` is not a member of this committee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| approve | `bool` | 
| call | `Box<<T as Config<I>>::Proposal>` | 

#### Python
```python
call = substrate.compose_call(
    'UpgradeCommittee', 'vote_or_propose', {'approve': 'bool', 'call': 'Call'}
)
```

---------
## Events

---------
### Approved
A motion was approved by the required threshold with the following
tally (yes votes, no votes and total seats given respectively as `MemberCount`).
Parameters: caller DID, proposal hash, yay vote count, nay vote count, total seats.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Hash` | ```[u8; 32]```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```

---------
### Executed
A motion was executed; `DispatchResult` is `Ok(())` if returned without error.
Parameters: caller DID, proposal hash, result of proposal dispatch.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Hash` | ```[u8; 32]```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### ExpiresAfterUpdated
Proposal expiry time has been updated.
Parameters: caller DID, new expiry time (if any).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `MaybeBlock<BlockNumber>` | ```{'Some': 'u32', 'None': None}```

---------
### FinalVotes
Final votes on a motion (given hash)
caller DID, ProposalIndex, Proposal hash, yes voters, no voter
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `ProposalIndex` | ```u32```
| None | `Hash` | ```[u8; 32]```
| None | `Vec<IdentityId>` | ```['[u8; 32]']```
| None | `Vec<IdentityId>` | ```['[u8; 32]']```

---------
### Proposed
A motion (given hash) has been proposed (by given account) with a threshold (given `MemberCount`).
Parameters: caller DID, proposal index, proposal hash.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `ProposalIndex` | ```u32```
| None | `Hash` | ```[u8; 32]```

---------
### Rejected
A motion was rejected by the required threshold with the following
tally (yes votes, no votes and total seats given respectively as `MemberCount`).
Parameters: caller DID, proposal hash, yay vote count, nay vote count, total seats.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Hash` | ```[u8; 32]```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```

---------
### ReleaseCoordinatorUpdated
Release coordinator has been updated.
Parameters: caller DID, DID of the release coordinator.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```

---------
### VoteRetracted
A vote on a motion (given hash) has been retracted.
caller DID, ProposalIndex, Proposal hash, vote that was retracted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `ProposalIndex` | ```u32```
| None | `Hash` | ```[u8; 32]```
| None | `bool` | ```bool```

---------
### VoteThresholdUpdated
Voting threshold has been updated
Parameters: caller DID, numerator, denominator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `u32` | ```u32```
| None | `u32` | ```u32```

---------
### Voted
A motion (given hash) has been voted on by given account, leaving
a tally (yes votes, no votes and total seats given respectively as `MemberCount`).
caller DID, Proposal index, Proposal hash, current vote, yay vote count, nay vote count, total seats.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `ProposalIndex` | ```u32```
| None | `Hash` | ```[u8; 32]```
| None | `bool` | ```bool```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```

---------
## Storage functions

---------
### ExpiresAfter
 Time after which a proposal will expire.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'ExpiresAfter', []
)
```

#### Return value
```python
{'None': None, 'Some': 'u32'}
```
---------
### Members
 The current members of the committee.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'Members', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### ProposalCount
 Proposals so far.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'ProposalCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ProposalOf
 Actual proposal for a given hash.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'ProposalOf', ['[u8; 32]']
)
```

#### Return value
```python
'Call'
```
---------
### Proposals
 The hashes of the active proposals.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'Proposals', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### ReleaseCoordinator
 Release coordinator.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'ReleaseCoordinator', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### VoteThreshold
 Vote threshold for an approval.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'VoteThreshold', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### Voting
 PolymeshVotes on a given proposal, if it is ongoing.

#### Python
```python
result = substrate.query(
    'UpgradeCommittee', 'Voting', ['[u8; 32]']
)
```

#### Return value
```python
{
    'ayes': ['[u8; 32]'],
    'expiry': {'None': None, 'Some': 'u32'},
    'index': 'u32',
    'nays': ['[u8; 32]'],
}
```
---------
## Errors

---------
### DuplicateProposal
Duplicate proposal.

---------
### DuplicateVote
Duplicate votes are not allowed.

---------
### FirstVoteReject
First vote on a proposal creates it, so it must be an approval.
All proposals are motions to execute something as &quot;GC majority&quot;.
To reject e.g., a PIP, a motion to reject should be *approved*.

---------
### InvalidProportion
Proportion must be a rational number.

---------
### MismatchedVotingIndex
Mismatched voting index.

---------
### NoSuchProposal
No such proposal.

---------
### NotAMember
A DID isn&\#x27;t part of the committee.
The DID may either be a caller or some other context.

---------
### ProposalExpired
Proposal exists, but it has expired.

---------
### ProposalsLimitReached
Maximum number of proposals has been reached.

---------