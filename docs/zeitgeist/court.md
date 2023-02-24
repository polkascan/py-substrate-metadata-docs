
# Court

---------
## Calls

---------
### exit_court
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Court', 'exit_court', {}
)
```

---------
### join_court
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Court', 'join_court', {}
)
```

---------
### vote
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| outcome | `OutcomeReport` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'vote', {
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
### ExitedJuror
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Juror` | ```{'status': ('Ok', 'Tardy')}```

---------
### JoinedJuror
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Juror` | ```{'status': ('Ok', 'Tardy')}```

---------
## Storage functions

---------
### CounterForJurors
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'Court', 'CounterForJurors', []
)
```

#### Return value
```python
'u32'
```
---------
### Jurors
 Accounts that stake funds to decide outcomes.

#### Python
```python
result = substrate.query(
    'Court', 'Jurors', ['AccountId']
)
```

#### Return value
```python
{'status': ('Ok', 'Tardy')}
```
---------
### JurorsSelectionNonce
 An extra layer of pseudo randomness.

#### Python
```python
result = substrate.query(
    'Court', 'JurorsSelectionNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### RequestedJurors
 Selected jurors that should vote a market outcome until a certain block number

#### Python
```python
result = substrate.query(
    'Court', 'RequestedJurors', ['u128', 'AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### Votes
 Votes of market outcomes for disputes

 Stores the vote block number and the submitted outcome.

#### Python
```python
result = substrate.query(
    'Court', 'Votes', ['u128', 'AccountId']
)
```

#### Return value
```python
('u64', {'Categorical': 'u16', 'Scalar': 'u128'})
```
---------
## Constants

---------
### CourtCaseDuration
 Block duration to cast a vote on an outcome.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Court', 'CourtCaseDuration')
```
---------
### PalletId
 Identifier of this pallet
#### Value
```python
'0x7a67652f636f7574'
```
#### Python
```python
constant = substrate.get_constant('Court', 'PalletId')
```
---------
### StakeWeight
 Weight used to calculate the necessary staking amount to become a juror
#### Value
```python
20000000000
```
#### Python
```python
constant = substrate.get_constant('Court', 'StakeWeight')
```
---------
### TreasuryPalletId
 Slashed funds are send to the treasury
#### Value
```python
'0x7a67652f74737279'
```
#### Python
```python
constant = substrate.get_constant('Court', 'TreasuryPalletId')
```
---------
## Errors

---------
### JurorAlreadyExists
It is not possible to insert a Juror that is already stored

---------
### JurorDoesNotExists
An account id does not exist on the jurors storage.

---------
### MarketDoesNotHaveCourtMechanism
On dispute or resolution, someone tried to pass a non-court market type

---------
### NoVotes
No-one voted on an outcome to resolve a market

---------
### OnlyJurorsCanVote
Forbids voting of unknown accounts

---------