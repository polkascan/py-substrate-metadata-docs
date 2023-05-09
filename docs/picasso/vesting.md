
# Vesting

---------
## Calls

---------
### claim
Unlock any vested funds of the origin account.

The dispatch origin for this call must be _Signed_ and the sender must have funds still
locked under this pallet.

- `asset`: The asset associated with the vesting schedule
- `vesting_schedule_ids`: The ids of the vesting schedules to be claimed

Emits `Claimed`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| vesting_schedule_ids | `VestingScheduleIdSet<T::VestingScheduleId, T::MaxVestingSchedules,>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim', {
    'asset': 'u128',
    'vesting_schedule_ids': {
        'All': None,
        'Many': ['u128'],
        'One': 'u128',
    },
}
)
```

---------
### claim_for
Unlock any vested funds of a `target` account.

The dispatch origin for this call must be _Signed_.

- `dest`: The account whose vested funds should be unlocked. Must have funds still
locked under this pallet.
- `asset`: The asset associated with the vesting schedule.
- `vesting_schedule_ids`: The ids of the vesting schedules to be claimed.

Emits `Claimed`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| asset | `AssetIdOf<T>` | 
| vesting_schedule_ids | `VestingScheduleIdSet<T::VestingScheduleId, T::MaxVestingSchedules,>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim_for', {
    'asset': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'vesting_schedule_ids': {
        'All': None,
        'Many': ['u128'],
        'One': 'u128',
    },
}
)
```

---------
### update_vesting_schedules
Update vesting schedules

The dispatch origin for this call must be _Root_ or democracy.

- `who`: The account whose vested funds should be updated.
- `asset`: The asset associated with the vesting schedules.
- `vesting_schedules`: The updated vesting schedules.

Emits `VestingSchedulesUpdated`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| asset | `AssetIdOf<T>` | 
| vesting_schedules | `Vec<VestingScheduleInfoOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'update_vesting_schedules', {
    'asset': 'u128',
    'vesting_schedules': [
        {
            'per_period': 'u128',
            'period_count': 'u32',
            'window': {
                'BlockNumberBased': {
                    'period': 'u32',
                    'start': 'u32',
                },
                'MomentBased': {
                    'period': 'u64',
                    'start': 'u64',
                },
            },
        },
    ],
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
### vested_transfer
Create a vested transfer.

The dispatch origin for this call must be _Root_ or Democracy.

- `from`: The account sending the vested funds.
- `beneficiary`: The account receiving the vested funds.
- `asset`: The asset associated with this vesting schedule.
- `schedule_info`: The vesting schedule data attached to the transfer.

Emits `VestingScheduleAdded`.

NOTE: This will unlock all schedules through the current block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `<T::Lookup as StaticLookup>::Source` | 
| beneficiary | `<T::Lookup as StaticLookup>::Source` | 
| asset | `AssetIdOf<T>` | 
| schedule_info | `VestingScheduleInfoOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vested_transfer', {
    'asset': 'u128',
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'from': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'schedule_info': {
        'per_period': 'u128',
        'period_count': 'u32',
        'window': {
            'BlockNumberBased': {
                'period': 'u32',
                'start': 'u32',
            },
            'MomentBased': {
                'period': 'u64',
                'start': 'u64',
            },
        },
    },
}
)
```

---------
## Events

---------
### Claimed
Claimed vesting.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| asset | `AssetIdOf<T>` | ```u128```
| vesting_schedule_ids | `VestingScheduleIdSet<T::VestingScheduleId, T::MaxVestingSchedules>` | ```{'All': None, 'One': 'u128', 'Many': ['u128']}```
| locked_amount | `BalanceOf<T>` | ```u128```
| claimed_amount_per_schedule | `BoundedBTreeMap<T::VestingScheduleId, BalanceOf<T>, T::
MaxVestingSchedules>` | ```scale_info::142```

---------
### VestingScheduleAdded
Added new vesting schedule.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `AccountIdOf<T>` | ```AccountId```
| to | `AccountIdOf<T>` | ```AccountId```
| asset | `AssetIdOf<T>` | ```u128```
| vesting_schedule_id | `T::VestingScheduleId` | ```u128```
| schedule | `VestingScheduleOf<T>` | ```{'vesting_schedule_id': 'u128', 'window': {'MomentBased': {'start': 'u64', 'period': 'u64'}, 'BlockNumberBased': {'start': 'u32', 'period': 'u32'}}, 'period_count': 'u32', 'per_period': 'u128', 'already_claimed': 'u128'}```
| schedule_amount | `BalanceOf<T>` | ```u128```

---------
### VestingSchedulesUpdated
Updated vesting schedules.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```

---------
## Storage functions

---------
### VestingScheduleNonce
 Counter used to uniquely identify vesting schedules within this pallet.

#### Python
```python
result = substrate.query(
    'Vesting', 'VestingScheduleNonce', []
)
```

#### Return value
```python
'u128'
```
---------
### VestingSchedules
 Vesting schedules of an account.

 VestingSchedules: map AccountId =&gt; Vec&lt;VestingSchedule&gt;

#### Python
```python
result = substrate.query(
    'Vesting', 'VestingSchedules', ['AccountId', 'u128']
)
```

#### Return value
```python
'scale_info::558'
```
---------
## Constants

---------
### MinVestedTransfer
 The minimum amount transferred to call `vested_transfer`.
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('Vesting', 'MinVestedTransfer')
```
---------
## Errors

---------
### AmountLow
The vested transfer amount is too low

---------
### InsufficientBalanceToLock
Insufficient amount of balance to lock

---------
### MaxVestingSchedulesExceeded
Failed because the maximum vesting schedules was exceeded

---------
### TooManyVestingSchedules
This account have too many vesting schedules

---------
### TryingToSelfVest
Trying to vest to ourselves

---------
### VestingScheduleNotFound
There is no vesting schedule with a given id

---------
### ZeroVestingPeriod
Vesting period is zero

---------
### ZeroVestingPeriodCount
Number of vests is zero

---------