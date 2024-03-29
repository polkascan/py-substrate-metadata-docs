
# ImbueDisputes

---------
## Calls

---------
### extend_dispute
See [`Pallet::extend_dispute`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dispute_key | `T::DisputeKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueDisputes', 'extend_dispute', {'dispute_key': 'u32'}
)
```

---------
### force_fail_dispute
See [`Pallet::force_fail_dispute`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dispute_key | `T::DisputeKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueDisputes', 'force_fail_dispute', {'dispute_key': 'u32'}
)
```

---------
### force_succeed_dispute
See [`Pallet::force_succeed_dispute`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dispute_key | `T::DisputeKey` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueDisputes', 'force_succeed_dispute', {'dispute_key': 'u32'}
)
```

---------
### vote_on_dispute
See [`Pallet::vote_on_dispute`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dispute_key | `T::DisputeKey` | 
| is_yay | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueDisputes', 'vote_on_dispute', {
    'dispute_key': 'u32',
    'is_yay': 'bool',
}
)
```

---------
## Events

---------
### DisputeCancelled
A dispute has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispute_key | `T::DisputeKey` | ```u32```

---------
### DisputeCompleted
A dispute has been completed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispute_key | `T::DisputeKey` | ```u32```
| dispute_result | `DisputeResult` | ```('Success', 'Failure')```

---------
### DisputeExtended
A dispute has been extended.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispute_key | `T::DisputeKey` | ```u32```

---------
### DisputeRaised
A dispute has been raised.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispute_key | `T::DisputeKey` | ```u32```

---------
### DisputeVotedOn
A disute has been voted on
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispute_key | `T::DisputeKey` | ```u32```
| who | `AccountIdOf<T>` | ```AccountId```
| vote | `bool` | ```bool```

---------
## Storage functions

---------
### Disputes
 Used to store the disputes that is being raised, given the dispute key it returns the Dispute
 Key: DisputeKey
 Value: Dispute&lt;T&gt;

#### Python
```python
result = substrate.query(
    'ImbueDisputes', 'Disputes', ['u32']
)
```

#### Return value
```python
{
    'expiration': 'u32',
    'is_extended': 'bool',
    'jury': ['AccountId'],
    'raised_by': 'AccountId',
    'specifiers': ['u32'],
    'votes': 'scale_info::503',
}
```
---------
### DisputesFinaliseOn
 Stores the dispute keys that will finalise on a given block.
 Key: BlockNumber
 Value: Vec&lt;DisputeKey&gt;

#### Python
```python
result = substrate.query(
    'ImbueDisputes', 'DisputesFinaliseOn', ['u32']
)
```

#### Return value
```python
['u32']
```
---------
## Errors

---------
### AutoFinaliseStateMismatch
A dispute key is not inserted in DisputesFinaliseOn as expected, this is a bug, contact development.

---------
### DisputeAlreadyExists
Dispute key already exists.

---------
### DisputeAlreadyExtended
The dispute has already been extended. You can only extend a dispute once.

---------
### DisputeDoesNotExist
Dispute key does not exist.

---------
### NotAJuryAccount

---------
### TooManyDisputeVotes
There have been more than required votes for a given dispute

---------
### TooManyDisputesThisBlock
There have been too many disputes on this block. Try next block.

---------