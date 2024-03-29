
# Democracy

---------
## Calls

---------
### blacklist
Permanently place a proposal into the blacklist. This prevents it from ever being
proposed again.

If called on a queued public or external proposal, then this will result in it being
removed. If the `ref_index` supplied is an active referendum with the proposal hash,
then it will be cancelled.

The dispatch origin of this call must be `BlacklistOrigin`.

- `proposal_hash`: The proposal hash to blacklist permanently.
- `ref_index`: An ongoing referendum whose hash is `proposal_hash`, which will be
cancelled.

Weight: `O(p)` (though as this is an high-privilege dispatch, we assume it has a
  reasonable value).
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `H256` | 
| maybe_ref_index | `Option<ReferendumIndex>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'blacklist', {
    'maybe_ref_index': (None, 'u32'),
    'proposal_hash': 'scale_info::12',
}
)
```

---------
### cancel_proposal
Remove a proposal.

The dispatch origin of this call must be `CancelProposalOrigin`.

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
### delegate
Delegate the voting power (with some given conviction) of the sending account.

The balance delegated is locked for as long as it&\#x27;s delegated, and thereafter for the
time appropriate for the conviction&\#x27;s lock period.

The dispatch origin of this call must be _Signed_, and the signing account must either:
  - be delegating already; or
  - have no voting activity (if there is, then it will need to be removed/consolidated
    through `reap_vote` or `unvote`).

- `to`: The account whose voting the `target` account&\#x27;s voting power will follow.
- `conviction`: The conviction that will be attached to the delegated votes. When the
  account is undelegated, the funds will be locked for the corresponding period.
- `balance`: The amount of the account&\#x27;s balance to be used in delegating. This must not
  be more than the account&\#x27;s current balance.

Emits `Delegated`.

