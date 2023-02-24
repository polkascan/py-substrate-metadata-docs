
# Styx

---------
## Calls

---------
### cross
Burns ZTG(styx.burnAmount()) to cross, granting the ability to claim your zeitgeist avatar.
The signer can only cross once.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Styx', 'cross', {}
)
```

---------
### set_burn_amount
Set the burn amount. Ensures the SetBurnAmountOrigin in the runtime.
Intended to be called by a governing body like the council.

\# Arguments

* `amount`: The amount of the new burn price
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Styx', 'set_burn_amount', {'amount': 'u128'}
)
```

---------
## Events

---------
### AccountCrossed
A account crossed and claimed their right to create their avatar.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### CrossingFeeChanged
The crossing fee was changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### BurnAmount
 An extra layer of pseudo randomness.

#### Python
```python
result = substrate.query(
    'Styx', 'BurnAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### Crossings
 Keep track of crossings. Accounts are only able to cross once.

#### Python
```python
result = substrate.query(
    'Styx', 'Crossings', ['AccountId']
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### FundDoesNotHaveEnoughFreeBalance
Account does not have enough balance to cross.

---------
### HasAlreadyCrossed
Account has already crossed.

---------