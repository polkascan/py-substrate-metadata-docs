
# CalamariVesting

---------
## Calls

---------
### update_vesting_schedule
Update vesting schedule.

- `new_schedule`: New schedule for vesting.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_schedule | `BoundedVec<Schedule, T::MaxScheduleLength>` | 

#### Python
```python
call = substrate.compose_call(
    'CalamariVesting', 'update_vesting_schedule', {'new_schedule': ['u64']}
)
```

---------
### vest
Unlock vested balance according to the schedule.

The dispatch origin for this call must be _Signed_ and the sender must have funds still
locked under this pallet.

Emits either `VestingCompleted` or `VestingUpdated`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CalamariVesting', 'vest', {}
)
```

---------
### vested_transfer
Create a vested transfer: send `target` balance with the vesting schedule.

The dispatch origin for this call must be _Signed_.

- `target`: The account receiving the vested funds.
- `locked_amount`: How much tokens will be transferred.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| locked_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CalamariVesting', 'vested_transfer', {
    'locked_amount': 'u128',
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
## Events

---------
### VestingCompleted
An \[account\] has become fully vested. No further vesting can happen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### VestingScheduleUpdated
Update a vesting schedule.
\[new_schedule\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BoundedVec<Schedule, T::MaxScheduleLength>` | ```['u64']```

---------
### VestingUpdated
The amount vested has been updated. This could indicate more funds are available.
The balance given is the amount which is left unvested (and thus locked).
\[account, unvested\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### VestingBalances
 Information regarding the vesting of a given account.

#### Python
```python
result = substrate.query(
    'CalamariVesting', 'VestingBalances', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### VestingSchedule
 Information regarding the vesting of a given account.

#### Python
```python
result = substrate.query(
    'CalamariVesting', 'VestingSchedule', []
)
```

#### Return value
```python
[('u8', 'u64')]
```
---------
## Constants

---------
### MaxScheduleLength
 The maximum length of schedule is allowed.
#### Value
```python
6
```
#### Python
```python
constant = substrate.get_constant('CalamariVesting', 'MaxScheduleLength')
```
---------
### MinVestedTransfer
 The minimum amount transferred to call `vested_transfer`.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('CalamariVesting', 'MinVestedTransfer')
```
---------
## Errors

---------
### AmountLow
Amount being transferred is too low to create a vesting schedule.

---------
### BalanceLow
Not enough tokens for vesting.

---------
### ClaimTooEarly
The first round of vesting is not done yet.

---------
### ExistingVestingSchedule
An existing vesting schedule already exists for this account that cannot be clobbered.

---------
### InvalidSchedule
Cannot input

---------
### InvalidScheduleLength
The length of new schedule cannot be bigger/smaller than 6.

---------
### NotVesting
The account given is not vesting.

---------
### UnsortedSchedule
The new schedule should be sorted.

---------