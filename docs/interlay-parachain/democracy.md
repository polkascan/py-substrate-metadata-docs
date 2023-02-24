
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
### cancel_queued
Cancel a proposal queued for enactment.

The dispatch origin of this call must be _Root_.

- `which`: The index of the referendum to cancel.

Weight: `O(D)` where `D` is the items in the dispatch queue. Weighted as `D = 10`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| which | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'cancel_queued', {'which': 'u32'}
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
### enact_proposal
Enact a proposal from a referendum. For now we just make the weight be the maximum.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'enact_proposal', {
    'index': 'u32',
    'proposal_hash': '[u8; 32]',
}
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
### fast_track_default
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
    'Democracy', 'fast_track_default', {'delay': 'u32', 'prop_index': 'u32'}
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
### note_imminent_preimage
Register the preimage for an upcoming proposal. This requires the proposal to be
in the dispatch queue. No deposit is needed. When this call is successful, i.e.
the preimage has not been uploaded before and matches some imminent proposal,
no fee is paid.

The dispatch origin of this call must be _Signed_.

- `encoded_proposal`: The preimage of a proposal.

Emits `PreimageNoted`.

Weight: `O(E)` with E size of `encoded_proposal` (protected by a required deposit).
#### Attributes
| Name | Type |
| -------- | -------- | 
| encoded_proposal | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'note_imminent_preimage', {'encoded_proposal': 'Bytes'}
)
```

---------
### note_preimage
Register the preimage for an upcoming proposal. This doesn&\#x27;t require the proposal to be
in the dispatch queue but does require a deposit, returned once enacted.

The dispatch origin of this call must be _Signed_.

- `encoded_proposal`: The preimage of a proposal.

Emits `PreimageNoted`.

Weight: `O(E)` with E size of `encoded_proposal` (protected by a required deposit).
#### Attributes
| Name | Type |
| -------- | -------- | 
| encoded_proposal | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'note_preimage', {'encoded_proposal': 'Bytes'}
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
| proposal_hash | `T::Hash` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'propose', {
    'proposal_hash': '[u8; 32]',
    'value': 'u128',
}
)
```

---------
### reap_preimage
Remove an expired proposal preimage and collect the deposit.

The dispatch origin of this call must be _Signed_.

- `proposal_hash`: The preimage hash of a proposal.
- `proposal_length_upper_bound`: an upper bound on length of the proposal. Extrinsic is weighted according
  to this value with no refund.

This will only work after `VotingPeriod` blocks from the time that the preimage was
noted, if it&\#x27;s the same account doing it. If it&\#x27;s a different account, then it&\#x27;ll only
work an additional `EnactmentPeriod` later.

Emits `PreimageReaped`.

Weight: `O(D)` where D is length of proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| proposal_len_upper_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'reap_preimage', {
    'proposal_hash': '[u8; 32]',
    'proposal_len_upper_bound': 'u32',
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
| seconds_upper_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'second', {
    'proposal': 'u32',
    'seconds_upper_bound': 'u32',
}
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
A referendum has been cancelled. \[ref_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ReferendumIndex` | ```u32```

---------
### Executed
A proposal has been enacted. \[ref_index, result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ReferendumIndex` | ```u32```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### FastTrack
A proposal has been fast tracked. \[ref_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ReferendumIndex` | ```u32```

---------
### FastTrackReferendum
A referendum has been fast tracked. \[ref_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ReferendumIndex` | ```u32```

---------
### NotPassed
A proposal has been rejected by referendum. \[ref_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ReferendumIndex` | ```u32```

---------
### Passed
A proposal has been approved by referendum. \[ref_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ReferendumIndex` | ```u32```

---------
### PreimageInvalid
A proposal could not be executed because its preimage was invalid.
\[proposal_hash, ref_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `ReferendumIndex` | ```u32```

---------
### PreimageMissing
A proposal could not be executed because its preimage was missing.
\[proposal_hash, ref_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `ReferendumIndex` | ```u32```

---------
### PreimageNoted
A proposal&\#x27;s preimage was noted, and the deposit taken. \[proposal_hash, who, deposit\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### PreimageReaped
A registered preimage was removed and the deposit collected by the reaper.
\[proposal_hash, provider, deposit, reaper\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `T::AccountId` | ```AccountId```

---------
### PreimageUsed
A proposal preimage was removed and used (the deposit was returned).
\[proposal_hash, provider, deposit\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Proposed
A motion has been proposed by a public account. \[proposal_index, deposit\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PropIndex` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### Started
A referendum has begun. \[ref_index, threshold\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ReferendumIndex` | ```u32```
| None | `VoteThreshold` | ```('SuperMajorityApprove', 'SuperMajorityAgainst', 'SimpleMajority')```

---------
### Tabled
A public proposal has been tabled for referendum vote. \[proposal_index, deposit,
depositors\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PropIndex` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `Vec<T::AccountId>` | ```['AccountId']```

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
### Preimages
 Map of hashes to the proposal preimage, along with who registered it and their deposit.
 The block number is the block at which it was deposited.

#### Python
```python
result = substrate.query(
    'Democracy', 'Preimages', ['[u8; 32]']
)
```

#### Return value
```python
{
    'Available': {
        'data': 'Bytes',
        'deposit': 'u128',
        'expiry': (None, 'u32'),
        'provider': 'AccountId',
        'since': 'u32',
    },
    'Missing': 'u32',
}
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
 The public proposals. Unsorted. The second item is the proposal&#x27;s hash.

#### Python
```python
result = substrate.query(
    'Democracy', 'PublicProps', []
)
```

#### Return value
```python
[('u32', '[u8; 32]', 'AccountId')]
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
        'proposal_hash': '[u8; 32]',
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
### StorageVersion
 Storage version of the pallet.

 New networks start with last version.

#### Python
```python
result = substrate.query(
    'Democracy', 'StorageVersion', []
)
```

#### Return value
```python
('V1', )
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
7200
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
2500000000000
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'MinimumDeposit')
```
---------
### PreimageByteDeposit
 The amount of balance that must be deposited per byte of preimage stored.
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'PreimageByteDeposit')
```
---------
### VotingPeriod
 How often (in blocks) to check for new votes.
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'VotingPeriod')
```
---------
## Errors

---------
### DuplicatePreimage
Preimage already noted

---------
### DuplicateProposal
Proposal already made

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
### PreimageInvalid
Invalid preimage

---------
### PreimageMissing
Preimage not found

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
### TooManyProposals
Maximum number of proposals reached.

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