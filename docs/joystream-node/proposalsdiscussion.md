
# ProposalsDiscussion

---------
## Calls

---------
### add_post
Adds a post with author origin check.

&lt;weight&gt;

\#\# Weight
`O (L)` where:
- `L` is the size of `text` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| post_author_id | `MemberId<T>` | 
| thread_id | `T::ThreadId` | 
| text | `Vec<u8>` | 
| editable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsDiscussion', 'add_post', {
    'editable': 'bool',
    'post_author_id': 'u64',
    'text': 'Bytes',
    'thread_id': 'u64',
}
)
```

---------
### change_thread_mode
Changes thread permission mode.

&lt;weight&gt;

\#\# Weight
`O (W)` if ThreadMode is close or O(1) otherwise where:
- `W` is the number of whitelisted members in `mode`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `MemberId<T>` | 
| thread_id | `T::ThreadId` | 
| mode | `ThreadMode<BTreeSet<<T as MembershipTypes>::MemberId>>` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsDiscussion', 'change_thread_mode', {
    'member_id': 'u64',
    'mode': {
        'Closed': 'scale_info::90',
        'Open': None,
    },
    'thread_id': 'u64',
}
)
```

---------
### delete_post
Remove post from storage, with the last parameter indicating whether to also hide it
in the UI.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| deleter_id | `MemberId<T>` | 
| post_id | `T::PostId` | 
| thread_id | `T::ThreadId` | 
| hide | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsDiscussion', 'delete_post', {
    'deleter_id': 'u64',
    'hide': 'bool',
    'post_id': 'u64',
    'thread_id': 'u64',
}
)
```

---------
### update_post
Updates a post with author origin check. Update attempts number is limited.

&lt;weight&gt;

\#\# Weight
`O (L)` where:
- `L` is the size of `text` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| thread_id | `T::ThreadId` | 
| post_id | `T::PostId` | 
| text | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsDiscussion', 'update_post', {
    'post_id': 'u64',
    'text': 'Bytes',
    'thread_id': 'u64',
}
)
```

---------
## Events

---------
### PostCreated
Emits on post creation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PostId` | ```u64```
| None | `MemberId` | ```u64```
| None | `ThreadId` | ```u64```
| None | `Vec<u8>` | ```Bytes```
| None | `bool` | ```bool```

---------
### PostDeleted
Emits on post deleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `ThreadId` | ```u64```
| None | `PostId` | ```u64```
| None | `bool` | ```bool```

---------
### PostUpdated
Emits on post update.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PostId` | ```u64```
| None | `MemberId` | ```u64```
| None | `ThreadId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### ThreadCreated
Emits on thread creation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ThreadId` | ```u64```
| None | `MemberId` | ```u64```

---------
### ThreadModeChanged
Emits on thread mode change.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ThreadId` | ```u64```
| None | `ThreadMode<BTreeSet<MemberId>>` | ```{'Open': None, 'Closed': 'scale_info::90'}```
| None | `MemberId` | ```u64```

---------
## Storage functions

---------
### PostCount
 Count of all posts that have been created.

#### Python
```python
result = substrate.query(
    'ProposalsDiscussion', 'PostCount', []
)
```

#### Return value
```python
'u64'
```
---------
### PostThreadIdByPostId
 Map thread id and post id to corresponding post.

#### Python
```python
result = substrate.query(
    'ProposalsDiscussion', 'PostThreadIdByPostId', ['u64', 'u64']
)
```

#### Return value
```python
{
    'author_id': 'u64',
    'cleanup_pay_off': {
        'amount': 'u128',
        'repayment_restricted_to': (None, 'AccountId'),
    },
    'last_edited': 'u32',
}
```
---------
### ThreadById
 Map thread identifier to corresponding thread.

#### Python
```python
result = substrate.query(
    'ProposalsDiscussion', 'ThreadById', ['u64']
)
```

#### Return value
```python
{
    'activated_at': 'u32',
    'author_id': 'u64',
    'mode': {'Closed': 'scale_info::90', 'Open': None},
}
```
---------
### ThreadCount
 Count of all threads that have been created.

#### Python
```python
result = substrate.query(
    'ProposalsDiscussion', 'ThreadCount', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### MaxWhiteListSize
 Exports const - author list size limit for the Closed discussion.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('ProposalsDiscussion', 'MaxWhiteListSize')
```
---------
### PostDeposit
 Exports const - fee for creating a post
#### Value
```python
1826241488
```
#### Python
```python
constant = substrate.get_constant('ProposalsDiscussion', 'PostDeposit')
```
---------
### PostLifeTime
 Exports const - maximum number of blocks before a post can be erased by anyone
#### Value
```python
600
```
#### Python
```python
constant = substrate.get_constant('ProposalsDiscussion', 'PostLifeTime')
```
---------
## Errors

---------
### ArithmeticError
Unexpected arithmetic error (overflow / underflow)

---------
### CannotDeletePost
Account can&\#x27;t delete post at the moment

---------
### CannotPostOnClosedThread
The thread has Closed mode. And post author doesn&\#x27;t belong to council or allowed members.

---------
### InsufficientBalanceForPost
Account has insufficient balance to create a post

---------
### MaxWhiteListSizeExceeded
Max allowed authors list limit exceeded.

---------
### NotAuthorOrCouncilor
Should be thread author or councilor.

---------
### PostDoesntExist
Post doesn&\#x27;t exist

---------
### RequireRootOrigin
Require root origin in extrinsics

---------
### ThreadDoesntExist
Thread doesn&\#x27;t exist

---------
### WhitelistedMemberDoesNotExist
At least one of the member ids provided as part of closed thread whitelist belongs
to a non-existing member.

---------