Weight: `O(R)` where R is the number of referendums the voter delegating to has
  voted on. Weight is charged as if maximum votes.
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `AccountIdLookupOf<T>` | 
| conviction | `Conviction` | 
| balance | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'delegate', {
    'balance': 'u128',
    'conviction': (
        'None',
        'Locked1x',
        'Locked2x',
        'Locked3x',
        'Locked4x',
        'Locked5x',
        'Locked6x',
    ),
    'to': {
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
### emergency_cancel
Schedule an emergency cancellation of a referendum. Cannot happen twice to the same
referendum.

The dispatch origin of this call must be `CancellationOrigin`.

-`ref_index`: The index of the referendum to cancel.

Weight: `O(1)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'emergency_cancel', {'ref_index': 'u32'}
)
```

---------
### external_propose
Schedule a referendum to be tabled once it is legal to schedule an external
referendum.

The dispatch origin of this call must be `ExternalOrigin`.

- `proposal_hash`: The preimage hash of the proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `BoundedCallOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose', {
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
}
)
```

---------
### external_propose_default
Schedule a negative-turnout-bias referendum to be tabled next once it is legal to
schedule an external referendum.

The dispatch of this call must be `ExternalDefaultOrigin`.

- `proposal_hash`: The preimage hash of the proposal.

Unlike `external_propose`, blacklisting has no effect on this and it may replace a
pre-scheduled `external_propose` call.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `BoundedCallOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose_default', {
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
}
)
```

---------
### external_propose_majority
Schedule a majority-carries referendum to be tabled next once it is legal to schedule
an external referendum.

The dispatch of this call must be `ExternalMajorityOrigin`.

- `proposal_hash`: The preimage hash of the proposal.

Unlike `external_propose`, blacklisting has no effect on this and it may replace a
pre-scheduled `external_propose` call.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `BoundedCallOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose_majority', {
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
}
)
```

---------
### fast_track
Schedule the currently externally-proposed majority-carries referendum to be tabled
immediately. If there is no externally-proposed referendum currently, or if there is one
but it is not a majority-carries referendum then it fails.

The dispatch of this call must be `FastTrackOrigin`.

- `proposal_hash`: The hash of the current external proposal.
- `voting_period`: The period that is allowed for voting on this proposal. Increased to
	Must be always greater than zero.
	For `FastTrackOrigin` must be equal or greater than `FastTrackVotingPeriod`.
- `delay`: The number of block after voting has ended in approval and this should be
  enacted. This doesn&\#x27;t have a minimum amount.

Emits `Started`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `H256` | 
| voting_period | `T::BlockNumber` | 
| delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'fast_track', {
    'delay': 'u32',
    'proposal_hash': 'scale_info::12',
    'voting_period': 'u32',
}
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
### remove_other_vote
Remove a vote for a referendum.

If the `target` is equal to the signer, then this function is exactly equivalent to
`remove_vote`. If not equal to the signer, then the vote must have expired,
either because the referendum was cancelled, because the voter lost the referendum or
because the conviction period is over.

The dispatch origin of this call must be _Signed_.

- `target`: The account of the vote to be removed; this account must have voted for
  referendum `index`.
- `index`: The index of referendum of the vote to be removed.

Weight: `O(R + log R)` where R is the number of referenda that `target` has voted on.
  Weight is calculated for the maximum number of vote.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'remove_other_vote', {
    'index': 'u32',
    'target': {
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
### remove_vote
Remove a vote for a referendum.

If:
- the referendum was cancelled, or
- the referendum is ongoing, or
- the referendum has ended such that
  - the vote of the account was in opposition to the result; or
  - there was no conviction to the account&\#x27;s vote; or
  - the account made a split vote
...then the vote is removed cleanly and a following call to `unlock` may result in more
funds being available.

If, however, the referendum has ended and:
- it finished corresponding to the vote of the account, and
- the account made a standard vote with conviction, and
- the lock period of the conviction is not over
...then the lock will be aggregated into the overall account&\#x27;s lock, which may involve
*overlocking* (where the two locks are combined into a single lock that is the maximum
of both the amount locked and the time is it locked for).

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
### set_metadata
Set or clear a metadata of a proposal or a referendum.

Parameters:
- `origin`: Must correspond to the `MetadataOwner`.
    - `ExternalOrigin` for an external proposal with the `SuperMajorityApprove`
      threshold.
    - `ExternalDefaultOrigin` for an external proposal with the `SuperMajorityAgainst`
      threshold.
    - `ExternalMajorityOrigin` for an external proposal with the `SimpleMajority`
      threshold.
    - `Signed` by a creator for a public proposal.
    - `Signed` to clear a metadata for a finished referendum.
    - `Root` to set a metadata for an ongoing referendum.
- `owner`: an identifier of a metadata owner.
- `maybe_hash`: The hash of an on-chain stored preimage. `None` to clear a metadata.
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `MetadataOwner` | 
| maybe_hash | `Option<PreimageHash>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'set_metadata', {
    'maybe_hash': (
        None,
        'scale_info::12',
    ),
    'owner': {
        'External': None,
        'Proposal': 'u32',
        'Referendum': 'u32',
    },
}
)
```

---------
### undelegate
Undelegate the voting power of the sending account.

Tokens may be unlocked following once an amount of time consistent with the lock period
of the conviction with which the delegation was issued.

The dispatch origin of this call must be _Signed_ and the signing account must be
currently delegating.

Emits `Undelegated`.

Weight: `O(R)` where R is the number of referendums the voter delegating to has
  voted on. Weight is charged as if maximum votes.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'undelegate', {}
)
```

---------
### unlock
Unlock tokens that have an expired lock.

The dispatch origin of this call must be _Signed_.

- `target`: The account to remove the lock on.

Weight: `O(R)` with R number of vote of target.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'unlock', {
    'target': {
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
### veto_external
Veto and blacklist the external proposal hash.

The dispatch origin of this call must be `VetoOrigin`.

- `proposal_hash`: The preimage hash of the proposal to veto and blacklist.

Emits `Vetoed`.

Weight: `O(V + log(V))` where V is number of `existing vetoers`
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'veto_external', {'proposal_hash': 'scale_info::12'}
)
```

---------
### vote
Vote in a referendum. If `vote.is_aye()`, the vote is to enact the proposal;
otherwise it is a vote to keep the status quo.

The dispatch origin of this call must be _Signed_.

- `ref_index`: The index of the referendum to vote for.
- `vote`: The vote configuration.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 
| vote | `AccountVote<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Democracy', 'vote', {
    'ref_index': 'u32',
    'vote': {
        'Split': {
            'aye': 'u128',
            'nay': 'u128',
        },
        'Standard': {
            'balance': 'u128',
            'vote': {
                'aye': 'bool',
                'conviction': (
                    'None',
                    'Locked1x',
                    'Locked2x',
                    'Locked3x',
                    'Locked4x',
                    'Locked5x',
                    'Locked6x',
                ),
            },
        },
    },
}
)
```

---------
## Events

---------
### Blacklisted
A proposal_hash has been blacklisted permanently.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `H256` | ```scale_info::12```

---------
### Cancelled
A referendum has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
### Delegated
An account has delegated their vote to another account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| target | `T::AccountId` | ```AccountId```

---------
### ExternalTabled
An external proposal has been tabled.
#### Attributes
No attributes

---------
### MetadataCleared
Metadata for a proposal or a referendum has been cleared.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `MetadataOwner` | ```{'External': None, 'Proposal': 'u32', 'Referendum': 'u32'}```
| hash | `PreimageHash` | ```scale_info::12```

---------
### MetadataSet
Metadata for a proposal or a referendum has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `MetadataOwner` | ```{'External': None, 'Proposal': 'u32', 'Referendum': 'u32'}```
| hash | `PreimageHash` | ```scale_info::12```

---------
### MetadataTransferred
Metadata has been transferred to new owner.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| prev_owner | `MetadataOwner` | ```{'External': None, 'Proposal': 'u32', 'Referendum': 'u32'}```
| owner | `MetadataOwner` | ```{'External': None, 'Proposal': 'u32', 'Referendum': 'u32'}```
| hash | `PreimageHash` | ```scale_info::12```

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
### ProposalCanceled
A proposal got canceled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| prop_index | `PropIndex` | ```u32```

---------
### Proposed
A motion has been proposed by a public account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```

---------
### Seconded
An account has secconded a proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| seconder | `T::AccountId` | ```AccountId```
| prop_index | `PropIndex` | ```u32```

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
### Undelegated
An account has cancelled a previous delegation operation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### Vetoed
An external proposal has been vetoed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| proposal_hash | `H256` | ```scale_info::12```
| until | `T::BlockNumber` | ```u32```

---------
### Voted
An account has voted in a referendum
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| voter | `T::AccountId` | ```AccountId```
| ref_index | `ReferendumIndex` | ```u32```
| vote | `AccountVote<BalanceOf<T>>` | ```{'Standard': {'vote': {'aye': 'bool', 'conviction': ('None', 'Locked1x', 'Locked2x', 'Locked3x', 'Locked4x', 'Locked5x', 'Locked6x')}, 'balance': 'u128'}, 'Split': {'aye': 'u128', 'nay': 'u128'}}```

---------
## Storage functions

---------
### Blacklist
 A record of who vetoed what. Maps proposal hash to a possible existent block number
 (until when it may not be resubmitted) and who vetoed it.

#### Python
```python
result = substrate.query(
    'Democracy', 'Blacklist', ['scale_info::12']
)
```

#### Return value
```python
('u32', ['AccountId'])
```
---------
### Cancellations
 Record of all proposals that have been subject to emergency cancellation.

#### Python
```python
result = substrate.query(
    'Democracy', 'Cancellations', ['scale_info::12']
)
```

#### Return value
```python
'bool'
```
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
### LastTabledWasExternal
 True if the last referendum tabled was submitted externally. False if it was a public
 proposal.

#### Python
```python
result = substrate.query(
    'Democracy', 'LastTabledWasExternal', []
)
```

#### Return value
```python
'bool'
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
### MetadataOf
 General information concerning any proposal or referendum.
 The `PreimageHash` refers to the preimage of the `Preimages` provider which can be a JSON
 dump or IPFS hash of a JSON file.

 Consider a garbage collection for a metadata of finished referendums to `unrequest` (remove)
 large preimages.

#### Python
```python
result = substrate.query(
    'Democracy', 'MetadataOf', [
    {
        'External': None,
        'Proposal': 'u32',
        'Referendum': 'u32',
    },
]
)
```

#### Return value
```python
'scale_info::12'
```
---------
### NextExternal
 The referendum to be tabled whenever it would be valid to table an external proposal.
 This happens when a referendum needs to be tabled and one of two conditions are met:
 - `LastTabledWasExternal` is `false`; or
 - `PublicProps` is empty.

#### Python
```python
result = substrate.query(
    'Democracy', 'NextExternal', []
)
```

#### Return value
```python
(
    {
        'Inline': 'Bytes',
        'Legacy': {'hash': 'scale_info::12'},
        'Lookup': {'hash': 'scale_info::12', 'len': 'u32'},
    },
    ('SuperMajorityApprove', 'SuperMajorityAgainst', 'SimpleMajority'),
)
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
 have recorded. The second item is the total amount of delegations, that will be added.

 TWOX-NOTE: SAFE as `AccountId`s are crypto hashes anyway.

#### Python
```python
result = substrate.query(
    'Democracy', 'VotingOf', ['AccountId']
)
```

#### Return value
```python
{
    'Delegating': {
        'balance': 'u128',
        'conviction': (
            'None',
            'Locked1x',
            'Locked2x',
            'Locked3x',
            'Locked4x',
            'Locked5x',
            'Locked6x',
        ),
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'target': 'AccountId',
    },
    'Direct': {
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'votes': [('u32', 'scale_info::49')],
    },
}
```
---------
## Constants

---------
### CooloffPeriod
 Period in blocks where an external proposal may not be re-submitted after being vetoed.
#### Value
```python
36000
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'CooloffPeriod')
```
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
### InstantAllowed
 Indicator for whether an emergency origin is even allowed to happen. Some chains may
 want to set this permanently to `false`, others may want to condition it on things such
 as an upgrade having happened recently.
#### Value
```python
True
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'InstantAllowed')
```
---------
### LaunchPeriod
 How often (in blocks) new public referenda are launched.
#### Value
```python
36000
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'LaunchPeriod')
```
---------
### MaxBlacklisted
 The maximum number of items which can be blacklisted.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'MaxBlacklisted')
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
 lead to extrinsic with very big weight: see `delegate` for instance.
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
100000000000000
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'MinimumDeposit')
```
---------
### VoteLockingPeriod
 The minimum period of vote locking.

 It should be no shorter than enactment period to ensure that in the case of an approval,
 those successful voters are locked into the consequences that their votes entail.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'VoteLockingPeriod')
