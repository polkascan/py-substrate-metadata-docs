
# Society

---------
## Calls

---------
### bestow_membership
See [`Pallet::bestow_membership`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'bestow_membership', {'candidate': 'AccountId'}
)
```

---------
### bid
See [`Pallet::bid`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'bid', {'value': 'u128'}
)
```

---------
### claim_membership
See [`Pallet::claim_membership`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'claim_membership', {}
)
```

---------
### cleanup_candidacy
See [`Pallet::cleanup_candidacy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| max | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'cleanup_candidacy', {
    'candidate': 'AccountId',
    'max': 'u32',
}
)
```

---------
### cleanup_challenge
See [`Pallet::cleanup_challenge`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| challenge_round | `RoundIndex` | 
| max | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'cleanup_challenge', {
    'challenge_round': 'u32',
    'max': 'u32',
}
)
```

---------
### defender_vote
See [`Pallet::defender_vote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'defender_vote', {'approve': 'bool'}
)
```

---------
### dissolve
See [`Pallet::dissolve`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'dissolve', {}
)
```

---------
### drop_candidate
See [`Pallet::drop_candidate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'drop_candidate', {'candidate': 'AccountId'}
)
```

---------
### found_society
See [`Pallet::found_society`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| founder | `AccountIdLookupOf<T>` | 
| max_members | `u32` | 
| max_intake | `u32` | 
| max_strikes | `u32` | 
| candidate_deposit | `BalanceOf<T, I>` | 
| rules | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'found_society', {
    'candidate_deposit': 'u128',
    'founder': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'max_intake': 'u32',
    'max_members': 'u32',
    'max_strikes': 'u32',
    'rules': 'Bytes',
}
)
```

