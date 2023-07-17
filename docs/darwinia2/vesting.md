
# Vesting

---------
## Calls

---------
### force_vested_transfer
Force a vested transfer.

The dispatch origin for this call must be _Root_.

- `source`: The account whose funds should be transferred.
- `target`: The account that should be transferred the vested funds.
- `schedule`: The vesting schedule attached to the transfer.

Emits `VestingCreated`.

NOTE: This will unlock all schedules through the current block.

\#\# Complexity
- `O(1)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `AccountIdLookupOf<T>` | 
| target | `AccountIdLookupOf<T>` | 
| schedule | `VestingInfo<BalanceOf<T>, T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'force_vested_transfer', {
    'schedule': {
        'locked': 'u128',
        'per_block': 'u128',
        'starting_block': 'u32',
    },
    'source': '[u8; 20]',
    'target': '[u8; 20]',
}
)
```

---------
### merge_schedules
Merge two vesting schedules together, creating a new vesting schedule that unlocks over
the highest possible start and end blocks. If both schedules have already started the
current block will be used as the schedule start; with the caveat that if one schedule
is finished by the current block, the other will be treated as the new merged schedule,
unmodified.

NOTE: If `schedule1_index == schedule2_index` this is a no-op.
NOTE: This will unlock all schedules through the current block prior to merging.
NOTE: If both schedules have ended by the current block, no new schedule will be created
and both will be removed.

Merged schedule attributes:
- `starting_block`: `MAX(schedule1.starting_block, scheduled2.starting_block,
  current_block)`.
- `ending_block`: `MAX(schedule1.ending_block, schedule2.ending_block)`.
- `locked`: `schedule1.locked_at(current_block) + schedule2.locked_at(current_block)`.

The dispatch origin for this call must be _Signed_.

- `schedule1_index`: index of the first schedule to merge.
- `schedule2_index`: index of the second schedule to merge.
#### Attributes
| Name | Type |
| -------- | -------- | 
| schedule1_index | `u32` | 
| schedule2_index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'merge_schedules', {
    'schedule1_index': 'u32',
    'schedule2_index': 'u32',
}
)
```

---------
### vest
Unlock any vested funds of the sender account.

The dispatch origin for this call must be _Signed_ and the sender must have funds still
locked under this pallet.

Emits either `VestingCompleted` or `VestingUpdated`.

\#\# Complexity
- `O(1)`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vest', {}
)
```

---------
### vest_other
Unlock any vested funds of a `target` account.

The dispatch origin for this call must be _Signed_.

- `target`: The account whose vested funds should be unlocked. Must have funds still
locked under this pallet.

Emits either `VestingCompleted` or `VestingUpdated`.

\#\# Complexity
- `O(1)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vest_other', {'target': '[u8; 20]'}
)
```

---------
### vested_transfer
Create a vested transfer.

The dispatch origin for this call must be _Signed_.

- `target`: The account receiving the vested funds.
- `schedule`: The vesting schedule attached to the transfer.

Emits `VestingCreated`.

NOTE: This will unlock all schedules through the current block.

\#\# Complexity
- `O(1)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 
| schedule | `VestingInfo<BalanceOf<T>, T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vested_transfer', {
    'schedule': {
        'locked': 'u128',
        'per_block': 'u128',
        'starting_block': 'u32',
    },
    'target': '[u8; 20]',
}
)
```

---------
## Events

---------
### VestingCompleted
An \[account\] has become fully vested.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```

---------
### VestingUpdated
The amount vested has been updated. This could indicate a change in funds available.
The balance given is the amount which is left unvested (and thus locked).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```
| unvested | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### StorageVersion
 Storage version of the pallet.

 New networks start with latest version, as determined by the genesis build.

#### Python
```python
result = substrate.query(
    'Vesting', 'StorageVersion', []
)
```

#### Return value
```python
('V0', 'V1')
```
---------
### Vesting
 Information regarding the vesting of a given account.

#### Python
```python
result = substrate.query(
    'Vesting', 'Vesting', ['[u8; 20]']
)
```

#### Return value
```python
[{'locked': 'u128', 'per_block': 'u128', 'starting_block': 'u32'}]
```
---------
## Constants

---------
### MaxVestingSchedules
#### Value
```python
28
```
#### Python
```python
constant = substrate.get_constant('Vesting', 'MaxVestingSchedules')
```
---------
### MinVestedTransfer
 The minimum amount transferred to call `vested_transfer`.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Vesting', 'MinVestedTransfer')
```
---------
## Errors

---------
### AmountLow
Amount being transferred is too low to create a vesting schedule.

---------
### AtMaxVestingSchedules
The account already has `MaxVestingSchedules` count of schedules and thus
cannot add another one. Consider merging existing schedules in order to add another.

---------
### InvalidScheduleParams
Failed to create a new schedule because some parameter was invalid.

---------
### NotVesting
The account given is not vesting.

---------
### ScheduleIndexOutOfBounds
An index was out of bounds of the vesting schedules.

---------