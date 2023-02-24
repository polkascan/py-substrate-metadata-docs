
# EqWrappedDot

---------
## Calls

---------
### deposit
Deposit amount of DOT
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'EqWrappedDot', 'deposit', {'amount': 'u128'}
)
```

---------
### initialize
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 
| transferable | `T::Balance` | 
| bond | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'EqWrappedDot', 'initialize', {
    'account_id': 'AccountId',
    'bond': 'u128',
    'transferable': 'u128',
}
)
```

---------
### set_total_unlocking
Set total unlocking. For maintenance purposes
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'EqWrappedDot', 'set_total_unlocking', {'value': 'u128'}
)
```

---------
### withdraw
Withdraw
params:
- amount - amount of DOT/EQDOT to withdraw/burn
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `WithdrawAmount<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'EqWrappedDot', 'withdraw', {
    'amount': {
        'Dot': 'u128',
        'EqDot': 'u128',
    },
}
)
```

---------
## Storage functions

---------
### CurrentBalance
 Current distribution of DOTs in staking.
 Relate to reservation coefficient by formula: RC = transferable / (transferable + staked)

#### Python
```python
result = substrate.query(
    'EqWrappedDot', 'CurrentBalance', []
)
```

#### Return value
```python
{'staked': 'u128', 'transferable': 'u128'}
```
---------
### LastWithdrawEra
 Last withdraw era

#### Python
```python
result = substrate.query(
    'EqWrappedDot', 'LastWithdrawEra', []
)
```

#### Return value
```python
'u32'
```
---------
### RelayStakingInfo
 Copies of `CurrentEra` and `Ledger` storages on relay chain.
 Will be updated every block in `on_finalize`.

#### Python
```python
result = substrate.query(
    'EqWrappedDot', 'RelayStakingInfo', []
)
```

#### Return value
```python
(
    'u32',
    {
        'active': 'u128',
        'claimed_rewards': ['u32'],
        'stash': 'AccountId',
        'total': 'u128',
        'unlocking': [{'era': 'u32', 'value': 'u128'}],
    },
)
```
---------
### StakingRoutinePeriodicity
 Periodicity of on-initialize functions: clear withdraw queue and rebalance transferable balance

#### Python
```python
result = substrate.query(
    'EqWrappedDot', 'StakingRoutinePeriodicity', []
)
```

#### Return value
```python
'u32'
```
---------
### TotalUnlocking
 Total unlocking sum

#### Python
```python
result = substrate.query(
    'EqWrappedDot', 'TotalUnlocking', []
)
```

#### Return value
```python
'u128'
```
---------
### WithdrawQueue
 Withdraw queue, (Beneficiary, DOT amount to withdraw, EQDOT amount to burn)

#### Python
```python
result = substrate.query(
    'EqWrappedDot', 'WithdrawQueue', []
)
```

#### Return value
```python
[('AccountId', 'u128', 'u128')]
```
---------
## Constants

---------
### MaxReserve
 Maximum reservation coefficient that can possibly be observed
 If reservation coefficient exceeds that value, `balance_staking` will balance it to `TargetReserve`
#### Value
```python
200000
```
#### Python
```python
constant = substrate.get_constant('EqWrappedDot', 'MaxReserve')
```
---------
### MinDeposit
 Min amount to deposit, by default 5 DOT
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('EqWrappedDot', 'MinDeposit')
```
---------
### MinReserve
 Minimum reservation coefficient that can possibly be observed
 If reservation coefficient falls below that value, `balance_staking` will balance it to `TargetReserve`
#### Value
```python
100000
```
#### Python
```python
constant = substrate.get_constant('EqWrappedDot', 'MinReserve')
```
---------
### PalletId
 Pallet identifier
#### Value
```python
'0x65712f7772646f74'
```
#### Python
```python
constant = substrate.get_constant('EqWrappedDot', 'PalletId')
```
---------
### ParachainId
#### Value
```python
2011
```
#### Python
```python
constant = substrate.get_constant('EqWrappedDot', 'ParachainId')
```
---------
### TargetReserve
 Reservation coefficient that is preferable, with deviation in range [`MinReserve`, `MaxReserve`]
#### Value
```python
150000
```
#### Python
```python
constant = substrate.get_constant('EqWrappedDot', 'TargetReserve')
```
---------
### WithdrawFee
 Fee payed for withdraw, also used in price calculation, by default 0.98940904738
#### Value
```python
989409
```
#### Python
```python
constant = substrate.get_constant('EqWrappedDot', 'WithdrawFee')
```
---------
## Errors

---------
### InsufficientDeposit
Amount to deposit less than min deposit amount

---------
### InsufficientWithdraw
Amount to withdraw less than min amount to withdraw

---------
### MathError
Math error

---------
### NotSupportedAsset
Not a price source for an asset

---------
### XcmBalanceConversionError
Error while converting balance to relay chain balance

---------
### XcmStakingBondExtraFailed
Xcm call pallet_staking::bond_extra failed

---------
### XcmStakingUnbondFailed
Xcm call pallet_staking::unbond failed

---------
### XcmStakingWithdrawUnbondedFailed
Xcm call pallet_staking::withraw_unbonded failed

---------
### XcmUnknownAsset
Asset without xcm information

---------