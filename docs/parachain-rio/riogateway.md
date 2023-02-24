
# RioGateway

---------
## Calls

---------
### add_supported_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| withdrawal_fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'add_supported_asset', {
    'currency_id': 'u32',
    'withdrawal_fee': 'u128',
}
)
```

---------
### apply_deposit_index
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'apply_deposit_index', {}
)
```

---------
### approve_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdraw_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'approve_withdraw', {'withdraw_id': 'u64'}
)
```

---------
### cancel_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdraw_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'cancel_withdraw', {'withdraw_id': 'u64'}
)
```

---------
### deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| depositor | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `CurrencyIdOf<T>` | 
| tx_hash | `TxHash` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'deposit', {
    'currency_id': 'u32',
    'depositor': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'tx_hash': '[u8; 32]',
    'value': 'u128',
}
)
```

---------
### finish_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdraw_id | `u64` | 
| tx_hash | `TxHash` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'finish_withdraw', {
    'tx_hash': '[u8; 32]',
    'withdraw_id': 'u64',
}
)
```

---------
### rebroadcast
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdraw_id | `u64` | 
| tx_hash | `TxHash` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'rebroadcast', {
    'tx_hash': '[u8; 32]',
    'withdraw_id': 'u64',
}
)
```

---------
### reject_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdraw_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'reject_withdraw', {'withdraw_id': 'u64'}
)
```

---------
### remove_supported_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'remove_supported_asset', {'currency_id': 'u32'}
)
```

---------
### request_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| value | `BalanceOf<T>` | 
| addr | `ChainAddress` | 
| memo | `Memo` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'request_withdraw', {
    'addr': 'Bytes',
    'currency_id': 'u32',
    'memo': 'Bytes',
    'value': 'u128',
}
)
```

---------
### set_auth
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| auths | `Auths` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'set_auth', {
    'auths': {'mask': 'u8'},
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### set_deposit_addr_info_of_asset_id
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| addr_info | `DepositAddrInfo<BBVec>` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'set_deposit_addr_info_of_asset_id', {
    'addr_info': {
        'Bip32': {
            'path': 'Bytes',
            'x_pub': 'Bytes',
        },
        'Create2': {
            'creator_address': 'Bytes',
            'implementation_address': 'Bytes',
            'vault_address': 'Bytes',
        },
    },
    'currency_id': 'u32',
}
)
```

---------
### set_max_deposit_index
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_count | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'set_max_deposit_index', {'new_count': 'u64'}
)
```

---------
### set_withdrawal_fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| withdrawal_fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'set_withdrawal_fee', {
    'currency_id': 'u32',
    'withdrawal_fee': 'u128',
}
)
```

---------
### unsafe_set_withdraw_state
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdraw_id | `u64` | 
| state | `Option<WithdrawState>` | 

#### Python
```python
call = substrate.compose_call(
    'RioGateway', 'unsafe_set_withdraw_state', {
    'state': (
        None,
        {
            'Approved': None,
            'Cancelled': None,
            'Pending': None,
            'ReBroadcasted': '[u8; 32]',
            'Rejected': None,
            'Success': '[u8; 32]',
        },
    ),
    'withdraw_id': 'u64',
}
)
```

---------
## Events

---------
### AuthChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `Auths` | ```{'mask': 'u8'}```

---------
### MaxDepositCountSetted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### NewDepositAddrInfoOfAssetId
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyIdOf<T>` | ```u32```
| None | `DAddrInfo` | ```{'Bip32': {'x_pub': 'Bytes', 'path': 'Bytes'}, 'Create2': {'creator_address': 'Bytes', 'implementation_address': 'Bytes', 'vault_address': 'Bytes'}}```

---------
### NewDepositIndex
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `u64` | ```u64```

---------
### NewDepositRecord
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyIdOf<T>` | ```u32```
| None | `DepositOf<T>` | ```{'account_id': 'AccountId', 'amount': 'u128'}```
| None | `TxHash` | ```[u8; 32]```

---------
### NewPendingWithdrawRecord
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```
| None | `WithdrawInfoOf<T>` | ```{'currency_id': 'u32', 'who': 'AccountId', 'value': 'u128', 'addr': 'Bytes', 'memo': 'Bytes'}```
| None | `BalanceOf<T>` | ```u128```

---------
### SupportedAssetAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `CurrencyIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### SupportedAssetRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `CurrencyIdOf<T>` | ```u32```

---------
### UnsafeRemoveWithdrawRecord
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### UnsafeSetWithdrawState
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```
| None | `WithdrawState` | ```{'Pending': None, 'Cancelled': None, 'Rejected': None, 'Approved': None, 'Success': '[u8; 32]', 'ReBroadcasted': '[u8; 32]'}```

---------
### WithdrawRebroadcasted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```
| None | `AccountIdOf<T>` | ```AccountId```
| None | `WithdrawState` | ```{'Pending': None, 'Cancelled': None, 'Rejected': None, 'Approved': None, 'Success': '[u8; 32]', 'ReBroadcasted': '[u8; 32]'}```

