
# Republic

---------
## Calls

---------
### transfer
Transfer funds from pallets account

The dispatch origin for this call must be _Root_ or _Manager_.

Parameters:
 - `asset`: The asset that will be transfered;
 - `target`: The account that should be transferred funds;
 - `value`: The amount of `asset` that will be transferred.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| target | `T::AccountId` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Republic', 'transfer', {
    'asset': 'u64',
    'target': 'AccountId',
    'value': 'u128',
}
)
```

---------
### vested_transfer
Transfer funds from pallets account with vesting

The dispatch origin for this call must be _Root_ or _Manager_.

Parameters:
 - `target`: The account that should be transferred funds.
 - `schedule`: The vesting schedule:
 -  First balance is the total amount that should be held for vesting.
 -  Second balance is how much should be unlocked per block.
 -  The block number is when the vesting should start.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `T::AccountId` | 
| schedule | `(T::Balance, T::Balance, T::BlockNumber)` | 

#### Python
```python
call = substrate.compose_call(
    'Republic', 'vested_transfer', {
    'schedule': (
        'u128',
        'u128',
        'u32',
    ),
    'target': 'AccountId',
}
)
```

---------
## Storage functions

---------
### PalletManager

#### Python
```python
result = substrate.query(
    'Republic', 'PalletManager', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### PalletId
 Pallet&#x27;s AccountId for balance
#### Value
```python
'0x65712f7265707562'
```
#### Python
```python
constant = substrate.get_constant('Republic', 'PalletId')
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