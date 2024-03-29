
# Council

---------
## Calls

---------
### close
Close a vote that is either approved, disapproved or whose voting period has ended.

May be called by any signed account in order to finish voting and close the proposal.

If called before the end of the voting period it will only close the vote if it is
has enough votes to be approved or disapproved.

If called after the end of the voting period abstentions are counted as rejections
unless there is a prime member set and the prime member cast an approval.

If the close operation completes successfully with disapproval, the transaction fee will
be waived. Otherwise execution of the approved operation will be charged to the caller.

+ `proposal_weight_bound`: The maximum amount of weight consumed by executing the closed
proposal.
+ `length_bound`: The upper bound for the length of the proposal in storage. Checked via
`storage::read` so it is `size_of::&lt;u32&gt;() == 4` larger than the pure length.

\#\# Complexity
- `O(B + M + P1 + P2)` where:
  - `B` is `proposal` size in bytes (length-fee-bounded)
  - `M` is members-count (code- and governance-bounded)
  - `P1` is the complexity of `proposal` preimage.
  - `P2` is proposal-count (code-bounded)
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `Weight` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'close', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': 'scale_info::16',
    'proposal_weight_bound': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### disapprove_proposal
Disapprove a proposal, close, and remove it from the system, regardless of its current
state.

Must be called by the Root origin.

Parameters:
* `proposal_hash`: The hash of the proposal that should be disapproved.

\#\# Complexity
O(P) where P is the number of max proposals
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'disapprove_proposal', {'proposal_hash': 'scale_info::16'}
)
```

---------
### execute
Dispatch a proposal from a member using the `Member` origin.

Origin must be a member of the collective.

\#\# Complexity:
- `O(B + M + P)` where:
- `B` is `proposal` size in bytes (length-fee-bounded)
- `M` members-count (code-bounded)
- `P` complexity of dispatching `proposal`
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'execute', {
    'length_bound': 'u32',
    'proposal': 'Call',
}
)
```

---------
### propose
Add a new proposal to either be voted on or executed directly.

Requires the sender to be member.

`threshold` determines whether `proposal` is executed directly (`threshold &lt; 2`)
or put up for voting.

\#\# Complexity
- `O(B + M + P1)` or `O(B + M + P2)` where:
  - `B` is `proposal` size in bytes (length-fee-bounded)
  - `M` is members-count (code- and governance-bounded)
  - branching is influenced by `threshold` where:
    - `P1` is proposal execution complexity (`threshold &lt; 2`)
    - `P2` is proposals-count (code-bounded) (`threshold &gt;= 2`)
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `MemberCount` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'propose', {
    'length_bound': 'u32',
    'proposal': 'Call',
    'threshold': 'u32',
}
)
```

---------
### set_members
Set the collective&\#x27;s membership.

- `new_members`: The new member list. Be nice to the chain and provide it sorted.
- `prime`: The prime member whose vote sets the default.
- `old_count`: The upper bound for the previous number of members in storage. Used for
  weight estimation.

The dispatch of this call must be `SetMembersOrigin`.

NOTE: Does not enforce the expected `MaxMembers` limit on the amount of members, but
      the weight estimations rely on it to estimate dispatchable weight.

\# WARNING:

The `pallet-collective` can also be managed by logic outside of the pallet through the
implementation of the trait [`ChangeMembers`].
Any call to `set_members` must be careful that the member set doesn&\#x27;t get out of sync
with other logic managing the member set.

\#\# Complexity:
- `O(MP + N)` where:
  - `M` old-members-count (code- and governance-bounded)
  - `N` new-members-count (code- and governance-bounded)
  - `P` proposals-count (code-bounded)
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_members | `Vec<T::AccountId>` | 
| prime | `Option<T::AccountId>` | 
| old_count | `MemberCount` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'set_members', {
    'new_members': ['AccountId'],
    'old_count': 'u32',
    'prime': (None, 'AccountId'),
}
)
```

---------
### vote
Add an aye or nay vote for the sender to the given proposal.

Requires the sender to be a member.

Transaction fees will be waived if the member is voting on any particular proposal
for the first time and the call is successful. Subsequent vote changes will charge a
fee.
\#\# Complexity
- `O(M)` where `M` is members-count (code- and governance-bounded)
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'vote', {
    'approve': 'bool',
    'index': 'u32',
    'proposal': 'scale_info::16',
}
)
```

---------
## Events

---------
### Approved
A motion was approved by the required threshold.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::16```

---------
### Closed
A proposal was closed because its threshold was reached or after its duration was up.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::16```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
### Disapproved
A motion was not approved by the required threshold.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::16```

---------
### Executed
A motion was executed; result will be `Ok` if it returned without error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::16```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### MemberExecuted
A single member did some action; result will be `Ok` if it returned without error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::16```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### Proposed
A motion (given hash) has been proposed (by given account) with a threshold (given
`MemberCount`).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```scale_info::16```
| threshold | `MemberCount` | ```u32```

---------
### Voted
A motion (given hash) has been voted on by given account, leaving
a tally (yes votes and no votes given respectively as `MemberCount`).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_hash | `T::Hash` | ```scale_info::16```
| voted | `bool` | ```bool```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
## Storage functions

---------
### Members
 The current members of the collective. This is stored sorted (just by value).

#### Python
```python
result = substrate.query(
    'Council', 'Members', []
)
```

#### Return value
```python
['AccountId']
```
---------
### Prime
 The prime member that helps determine the default vote behavior in case of absentations.

#### Python
```python
result = substrate.query(
    'Council', 'Prime', []
)
```

#### Return value
```python
'AccountId'
```
---------
### ProposalCount
 Proposals so far.

#### Python
```python
result = substrate.query(
    'Council', 'ProposalCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ProposalOf
 Actual proposal for a given hash, if it&#x27;s current.

#### Python
```python
result = substrate.query(
    'Council', 'ProposalOf', ['scale_info::16']
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
    'Council', 'Proposals', []
)
```

#### Return value
```python
['scale_info::16']
```
---------
### Voting
 Votes on a given proposal, if it is ongoing.

#### Python
```python
result = substrate.query(
    'Council', 'Voting', ['scale_info::16']
)
```

#### Return value
```python
{'ayes': ['AccountId'], 'end': 'u32', 'index': 'u32', 'nays': ['AccountId'], 'threshold': 'u32'}
```
---------
## Constants

---------
### MaxProposalWeight
 The maximum weight of a dispatch call that can be proposed and executed.
#### Value
```python
{'proof_size': 5242880, 'ref_time': 500000000000}
```
#### Python
```python
constant = substrate.get_constant('Council', 'MaxProposalWeight')
```
---------
## Errors

---------
### AlreadyInitialized
Members are already initialized!

---------
### DuplicateProposal
Duplicate proposals not allowed

---------
### DuplicateVote
Duplicate vote ignored

---------
### NotMember
Account is not a member

---------
### ProposalMissing
Proposal must exist

---------
### TooEarly
The close call was made too early, before the end of the voting.

---------
### TooManyProposals
There can only be a maximum of `MaxProposals` active proposals.

---------
### WrongIndex
Mismatched index

---------
### WrongProposalLength
The given length bound for the proposal was too low.

---------
### WrongProposalWeight
The given weight bound for the proposal was too low.

---------