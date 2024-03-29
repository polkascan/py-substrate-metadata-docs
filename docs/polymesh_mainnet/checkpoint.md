
# Checkpoint

---------
## Calls

---------
### create_checkpoint
Creates a single checkpoint at the current time.

\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ticker`.
- `ticker` to create the checkpoint for.

\# Errors
- `UnauthorizedAgent` if the DID of `origin` isn&\#x27;t a permissioned agent for `ticker`.
- `CounterOverflow` if the total checkpoint counter would overflow.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'Checkpoint', 'create_checkpoint', {'ticker': '[u8; 12]'}
)
```

---------
### create_schedule
Creates a schedule generating checkpoints
in the future at either a fixed time or at intervals.

The schedule starts out with `strong_ref_count(schedule_id) &lt;- 0`.

\# Arguments
- `origin` is a signer that has permissions to act as owner of `ticker`.
- `ticker` to create the schedule for.
- `schedule` that will generate checkpoints.

\# Errors
- `UnauthorizedAgent` if the DID of `origin` isn&\#x27;t a permissioned agent for `ticker`.
- `InsufficientAccountBalance` if the protocol fee could not be charged.
- `CounterOverflow` if the schedule ID or total checkpoint counters would overflow.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| schedule | `ScheduleCheckpoints` | 

#### Python
```python
call = substrate.compose_call(
    'Checkpoint', 'create_schedule', {
    'schedule': {
        'pending': 'scale_info::173',
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### remove_schedule
Removes the checkpoint schedule of an asset identified by `id`.

\# Arguments
- `origin` is a signer that has permissions to act as owner of `ticker`.
- `ticker` to remove the schedule from.
- `id` of the schedule, when it was created by `created_schedule`.

\# Errors
- `UnauthorizedAgent` if the DID of `origin` isn&\#x27;t a permissioned agent for `ticker`.
- `NoCheckpointSchedule` if `id` does not identify a schedule for this `ticker`.
- `ScheduleNotRemovable` if `id` exists but is not removable.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| id | `ScheduleId` | 

#### Python
```python
call = substrate.compose_call(
    'Checkpoint', 'remove_schedule', {'id': 'u64', 'ticker': '[u8; 12]'}
)
```

---------
### set_schedules_max_complexity
Sets the max complexity of a schedule set for an arbitrary ticker to `max_complexity`.
The new maximum is not enforced retroactively,
and only applies once new schedules are made.

Must be called as a PIP (requires &quot;root&quot;).

\# Arguments
- `origin` is the root origin.
- `max_complexity` allowed for an arbitrary ticker&\#x27;s schedule set.
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_complexity | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Checkpoint', 'set_schedules_max_complexity', {'max_complexity': 'u64'}
)
```

---------
## Events

---------
### CheckpointCreated
A checkpoint was created.

(caller DID, ticker, checkpoint ID, total supply, checkpoint timestamp)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `Ticker` | ```[u8; 12]```
| None | `CheckpointId` | ```u64```
| None | `Balance` | ```u128```
| None | `Moment` | ```u64```

---------
### MaximumSchedulesComplexityChanged
The maximum complexity for an arbitrary ticker&\#x27;s schedule set was changed.

(GC DID, the new maximum)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `u64` | ```u64```

---------
### ScheduleCreated
A checkpoint schedule was created.

(caller DID, ticker, schedule id, schedule)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `ScheduleId` | ```u64```
| None | `ScheduleCheckpoints` | ```{'pending': 'scale_info::173'}```

---------
### ScheduleRemoved
A checkpoint schedule was removed.

(caller DID, ticker, schedule id, schedule)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `ScheduleId` | ```u64```
| None | `ScheduleCheckpoints` | ```{'pending': 'scale_info::173'}```

---------
## Storage functions

---------
### Balance
 Balance of a DID at a checkpoint.

 (ticker, did, checkpoint ID) -&gt; Balance of a DID at a checkpoint

#### Python
```python
result = substrate.query(
    'Checkpoint', 'Balance', [('[u8; 12]', 'u64'), '[u8; 32]']
)
```

