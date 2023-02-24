
# Society

---------
## Calls

---------
### bid
A user outside of the society can make a bid for entry.

Payment: `CandidateDeposit` will be reserved for making a bid. It is returned
when the bid becomes a member, or if the bid calls `unbid`.

The dispatch origin for this call must be _Signed_.

Parameters:
- `value`: A one time payment the bid would like to receive when joining the society.

\# &lt;weight&gt;
Key: B (len of bids), C (len of candidates), M (len of members), X (balance reserve)
- Storage Reads:
	- One storage read to check for suspended candidate. O(1)
	- One storage read to check for suspended member. O(1)
	- One storage read to retrieve all current bids. O(B)
	- One storage read to retrieve all current candidates. O(C)
	- One storage read to retrieve all members. O(M)
- Storage Writes:
	- One storage mutate to add a new bid to the vector O(B) (TODO: possible optimization
   w/ read)
	- Up to one storage removal if bid.len() &gt; MAX_BID_COUNT. O(1)
- Notable Computation:
	- O(B + C + log M) search to check user is not already a part of society.
	- O(log B) search to insert the new bid sorted.
- External Pallet Operations:
	- One balance reserve operation. O(X)
	- Up to one balance unreserve operation if bids.len() &gt; MAX_BID_COUNT.
- Events:
	- One event for new bid.
	- Up to one event for AutoUnbid if bid.len() &gt; MAX_BID_COUNT.

Total Complexity: O(M + B + C + logM + logB + X)
\# &lt;/weight&gt;
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
### defender_vote
As a member, vote on the defender.

The dispatch origin for this call must be _Signed_ and a member.

Parameters:
- `approve`: A boolean which says if the candidate should be
approved (`true`) or rejected (`false`).

\# &lt;weight&gt;
- Key: M (len of members)
- One storage read O(M) and O(log M) search to check user is a member.
- One storage write to add vote to votes. O(1)
- One event.

Total Complexity: O(M + logM)
\# &lt;/weight&gt;
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
### found
Found the society.

This is done as a discrete action in order to allow for the
pallet to be included into a running chain and can only be done once.

The dispatch origin for this call must be from the _FounderSetOrigin_.

Parameters:
- `founder` - The first member and head of the newly founded society.
- `max_members` - The initial max number of members for the society.
- `rules` - The rules of this society concerning membership.

\# &lt;weight&gt;
- Two storage mutates to set `Head` and `Founder`. O(1)
- One storage write to add the first member to society. O(1)
- One event.

Total Complexity: O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| founder | `AccountIdLookupOf<T>` | 
| max_members | `u32` | 
| rules | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'found', {
    'founder': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'max_members': 'u32',
    'rules': 'Bytes',
}
)
```

---------
### judge_suspended_candidate
Allow suspended judgement origin to make judgement on a suspended candidate.

If the judgement is `Approve`, we add them to society as a member with the appropriate
payment for joining society.

If the judgement is `Reject`, we either slash the deposit of the bid, giving it back
to the society treasury, or we ban the voucher from vouching again.

If the judgement is `Rebid`, we put the candidate back in the bid pool and let them go
through the induction process again.

The dispatch origin for this call must be from the _SuspensionJudgementOrigin_.

Parameters:
- `who` - The suspended candidate to be judged.
- `judgement` - `Approve`, `Reject`, or `Rebid`.

\# &lt;weight&gt;
Key: B (len of bids), M (len of members), X (balance action)
- One storage read to check `who` is a suspended candidate.
- One storage removal of the suspended candidate.
- Approve Logic
	- One storage read to get the available pot to pay users with. O(1)
	- One storage write to update the available pot. O(1)
	- One storage read to get the current block number. O(1)
	- One storage read to get all members. O(M)
	- Up to one unreserve currency action.
	- Up to two new storage writes to payouts.
	- Up to one storage write with O(log M) binary search to add a member to society.
- Reject Logic
	- Up to one repatriate reserved currency action. O(X)
	- Up to one storage write to ban the vouching member from vouching again.
- Rebid Logic
	- Storage mutate with O(log B) binary search to place the user back into bids.
- Up to one additional event if unvouch takes place.
- One storage removal.
- One event for the judgement.

Total Complexity: O(M + logM + B + X)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| judgement | `Judgement` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'judge_suspended_candidate', {
    'judgement': (
        'Rebid',
        'Reject',
        'Approve',
    ),
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
### judge_suspended_member
Allow suspension judgement origin to make judgement on a suspended member.

If a suspended member is forgiven, we simply add them back as a member, not affecting
any of the existing storage items for that member.

If a suspended member is rejected, remove all associated storage items, including
their payouts, and remove any vouched bids they currently have.

The dispatch origin for this call must be from the _SuspensionJudgementOrigin_.

Parameters:
- `who` - The suspended member to be judged.
- `forgive` - A boolean representing whether the suspension judgement origin forgives
  (`true`) or rejects (`false`) a suspended member.

\# &lt;weight&gt;
Key: B (len of bids), M (len of members)
- One storage read to check `who` is a suspended member. O(1)
- Up to one storage write O(M) with O(log M) binary search to add a member back to
  society.
- Up to 3 storage removals O(1) to clean up a removed member.
- Up to one storage write O(B) with O(B) search to remove vouched bid from bids.
- Up to one additional event if unvouch takes place.
- One storage removal. O(1)
- One event for the judgement.

Total Complexity: O(M + logM + B)
\# &lt;/weight&gt;
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
### payout
Transfer the first matured payout for the sender and remove it from the records.

NOTE: This extrinsic needs to be called multiple times to claim multiple matured
payouts.

Payment: The member will receive a payment equal to their first matured
payout to their free balance.

The dispatch origin for this call must be _Signed_ and a member with
payouts remaining.

\# &lt;weight&gt;
Key: M (len of members), P (number of payouts for a particular member)
- One storage read O(M) and O(log M) search to check signer is a member.
- One storage read O(P) to get all payouts for a member.
- One storage read O(1) to get the current block number.
- One currency transfer call. O(X)
- One storage write or removal to update the member&\#x27;s payouts. O(P)

Total Complexity: O(M + logM + P + X)
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'payout', {}
)
```

