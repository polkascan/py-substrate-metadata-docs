
# Slots

---------
## Calls

---------
### clear_all_leases
Clear all leases for a Para Id, refunding any deposits back to the original owners.

The dispatch origin for this call must match `T::ForceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Slots', 'clear_all_leases', {'para': 'u32'}
)
```

---------
### force_lease
Just a connect into the `lease_out` call, in case Root wants to force some lease to happen
independently of any other on-chain mechanism to use it.

The dispatch origin for this call must match `T::ForceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| leaser | `T::AccountId` | 
| amount | `BalanceOf<T>` | 
| period_begin | `LeasePeriodOf<T>` | 
| period_count | `LeasePeriodOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Slots', 'force_lease', {
    'amount': 'u128',
    'leaser': 'AccountId',
    'para': 'u32',
    'period_begin': 'u32',
    'period_count': 'u32',
}
)
```

---------
### trigger_onboard
Try to onboard a parachain that has a lease for the current lease period.

This function can be useful if there was some state issue with a para that should
have onboarded, but was unable to. As long as they have a lease period, we can
let them onboard from here.

Origin must be signed, but can be called by anyone.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Slots', 'trigger_onboard', {'para': 'u32'}
)
```

---------
## Events

---------
### Leased
A para has won the right to a continuous set of lease periods as a parachain.
First balance is any extra amount reserved on top of the para&\#x27;s existing deposit.
Second balance is the total amount reserved.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```
| leaser | `T::AccountId` | ```AccountId```
| period_begin | `LeasePeriodOf<T>` | ```u32```
| period_count | `LeasePeriodOf<T>` | ```u32```
| extra_reserved | `BalanceOf<T>` | ```u128```
| total_amount | `BalanceOf<T>` | ```u128```

---------
### NewLeasePeriod
A new `[lease_period]` is beginning.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lease_period | `LeasePeriodOf<T>` | ```u32```

---------
## Storage functions

---------
### Leases
 Amounts held on deposit for each (possibly future) leased parachain.

 The actual amount locked on its behalf by any account at any time is the maximum of the second values
 of the items in this list whose first value is the account.

 The first item in the list is the amount locked for the current Lease Period. Following
 items are for the subsequent lease periods.

 The default value (an empty list) implies that the parachain no longer exists (or never
 existed) as far as this pallet is concerned.

 If a parachain doesn&#x27;t exist *yet* but is scheduled to exist in the future, then it
 will be left-padded with one or more `None`s to denote the fact that nothing is held on
 deposit for the non-existent chain currently, but is held at some point in the future.

 It is illegal for a `None` value to trail in the list.

#### Python
```python
result = substrate.query(
    'Slots', 'Leases', ['u32']
)
```

#### Return value
```python
[(None, ('AccountId', 'u128'))]
```
---------
## Constants

---------
### LeaseOffset
 The number of blocks to offset each lease period by.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Slots', 'LeaseOffset')
```
---------
### LeasePeriod
 The number of blocks over which a single period lasts.
#### Value
```python
604800
```
#### Python
```python
constant = substrate.get_constant('Slots', 'LeasePeriod')
```
---------
## Errors

---------
### LeaseError
There was an error with the lease.

---------
### ParaNotOnboarding
The parachain ID is not onboarding.

---------