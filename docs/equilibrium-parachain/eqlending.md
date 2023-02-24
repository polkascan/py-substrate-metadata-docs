
# EqLending

---------
## Calls

---------
### deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'EqLending', 'deposit', {'asset': 'u64', 'value': 'u128'}
)
```

---------
### payout
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqLending', 'payout', {'asset': 'u64', 'who': 'AccountId'}
)
```

---------
### withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'EqLending', 'withdraw', {'asset': 'u64', 'value': 'u128'}
)
```

---------
## Events

---------
### Deposit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset | `Asset` | ```u64```
| value | `T::Balance` | ```u128```

---------
### Payout
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset | `Asset` | ```u64```
| payout | `T::Balance` | ```u128```

---------
### Withdraw
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset | `Asset` | ```u64```
| value | `T::Balance` | ```u128```

---------
## Storage functions

---------
### CumulatedReward
 Table with accumulated rewards per asset
 cumulated_reward[i+i] &gt; cumulated_reward[i] is guaranteed

#### Python
```python
result = substrate.query(
    'EqLending', 'CumulatedReward', ['u64']
)
```

#### Return value
```python
'u128'
```
---------
### Lenders
 Lenders deposits

#### Python
```python
result = substrate.query(
    'EqLending', 'Lenders', ['AccountId', 'u64']
)
```

#### Return value
```python
{'last_reward': 'u128', 'value': 'u128'}
```
---------
### LendersAggregates
 Total lending amount per asset

#### Python
```python
result = substrate.query(
    'EqLending', 'LendersAggregates', ['u64']
)
```

#### Return value
```python
'u128'
```
---------
### OnlyBailsmanTill
 Timestamp of switching from bailsman pool to lending pool

#### Python
```python
result = substrate.query(
    'EqLending', 'OnlyBailsmanTill', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### ModuleId
 Lending pool ModuleId
#### Value
```python
'0x65712f6c656e6472'
```
#### Python
```python
constant = substrate.get_constant('EqLending', 'ModuleId')
```
---------
## Errors

---------
### BailsmanCantBeUnregistered
Bailsman can not be unregistered because of debt weight

---------
### BailsmanCantGenerateDebt
Bailsman can&\#x27;t generate debt

---------
### DebtExceedLiquidity
Not allowed because of debt weight

---------
### NoLendersToClaim
Try to add reward to pool without lenders

---------
### NotALender
User do not deposit to lending pool

---------
### NotEnoughToWithdraw
Try to withdraw more than deposited

---------
### Overflow
Overflow

---------
### WrongAssetType
Only physical asset types allowed to deposit/withdraw in lending pool

---------