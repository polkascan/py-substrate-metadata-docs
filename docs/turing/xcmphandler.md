
# XcmpHandler

---------
## Calls

---------
### add_chain_currency_data
Add or update XCM data for a chain/currency pair.
For now we only support our native currency.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para_id | `ParachainId` | 
| currency_id | `T::CurrencyId` | 
| xcm_data | `XcmCurrencyData` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpHandler', 'add_chain_currency_data', {
    'currency_id': 'u32',
    'para_id': 'u32',
    'xcm_data': {
        'fee_per_second': 'u128',
        'flow': (
            'Normal',
            'Alternate',
        ),
        'instruction_weight': 'u64',
        'native': 'bool',
    },
}
)
```

---------
### remove_chain_currency_data
Remove XCM data for a chain/currency pair.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para_id | `ParachainId` | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpHandler', 'remove_chain_currency_data', {
    'currency_id': 'u32',
    'para_id': 'u32',
}
)
```

---------
## Events

---------
### XcmDataAdded
XCM data was added for a chain/currency pair.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParachainId` | ```u32```
| currency_id | `T::CurrencyId` | ```u32```

---------
### XcmDataRemoved
XCM data was removed for a chain/currency pair.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParachainId` | ```u32```
| currency_id | `T::CurrencyId` | ```u32```

---------
### XcmFeesFailed
XCM fees failed to transfer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| source | `T::AccountId` | ```AccountId```
| dest | `T::AccountId` | ```AccountId```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### XcmFeesPaid
XCM fees successfully paid.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| source | `T::AccountId` | ```AccountId```
| dest | `T::AccountId` | ```AccountId```

---------
### XcmSent
XCM sent to target chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParachainId` | ```u32```

---------
### XcmTransactedLocally
XCM transacted in local chain.
#### Attributes
No attributes

---------
## Storage functions

---------
### XcmChainCurrencyData
 Stores XCM data for a chain/currency pair.

#### Python
```python
result = substrate.query(
    'XcmpHandler', 'XcmChainCurrencyData', ['u32', 'u32']
)
```

#### Return value
```python
{
    'fee_per_second': 'u128',
    'flow': ('Normal', 'Alternate'),
    'instruction_weight': 'u64',
    'native': 'bool',
}
```
---------
## Constants

---------
### GetNativeCurrencyId
 The currencyId for the native currency.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('XcmpHandler', 'GetNativeCurrencyId')
```
---------
## Errors

---------
### CannotReanchor
Unable to reanchor the asset.

---------
### CurrencyChainComboNotFound
There is no entry for that currency/chain combination.

---------
### CurrencyChainComboNotSupported
We only support certain currency/chain combinations.

---------
### CurrencyNotSupported
Currency not supported

---------
### ErrorGettingCallWeight
Failed to get weight of call.

---------
### ErrorSendingXcmToTarget
Failed to send XCM to target.

---------
### FailedMultiLocationToJunction
Failed when creating the multilocation for descend origin.

---------
### FeeOverflow
Either the weight or fee per second is too large.

---------
### WeightOverflow
Either the instruction weight or the transact weight is too large.

---------
### XcmExecutionFailed
Failed to execute XCM in local chain.

---------