---------
### set_max_members
Allows root origin to change the maximum number of members in society.
Max membership count must be greater than 1.

The dispatch origin for this call must be from _ROOT_.

Parameters:
- `max` - The maximum number of members for the society.

\# &lt;weight&gt;
- One storage write to update the max. O(1)
- One event.

Total Complexity: O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| max | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'set_max_members', {'max': 'u32'}
)
```

---------
### unbid
A bidder can remove their bid for entry into society.
By doing so, they will have their candidate deposit returned or
they will unvouch their voucher.

Payment: The bid deposit is unreserved if the user made a bid.

The dispatch origin for this call must be _Signed_ and a bidder.

Parameters:
- `pos`: Position in the `Bids` vector of the bid who wants to unbid.

\# &lt;weight&gt;
Key: B (len of bids), X (balance unreserve)
- One storage read and write to retrieve and update the bids. O(B)
- Either one unreserve balance action O(X) or one vouching storage removal. O(1)
- One event.

Total Complexity: O(B + X)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| pos | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'unbid', {'pos': 'u32'}
)
```

---------
### unfound
Annul the founding of the society.

The dispatch origin for this call must be Signed, and the signing account must be both
the `Founder` and the `Head`. This implies that it may only be done when there is one
member.

\# &lt;weight&gt;
- Two storage reads O(1).
- Four storage removals O(1).
- One event.

Total Complexity: O(1)
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Society', 'unfound', {}
)
```

---------
### unvouch
As a vouching member, unvouch a bid. This only works while vouched user is
only a bidder (and not a candidate).

The dispatch origin for this call must be _Signed_ and a vouching member.

Parameters:
- `pos`: Position in the `Bids` vector of the bid who should be unvouched.

\# &lt;weight&gt;
Key: B (len of bids)
- One storage read O(1) to check the signer is a vouching member.
- One storage mutate to retrieve and update the bids. O(B)
- One vouching storage removal. O(1)
- One event.

Total Complexity: O(B)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| pos | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Society', 'unvouch', {'pos': 'u32'}
)
```

---------
### vote
As a member, vote on a candidate.

The dispatch origin for this call must be _Signed_ and a member.

Parameters:
- `candidate`: The candidate that the member would like to bid on.
- `approve`: A boolean which says if the candidate should be approved (`true`) or
  rejected (`false`).

\# &lt;weight&gt;
Key: C (len of candidates), M (len of members)
- One storage read O(M) and O(log M) search to check user is a member.
- One account lookup.
- One storage read O(C) and O(C) search to check that user is a candidate.
- One storage write to add vote to votes. O(1)
- One event.

Total Complexity: O(M + logM + C)
\# &lt;/weight&gt;
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
As a member, vouch for someone to join society by placing a bid on their behalf.

There is no deposit required to vouch for a new bid, but a member can only vouch for
one bid at a time. If the bid becomes a suspended candidate and ultimately rejected by
the suspension judgement origin, the member will be banned from vouching again.

As a vouching member, you can claim a tip if the candidate is accepted. This tip will
be paid as a portion of the reward the member will receive for joining the society.

The dispatch origin for this call must be _Signed_ and a member.

Parameters:
- `who`: The user who you would like to vouch for.
- `value`: The total reward to be paid between you and the candidate if they become
a member in the society.
- `tip`: Your cut of the total `value` payout when the candidate is inducted into
the society. Tips larger than `value` will be saturated upon payout.

\# &lt;weight&gt;
Key: B (len of bids), C (len of candidates), M (len of members)
- Storage Reads:
	- One storage read to retrieve all members. O(M)
	- One storage read to check member is not already vouching. O(1)
	- One storage read to check for suspended candidate. O(1)
	- One storage read to check for suspended member. O(1)
	- One storage read to retrieve all current bids. O(B)
	- One storage read to retrieve all current candidates. O(C)
