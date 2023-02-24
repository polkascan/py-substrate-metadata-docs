
# PhragmenElection

---------
## Calls

---------
### clean_defunct_voters
Clean all voters who are defunct (i.e. they do not serve any purpose at all). The
deposit of the removed voters are returned.

This is an root function to be used only for cleaning the state.

The dispatch origin of this call must be root.

\# &lt;weight&gt;
The total number of voters and those that are defunct must be provided as witness data.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| num_voters | `u32` | 
| num_defunct | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PhragmenElection', 'clean_defunct_voters', {
    'num_defunct': 'u32',
    'num_voters': 'u32',
}
)
```

---------
### remove_member
Remove a particular member from the set. This is effective immediately and the bond of
the outgoing member is slashed.

If a runner-up is available, then the best runner-up will be removed and replaces the
outgoing member. Otherwise, if `rerun_election` is `true`, a new phragmen election is
started, else, nothing happens.

If `slash_bond` is set to true, the bond of the member being removed is slashed. Else,
it is returned.

The dispatch origin of this call must be root.

Note that this does not affect the designated block number of the next election.

\# &lt;weight&gt;
If we have a replacement, we use a small weight. Else, since this is a root call and
will go into phragmen, we assume full block for now.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| slash_bond | `bool` | 
| rerun_election | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'PhragmenElection', 'remove_member', {
    'rerun_election': 'bool',
    'slash_bond': 'bool',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_voter
Remove `origin` as a voter.

This removes the lock and returns the deposit.

The dispatch origin of this call must be signed and be a voter.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PhragmenElection', 'remove_voter', {}
)
```

---------
### renounce_candidacy
Renounce one&\#x27;s intention to be a candidate for the next election round. 3 potential
outcomes exist:

- `origin` is a candidate and not elected in any set. In this case, the deposit is
  unreserved, returned and origin is removed as a candidate.
- `origin` is a current runner-up. In this case, the deposit is unreserved, returned and
  origin is removed as a runner-up.
- `origin` is a current member. In this case, the deposit is unreserved and origin is
  removed as a member, consequently not being a candidate for the next round anymore.
  Similar to [`remove_member`](Self::remove_member), if replacement runners exists, they
  are immediately used. If the prime is renouncing, then no prime will exist until the
  next round.

The dispatch origin of this call must be signed, and have one of the above roles.

\# &lt;weight&gt;
The type of renouncing must be provided as witness data.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| renouncing | `Renouncing` | 

#### Python
```python
call = substrate.compose_call(
    'PhragmenElection', 'renounce_candidacy', {
    'renouncing': {
        'Candidate': 'u32',
        'Member': None,
        'RunnerUp': None,
    },
}
)
```

---------
### submit_candidacy
Submit oneself for candidacy. A fixed amount of deposit is recorded.

All candidates are wiped at the end of the term. They either become a member/runner-up,
or leave the system while their deposit is slashed.

The dispatch origin of this call must be signed.

\#\#\# Warning

Even if a candidate ends up being a member, they must call [`Call::renounce_candidacy`]
to get their deposit back. Losing the spot in an election will always lead to a slash.

\# &lt;weight&gt;
The number of current candidates must be provided as witness data.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PhragmenElection', 'submit_candidacy', {'candidate_count': 'u32'}
)
```

---------
### vote
Vote for a set of candidates for the upcoming round of election. This can be called to
set the initial votes, or update already existing votes.

Upon initial voting, `value` units of `who`&\#x27;s balance is locked and a deposit amount is
reserved. The deposit is based on the number of votes and can be updated over time.

The `votes` should:
  - not be empty.
  - be less than the number of possible candidates. Note that all current members and
    runners-up are also automatically candidates for the next round.

If `value` is more than `who`&\#x27;s free balance, then the maximum of the two is used.

The dispatch origin of this call must be signed.

\#\#\# Warning

It is the responsibility of the caller to **NOT** place all of their balance into the
lock and keep some for further operations.

\# &lt;weight&gt;
We assume the maximum weight among all 3 cases: vote_equal, vote_more and vote_less.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| votes | `Vec<T::AccountId>` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhragmenElection', 'vote', {
    'value': 'u128',
    'votes': ['AccountId'],
}
)
```

---------
## Events

---------
### CandidateSlashed
A candidate was slashed by amount due to failing to obtain a seat as member or
runner-up.

Note that old members and runners-up are also candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `<T as frame_system::Config>::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### ElectionError
Internal error happened while trying to perform election.
#### Attributes
No attributes

---------
### EmptyTerm
No (or not enough) candidates existed for this round. This is different from
`NewTerm(\[\])`. See the description of `NewTerm`.
#### Attributes
No attributes

---------
### MemberKicked
A member has been removed. This should always be followed by either `NewTerm` or
`EmptyTerm`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `<T as frame_system::Config>::AccountId` | ```AccountId```

---------
### NewTerm
A new term with new_members. This indicates that enough candidates existed to run
the election, not that enough have has been elected. The inner value must be examined
for this purpose. A `NewTerm(\[\])` indicates that some candidates got their bond
slashed and none were elected, whilst `EmptyTerm` means that no candidates existed to
begin with.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_members | `Vec<(<T as frame_system::Config>::AccountId, BalanceOf<T>)>` | ```[('AccountId', 'u128')]```

---------
### Renounced
Someone has renounced their candidacy.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `<T as frame_system::Config>::AccountId` | ```AccountId```

---------
### SeatHolderSlashed
A seat holder was slashed by amount by being forcefully removed from the set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| seat_holder | `<T as frame_system::Config>::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Candidates
 The present candidate list. A current member or runner-up can never enter this vector
 and is always implicitly assumed to be a candidate.

 Second element is the deposit.

 Invariant: Always sorted based on account id.

