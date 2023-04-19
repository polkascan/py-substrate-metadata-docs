
# PhalaPhatTokenomic

---------
## Calls

---------
### adjust_stake
Adjust stake to given contract.

Phat contracts accept depoits from accounts. The deposit info would be sent the cluster&\#x27;s
system contract. Then the system contract would invoke the driver contract (if installed)
to process the deposit info. A public good cluster usually would set the contracts&\#x27; scheduling
weights according to the total depoit on contracts. More weights means it would get more
compute resource to run the contract. The weights are applied on contract query and Sidevm
CPU round scheduling.

If users stake on a contract doesn&\#x27;t deployed yet. The deposit would send to the cluster
even if the contract is deployed later. User can re-stake with or without changing the amount
to sync the depoit the the cluster after the contract is actually deployed.
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
    'contract': '[u8; 32]',
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
| cluster | `Option<ContractClusterId>` | ```(None, '[u8; 32]')```
| contract | `ContractId` | ```[u8; 32]```
| deposit | `BalanceOf<T>` | ```u128```

---------
### UserStakeChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `Option<ContractClusterId>` | ```(None, '[u8; 32]')```
| account | `T::AccountId` | ```AccountId```
| contract | `ContractId` | ```[u8; 32]```
| stake | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ContractTotalStakes
 Map of contracts to their total stakes received

#### Python
```python
result = substrate.query(
    'PhalaPhatTokenomic', 'ContractTotalStakes', ['[u8; 32]']
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
    'PhalaPhatTokenomic', 'ContractUserStakes', ['AccountId', '[u8; 32]']
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