---------
### WithdrawStatusChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```
| None | `AccountIdOf<T>` | ```AccountId```
| None | `WithdrawState` | ```{'Pending': None, 'Cancelled': None, 'Rejected': None, 'Approved': None, 'Success': '[u8; 32]', 'ReBroadcasted': '[u8; 32]'}```
| None | `WithdrawState` | ```{'Pending': None, 'Cancelled': None, 'Rejected': None, 'Approved': None, 'Success': '[u8; 32]', 'ReBroadcasted': '[u8; 32]'}```

---------
### WithdrawaFeeSetted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `CurrencyIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ActiveWithdrawStates
 withdrawal status for an id

#### Python
```python
result = substrate.query(
    'RioGateway', 'ActiveWithdrawStates', ['u64']
)
```

#### Return value
```python
{
    'Approved': None,
    'Cancelled': None,
    'Pending': None,
    'ReBroadcasted': '[u8; 32]',
    'Rejected': None,
    'Success': '[u8; 32]',
}
```
---------
### Admins

#### Python
```python
result = substrate.query(
    'RioGateway', 'Admins', ['AccountId']
)
```

#### Return value
```python
{'mask': 'u8'}
```
---------
### ConsumedFee
 Consumed Fee for every Withdrawal Id

#### Python
```python
result = substrate.query(
    'RioGateway', 'ConsumedFee', ['u64']
)
```

#### Return value
```python
'u128'
```
---------
### DepoistIndexOfAccountId
 map of bip32 path index of an account. if this account have not apply deposit, it would be None

#### Python
```python
result = substrate.query(
    'RioGateway', 'DepoistIndexOfAccountId', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### DepositAddrInfoOfAssetId
 Store gateway deposit addr basic info for an asset.

#### Python
```python
result = substrate.query(
    'RioGateway', 'DepositAddrInfoOfAssetId', ['u32']
)
```

#### Return value
```python
{
    'Bip32': {'path': 'Bytes', 'x_pub': 'Bytes'},
    'Create2': {
        'creator_address': 'Bytes',
        'implementation_address': 'Bytes',
        'vault_address': 'Bytes',
    },
}
```
---------
### DepositHistory
 keep a history of depoists in case of double spent

#### Python
```python
result = substrate.query(
    'RioGateway', 'DepositHistory', ['u32', '[u8; 32]']
)
```

#### Return value
```python
{'account_id': 'AccountId', 'amount': 'u128'}
```
---------
### MaxDepositIndex
 Current max deposit index, if more than this count, would return error for user.

#### Python
```python
result = substrate.query(
    'RioGateway', 'MaxDepositIndex', []
)
```

#### Return value
```python
'u64'
```
---------
### NextDepositIndex
 Next deposit index

#### Python
```python
result = substrate.query(
    'RioGateway', 'NextDepositIndex', []
)
```

#### Return value
```python
'u64'
```
---------
### NextWithdrawalId
 Withdrawal Id

#### Python
```python
result = substrate.query(
    'RioGateway', 'NextWithdrawalId', []
)
```

#### Return value
```python
'u64'
```
---------
### PendingWithdrawals
 after withdraw req is fired, it will be append here first, waiting for approval

#### Python
```python
result = substrate.query(
    'RioGateway', 'PendingWithdrawals', ['u64']
)
```

#### Return value
```python
{
    'addr': 'Bytes',
    'currency_id': 'u32',
    'memo': 'Bytes',
    'value': 'u128',
    'who': 'AccountId',
}
```
---------
### SupportedAssets

#### Python
```python
result = substrate.query(
    'RioGateway', 'SupportedAssets', ['u32']
)
```

#### Return value
```python
'bool'
```
---------
### WithdrawalFee
 set a fixed withdrawal fee for a asset

#### Python
```python
result = substrate.query(
    'RioGateway', 'WithdrawalFee', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### AlreadyAppliedIndex
already applied for deposit path index

---------
### AssetExisted
already set this asset before

---------
### AssetNotSupported
not supported asset

---------
### CanNotAssignIndex
can&\#x27;t assign an index now.

---------
### CanNotCancelOtherWithdrawals
not owner for this withdraw

---------
### InvalidWithdraw
apply an invalid withdraw

---------
### InvalidWithdrawalState
The previously withdraw record is an invalid withdraw state

---------
### TransactionRepeated
Repeated transaction

---------
### UnAuthorized
UnAuthorized Operation

---------
### WithdrawalRecordNotExisted
Pending withdraw not found

---------