#### Python
```python
result = substrate.query(
    'PhragmenElection', 'Candidates', []
)
```

#### Return value
```python
[('AccountId', 'u128')]
```
---------
### ElectionRounds
 The total number of vote rounds that have happened, excluding the upcoming one.

#### Python
```python
result = substrate.query(
    'PhragmenElection', 'ElectionRounds', []
)
```

#### Return value
```python
'u32'
```
---------
### Members
 The current elected members.

 Invariant: Always sorted based on account id.

#### Python
```python
result = substrate.query(
    'PhragmenElection', 'Members', []
)
```

#### Return value
```python
[{'deposit': 'u128', 'stake': 'u128', 'who': 'AccountId'}]
```
---------
### RunnersUp
 The current reserved runners-up.

 Invariant: Always sorted based on rank (worse to best). Upon removal of a member, the
 last (i.e. _best_) runner-up will be replaced.

#### Python
```python
result = substrate.query(
    'PhragmenElection', 'RunnersUp', []
)
```

#### Return value
```python
[{'deposit': 'u128', 'stake': 'u128', 'who': 'AccountId'}]
```
---------
### Voting
 Votes and locked stake of a particular voter.

 TWOX-NOTE: SAFE as `AccountId` is a crypto hash.

#### Python
```python
result = substrate.query(
    'PhragmenElection', 'Voting', ['AccountId']
)
```

#### Return value
```python
{'deposit': 'u128', 'stake': 'u128', 'votes': ['AccountId']}
```
---------
## Constants

---------
### CandidacyBond
 How much should be locked up in order to submit one&#x27;s candidacy.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'CandidacyBond')
```
---------
### DesiredMembers
 Number of members to elect.
#### Value
```python
7
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'DesiredMembers')
```
---------
### DesiredRunnersUp
 Number of runners_up to keep.
#### Value
```python
7
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'DesiredRunnersUp')
```
---------
### MaxCandidates
 The maximum number of candidates in a phragmen election.

 Warning: The election happens onchain, and this value will determine
 the size of the election. When this limit is reached no more
 candidates are accepted in the election.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'MaxCandidates')
```
---------
### MaxVoters
 The maximum number of voters to allow in a phragmen election.

 Warning: This impacts the size of the election which is run onchain.
 When the limit is reached the new voters are ignored.
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'MaxVoters')
```
---------
### PalletId
 Identifier for the elections-phragmen pallet&#x27;s lock
#### Value
```python
'0x706872656c656374'
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'PalletId')
```
---------
### TermDuration
 How long each seat is kept. This defines the next block number at which an election
 round will happen. If set to zero, no elections are ever triggered and the module will
 be in passive mode.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'TermDuration')
```
---------
### VotingBondBase
 Base deposit associated with voting.

 This should be sensibly high to economically ensure the pallet cannot be attacked by
 creating a gigantic number of votes.
#### Value
```python
3990000000000
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'VotingBondBase')
```
---------
### VotingBondFactor
 The amount of bond that need to be locked for each vote (32 bytes).
#### Value
```python
1920000000000
```
#### Python
```python
constant = substrate.get_constant('PhragmenElection', 'VotingBondFactor')
```
---------
## Errors

---------
### DuplicatedCandidate
Duplicated candidate submission.

---------
### InsufficientCandidateFunds
Candidate does not have enough funds.

---------
### InvalidRenouncing
The renouncing origin presented a wrong `Renouncing` parameter.

---------
### InvalidReplacement
Prediction regarding replacement after member removal is wrong.

---------
### InvalidVoteCount
The provided count of number of votes is incorrect.

---------
### InvalidWitnessData
The provided count of number of candidates is incorrect.

---------
### LowBalance
Cannot vote with stake less than minimum balance.

---------
### MaximumVotesExceeded
Cannot vote more than maximum allowed.

---------
### MemberSubmit
Member cannot re-submit candidacy.

---------
### MustBeVoter
Must be a voter.

---------
### NoVotes
Must vote for at least one candidate.

---------
### NotMember
Not a member.

---------
### RunnerUpSubmit
Runner cannot re-submit candidacy.

---------
### TooManyCandidates
Too many candidates have been created.

---------
### TooManyVotes
Cannot vote more than candidates.

---------
### UnableToPayBond
Voter can not pay voting bond.

---------
### UnableToVote
Cannot vote when no candidates or members exist.

---------