- Storage Writes:
	- One storage write to insert vouching status to the member. O(1)
	- One storage mutate to add a new bid to the vector O(B) (TODO: possible optimization
   w/ read)
	- Up to one storage removal if bid.len() &gt; MAX_BID_COUNT. O(1)
- Notable Computation:
	- O(log M) search to check sender is a member.
	- O(B + C + log M) search to check user is not already a part of society.
	- O(log B) search to insert the new bid sorted.
- External Pallet Operations:
	- One balance reserve operation. O(X)
	- Up to one balance unreserve operation if bids.len() &gt; MAX_BID_COUNT.
- Events:
	- One event for vouch.
	- Up to one event for AutoUnbid if bid.len() &gt; MAX_BID_COUNT.

Total Complexity: O(M + B + C + logM + logB + X)
\# &lt;/weight&gt;
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
### NewMaxMembers
A new \[max\] member count has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| max | `u32` | ```u32```

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
 The current set of candidates; bidders that are attempting to become members.

#### Python
```python
result = substrate.query(
    'Society', 'Candidates', []
)
```

#### Return value
```python
[
    {'kind': {'Deposit': 'u128', 'Vouch': ('AccountId', 'u128')}, 'value': 'u128', 'who': 'AccountId'},
]
```
---------
### Defender
 The defending member currently being challenged.

#### Python
```python
result = substrate.query(
    'Society', 'Defender', []
)
```

#### Return value
```python
'AccountId'
```
---------
### DefenderVotes
 Votes for the defender.

#### Python
```python
result = substrate.query(
    'Society', 'DefenderVotes', ['AccountId']
)
```

#### Return value
```python
('Skeptic', 'Reject', 'Approve')
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
 The most primary from the most recently approved members.

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
### MaxMembers
 The max number of members for the society at one time.

#### Python
```python
result = substrate.query(
    'Society', 'MaxMembers', []
)
```

#### Return value
```python
'u32'
```
---------
### Members
 The current set of members, ordered.

#### Python
```python
result = substrate.query(
    'Society', 'Members', []
)
```

#### Return value
```python
['AccountId']
```
---------
### Payouts
 Pending payouts; ordered by block number, with the amount that should be paid out.

#### Python
```python
result = substrate.query(
    'Society', 'Payouts', ['AccountId']
)
```

#### Return value
```python
[('u32', 'u128')]
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
'[u8; 32]'
```
---------
### Strikes
 The ongoing number of losing votes cast by the member.

#### Python
```python
result = substrate.query(
    'Society', 'Strikes', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### SuspendedCandidates
 The set of suspended candidates.

#### Python
```python
result = substrate.query(
    'Society', 'SuspendedCandidates', ['AccountId']
)
```

#### Return value
```python
('u128', {'Deposit': 'u128', 'Vouch': ('AccountId', 'u128')})
```
---------
### SuspendedMembers
 The set of suspended members.

#### Python
```python
result = substrate.query(
    'Society', 'SuspendedMembers', ['AccountId']
)
```

#### Return value
```python
'bool'
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
('Skeptic', 'Reject', 'Approve')
```
---------
### Vouching
 Members currently vouching or banned from vouching again

#### Python
```python
result = substrate.query(
    'Society', 'Vouching', ['AccountId']
)
```

#### Return value
```python
('Vouching', 'Banned')
```
---------
## Constants

---------
### CandidateDeposit
 The minimum amount of a deposit required for a bid to be made.
#### Value
```python
333333333330
```
#### Python
```python
constant = substrate.get_constant('Society', 'CandidateDeposit')
```
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
### MaxCandidateIntake
 The maximum number of candidates that we accept per round.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Society', 'MaxCandidateIntake')
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
### MaxStrikes
 The number of times a member may vote the wrong way (or not at all, when they are a
 skeptic) before they become suspended.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Society', 'MaxStrikes')
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
### RotationPeriod
 The number of blocks between candidate/membership rotation periods.
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('Society', 'RotationPeriod')
```
---------
### WrongSideDeduction
 The amount of the unpaid reward that gets deducted in the case that either a skeptic
 doesn&#x27;t vote or someone votes in the wrong way.
#### Value
```python
66666666666
```
#### Python
```python
constant = substrate.get_constant('Society', 'WrongSideDeduction')
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
### AlreadyFounded
Society already founded.

---------
### AlreadyMember
User is already a member.

---------
### AlreadyVouching
Member is already vouching or banned from vouching again.

---------
### BadPosition
An incorrect position was provided.

---------
### Founder
Cannot remove the founder.

---------
### Head
Cannot remove the head of the chain.

---------
### InsufficientPot
Not enough in pot to accept candidate.

---------
### MaxMembers
Too many members in the society.

---------
### NoPayout
Nothing to payout.

---------
### NotCandidate
User is not a candidate.

---------
### NotFounder
The caller is not the founder.

---------
### NotHead
The caller is not the head.

---------
### NotMember
User is not a member.

---------
### NotSuspended
User is not suspended.

---------
### NotVouching
Member is not vouching.

---------
### Suspended
User is suspended.

---------