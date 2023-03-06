
# CorporateBallot

---------
## Calls

---------
### attach_ballot
Attach a corporate ballot to the CA identified by `ca_id`.

The ballot will admit votes within `range`.
The ballot&\#x27;s metadata is provided by `meta`,
which includes the ballot title, the motions, their choices, etc.
See the `BallotMeta` for more.

\#\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ca_id.ticker`.
- `ca_id` identifies the CA to attach the ballot to.
- `range` specifies when voting starts and ends.
- `meta` specifies the ballot&\#x27;s metadata as aforementioned.
- `rcv` specifies whether RCV is enabled for this ballot.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchCA` if `ca_id` does not identify an existing CA.
- `CANotNotice` if the CA is not of the `IssuerNotice` kind.
- `StartAfterEnd` if `range.start &gt; range.end`.
- `NowAfterEnd` if `now &gt; range.end` where `now` is the current timestamp.
- `NoRecordDate` if CA has no record date.
- `RecordDateAfterStart` if `date &gt; range.start` where `date` is the CA&\#x27;s record date.
- `AlreadyExists` if there&\#x27;s a ballot already.
- `NumberOfChoicesOverflow` if the total choice in `meta` overflows `usize`.
- `TooLong` if any of the embedded strings in `meta` are too long.
- `InsufficientBalance` if the protocol fee couldn&\#x27;t be charged.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 
| range | `BallotTimeRange` | 
| meta | `BallotMeta` | 
| rcv | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateBallot', 'attach_ballot', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    'meta': {
        'motions': [
            {
                'choices': ['Bytes'],
                'info_link': 'Bytes',
                'title': 'Bytes',
            },
        ],
        'title': 'Bytes',
    },
    'range': {
        'end': 'u64',
        'start': 'u64',
    },
    'rcv': 'bool',
}
)
```

---------
### change_end
Amend the end date of the ballot of the CA identified by `ca_id`.

\#\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ca_id.ticker`.
- `ca_id` identifies the attached ballot&\#x27;s CA.
- `end` specifies the new end date of the ballot.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchBallot` if `ca_id` does not identify a ballot.
- `VotingAlreadyStarted` if `start &gt;= now`, where `now` is the current time.
- `StartAfterEnd` if `start &gt; end`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 
| end | `Moment` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateBallot', 'change_end', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    'end': 'u64',
}
)
```

---------
### change_meta
Amend the metadata (title, motions, etc.) of the ballot of the CA identified by `ca_id`.

\#\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ca_id.ticker`.
- `ca_id` identifies the attached ballot&\#x27;s CA.
- `meta` specifies the new metadata.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchBallot` if `ca_id` does not identify a ballot.
- `VotingAlreadyStarted` if `start &gt;= now`, where `now` is the current time.
- `NumberOfChoicesOverflow` if the total choice in `meta` overflows `usize`.
- `TooLong` if any of the embedded strings in `meta` are too long.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 
| meta | `BallotMeta` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateBallot', 'change_meta', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    'meta': {
        'motions': [
            {
                'choices': ['Bytes'],
                'info_link': 'Bytes',
                'title': 'Bytes',
            },
        ],
        'title': 'Bytes',
    },
}
)
```

---------
### change_rcv
Amend RCV support for the ballot of the CA identified by `ca_id`.

\#\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ca_id.ticker`.
- `ca_id` identifies the attached ballot&\#x27;s CA.
- `rcv` specifies if RCV is to be supported or not.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchBallot` if `ca_id` does not identify a ballot.
- `VotingAlreadyStarted` if `start &gt;= now`, where `now` is the current time.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 
| rcv | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateBallot', 'change_rcv', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    'rcv': 'bool',
}
)
```

---------
### remove_ballot
Remove the ballot of the CA identified by `ca_id`.

\#\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ca_id.ticker`.
- `ca_id` identifies the attached ballot&\#x27;s CA.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchBallot` if `ca_id` does not identify a ballot.
- `VotingAlreadyStarted` if `start &gt;= now`, where `now` is the current time.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateBallot', 'remove_ballot', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
}
)
```

---------
### vote
Cast `votes` in the ballot attached to the CA identified by `ca_id`.

\#\# Arguments
- `origin` which must be a permissioned signer targeted by the CA.
- `ca_id` identifies the attached ballot&\#x27;s CA.
- `votes` specifies the balances to assign to each choice in the ballot.
   The full voting power of `origin`&\#x27;s DID may be used for each motion in the ballot.

\# Errors
- `NoSuchBallot` if `ca_id` does not identify a ballot.
- `VotingNotStarted` if the voting period hasn&\#x27;t commenced yet.
- `VotingAlreadyEnded` if the voting period has ended.
- `WrongVoteCount` if the number of choices in the ballot does not match `votes.len()`.
- `NoSuchCA` if `ca_id` does not identify an existing CA.
- `NotTargetedByCA` if the CA does not target `origin`&\#x27;s DID.
- `InsufficientVotes` if the voting power used for any motion in `votes`
   exceeds `origin`&\#x27;s DID&\#x27;s voting power.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 
| votes | `Vec<BallotVote>` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateBallot', 'vote', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    'votes': [
        {
            'fallback': (None, 'u16'),
            'power': 'u128',
        },
    ],
}
)
```

