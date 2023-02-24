
# Authorized

---------
## Calls

---------
### authorize_market_outcome
Overwrites already provided outcomes for the same market and account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| outcome | `OutcomeReport` | 

#### Python
```python
call = substrate.compose_call(
    'Authorized', 'authorize_market_outcome', {
    'market_id': 'u128',
    'outcome': {
        'Categorical': 'u16',
        'Scalar': 'u128',
    },
}
)
```

---------
## Storage functions

---------
### AuthorizedOutcomeReports
 Maps the market id to the outcome reported by the authorized account.    

#### Python
```python
result = substrate.query(
    'Authorized', 'AuthorizedOutcomeReports', ['u128']
)
```

#### Return value
```python
{'outcome': {'Categorical': 'u16', 'Scalar': 'u128'}, 'resolve_at': 'u64'}
```
---------
## Constants

---------
### CorrectionPeriod
 The period, in which the authority can correct the outcome of a market.
 This value must not be zero.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Authorized', 'CorrectionPeriod')
```
---------
### PalletId
 Identifier of this pallet
#### Value
```python
'0x7a67652f61747a64'
```
#### Python
```python
constant = substrate.get_constant('Authorized', 'PalletId')
```
---------
## Errors

---------
### MarketDoesNotHaveDisputeMechanismAuthorized
The market unexpectedly has the incorrect dispute mechanism.

---------
### MarketIsNotDisputed
An account attempts to submit a report to an undisputed market.

---------
### OnlyOneDisputeAllowed
Only one dispute is allowed.

---------
### OutcomeMismatch
The report does not match the market&\#x27;s type.

---------