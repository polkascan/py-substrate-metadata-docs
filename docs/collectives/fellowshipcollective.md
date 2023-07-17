
# FellowshipCollective

---------
## Calls

---------
### add_member
Introduce a new member.

- `origin`: Must be the `AdminOrigin`.
- `who`: Account of non-member which will become a member.
- `rank`: The rank to give the new member.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCollective', 'add_member', {
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
### cleanup_poll
Remove votes from the given poll. It must have ended.

- `origin`: Must be `Signed` by any account.
- `poll_index`: Index of a poll which is completed and for which votes continue to
  exist.
- `max`: Maximum number of vote items from remove in this call.

Transaction fees are waived if the operation is successful.

Weight `O(max)` (less if there are fewer items to remove than `max`).
#### Attributes
| Name | Type |
| -------- | -------- | 
| poll_index | `PollIndexOf<T, I>` | 
| max | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCollective', 'cleanup_poll', {'max': 'u32', 'poll_index': 'u32'}
)
```

---------
### demote_member
Decrement the rank of an existing member by one. If the member is already at rank zero,
then they are removed entirely.

- `origin`: Must be the `AdminOrigin`.
- `who`: Account of existing member of rank greater than zero.

Weight: `O(1)`, less if the member&\#x27;s index is highest in its rank.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCollective', 'demote_member', {
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
### promote_member
Increment the rank of an existing member by one.

- `origin`: Must be the `AdminOrigin`.
- `who`: Account of existing member.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCollective', 'promote_member', {
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
### remove_member
Remove the member entirely.

- `origin`: Must be the `AdminOrigin`.
- `who`: Account of existing member of rank greater than zero.
- `min_rank`: The rank of the member or greater.

Weight: `O(min_rank)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| min_rank | `Rank` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCollective', 'remove_member', {
    'min_rank': 'u16',
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
### vote
Add an aye or nay vote for the sender to the given proposal.

- `origin`: Must be `Signed` by a member account.
- `poll`: Index of a poll which is ongoing.
- `aye`: `true` if the vote is to approve the proposal, `false` otherwise.

Transaction fees are be waived if the member is voting on any particular proposal
for the first time and the call is successful. Subsequent vote changes will charge a
fee.

Weight: `O(1)`, less if there was no previous vote on the poll by the member.
#### Attributes
| Name | Type |
| -------- | -------- | 
| poll | `PollIndexOf<T, I>` | 
| aye | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCollective', 'vote', {'aye': 'bool', 'poll': 'u32'}
)
```

---------
## Events

---------
### MemberAdded
A member `who` has been added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### MemberRemoved
The member `who` of given `rank` has been removed from the collective.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| rank | `Rank` | ```u16```

---------
### RankChanged
The member `who`se rank has been changed to the given `rank`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| rank | `Rank` | ```u16```

---------
### Voted
The member `who` has voted for the `poll` with the given `vote` leading to an updated
`tally`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| poll | `PollIndexOf<T, I>` | ```u32```
| vote | `VoteRecord` | ```{'Aye': 'u32', 'Nay': 'u32'}```
| tally | `TallyOf<T, I>` | ```{'bare_ayes': 'u32', 'ayes': 'u32', 'nays': 'u32'}```

---------
## Storage functions

---------
### IdToIndex
 The index of each ranks&#x27;s member into the group of members who have at least that rank.

#### Python
```python
result = substrate.query(
    'FellowshipCollective', 'IdToIndex', ['u16', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### IndexToId
 The members in the collective by index. All indices in the range `0..MemberCount` will
 return `Some`, however a member&#x27;s index is not guaranteed to remain unchanged over time.

#### Python
```python
result = substrate.query(
    'FellowshipCollective', 'IndexToId', ['u16', 'u32']
)
```

#### Return value
```python
'AccountId'
```
---------
### MemberCount
 The number of members in the collective who have at least the rank according to the index
 of the vec.

#### Python
```python
result = substrate.query(
    'FellowshipCollective', 'MemberCount', ['u16']
)
```

#### Return value
```python
'u32'
```
---------
### Members
 The current members of the collective.

#### Python
```python
result = substrate.query(
    'FellowshipCollective', 'Members', ['AccountId']
)
```

#### Return value
```python
{'rank': 'u16'}
```
---------
### Voting
 Votes on a given proposal, if it is ongoing.

#### Python
```python
result = substrate.query(
    'FellowshipCollective', 'Voting', ['u32', 'AccountId']
)
```

#### Return value
```python
{'Aye': 'u32', 'Nay': 'u32'}
```
---------
### VotingCleanup

#### Python
```python
result = substrate.query(
    'FellowshipCollective', 'VotingCleanup', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
## Errors

---------
### AlreadyMember
Account is already a member.

---------
### Corruption
Unexpected error in state.

---------
### InvalidWitness
The information provided is incorrect.

---------
### NoPermission
The origin is not sufficiently privileged to do the operation.

---------
### NoneRemaining
There are no further records to be removed.

---------
### NotMember
Account is not a member.

---------
### NotPolling
The given poll index is unknown or has closed.

---------
### Ongoing
The given poll is still ongoing.

---------
### RankTooLow
The member&\#x27;s rank is too low to vote.

---------