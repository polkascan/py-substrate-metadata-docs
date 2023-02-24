
# Vesting

---------
## Calls

---------
### force_set_cliff
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| cliff_block | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'force_set_cliff', {
    'cliff_block': 'u32',
    'target': {
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
### force_set_vested
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| schedule | `VestingInfo<BalanceOf<T>, T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'force_set_vested', {
    'schedule': {
        'locked': 'u128',
        'per_block': 'u128',
        'starting_block': 'u32',
    },
    'source': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'target': {
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
### force_vested_transfer
Force a vested transfer.

The dispatch origin for this call must be _Root_.

- `source`: The account whose funds should be transferred.
- `target`: The account that should be transferred the vested funds.
- `amount`: The amount of funds to transfer and will be vested.
- `schedule`: The vesting schedule attached to the transfer.

Emits `VestingCreated`.

\# &lt;weight&gt;
- `O(1)`.
- DbWeight: 4 Reads, 4 Writes
    - Reads: Vesting Storage, Balances Locks, Target Account, Source Account
    - Writes: Vesting Storage, Balances Locks, Target Account, Source Account
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| target | `<T::Lookup as StaticLookup>::Source` | 
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
    'source': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'target': {
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
### init_vesting_start_at
#### Attributes
| Name | Type |
| -------- | -------- | 
| vesting_start_at | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'init_vesting_start_at', {'vesting_start_at': 'u32'}
)
```

---------
### set_vesting_per_block
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| per_block | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'set_vesting_per_block', {
    'per_block': 'u128',
    'target': {
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
### vest
Unlock any vested funds of the sender account.

The dispatch origin for this call must be _Signed_ and the sender must have funds still
locked under this pallet.

Emits either `VestingCompleted` or `VestingUpdated`.

\# &lt;weight&gt;
- `O(1)`.
- DbWeight: 2 Reads, 2 Writes
    - Reads: Vesting Storage, Balances Locks, [Sender Account]
    - Writes: Vesting Storage, Balances Locks, [Sender Account]
\# &lt;/weight&gt;
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

\# &lt;weight&gt;
- `O(1)`.
- DbWeight: 3 Reads, 3 Writes
    - Reads: Vesting Storage, Balances Locks, Target Account
    - Writes: Vesting Storage, Balances Locks, Target Account
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vest_other', {
    'target': {
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

The dispatch origin for this call must be _Signed_.

- `target`: The account that should be transferred the vested funds.
- `amount`: The amount of funds to transfer and will be vested.
- `schedule`: The vesting schedule attached to the transfer.

Emits `VestingCreated`.

\# &lt;weight&gt;
- `O(1)`.
- DbWeight: 3 Reads, 3 Writes
    - Reads: Vesting Storage, Balances Locks, Target Account, [Sender Account]
    - Writes: Vesting Storage, Balances Locks, Target Account, [Sender Account]
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
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
    'target': {
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
## Events

---------
### VestingCompleted
An \[account\] has become fully vested. No further vesting can happen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### VestingUpdated
The amount vested has been updated. This could indicate more funds are available. The
balance given is the amount which is left unvested (and thus locked).
\[account, unvested\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Cliff
 Cliff vesting

#### Python
```python
result = substrate.query(
    'Vesting', 'Cliff', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### Vesting
 Information regarding the vesting of a given account.

#### Python
```python
result = substrate.query(
    'Vesting', 'Vesting', ['AccountId']
)
```

#### Return value
```python
{'locked': 'u128', 'per_block': 'u128', 'starting_block': 'u32'}
```
---------
### VestingStartAt
 Start at

#### Python
```python
result = substrate.query(
    'Vesting', 'VestingStartAt', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### MinVestedTransfer
 The minimum amount transferred to call `vested_transfer`.
#### Value
```python
10000000000
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
### ExistingVestingSchedule
An existing vesting schedule already exists for this account that cannot be clobbered.

---------
### NotVesting
The account given is not vesting.

---------
### SamePerBlock
change to the same per_block param

---------
### VestingStartAtNotSet
VestingStartAt storage is not set

---------
### WrongCliffVesting
Wrong vesting during cliff period

---------
### WrongLockedAmount
Wrong amount

---------