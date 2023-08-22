
# XcmInterface

---------
## Calls

---------
### transfer_statemine_assets
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| asset_id | `u32` | 
| dest | `Option<AccountIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'XcmInterface', 'transfer_statemine_assets', {
    'amount': 'u128',
    'asset_id': 'u32',
    'dest': (None, 'AccountId'),
}
)
```

---------
### update_xcm_dest_weight_and_fee
Sets the xcm_dest_weight and fee for XCM operation of XcmInterface.

Parameters:
- `updates`: vec of tuple: (XcmInterfaceOperation, WeightChange, FeeChange).
#### Attributes
| Name | Type |
| -------- | -------- | 
| updates | `Vec<(XcmInterfaceOperation, Option<Weight>, Option<BalanceOf<T>>)>` | 

#### Python
```python
call = substrate.compose_call(
    'XcmInterface', 'update_xcm_dest_weight_and_fee', {
    'updates': [
        (
            (
                'UmpContributeTransact',
                'StatemineTransfer',
            ),
            (
                None,
                {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            ),
            (None, 'u128'),
        ),
    ],
}
)
```

---------
## Events

---------
### TransferredStatemineMultiAsset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### XcmDestWeightUpdated
Xcm dest weight has been updated. \[xcm_operation, new_xcm_dest_weight\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `XcmInterfaceOperation` | ```('UmpContributeTransact', 'StatemineTransfer')```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### XcmFeeUpdated
Xcm dest weight has been updated. \[xcm_operation, new_xcm_dest_weight\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `XcmInterfaceOperation` | ```('UmpContributeTransact', 'StatemineTransfer')```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### CurrentNonce
 Tracker for the next nonce index

#### Python
```python
result = substrate.query(
    'XcmInterface', 'CurrentNonce', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### XcmDestWeightAndFee
 The dest weight limit and fee for execution XCM msg sent by XcmInterface. Must be
 sufficient, otherwise the execution of XCM msg on relaychain will fail.

 XcmDestWeightAndFee: map: XcmInterfaceOperation =&gt; (Weight, Balance)

#### Python
```python
result = substrate.query(
    'XcmInterface', 'XcmDestWeightAndFee', [
    (
        'UmpContributeTransact',
        'StatemineTransfer',
    ),
]
)
```

#### Return value
```python
({'proof_size': 'u64', 'ref_time': 'u64'}, 'u128')
```
---------
## Constants

---------
### CallBackTimeOut
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'CallBackTimeOut')
```
---------
### ContributionFee
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'ContributionFee')
```
---------
### ContributionWeight
#### Value
```python
{'proof_size': 1000000, 'ref_time': 1000000000}
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'ContributionWeight')
```
---------
### ParachainId
#### Value
```python
2001
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'ParachainId')
```
---------
### ParachainSovereignAccount
 The account of parachain on the relaychain.
#### Value
```python
'eGJrytyJYDzMGM1uji4Bx5ntw3xF6aifJ7Xvo3mE48cgW5N'
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'ParachainSovereignAccount')
```
---------
### RelayNetwork
#### Value
```python
'Kusama'
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'RelayNetwork')
```
---------
### RelaychainCurrencyId
 The currency id of the RelayChain
#### Value
```python
{'Token': 'KSM'}
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'RelaychainCurrencyId')
```
---------
### StatemineTransferFee
#### Value
```python
4000000000
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'StatemineTransferFee')
```
---------
### StatemineTransferWeight
#### Value
```python
{'proof_size': 0, 'ref_time': 4000000000}
```
#### Python
```python
constant = substrate.get_constant('XcmInterface', 'StatemineTransferWeight')
```
---------
## Errors

---------
### FeeConvertFailed

---------
### XcmExecutionFailed

---------
### XcmSendFailed

---------