---------
### judge_suspended_member
See [`Pallet::judge_suspended_member`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| forgive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'judge_suspended_member', {
    'forgive': 'bool',
    'who': {
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
### kick_candidate
See [`Pallet::kick_candidate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'kick_candidate', {'candidate': 'AccountId'}
)
```

---------
### payout
See [`Pallet::payout`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'payout', {}
)
```

---------
### punish_skeptic
See [`Pallet::punish_skeptic`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'punish_skeptic', {}
)
```

---------
### resign_candidacy
See [`Pallet::resign_candidacy`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'resign_candidacy', {}
)
```

---------
### set_parameters
See [`Pallet::set_parameters`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_members | `u32` | 
| max_intake | `u32` | 
| max_strikes | `u32` | 
| candidate_deposit | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'set_parameters', {
    'candidate_deposit': 'u128',
    'max_intake': 'u32',
    'max_members': 'u32',
    'max_strikes': 'u32',
}
)
```

---------
### unbid
See [`Pallet::unbid`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'unbid', {}
)
```

---------
### unvouch
See [`Pallet::unvouch`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'unvouch', {}
)
```

---------
### vote
See [`Pallet::vote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdLookupOf<T>` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'vote', {
    'approve': 'bool',
    'candidate': {
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
### vouch
See [`Pallet::vouch`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| value | `BalanceOf<T, I>` | 
| tip | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'vouch', {
    'tip': 'u128',
    'value': 'u128',
    'who': {
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
### waive_repay
See [`Pallet::waive_repay`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'waive_repay', {'amount': 'u128'}
)
```

---------
## Events

---------
### AutoUnbid
A candidate was dropped (due to an excess of bids in the system).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```AccountId```

---------
### Bid
A membership bid just happened. The given account is the candidate&\#x27;s ID and their offer
is the second.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate_id | `T::AccountId` | ```AccountId```
| offer | `BalanceOf<T, I>` | ```u128```

---------
### CandidateSuspended
A candidate has been suspended
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```AccountId```

---------
### Challenged
A member has been challenged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```

---------
### DefenderVote
A vote has been placed for a defending member
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| voter | `T::AccountId` | ```AccountId```
| vote | `bool` | ```bool```

---------
### Deposit
Some funds were deposited into the society account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| value | `BalanceOf<T, I>` | ```u128```

---------
### Elevated
A \[member\] got elevated to \[rank\].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```
| rank | `Rank` | ```u32```

---------
### Founded
The society is founded by the given identity.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| founder | `T::AccountId` | ```AccountId```

---------
### Inducted
A group of candidates have been inducted. The batch&\#x27;s primary is the first value, the
batch in full is the second.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| primary | `T::AccountId` | ```AccountId```
| candidates | `Vec<T::AccountId>` | ```['AccountId']```

---------
### MemberSuspended
A member has been suspended
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```

---------
### NewParams
A new set of \[params\] has been set for the group.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| params | `GroupParamsFor<T, I>` | ```{'max_members': 'u32', 'max_intake': 'u32', 'max_strikes': 'u32', 'candidate_deposit': 'u128'}```

---------
### SuspendedMemberJudgement
A suspended member has been judged.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| judged | `bool` | ```bool```

---------
### Unbid
A candidate was dropped (by their request).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```AccountId```

---------
### Unfounded
Society is unfounded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| founder | `T::AccountId` | ```AccountId```

---------
### Unvouch
A candidate was dropped (by request of who vouched for them).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```AccountId```

---------
### Vote
A vote has been placed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```AccountId```
| voter | `T::AccountId` | ```AccountId```
| vote | `bool` | ```bool```

---------
### Vouch
A membership bid just happened by vouching. The given account is the candidate&\#x27;s ID and
their offer is the second. The vouching party is the third.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate_id | `T::AccountId` | ```AccountId```
| offer | `BalanceOf<T, I>` | ```u128```
| vouching | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Bids
 The current bids, stored ordered by the value of the bid.

#### Python
```python
result = substrate.query(
    'Society', 'Bids', []
)
```

#### Return value
```python
[
    {'kind': {'Deposit': 'u128', 'Vouch': ('AccountId', 'u128')}, 'value': 'u128', 'who': 'AccountId'},
]
```
---------
### Candidates

#### Python
```python
result = substrate.query(
    'Society', 'Candidates', ['AccountId']
)
```

#### Return value
```python
{
    'bid': 'u128',
    'kind': {'Deposit': 'u128', 'Vouch': ('AccountId', 'u128')},
    'round': 'u32',
    'skeptic_struck': 'bool',
    'tally': {'approvals': 'u32', 'rejections': 'u32'},
}
```
---------
### ChallengeRoundCount
 The number of challenge rounds there have been. Used to identify stale DefenderVotes.

#### Python
```python
result = substrate.query(
    'Society', 'ChallengeRoundCount', []
)
```

#### Return value
```python
'u32'
```
---------
### DefenderVotes
 Votes for the defender, keyed by challenge round.

#### Python
```python
result = substrate.query(
    'Society', 'DefenderVotes', ['u32', 'AccountId']
)
```

#### Return value
```python
{'approve': 'bool', 'weight': 'u32'}
```
---------
### Defending
 The defending member currently being challenged, along with a running tally of votes.

#### Python
```python
result = substrate.query(
    'Society', 'Defending', []
)
```

#### Return value
```python
('AccountId', 'AccountId', {'approvals': 'u32', 'rejections': 'u32'})
```
---------
### Founder
 The first member.

#### Python
```python
result = substrate.query(
    'Society', 'Founder', []
)
```

#### Return value
```python
'AccountId'
```
---------
### Head
 The most primary from the most recently approved rank 0 members in the society.

#### Python
```python
result = substrate.query(
    'Society', 'Head', []
)
```

#### Return value
```python
'AccountId'
```
---------
### MemberByIndex
 The current items in `Members` keyed by their unique index. Keys are densely populated
 `0..MemberCount` (does not include `MemberCount`).

#### Python
```python
result = substrate.query(
    'Society', 'MemberByIndex', ['u32']
)
```

#### Return value
```python
'AccountId'
```
---------
### MemberCount
 The number of items in `Members` currently. (Doesn&#x27;t include `SuspendedMembers`.)

#### Python
```python
result = substrate.query(
    'Society', 'MemberCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Members
 The current members and their rank. Doesn&#x27;t include `SuspendedMembers`.

#### Python
```python
result = substrate.query(
    'Society', 'Members', ['AccountId']
)
```

#### Return value
```python
{
    'index': 'u32',
    'rank': 'u32',
    'strikes': 'u32',
    'vouching': (None, ('Vouching', 'Banned')),
}
```
---------
### NextHead
 At the end of the claim period, this contains the most recently approved members (along with
 their bid and round ID) who is from the most recent round with the lowest bid. They will
 become the new `Head`.

#### Python
```python
result = substrate.query(
    'Society', 'NextHead', []
)
```

#### Return value
```python
{'bid': 'u128', 'round': 'u32', 'who': 'AccountId'}
```
---------
### Parameters
 The max number of members for the society at one time.

#### Python
```python
result = substrate.query(
    'Society', 'Parameters', []
)
```

#### Return value
```python
{
    'candidate_deposit': 'u128',
    'max_intake': 'u32',
    'max_members': 'u32',
    'max_strikes': 'u32',
}
```
---------
### Payouts
 Information regarding rank-0 payouts, past and future.

#### Python
```python
result = substrate.query(
    'Society', 'Payouts', ['AccountId']
)
```

#### Return value
```python
{'paid': 'u128', 'payouts': [('u32', 'u128')]}
```
---------
### Pot
 Amount of our account balance that is specifically for the next round&#x27;s bid(s).

#### Python
```python
result = substrate.query(
    'Society', 'Pot', []
)
```

#### Return value
```python
'u128'
```
---------
### RoundCount
 The number of rounds which have passed.

#### Python
```python
result = substrate.query(
    'Society', 'RoundCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Rules
 A hash of the rules of this society concerning membership. Can only be set once and
 only by the founder.

#### Python
```python
result = substrate.query(
    'Society', 'Rules', []
)
```

#### Return value
```python
'scale_info::12'
```
---------
### Skeptic
 The current skeptic.

#### Python
```python
result = substrate.query(
    'Society', 'Skeptic', []
)
```

#### Return value
```python
'AccountId'
```
---------
### SuspendedMembers
 The set of suspended members, with their old membership record.

#### Python
```python
result = substrate.query(
    'Society', 'SuspendedMembers', ['AccountId']
)
```

#### Return value
```python
{
    'index': 'u32',
    'rank': 'u32',
    'strikes': 'u32',
    'vouching': (None, ('Vouching', 'Banned')),
}
```
---------
### VoteClearCursor
 Clear-cursor for Vote, map from Candidate -&gt; (Maybe) Cursor.

#### Python
```python
result = substrate.query(
    'Society', 'VoteClearCursor', ['AccountId']
)
```

#### Return value
```python
'Bytes'
```
---------
### Votes
 Double map from Candidate -&gt; Voter -&gt; (Maybe) Vote.

#### Python
```python
result = substrate.query(
    'Society', 'Votes', ['AccountId', 'AccountId']
)
```

#### Return value
```python
{'approve': 'bool', 'weight': 'u32'}
```
---------
## Constants

---------
### ChallengePeriod
 The number of blocks between membership challenges.
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('Society', 'ChallengePeriod')
```
---------
### ClaimPeriod
 The number of blocks on which new candidates can claim their membership and be the
 named head.
#### Value
```python
28800
```
#### Python
```python
constant = substrate.get_constant('Society', 'ClaimPeriod')
```
---------
### GraceStrikes
 The maximum number of strikes before a member gets funds slashed.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Society', 'GraceStrikes')
```
---------
### MaxBids
 The maximum number of bids at once.
#### Value
```python
512
```
#### Python
```python
constant = substrate.get_constant('Society', 'MaxBids')
```
---------
### MaxLockDuration
 The maximum duration of the payout lock.
#### Value
```python
15552000
```
#### Python
```python
constant = substrate.get_constant('Society', 'MaxLockDuration')
```
---------
### MaxPayouts
 The maximum number of payouts a member may have waiting unclaimed.
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('Society', 'MaxPayouts')
```
---------
### PalletId
 The societies&#x27;s pallet id
#### Value
```python
'0x70792f736f636965'
```
#### Python
```python
constant = substrate.get_constant('Society', 'PalletId')
```
---------
### PeriodSpend
 The amount of incentive paid within each period. Doesn&#x27;t include VoterTip.
#### Value
```python
16666666666500
```
#### Python
```python
constant = substrate.get_constant('Society', 'PeriodSpend')
```
---------
### VotingPeriod
 The number of blocks on which new candidates should be voted on. Together with
 `ClaimPeriod`, this sums to the number of blocks between candidate intake periods.
#### Value
```python
72000
```
#### Python
```python
constant = substrate.get_constant('Society', 'VotingPeriod')
```
---------
## Errors

---------
### AlreadyBid
User has already made a bid.

---------
### AlreadyCandidate
User is already a candidate.

---------
### AlreadyElevated
The member is already elevated to this rank.

---------
### AlreadyFounded
Society already founded.

---------
### AlreadyMember
User is already a member.

---------
### AlreadyPunished
The skeptic has already been punished for this offence.

---------
### AlreadyVouching
Member is already vouching or banned from vouching again.

---------
### Approved
The candidacy cannot be dropped as the candidate was clearly approved.

---------
### Expired
The skeptic need not vote on candidates from expired rounds.

---------
### Founder
Cannot remove the founder.

---------
### Head
Cannot remove the head of the chain.

---------
### InProgress
The candidacy cannot be concluded as the voting is still in progress.

---------
### InsufficientFunds
Funds are insufficient to pay off society debts.

---------
### InsufficientPot
Not enough in pot to accept candidate.

---------
### MaxMembers
Too many members in the society.

---------
### NoDefender
There is no defender currently.

---------
### NoPayout
Nothing to payout.

---------
### NoVotes
The candidate/defender has no stale votes to remove.

---------
### NotApproved
The membership cannot be claimed as the candidate was not clearly approved.

---------
### NotBidder
User is not a bidder.

---------
### NotCandidate
User is not a candidate.

---------
### NotFounder
The caller is not the founder.

---------
### NotGroup
Group doesn&\#x27;t exist.

---------
### NotHead
The caller is not the head.

---------
### NotMember
User is not a member.

---------
### NotRejected
The candidate cannot be kicked as the candidate was not clearly rejected.

---------
### NotSuspended
User is not suspended.

---------
### NotVouchingOnBidder
Member is not vouching.

---------
### Rejected
The candidacy cannot be bestowed as the candidate was clearly rejected.

---------
### Suspended
User is suspended.

---------
### TooEarly
The candidacy cannot be pruned until a full additional intake period has passed.

---------
### Voted
The skeptic already voted.

---------