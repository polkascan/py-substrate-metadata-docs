
# SimpleDisputes

---------
## Calls

---------
### suggest_outcome
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| outcome | `OutcomeReport` | 

#### Python
```python
call = substrate.compose_call(
    'SimpleDisputes', 'suggest_outcome', {
    'market_id': 'u128',
    'outcome': {
        'Categorical': 'u16',
        'Scalar': 'u128',
    },
}
)
```

---------
## Events

---------
### OutcomeReserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```
| dispute | `MarketDispute<T::AccountId, T::BlockNumber, BalanceOf<T>>` | ```{'at': 'u64', 'by': 'AccountId', 'outcome': {'Categorical': 'u16', 'Scalar': 'u128'}, 'bond': 'u128'}```

---------
## Storage functions

---------
### Disputes
 For each market, this holds the dispute information for each dispute that&#x27;s
 been issued.

#### Python
```python
result = substrate.query(
    'SimpleDisputes', 'Disputes', ['u128']
)
```

#### Return value
```python
[
    {
        'at': 'u64',
        'bond': 'u128',
        'by': 'AccountId',
        'outcome': {'Categorical': 'u16', 'Scalar': 'u128'},
    },
]
```
---------
## Constants

---------
### MaxDisputes
 The maximum number of disputes allowed on any single market.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('SimpleDisputes', 'MaxDisputes')
```
---------
### OutcomeBond
 The base amount of currency that must be bonded in order to create a dispute.
#### Value
```python
20000000000000
```
#### Python
```python
constant = substrate.get_constant('SimpleDisputes', 'OutcomeBond')
```
---------
### OutcomeFactor
 The additional amount of currency that must be bonded when creating a subsequent
 dispute.
#### Value
```python
20000000000
```
#### Python
```python
constant = substrate.get_constant('SimpleDisputes', 'OutcomeFactor')
```
---------
### PalletId
 The pallet identifier.
#### Value
```python
'0x7a67652f73656470'
```
#### Python
```python
constant = substrate.get_constant('SimpleDisputes', 'PalletId')
```
---------
## Errors

---------
### CannotDisputeSameOutcome

---------
### InvalidMarketStatus
1. Any resolution must either have a `Disputed` or `Reported` market status
2. If status is `Disputed`, then at least one dispute must exist

---------
### MarketDoesNotHaveSimpleDisputesMechanism
On dispute or resolution, someone tried to pass a non-simple-disputes market type

---------
### MarketIsNotReported

---------
### MaxDisputesReached
The maximum number of disputes has been reached.

---------
### OutcomeMismatch

---------
### StorageOverflow

---------