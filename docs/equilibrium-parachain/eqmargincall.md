
# EqMarginCall

---------
## Calls

---------
### try_margincall_external
Tries to margin-call an account from another account signed call.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T as system::Config>::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqMarginCall', 'try_margincall_external', {'who': 'AccountId'}
)
```

---------
## Events

---------
### MaintenanceMarginCall
Event is fired when an account achieves the `maintenance_margin` level.
\[main_acc, maybe(subacc_type,subacc_id), timer\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Option<(SubAccType, T::AccountId)>` | ```(None, (('Bailsman', 'Trader', 'Borrower'), 'AccountId'))```
| None | `u64` | ```u64```

---------
### MarginCallExecuted
Event is fired when an account is liquidated.
\[main_acc, maybe(subacc_type,subacc_id)\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Option<(SubAccType, T::AccountId)>` | ```(None, (('Bailsman', 'Trader', 'Borrower'), 'AccountId'))```

---------
## Storage functions

---------
### MaintenanceTimers

#### Python
```python
result = substrate.query(
    'EqMarginCall', 'MaintenanceTimers', ['AccountId']
)
```

#### Return value
```python
(None, 'u64')
```
---------
## Constants

---------
### CriticalMargin
 `critical_margin` setting, when the margin is below this value, a position is liquidated immediately
#### Value
```python
50000000
```
#### Python
```python
constant = substrate.get_constant('EqMarginCall', 'CriticalMargin')
```
---------
### InitialMargin
 `initial_margin` setting, when the margin is below this value, borrowing is prohibited
#### Value
```python
200000000
```
#### Python
```python
constant = substrate.get_constant('EqMarginCall', 'InitialMargin')
```
---------
### MaintenanceMargin
 `maintenance_margin` setting, when the margin is below this value, a MaintenanceMarginCall event is fired
#### Value
```python
100000000
```
#### Python
```python
constant = substrate.get_constant('EqMarginCall', 'MaintenanceMargin')
```
---------
### MaintenancePeriod
 `maintenance_period` setting, a time period (in seconds) when the margin account can be topped up to the `initial_margin` setting to avoid a margin call
#### Value
```python
86400
```
#### Python
```python
constant = substrate.get_constant('EqMarginCall', 'MaintenancePeriod')
```
---------
## Errors

---------
### ZeroCollateral
Not allowed with zero collateral

---------