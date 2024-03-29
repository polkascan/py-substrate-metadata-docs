
# PhalaPhatTokenomic

---------
## Calls

---------
### adjust_stake
See [`Pallet::adjust_stake`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `ContractId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatTokenomic', 'adjust_stake', {
    'amount': 'u128',
    'contract': 'scale_info::12',
}
)
```

---------
## Events

---------
### ContractDepositChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `Option<ContractClusterId>` | ```(None, 'scale_info::12')```
| contract | `ContractId` | ```scale_info::12```
| deposit | `BalanceOf<T>` | ```u128```

---------
### UserStakeChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `Option<ContractClusterId>` | ```(None, 'scale_info::12')```
| account | `T::AccountId` | ```AccountId```
| contract | `ContractId` | ```scale_info::12```
| stake | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ContractTotalStakes
 Map of contracts to their total stakes received

#### Python
```python
result = substrate.query(
    'PhalaPhatTokenomic', 'ContractTotalStakes', ['scale_info::12']
)
```

#### Return value
```python
'u128'
```
---------
### ContractUserStakes
 Stake of user to contract

#### Python
```python
result = substrate.query(
    'PhalaPhatTokenomic', 'ContractUserStakes', ['AccountId', 'scale_info::12']
)
```

#### Return value
```python
'u128'
```
---------
### MinStake
 Minimum allowed stake

#### Python
```python
result = substrate.query(
    'PhalaPhatTokenomic', 'MinStake', []
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### InvalidAmountOfStake

---------