
# EqRate

---------
## Calls

---------
### delete_account
Request to delete an account and all of it subaccounts

The dispatch origin for this call must be _None_ (unsigned transaction).

Parameters:
 - `request`: OperationRequest.
 - `_signature`: OperationRequest signature
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `OperationRequest<T::AccountId, T::BlockNumber>` | 
| signature | `<T::AuthorityId as RuntimeAppPublic>::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'EqRate', 'delete_account', {
    'request': {
        'account': (None, 'AccountId'),
        'authority_index': 'u32',
        'block_num': 'u32',
        'higher_priority': 'bool',
        'validators_len': 'u32',
    },
    'signature': '[u8; 64]',
}
)
```

---------
### delete_account_external
Request to delete an account and all of it subaccounts
This function is used by any user and executed by substrate transaction

The dispatch origin for this call must be `Signed` by the transactor.

Parameters:
 - `account`: Account that should be checked for deletion.
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `<T as system::Config>::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqRate', 'delete_account_external', {'account': 'AccountId'}
)
```

---------
### deposit
Request to deposit asset for account

The dispatch origin for this call must be _None_ (unsigned transaction).

Parameters:
 - `request`: OperationRequest.
 - `_signature`: OperationRequest signature
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `BalanceRemovalRequest<T::AccountId, Asset, T::Balance, T::BlockNumber
>` | 
| signature | `<T::AuthorityId as RuntimeAppPublic>::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'EqRate', 'deposit', {
    'request': {
        'account': 'AccountId',
        'amount': 'u128',
        'asset': 'u64',
        'authority_index': 'u32',
        'block_num': 'u32',
        'higher_priority': 'bool',
        'validators_len': 'u32',
    },
    'signature': '[u8; 64]',
}
)
```

---------
### reinit
Request to check account balance for margin call and withdraw fees.

The dispatch origin for this call must be _None_ (unsigned transaction).
Parameters:
 - `request`: OperationRequest.
 - `_signature`: OperationRequest signature
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `OperationRequest<T::AccountId, T::BlockNumber>` | 
| signature | `<T::AuthorityId as RuntimeAppPublic>::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'EqRate', 'reinit', {
    'request': {
        'account': (None, 'AccountId'),
        'authority_index': 'u32',
        'block_num': 'u32',
        'higher_priority': 'bool',
        'validators_len': 'u32',
    },
    'signature': '[u8; 64]',
}
)
```

---------
### reinit_external
Request to check account balance for margin call and withdraw fees.
This function is used by any user and executed by substrate transaction

The dispatch origin for this call must be `Signed` by the transactor.

Parameters:
 - `account`: Account that should be checked for margin call and charged fee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `<T as system::Config>::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqRate', 'reinit_external', {'owner': 'AccountId'}
)
```

---------
### set_auto_reinit_enabled
Enables or disables offchain workers. `true` to enable offchain worker
operations, `false` to disable them.
#### Attributes
| Name | Type |
| -------- | -------- | 
| enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'EqRate', 'set_auto_reinit_enabled', {'enabled': 'bool'}
)
```

---------
### set_now_millis_offset
Function used in test builds for time move
#### Attributes
| Name | Type |
| -------- | -------- | 
| offset | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'EqRate', 'set_now_millis_offset', {'offset': 'u64'}
)
```

---------
### withdraw
Request to burn asset for account

The dispatch origin for this call must be _None_ (unsigned transaction).

Parameters:
 - `request`: OperationRequest.
 - `_signature`: OperationRequest signature
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `BalanceRemovalRequest<T::AccountId, Asset, T::Balance, T::BlockNumber
>` | 
| signature | `<T::AuthorityId as RuntimeAppPublic>::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'EqRate', 'withdraw', {
    'request': {
        'account': 'AccountId',
        'amount': 'u128',
        'asset': 'u64',
        'authority_index': 'u32',
        'block_num': 'u32',
        'higher_priority': 'bool',
        'validators_len': 'u32',
    },
    'signature': '[u8; 64]',
}
)
```

---------
## Storage functions

---------
### AutoReinitEnabled
 Stores flag for on/off setting for offchain workers (reinits)

#### Python
```python
result = substrate.query(
    'EqRate', 'AutoReinitEnabled', []
)
```

#### Return value
```python
'bool'
```
---------
### Keys
 Pallet storage for keys

#### Python
```python
result = substrate.query(
    'EqRate', 'Keys', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### LastFeeUpdate
 Pallet storage - last update timestamps in seconds for each `AccountId` that has balances

#### Python
```python
result = substrate.query(
    'EqRate', 'LastFeeUpdate', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### NowMillisOffset
 Pallet storage used for time offset in test builds. Disabled by &quot;production&quot; feature.

#### Python
```python
result = substrate.query(
    'EqRate', 'NowMillisOffset', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### Alpha
 Pricing model scaling factor
#### Value
```python
15000000000000000000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'Alpha')
```
---------
### BailsmanModuleId
 Gets bailsman module account for margincall and fee transfers
#### Value
```python
'0x65712f6261696c73'
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'BailsmanModuleId')
```
---------
### BaseBailsmanFee
 Base bailsman fee
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'BaseBailsmanFee')
```
---------
### BaseLenderFee
 Base lender fee
#### Value
```python
5000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'BaseLenderFee')
```
---------
### LenderPart
 Lender part of prime rate
#### Value
```python
300000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'LenderPart')
```
---------
### LendingModuleId
 For transferring fee to lending pool
#### Value
```python
'0x65712f6c656e6472'
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'LendingModuleId')
```
---------
### MinSurplus
 Minimum new debt for system reinit
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'MinSurplus')
```
---------
### MinTempBailsman
 Minimum temp bailsmen balances for Bailsman pallet reinit
#### Value
```python
50000000000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'MinTempBailsman')
```
---------
### RiskLowerBound
 Lower bound for scaling risk model
#### Value
```python
500000000000000000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'RiskLowerBound')
```
---------
### RiskNSigma
 Number of standard deviations to consider when stress testing
#### Value
```python
5000000000000000000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'RiskNSigma')
```
---------
### RiskUpperBound
 Upper bound for scaling risk model
#### Value
```python
2000000000000000000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'RiskUpperBound')
```
---------
### TreasuryFee
 Treasury fee rate
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'TreasuryFee')
```
---------
### TreasuryModuleId
 For transferring fee to treasury
#### Value
```python
'0x65712f7472737279'
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'TreasuryModuleId')
```
---------
### UnsignedPriority
 For unsigned transaction priority calculation
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'UnsignedPriority')
```
---------
### WeightFeeTreasury
 Fee part that stays in Treasury pallet
#### Value
```python
80
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'WeightFeeTreasury')
```
---------
### WeightFeeValidator
 Fee part that goes to validator
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('EqRate', 'WeightFeeValidator')
```
---------
## Errors

---------
### AssetNotInRemovalQueue
Asset is not in removal queue

---------
### AutoReinitIsDisabled
Auto reinit is disabled

---------
### ExternalError
Some external error while rate calculation

---------
### InvalidOffset
Error used during time offset in test builds

---------
### LastUpdateInFuture
Last update in fututure

---------
### MathError
Math error in rate calculation

---------
### MethodNotAllowed
This method is not allowed in production

---------
### NoFinancial
Financial parameters are outdated

---------
### NoPrices
Prices are outdated

---------
### ValidationError
Validation error

---------
### ValueError
Error in rate calculation

---------