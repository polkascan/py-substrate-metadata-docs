
# Democracy

---------
## Calls

---------
### cancel_proposal
Remove a proposal.

- `prop_index`: The index of the proposal to cancel.

Weight: `O(p)` where `p = PublicProps::&lt;T&gt;::decode_len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| prop_index | `PropIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'cancel_proposal', {'prop_index': 'u32'}
)
```

---------
### cancel_referendum
Remove a referendum.

The dispatch origin of this call must be _Root_.

- `ref_index`: The index of the referendum to cancel.

\# Weight: `O(1)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'cancel_referendum', {'ref_index': 'u32'}
)
```

---------
### clear_public_proposals
Clears all public proposals.

The dispatch origin of this call must be _Root_.

Weight: `O(1)`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'clear_public_proposals', {}
)
```

---------
### fast_track
Schedule a proposal to be tabled immediately with the `FastTrackVotingPeriod`.

The dispatch of this call must be `FastTrackOrigin`.

- `prop_index`: The index of the current external proposal.
- `delay`: The number of blocks to wait after approval before execution.

Emits `Started` and `FastTrack`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| prop_index | `PropIndex` | 
| delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'fast_track', {'delay': 'u32', 'prop_index': 'u32'}
)
```

---------
### fast_track_referendum
Reduces the voting period of an existing referendum.

The dispatch of this call must be `FastTrackOrigin`.

- `ref_index`: The index of the referendum.

Emits `FastTrackReferendum`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `PropIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'fast_track_referendum', {'ref_index': 'u32'}
)
```

---------
### propose
Propose a sensitive action to be taken.

The dispatch origin of this call must be _Signed_ and the sender must
have funds to cover the deposit.

- `proposal_hash`: The hash of the proposal preimage.
- `value`: The amount of deposit (must be at least `MinimumDeposit`).

Emits `Proposed`.

Weight: `O(p)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `BoundedCallOf<T>` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'propose', {
    'proposal': {
        'Inline': 'Bytes',
        'Legacy': {
            'hash': 'scale_info::12',
        },
        'Lookup': {
            'hash': 'scale_info::12',
            'len': 'u32',
        },
    },
    'value': 'u128',
}
)
```

---------
### remove_vote
Remove a vote for an ongoing referendum.

The dispatch origin of this call must be _Signed_, and the signer must have a vote
registered for referendum `index`.

- `index`: The index of referendum of the vote to be removed.

Weight: `O(R + log R)` where R is the number of referenda that `target` has voted on.
  Weight is calculated for the maximum number of vote.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'remove_vote', {'index': 'u32'}
)
```

---------
### second
Signals agreement with a particular proposal.

The dispatch origin of this call must be _Signed_ and the sender
must have funds to cover the deposit, equal to the original deposit.

- `proposal`: The index of the proposal to second.
- `seconds_upper_bound`: an upper bound on the current number of seconds on this proposal. Extrinsic is
  weighted according to this value with no refund.

Weight: `O(S)` where S is the number of seconds a proposal already has.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `PropIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'second', {'proposal': 'u32'}
)
```

---------
### spend_from_treasury
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 
| beneficiary | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'spend_from_treasury', {
    'beneficiary': 'AccountId',
    'value': 'u128',
}
)
```

---------
### table_proposal
Same as `fast_track` but with the default `VotingPeriod`.

The dispatch of this call must be `FastTrackOrigin`.

- `prop_index`: The index of the proposal.
- `delay`: The number of blocks to wait after approval before execution.

Emits `Started` and `FastTrack`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| prop_index | `PropIndex` | 
| delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'table_proposal', {'delay': 'u32', 'prop_index': 'u32'}
)
```

---------
### vote
Vote in a referendum. If `vote.is_aye()`, the vote is to enact the proposal;
otherwise it is a vote to keep the status quo.

The dispatch origin of this call must be _Signed_.

- `ref_index`: The index of the referendum to vote for.
- `vote`: The vote configuration.

Weight: `O(R)` where R is the number of referendums the voter has voted on.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 
| vote | `Vote<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'vote', {
    'ref_index': 'u32',
    'vote': {
        'aye': 'bool',
        'balance': 'u128',
    },
}
)
```

---------
## Events

---------
### Cancelled
A referendum has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
### CancelledProposal
A proposal has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| prop_index | `PropIndex` | ```u32```

---------
### FastTrack
A proposal has been fast tracked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
### FastTrackReferendum
A referendum has been fast tracked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
### NotPassed
A proposal has been rejected by referendum.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
### Passed
A proposal has been approved by referendum.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
### Proposed
A motion has been proposed by a public account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```

---------
### Started
A referendum has begun.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```
| threshold | `VoteThreshold` | ```('SuperMajorityApprove', 'SuperMajorityAgainst', 'SimpleMajority')```

---------
### Tabled
A public proposal has been tabled for referendum vote.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### DepositOf
 Those who have locked a deposit.

 TWOX-NOTE: Safe, as increasing integer keys are safe.

