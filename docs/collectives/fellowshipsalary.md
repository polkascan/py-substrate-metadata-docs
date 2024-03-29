
# FellowshipSalary

---------
## Calls

---------
### bump
See [`Pallet::bump`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FellowshipSalary', 'bump', {}
)
```

---------
### check_payment
See [`Pallet::check_payment`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FellowshipSalary', 'check_payment', {}
)
```

---------
### induct
See [`Pallet::induct`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FellowshipSalary', 'induct', {}
)
```

---------
### init
See [`Pallet::init`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FellowshipSalary', 'init', {}
)
```

---------
### payout
See [`Pallet::payout`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FellowshipSalary', 'payout', {}
)
```

---------
### payout_other
See [`Pallet::payout_other`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipSalary', 'payout_other', {'beneficiary': 'AccountId'}
)
```

---------
### register
See [`Pallet::register`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FellowshipSalary', 'register', {}
)
```

---------
## Events

---------
### CycleStarted
The next cycle begins.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `CycleIndexOf<T>` | ```u32```

---------
### Inducted
A member is inducted into the payroll.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### Paid
A payment happened.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| beneficiary | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```
| id | `<T::Paymaster as Pay>::Id` | ```u64```

---------
### Registered
A member registered for a payout.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Claimant
 The status of a claimant.

#### Python
```python
result = substrate.query(
    'FellowshipSalary', 'Claimant', ['AccountId']
)
```

#### Return value
```python
{
    'last_active': 'u32',
    'status': {
        'Attempted': {
            'amount': 'u128',
            'id': 'u64',
            'registered': (None, 'u128'),
        },
        'Nothing': None,
        'Registered': 'u128',
    },
}
```
---------
### Status
 The overall status of the system.

#### Python
```python
result = substrate.query(
    'FellowshipSalary', 'Status', []
)
```

#### Return value
```python
{
    'budget': 'u128',
    'cycle_index': 'u32',
    'cycle_start': 'u32',
    'total_registrations': 'u128',
    'total_unregistered_paid': 'u128',
}
```
---------
## Constants

---------
### Budget
 The total budget per cycle.

 This may change over the course of a cycle without any problem.
#### Value
```python
250000000000
```
#### Python
```python
constant = substrate.get_constant('FellowshipSalary', 'Budget')
```
---------
### PayoutPeriod
 The number of blocks within a cycle which accounts have to claim the payout.

 The number of blocks between sequential payout cycles is the sum of this and
 `RegistrationPeriod`.
#### Value
```python
108000
```
#### Python
```python
constant = substrate.get_constant('FellowshipSalary', 'PayoutPeriod')
```
---------
### RegistrationPeriod
 The number of blocks within a cycle which accounts have to register their intent to
 claim.

 The number of blocks between sequential payout cycles is the sum of this and
 `PayoutPeriod`.
#### Value
```python
108000
```
#### Python
```python
constant = substrate.get_constant('FellowshipSalary', 'RegistrationPeriod')
```
---------
## Errors

---------
### AlreadyInducted
The account is already inducted.

---------
### AlreadyStarted
The salary system has already been started.

---------
### Bankrupt
There is no budget left for the payout.

---------
### ClaimZero
The member&\#x27;s claim is zero.

---------
### Inconclusive
The payment has neither failed nor succeeded yet.

---------
### NoClaim
The member does not have a current valid claim.

---------
### NotCurrent
The cycle is after that in which the payment was made.

---------
### NotInducted

---------
### NotMember
The account is not a ranked member.

---------
### NotStarted
The payout cycles have not yet started.

---------
### NotYet
Cycle is not yet over.

---------
### PayError
There was some issue with the mechanism of payment.

---------
### TooEarly
Current cycle&\#x27;s payment period is not yet begun.

---------
### TooLate
Current cycle&\#x27;s registration period is over.

---------