#### Return value
```python
'u128'
```
---------
### BalanceUpdates
 Checkpoints where a DID&#x27;s balance was updated.
 (ticker, did) -&gt; [checkpoint ID where user balance changed]

#### Python
```python
result = substrate.query(
    'Checkpoint', 'BalanceUpdates', ['[u8; 12]', '[u8; 32]']
)
```

#### Return value
```python
['u64']
```
---------
### CachedNextCheckpoints
 Cached next checkpoint for each schedule.

 This is used to quickly find the next checkpoint from a ticker&#x27;s schedules.

 (ticker) -&gt; next checkpoints

#### Python
```python
result = substrate.query(
    'Checkpoint', 'CachedNextCheckpoints', ['[u8; 12]']
)
```

#### Return value
```python
{'next_at': 'u64', 'schedules': 'scale_info::636', 'total_pending': 'u64'}
```
---------
### CheckpointIdSequence
 Checkpoints ID generator sequence.
 ID of first checkpoint is 1 instead of 0.

 (ticker) -&gt; no. of checkpoints

#### Python
```python
result = substrate.query(
    'Checkpoint', 'CheckpointIdSequence', ['[u8; 12]']
)
```

#### Return value
```python
'u64'
```
---------
### ScheduleIdSequence
 Checkpoint schedule ID sequence for tickers.

 (ticker) -&gt; schedule ID

#### Python
```python
result = substrate.query(
    'Checkpoint', 'ScheduleIdSequence', ['[u8; 12]']
)
```

#### Return value
```python
'u64'
```
---------
### SchedulePoints
 All the checkpoints a given schedule originated.

 (ticker, schedule ID) -&gt; [checkpoint ID]

#### Python
```python
result = substrate.query(
    'Checkpoint', 'SchedulePoints', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
['u64']
```
---------
### ScheduleRefCount
 How many &quot;strong&quot; references are there to a given `ScheduleId`?

 The presence of a &quot;strong&quot; reference, in the sense of `Rc&lt;T&gt;`,
 entails that the referenced schedule cannot be removed.
 Thus, as long as `strong_ref_count(schedule_id) &gt; 0`,
 `remove_schedule(schedule_id)` will error.

 (ticker, schedule ID) -&gt; strong ref count

#### Python
```python
result = substrate.query(
    'Checkpoint', 'ScheduleRefCount', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
'u32'
```
---------
### ScheduledCheckpoints
 Scheduled checkpoints.

 (ticker, schedule ID) -&gt; schedule checkpoints

#### Python
```python
result = substrate.query(
    'Checkpoint', 'ScheduledCheckpoints', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
{'pending': 'scale_info::173'}
```
---------
### SchedulesMaxComplexity
 The maximum complexity allowed for a ticker&#x27;s schedules.

#### Python
```python
result = substrate.query(
    'Checkpoint', 'SchedulesMaxComplexity', []
)
```

#### Return value
```python
'u64'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'Checkpoint', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### Timestamps
 Checkpoint timestamps.

 Every schedule-originated checkpoint maps its ID to its due time.
 Every checkpoint manually created maps its ID to the time of recording.

 (ticker) -&gt; (checkpoint ID) -&gt; checkpoint timestamp

#### Python
```python
result = substrate.query(
    'Checkpoint', 'Timestamps', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
'u64'
```
---------
### TotalSupply
 Total supply of the token at the checkpoint.

 (ticker, checkpointId) -&gt; total supply at given checkpoint

#### Python
```python
result = substrate.query(
    'Checkpoint', 'TotalSupply', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### NoSuchSchedule
A checkpoint schedule does not exist for the asset.

---------
### ScheduleFinished
The schedule has no more checkpoints.

---------
### ScheduleHasExpiredCheckpoints
The schedule has expired checkpoints.

---------
### ScheduleIsEmpty
Can&\#x27;t create an empty schedule.

---------
### ScheduleNotRemovable
A checkpoint schedule is not removable as `ref_count(schedule_id) &gt; 0`.

---------
### SchedulesOverMaxComplexity
The new schedule would put the ticker over the maximum complexity allowed.

---------