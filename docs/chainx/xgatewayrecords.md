
# XGatewayRecords

---------
## Calls

---------
### root_deposit
Deposit asset token.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| asset_id | `AssetId` | 
| balance | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayRecords', 'root_deposit', {
    'asset_id': 'u32',
    'balance': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### root_withdraw
Withdraw asset token (only lock token)

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| asset_id | `AssetId` | 
| balance | `BalanceOf<T>` | 
| addr | `AddrStr` | 
| memo | `Memo` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayRecords', 'root_withdraw', {
    'addr': 'Bytes',
    'asset_id': 'u32',
    'balance': 'u128',
    'memo': 'Bytes',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### set_withdrawal_state
Set the state of withdrawal record with given id and state.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdrawal_id | `WithdrawalRecordId` | 
| state | `WithdrawalState` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayRecords', 'set_withdrawal_state', {
    'state': (
        'Applying',
        'Processing',
        'NormalFinish',
        'RootFinish',
        'NormalCancel',
        'RootCancel',
    ),
    'withdrawal_id': 'u32',
}
)
```

---------
### set_withdrawal_state_list
Set the state of withdrawal records in batches.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| item | `Vec<(WithdrawalRecordId, WithdrawalState)>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayRecords', 'set_withdrawal_state_list', {
    'item': [
        (
            'u32',
            (
                'Applying',
                'Processing',
                'NormalFinish',
                'RootFinish',
                'NormalCancel',
                'RootCancel',
            ),
        ),
    ],
}
)
```

---------
## Events

---------
### Deposited
An account deposited some asset. [who, asset_id, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### WithdrawalCanceled
A withdrawal proposal was canceled. [withdrawal_id, withdrawal_state]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WithdrawalRecordId` | ```u32```
| None | `WithdrawalState` | ```('Applying', 'Processing', 'NormalFinish', 'RootFinish', 'NormalCancel', 'RootCancel')```

---------
### WithdrawalCreated
A withdrawal application was created. [withdrawal_id, record_info]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WithdrawalRecordId` | ```u32```
| None | `WithdrawalRecordOf<T>` | ```{'asset_id': 'u32', 'applicant': 'AccountId', 'balance': 'u128', 'addr': 'Bytes', 'ext': 'Bytes', 'height': 'u32'}```

---------
### WithdrawalFinished
A withdrawal proposal was finished successfully. [withdrawal_id, withdrawal_state]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WithdrawalRecordId` | ```u32```
| None | `WithdrawalState` | ```('Applying', 'Processing', 'NormalFinish', 'RootFinish', 'NormalCancel', 'RootCancel')```

---------
### WithdrawalProcessed
A withdrawal proposal was processed. [withdrawal_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WithdrawalRecordId` | ```u32```

---------
### WithdrawalRecovered
A withdrawal proposal was recovered. [withdrawal_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WithdrawalRecordId` | ```u32```

---------
## Storage functions

---------
### NextWithdrawalRecordId
 The id of next withdrawal record.

#### Python
```python
result = substrate.query(
    'XGatewayRecords', 'NextWithdrawalRecordId', []
)
```

#### Return value
```python
'u32'
```
---------
### PendingWithdrawals
 Withdraw applications collection, use serial numbers to mark them.

#### Python
```python
result = substrate.query(
    'XGatewayRecords', 'PendingWithdrawals', ['u32']
)
```

#### Return value
```python
{
    'addr': 'Bytes',
    'applicant': 'AccountId',
    'asset_id': 'u32',
    'balance': 'u128',
    'ext': 'Bytes',
    'height': 'u32',
}
```
---------
### WithdrawalStateOf
 The state of withdraw record corresponding to an id.

#### Python
```python
result = substrate.query(
    'XGatewayRecords', 'WithdrawalStateOf', ['u32']
)
```

#### Return value
```python
(
    'Applying',
    'Processing',
    'NormalFinish',
    'RootFinish',
    'NormalCancel',
    'RootCancel',
)
```
---------
## Errors

---------
### InvalidAccount
The applicant is not this account

---------
### InvalidState
State only allow `RootFinish` and `RootCancel`

---------
### NotApplyingState
WithdrawalRecord state not `Applying`

---------
### NotExisted
Id not in withdrawal records

---------
### NotProcessingState
WithdrawalRecord state not `Processing`

---------
### UnexpectedChain
Meet unexpected chain

---------