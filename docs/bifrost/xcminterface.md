
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
- `updates`: vec of tuple: (XcmOperationType, WeightChange, FeeChange).
#### Attributes
| Name | Type |
| -------- | -------- | 
| updates | `Vec<(CurrencyIdOf<T>, XcmOperationType, Weight, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'XcmInterface', 'update_xcm_dest_weight_and_fee', {
    'updates': [
        (
            {
                'BLP': 'u32',
                'ForeignAsset': 'u32',
                'LPToken': (
                    (
                        'ASG',
                        'BNC',
                        'KUSD',
                        'DOT',
                        'KSM',
                        'ETH',
                        'KAR',
                        'ZLK',
                        'PHA',
                        'RMRK',
                        'MOVR',
                    ),
                    'u8',
                    (
                        'ASG',
                        'BNC',
                        'KUSD',
                        'DOT',
                        'KSM',
                        'ETH',
                        'KAR',
                        'ZLK',
                        'PHA',
                        'RMRK',
                        'MOVR',
                    ),
                    'u8',
                ),
                'Native': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'Stable': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'Token2': 'u8',
                'VSBond': (
                    (
                        'ASG',
                        'BNC',
                        'KUSD',
                        'DOT',
                        'KSM',
                        'ETH',
                        'KAR',
                        'ZLK',
                        'PHA',
                        'RMRK',
                        'MOVR',
                    ),
                    'u32',
                    'u32',
                    'u32',
                ),
                'VSBond2': (
                    'u8',
                    'u32',
                    'u32',
                    'u32',
                ),
                'VSToken': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'VSToken2': 'u8',
                'VToken': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'VToken2': 'u8',
            },
            (
                'UmpContributeTransact',
                'StatemineTransfer',
                'Bond',
                'WithdrawUnbonded',
                'BondExtra',
                'Unbond',
                'Rebond',
                'Delegate',
                'Payout',
                'Liquidize',
                'TransferBack',
                'TransferTo',
                'Chill',
                'Undelegate',
                'CancelLeave',
                'XtokensTransferBack',
                'ExecuteLeave',
                'ConvertAsset',
                'Vote',
                'RemoveVote',
                'Any',
            ),
            {
                'proof_size': 'u64',
                'ref_time': 'u64',
            },
            'u128',
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
### XcmDestWeightAndFeeUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `XcmOperationType` | ```('UmpContributeTransact', 'StatemineTransfer', 'Bond', 'WithdrawUnbonded', 'BondExtra', 'Unbond', 'Rebond', 'Delegate', 'Payout', 'Liquidize', 'TransferBack', 'TransferTo', 'Chill', 'Undelegate', 'CancelLeave', 'XtokensTransferBack', 'ExecuteLeave', 'ConvertAsset', 'Vote', 'RemoveVote', 'Any')```
| None | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32', 'BLP': 'u32'}```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### CurrentNonce

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
### XcmWeightAndFee
 The dest weight limit and fee for execution XCM msg sent by XcmInterface. Must be
 sufficient, otherwise the execution of XCM msg on relaychain will fail.

 XcmWeightAndFee: map: XcmOperationType =&gt; (Weight, Balance)

#### Python
```python
result = substrate.query(
    'XcmInterface', 'XcmWeightAndFee', [
    {
        'BLP': 'u32',
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
    (
        'UmpContributeTransact',
        'StatemineTransfer',
        'Bond',
        'WithdrawUnbonded',
        'BondExtra',
        'Unbond',
        'Rebond',
        'Delegate',
        'Payout',
        'Liquidize',
        'TransferBack',
        'TransferTo',
        'Chill',
        'Undelegate',
        'CancelLeave',
        'XtokensTransferBack',
        'ExecuteLeave',
        'ConvertAsset',
        'Vote',
        'RemoveVote',
        'Any',
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
## Errors

---------
### FailToConvert

---------
### FeeConvertFailed

---------
### OperationWeightAndFeeNotExist

---------
### XcmExecutionFailed

---------
### XcmSendFailed

---------