---------
## Events

---------
### Created
A corporate ballot was created.

(Agent DID, CA&\#x27;s ID, Voting start/end, Ballot metadata, RCV enabled?)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `BallotTimeRange` | ```{'start': 'u64', 'end': 'u64'}```
| None | `BallotMeta` | ```{'title': 'Bytes', 'motions': [{'title': 'Bytes', 'info_link': 'Bytes', 'choices': ['Bytes']}]}```
| None | `bool` | ```bool```

---------
### MetaChanged
A corporate ballot changed its metadata.

(Agent DID, CA&\#x27;s ID, New metadata)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `BallotMeta` | ```{'title': 'Bytes', 'motions': [{'title': 'Bytes', 'info_link': 'Bytes', 'choices': ['Bytes']}]}```

---------
### RCVChanged
A corporate ballot changed its RCV support.

(Agent DID, CA&\#x27;s ID, New support)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `bool` | ```bool```

---------
### RangeChanged
A corporate ballot changed its start/end date range.

(Agent DID, CA&\#x27;s ID, Voting start/end)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `BallotTimeRange` | ```{'start': 'u64', 'end': 'u64'}```

---------
### Removed
A corporate ballot was removed.

(Agent DID, CA&\#x27;s ID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```

---------
### VoteCast
A vote was cast in a corporate ballot.

(voter DID, CAId, Votes)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `Vec<BallotVote>` | ```[{'power': 'u128', 'fallback': (None, 'u16')}]```

---------
## Storage functions

---------
### Metas
 Metadata of a corporate ballot.

 (CAId) =&gt; BallotMeta

#### Python
```python
result = substrate.query(
    'CorporateBallot', 'Metas', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
]
)
```

#### Return value
```python
{'motions': [{'choices': ['Bytes'], 'info_link': 'Bytes', 'title': 'Bytes'}], 'title': 'Bytes'}
```
---------
### MotionNumChoices
 Stores how many choices there are in each motion.

 At all times, the invariant holds that `motion_choices[idx]` is equal to
 `metas.unwrap().motions[idx].choices.len()`. That is, this is just a cache,
 used to avoid fetching all the motions with their associated texts.

 `u16` choices should be more than enough to fit real use cases.

 (CAId) =&gt; Number of choices in each motion.

#### Python
```python
result = substrate.query(
    'CorporateBallot', 'MotionNumChoices', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
]
)
```

#### Return value
```python
['u16']
```
---------
### RCV
 Is ranked choice voting (RCV) enabled for this ballot?
 For an understanding of how RCV is handled, see note on `BallotVote`&#x27;s `fallback` field.

 (CAId) =&gt; bool

#### Python
```python
result = substrate.query(
    'CorporateBallot', 'RCV', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
]
)
```

#### Return value
```python
'bool'
```
---------
### Results
 Stores the total vote tally on each choice.

 RCV is not accounted for,
 as there are too many wants to interpret the graph,
 and because it would not be efficient.

 (CAId) =&gt; [current vote weights]

#### Python
```python
result = substrate.query(
    'CorporateBallot', 'Results', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
]
)
```

#### Return value
```python
['u128']
```
---------
### TimeRanges
 Time details of a corporate ballot associated with a CA.
 The timestamps denote when voting starts and stops.

 (CAId) =&gt; BallotTimeRange

#### Python
```python
result = substrate.query(
    'CorporateBallot', 'TimeRanges', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
]
)
```

#### Return value
```python
{'end': 'u64', 'start': 'u64'}
```
---------
### Votes
 Stores each DID&#x27;s votes in a given ballot.
 See the documentation of `BallotVote` for notes on semantics.

 (CAId) =&gt; (DID) =&gt; [vote weight]

 User must enter 0 vote weight if they don&#x27;t want to vote for a choice.

#### Python
```python
result = substrate.query(
    'CorporateBallot', 'Votes', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    '[u8; 32]',
]
)
```

#### Return value
```python
[{'fallback': (None, 'u16'), 'power': 'u128'}]
```
---------
## Errors

---------
### AlreadyExists
A corporate ballot already exists for this CA.

---------
### CANotNotice
A corporate ballot was made for a non `IssuerNotice` CA.

---------
### InsufficientVotes
Voting power used by a DID on a motion exceeds that which is available to them.

---------
### NoSuchBallot
A corporate ballot doesn&\#x27;t exist for this CA.

---------
### NoSuchRCVFallback
The RCV fallback of some choice does not exist.

---------
### NowAfterEnd
A corporate ballot&\#x27;s end time was strictly before the current time.

---------
### NumberOfChoicesOverflow
If some motion in a corporate ballot has more choices than would fit in `u16`.

---------
### RCVNotAllowed
RCV is not allowed for this ballot.

---------
### RCVSelfCycle
The RCV fallback points to the origin choice.

---------
### StartAfterEnd
A corporate ballot&\#x27;s start time was strictly after the ballot&\#x27;s end.

---------
### VotingAlreadyEnded
Voting ended already.

---------
### VotingAlreadyStarted
Voting started already. Amending a ballot is no longer possible.

---------
### VotingNotStarted
Voting hasn&\#x27;t started yet.

---------
### WrongVoteCount
Provided list of balances does not match the total number of choices.

---------