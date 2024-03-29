
# PalletXcmHelper

---------
## Calls

---------
### update_xcm_weight_fee
Update xcm fees amount to be used in xcm.Withdraw message
#### Attributes
| Name | Type |
| -------- | -------- | 
| xcm_call | `XcmCall` | 
| xcm_weight_fee_misc | `XcmWeightFeeMisc<Weight, BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'PalletXcmHelper', 'update_xcm_weight_fee', {
    'xcm_call': (
        'Bond',
        'BondExtra',
        'Unbond',
        'Rebond',
        'WithdrawUnbonded',
        'Nominate',
    ),
    'xcm_weight_fee_misc': {
        'fee': 'u128',
        'weight': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
    },
}
)
```

---------
## Events

---------
### XcmWeightFeeUpdated
Xcm fee and weight updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `XcmWeightFeeMisc<Weight, BalanceOf<T>>` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'fee': 'u128'}```

---------
## Storage functions

---------
### XcmWeightFee

#### Python
```python
result = substrate.query(
    'PalletXcmHelper', 'XcmWeightFee', [
    (
        'Bond',
        'BondExtra',
        'Unbond',
        'Rebond',
        'WithdrawUnbonded',
        'Nominate',
    ),
]
)
```

#### Return value
```python
{'fee': 'u128', 'weight': {'proof_size': 'u64', 'ref_time': 'u64'}}
```
---------
## Constants

---------
### NotifyTimeout
 Notify call timeout
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('PalletXcmHelper', 'NotifyTimeout')
```
---------
### PalletId
 Pallet account for collecting xcm fees
#### Value
```python
'0x636f6d2f66656573'
```
#### Python
```python
constant = substrate.get_constant('PalletXcmHelper', 'PalletId')
```
---------
### RefundLocation
 Account on relaychain for receiving refunded fees
#### Value
```python
'63H4NwjfrUPjNjd7WQByN6euwPq2WSd1UhrwvSQU2xfTJSoL'
```
#### Python
```python
constant = substrate.get_constant('PalletXcmHelper', 'RefundLocation')
```
---------
### RelayCurrency
 Relay currency
#### Value
```python
79228162514264337593543950342
```
#### Python
```python
constant = substrate.get_constant('PalletXcmHelper', 'RelayCurrency')
```
---------
### RelayNetwork
 Relay network
#### Value
```python
'Polkadot'
```
#### Python
```python
constant = substrate.get_constant('PalletXcmHelper', 'RelayNetwork')
```
---------
## Errors

---------
### ConvertAccountError
Can not convert account success

---------
### InsufficientXcmFees
Insufficient xcm fees

---------
### MultiLocationNotInvertible
`MultiLocation` value ascend more parents than known ancestors of local location.

---------
### SendFailure
The message and destination was recognized as being reachable but
the operation could not be completed.

---------
### ZeroXcmFees
Xcm fees cannot be zero

---------
### ZeroXcmWeightMisc
XcmWeightMisc cannot have zero value

---------