#### Python
```python
result = substrate.query(
    'Democracy', 'DepositOf', ['u32']
)
```

#### Return value
```python
(['AccountId'], 'u128')
```
---------
### LowestUnbaked
 The lowest referendum index representing an unbaked referendum. Equal to
 `ReferendumCount` if there isn&#x27;t a unbaked referendum.

#### Python
```python
result = substrate.query(
    'Democracy', 'LowestUnbaked', []
)
```

#### Return value
```python
'u32'
```
---------
### NextLaunchTimestamp

#### Python
```python
result = substrate.query(
    'Democracy', 'NextLaunchTimestamp', []
)
```

#### Return value
```python
'u64'
```
---------
### PublicPropCount
 The number of (public) proposals that have been made so far.

#### Python
```python
result = substrate.query(
    'Democracy', 'PublicPropCount', []
)
```

#### Return value
```python
'u32'
```
---------
### PublicProps
 The public proposals. Unsorted. The second item is the proposal.

#### Python
```python
result = substrate.query(
    'Democracy', 'PublicProps', []
)
```

#### Return value
```python
[
    (
        'u32',
        {
            'Inline': 'Bytes',
            'Legacy': {'hash': 'scale_info::12'},
            'Lookup': {'hash': 'scale_info::12', 'len': 'u32'},
        },
        'AccountId',
    ),
]
```
---------
### ReferendumCount
 The next free referendum index, aka the number of referenda started so far.

#### Python
```python
result = substrate.query(
    'Democracy', 'ReferendumCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ReferendumInfoOf
 Information concerning any given referendum.

 TWOX-NOTE: SAFE as indexes are not under an attacker’s control.

#### Python
```python
result = substrate.query(
    'Democracy', 'ReferendumInfoOf', ['u32']
)
```

#### Return value
```python
{
    'Finished': {'approved': 'bool', 'end': 'u32'},
    'Ongoing': {
        'delay': 'u32',
        'end': 'u32',
        'proposal': {
            'Inline': 'Bytes',
            'Legacy': {'hash': 'scale_info::12'},
            'Lookup': {'hash': 'scale_info::12', 'len': 'u32'},
        },
        'tally': {'ayes': 'u128', 'nays': 'u128', 'turnout': 'u128'},
        'threshold': (
            'SuperMajorityApprove',
            'SuperMajorityAgainst',
            'SimpleMajority',
        ),
    },
}
```
---------
### VotingOf
 All votes for a particular voter. We store the balance for the number of votes that we
 have recorded.

 TWOX-NOTE: SAFE as `AccountId`s are crypto hashes anyway.

#### Python
```python
result = substrate.query(
    'Democracy', 'VotingOf', ['AccountId']
)
```

#### Return value
```python
{'votes': [('u32', {'aye': 'bool', 'balance': 'u128'})]}
```
---------
## Constants

---------
### EnactmentPeriod
 The period between a proposal being approved and enacted.

 It should generally be a little more than the unstake period to ensure that
 voting stakers have an opportunity to remove themselves from the system in the case
 where they are on the losing side of a vote.
#### Value
```python
1800
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'EnactmentPeriod')
```
---------
### FastTrackVotingPeriod
 Minimum voting period allowed for a fast-track referendum.
#### Value
```python
900
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'FastTrackVotingPeriod')
```
---------
### MaxDeposits
 The maximum number of deposits a public proposal may have at any time.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'MaxDeposits')
```
---------
### MaxProposals
 The maximum number of public proposals that can exist at any time.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'MaxProposals')
```
---------
### MaxVotes
 The maximum number of votes for an account.

 Also used to compute weight, an overly big value can
 lead to extrinsic with very big weight.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'MaxVotes')
```
---------
### MinimumDeposit
 The minimum amount to be used as a deposit for a public referendum proposal.
#### Value
```python
5000000000000
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'MinimumDeposit')
```
---------
### VotingPeriod
 How often (in blocks) to check for new votes.
#### Value
```python
14400
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'VotingPeriod')
```
---------
## Errors

---------
### Imminent
Imminent

---------
### InsufficientFunds
Too high a balance was provided that the account cannot afford.

---------
### MaxVotesReached
Maximum number of votes reached.

---------
### NoneWaiting
No proposals waiting

---------
### NotImminent
Not imminent

---------
### NotProposer
The given account did not make this proposal.

---------
### NotVoter
The given account did not vote on the referendum.

---------
### PreimageMissing
Preimage does not exist

---------
### ProposalMissing
Proposal does not exist

---------
### ReferendumFastTrackFailed
Fast tracking failed, because the referendum is
ending sooner than the fast track voting period.

---------
### ReferendumInvalid
Vote given for invalid referendum

---------
### TooEarly
Too early

---------
### TooMany
Maximum number of items reached.

---------
### TryIntoIntError
Unable to convert value.

---------
### ValueLow
Value too low

---------
### WrongUpperBound
Invalid upper bound.

---------