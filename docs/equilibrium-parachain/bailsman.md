
# Bailsman

---------
## Calls

---------
### redistribute
Operation to redistribute single bailsman manually.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Bailsman', 'redistribute', {'who': 'AccountId'}
)
```

---------
### redistribute_unsigned
Request to redistribute single bailsman sent by offchain worker.
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `DistributionRequest<T::AccountId, T::BlockNumber>` | 
| signature | `<T::AuthorityId as RuntimeAppPublic>::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'Bailsman', 'redistribute_unsigned', {
    'request': {
        'auth_idx': 'u32',
        'bailsman': 'AccountId',
        'block_number': 'u32',
        'curr_distr_id': 'u32',
        'higher_priority': 'bool',
        'last_distr_id': 'u32',
        'queue_len': 'u32',
        'val_len': 'u32',
    },
    'signature': '[u8; 64]',
}
)
```

---------
### toggle_auto_redistribution
#### Attributes
| Name | Type |
| -------- | -------- | 
| enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Bailsman', 'toggle_auto_redistribution', {'enabled': 'bool'}
)
```

---------
## Events

---------
### UnregisteredBailsman
Bailsman subaccount is no longer a bailsman. \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### AutoRedistributionEnabled

#### Python
```python
result = substrate.query(
    'Bailsman', 'AutoRedistributionEnabled', []
)
```

#### Return value
```python
'bool'
```
---------
### BailsmenCount
 Store total amount of bailsmen

#### Python
```python
result = substrate.query(
    'Bailsman', 'BailsmenCount', []
)
```

#### Return value
```python
'u32'
```
---------
### DistributionQueue
 Store id for next distribution and distribution queue

#### Python
```python
result = substrate.query(
    'Bailsman', 'DistributionQueue', []
)
```

#### Return value
```python
(
    'u32',
    [
        (
            'u32',
            {
                'distribution_balances': [('u64', 'scale_info::10')],
                'prices': [('u64', 'u128')],
                'remaining_bailsmen': 'u32',
                'total_usd': 'u128',
            },
        ),
    ],
)
```
---------
### LastDistribution
 Store last redistributed id for each bailsman

#### Python
```python
result = substrate.query(
    'Bailsman', 'LastDistribution', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### MaxBailsmenToDistribute
 Amount of bailsmen to redistribute per block in offchain
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Bailsman', 'MaxBailsmenToDistribute')
```
---------
### MinTempBalanceUsd
 Minimal sum of the collateral and debt abs values to distribute temp Bailsman balances
#### Value
```python
50000000000
```
#### Python
```python
constant = substrate.get_constant('Bailsman', 'MinTempBalanceUsd')
```
---------
### MinimalCollateral
 Minimum amount of balances account should have to register as bailsman
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Bailsman', 'MinimalCollateral')
```
---------
### PalletId
 Pallet&#x27;s AccountId for balances
#### Value
```python
'0x65712f6261696c73'
```
#### Python
```python
constant = substrate.get_constant('Bailsman', 'PalletId')
```
---------
### QueueLengthWeightConstant
 Special constant for improving weight in unsigned extrinsics
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Bailsman', 'QueueLengthWeightConstant')
```
---------
### UnsignedPriority
 Priority for offchain extrinsics
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Bailsman', 'UnsignedPriority')
```
---------
## Errors

---------
### AlreadyBailsman
Cannot register account as bailsman because account is already a bailsman

---------
### BailsmanHasDebt
Cannot register/unregister or transfer from bailsman: bailsman account should not have negative balances

---------
### CollateralMustBeMoreThanMin
Account has insufficient balance to register as bailsman

---------
### Convert
Balance convertion error

---------
### NeedToMcBailsmanFirstly
Bailsman cannot have debt &gt; collat

---------
### NotBailsman
Cannot unregister bailsman account - account is not bailsman

---------
### PriceNotFound
Price not found for redistribution

---------
### PricesAreOutdated
Prices received from oracle are outdated

---------
### TempBalancesNotDistributed
Need to distribute temp balances

---------
### TempBalancesTransfer
No basic transfers from / to bailsman temp balances

---------
### TotalBailsmenPoolBalanceIsNegative
Bailsmen cannot have negative total balance

---------
### WrongMargin
Wrong margin for operation performing

---------