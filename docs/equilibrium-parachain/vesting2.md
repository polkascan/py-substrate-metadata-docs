
# Vesting2

---------
## Calls

---------
### force_vested_transfer
Force a vested transfer.

The dispatch origin for this call must be _Root_.

- `source`: The account whose funds should be transferred.
- `target`: The account that should be transferred the vested funds.
- `amount`: The amount of funds to transfer and will be vested.
- `schedule`: The vesting schedule attached to the transfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| schedule | `VestingInfo<T::Balance, T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting2', 'force_vested_transfer', {
    'schedule': {
        'locked': 'u128',
        'per_block': 'u128',
        'starting_block': 'u32',
    },
    'source': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
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
### vest
Unlock any vested funds of the sender account.

The dispatch origin for this call must be _Signed_ and the sender must have funds still
locked under this module.

Emits either `VestingCompleted` or `VestingUpdated`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Vesting2', 'vest', {}
)
```

---------
### vest_other
Unlock any vested funds of a `target` account.

The dispatch origin for this call must be _Signed_.

- `target`: The account whose vested funds should be unlocked. Must have funds still
locked under this module.

Emits either `VestingCompleted` or `VestingUpdated`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting2', 'vest_other', {
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
### NewAccountsPerBlock
New value of AccountsPerBlock set
\[accounts_per_block\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### VestingCompleted
An `account` has become fully vested. No further vesting can happen
\[account\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### VestingUpdated
The amount vested has been updated. This could indicate more funds are available. The
balance given is the amount which is left unvested (and thus locked)
\[account, unvested\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Vested
 Pallet storage: information about already vested balances for given account

#### Python
```python
result = substrate.query(
    'Vesting2', 'Vested', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### Vesting
 Pallet storage: information regarding the vesting of a given account

#### Python
```python
result = substrate.query(
    'Vesting2', 'Vesting', ['AccountId']
)
```

#### Return value
```python
{'locked': 'u128', 'per_block': 'u128', 'starting_block': 'u32'}
```
---------
## Constants

---------
### MinVestedTransfer
 The minimum amount transferred to call `vested_transfer`
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('Vesting2', 'MinVestedTransfer')
```
---------
### PalletId
#### Value
```python
'0x65712f7665737432'
```
#### Python
```python
constant = substrate.get_constant('Vesting2', 'PalletId')
```
---------
## Errors

---------
### AmountLow
Amount being transferred is too low to create a vesting schedule

---------
### ExistingVestingSchedule
An existing vesting schedule already exists for this account that cannot be clobbered

---------
### MethodNotAllowed
This method is not allowed in production

---------
### NotVesting
The account given is not vesting

---------
### TransfersAreDisabled
Self documented error code

---------