```
---------
### VotingPeriod
 How often (in blocks) to check for new votes.
#### Value
```python
36000
```
#### Python
```python
constant = substrate.get_constant('Democracy', 'VotingPeriod')
```
---------
## Errors

---------
### AlreadyCanceled
Cannot cancel the same proposal twice

---------
### AlreadyDelegating
The account is already delegating.

---------
### AlreadyVetoed
Identity may not veto a proposal twice

---------
### DuplicateProposal
Proposal already made

---------
### InstantNotAllowed
The instant referendum origin is currently disallowed.

---------
### InsufficientFunds
Too high a balance was provided that the account cannot afford.

---------
### InvalidHash
Invalid hash

---------
### MaxVotesReached
Maximum number of votes reached.

---------
### NoPermission
The actor has no permission to conduct the action.

---------
### NoProposal
No external proposal

---------
### NoneWaiting
No proposals waiting

---------
### Nonsense
Delegation to oneself makes no sense.

---------
### NotDelegating
The account is not currently delegating.

---------
### NotSimpleMajority
Next external proposal not simple majority

---------
### NotVoter
The given account did not vote on the referendum.

---------
### PreimageNotExist
The preimage does not exist.

---------
### ProposalBlacklisted
Proposal still blacklisted

---------
### ProposalMissing
Proposal does not exist

---------
### ReferendumInvalid
Vote given for invalid referendum

---------
### TooMany
Maximum number of items reached.

---------
### ValueLow
Value too low

---------
### VotesExist
The account currently has votes attached to it and the operation cannot succeed until
these are removed, either through `unvote` or `reap_vote`.

---------
### VotingPeriodLow
Voting period too low

---------
### WrongUpperBound
Invalid upper bound.

---------