
# Estimates

---------
## Calls

---------
### active_pallet
#### Attributes
| Name | Type |
| -------- | -------- | 
| active | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Estimates', 'active_pallet', {'active': 'bool'}
)
```

---------
### choose_winner
#### Attributes
| Name | Type |
| -------- | -------- | 
| trigger_payload | `ChooseTrigerPayload<T::Public>` | 
| signature | `OffchainSignature<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Estimates', 'choose_winner', {
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'trigger_payload': {
        'public': {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
        'symbol': (
            'Bytes',
            ('DEVIATION', 'RANGE'),
        ),
    },
}
)
```

---------
### data_cleaning
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Estimates', 'data_cleaning', {}
)
```

---------
### force_complete
#### Attributes
| Name | Type |
| -------- | -------- | 
| symbol | `Vec<u8>` | 
| estimates_type | `EstimatesType` | 
| ruling_price | `u64` | 
| ruling_fraction_length | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Estimates', 'force_complete', {
    'estimates_type': (
        'DEVIATION',
        'RANGE',
    ),
    'ruling_fraction_length': 'u32',
    'ruling_price': 'u64',
    'symbol': 'Bytes',
}
)
```

---------
### new_estimates
#### Attributes
| Name | Type |
| -------- | -------- | 
| symbol | `Vec<u8>` | 
| start | `T::BlockNumber` | 
| end | `T::BlockNumber` | 
| distribute | `T::BlockNumber` | 
| estimates_type | `EstimatesType` | 
| deviation | `Option<Permill>` | 
| range | `Option<Vec<u64>>` | 
| range_fraction_length | `Option<u32>` | 
| multiplier | `Vec<MultiplierOption>` | 
| init_reward | `BalanceOf<T>` | 
| price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Estimates', 'new_estimates', {
    'deviation': (None, 'u32'),
    'distribute': 'u32',
    'end': 'u32',
    'estimates_type': (
        'DEVIATION',
        'RANGE',
    ),
    'init_reward': 'u128',
    'multiplier': [{'Base': 'u8'}],
    'price': 'u128',
    'range': (None, ['u64']),
    'range_fraction_length': (
        None,
        'u32',
    ),
    'start': 'u32',
    'symbol': 'Bytes',
}
)
```

---------
### participate_estimates
#### Attributes
| Name | Type |
| -------- | -------- | 
| symbol | `Vec<u8>` | 
| estimated_type | `EstimatesType` | 
| estimated_price | `Option<u64>` | 
| estimated_fraction_length | `Option<u32>` | 
| range_index | `Option<u8>` | 
| multiplier | `MultiplierOption` | 
| bsc_address | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'Estimates', 'participate_estimates', {
    'bsc_address': (None, 'Bytes'),
    'estimated_fraction_length': (
        None,
        'u32',
    ),
    'estimated_price': (None, 'u64'),
    'estimated_type': (
        'DEVIATION',
        'RANGE',
    ),
    'multiplier': {'Base': 'u8'},
    'range_index': (None, 'u8'),
    'symbol': 'Bytes',
}
)
```

---------
### preference
#### Attributes
| Name | Type |
| -------- | -------- | 
| admins | `Option<Vec<T::AccountId>>` | 
| locked_estimates | `Option<T::BlockNumber>` | 
| minimum_ticket_price | `Option<BalanceOf<T>>` | 
| minimum_init_reward | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Estimates', 'preference', {
    'admins': (None, ['AccountId']),
    'locked_estimates': (None, 'u32'),
    'minimum_init_reward': (
        None,
        'u128',
    ),
    'minimum_ticket_price': (
        None,
        'u128',
    ),
}
)
```

---------
## Events

---------
### ActiveEstimates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| estimate | `SymbolEstimatesConfig<T::BlockNumber, BalanceOf<T>>` | ```{'symbol': 'Bytes', 'estimates_type': ('DEVIATION', 'RANGE'), 'id': 'u64', 'ticket_price': 'u128', 'symbol_completed_price': 'u64', 'symbol_fraction': 'u32', 'start': 'u32', 'end': 'u32', 'distribute': 'u32', 'multiplier': [{'Base': 'u8'}], 'deviation': (None, 'u32'), 'range': (None, ['u64']), 'total_reward': 'u128', 'state': ('InActive', 'Active', 'WaitingPayout', 'Completed', 'Unresolved')}```

---------
### ChooseWinner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| record | `ChooseType<T::AccountId>` | ```{'DEVIATION': {'low_price': 'u64', 'high_price': 'u64', 'check_list': [('AccountId', (None, 'u64'))]}, 'RANGE': {'range': ['u64'], 'check_list': [('AccountId', (None, 'u8'))]}}```

---------
### CompletedEstimates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| config | `SymbolEstimatesConfig<T::BlockNumber, BalanceOf<T>>` | ```{'symbol': 'Bytes', 'estimates_type': ('DEVIATION', 'RANGE'), 'id': 'u64', 'ticket_price': 'u128', 'symbol_completed_price': 'u64', 'symbol_fraction': 'u32', 'start': 'u32', 'end': 'u32', 'distribute': 'u32', 'multiplier': [{'Base': 'u8'}], 'deviation': (None, 'u32'), 'range': (None, ['u64']), 'total_reward': 'u128', 'state': ('InActive', 'Active', 'WaitingPayout', 'Completed', 'Unresolved')}```
| winners | `Vec<(T::AccountId, BalanceOf<T>)>` | ```[('AccountId', 'u128')]```

---------
### Deposit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### NewEstimates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| estimate | `SymbolEstimatesConfig<T::BlockNumber, BalanceOf<T>>` | ```{'symbol': 'Bytes', 'estimates_type': ('DEVIATION', 'RANGE'), 'id': 'u64', 'ticket_price': 'u128', 'symbol_completed_price': 'u64', 'symbol_fraction': 'u32', 'start': 'u32', 'end': 'u32', 'distribute': 'u32', 'multiplier': [{'Base': 'u8'}], 'deviation': (None, 'u32'), 'range': (None, ['u64']), 'total_reward': 'u128', 'state': ('InActive', 'Active', 'WaitingPayout', 'Completed', 'Unresolved')}```
| who | `T::AccountId` | ```AccountId```

---------
### ParticipateEstimates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| symbol | `BoundedVec<u8, StringLimit>` | ```Bytes```
| id | `u64` | ```u64```
| estimate | `AccountParticipateEstimates<T::AccountId, T::BlockNumber>` | ```{'account': 'AccountId', 'end': 'u32', 'estimates': (None, 'u64'), 'range_index': (None, 'u8'), 'bsc_address': (None, 'Bytes'), 'multiplier': {'Base': 'u8'}, 'reward': 'u128'}```
| who | `T::AccountId` | ```AccountId```
| estimate_type | `EstimatesType` | ```('DEVIATION', 'RANGE')```
| deposit | `BalanceOf<T>` | ```u128```

---------
### RemovedEstimates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| list | `BoundedVecOfCompletedEstimates::<T::BlockNumber, BalanceOf<T>>` | ```[{'symbol': 'Bytes', 'estimates_type': ('DEVIATION', 'RANGE'), 'id': 'u64', 'ticket_price': 'u128', 'symbol_completed_price': 'u64', 'symbol_fraction': 'u32', 'start': 'u32', 'end': 'u32', 'distribute': 'u32', 'multiplier': ['scale_info::125'], 'deviation': (None, 'u32'), 'range': (None, ['u64']), 'total_reward': 'u128', 'state': ('InActive', 'Active', 'WaitingPayout', 'Completed', 'Unresolved')}]```

---------
### Reserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `[u8; 8]` | ```[u8; 8]```
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ActiveEstimates

#### Python
```python
result = substrate.query(
    'Estimates', 'ActiveEstimates', [('Bytes', ('DEVIATION', 'RANGE'))]
)
```

#### Return value
```python
{
    'deviation': (None, 'u32'),
    'distribute': 'u32',
    'end': 'u32',
    'estimates_type': ('DEVIATION', 'RANGE'),
    'id': 'u64',
    'multiplier': [{'Base': 'u8'}],
    'range': (None, ['u64']),
    'start': 'u32',
    'state': (
        'InActive',
        'Active',
        'WaitingPayout',
        'Completed',
        'Unresolved',
    ),
    'symbol': 'Bytes',
    'symbol_completed_price': 'u64',
    'symbol_fraction': 'u32',
    'ticket_price': 'u128',
    'total_reward': 'u128',
}
```
---------
### ActivePallet

#### Python
```python
result = substrate.query(
    'Estimates', 'ActivePallet', []
)
```

#### Return value
```python
'bool'
```
---------
### Admins
 admin account

#### Python
```python
result = substrate.query(
    'Estimates', 'Admins', []
)
```

#### Return value
```python
['AccountId']
```
---------
### CompletedEstimates

#### Python
```python
result = substrate.query(
    'Estimates', 'CompletedEstimates', [('Bytes', ('DEVIATION', 'RANGE'))]
)
```

#### Return value
```python
[
    {
        'deviation': (None, 'u32'),
        'distribute': 'u32',
        'end': 'u32',
        'estimates_type': ('DEVIATION', 'RANGE'),
        'id': 'u64',
        'multiplier': ['scale_info::125'],
        'range': (None, ['u64']),
        'start': 'u32',
        'state': (
            'InActive',
            'Active',
            'WaitingPayout',
            'Completed',
            'Unresolved',
        ),
        'symbol': 'Bytes',
        'symbol_completed_price': 'u64',
        'symbol_fraction': 'u32',
        'ticket_price': 'u128',
        'total_reward': 'u128',
    },
]
```
---------
### EstimatesInitDeposit

#### Python
```python
result = substrate.query(
    'Estimates', 'EstimatesInitDeposit', [('Bytes', ('DEVIATION', 'RANGE')), 'u64']
)
```

#### Return value
```python
'u128'
```
---------
### LockedEstimates

#### Python
```python
result = substrate.query(
    'Estimates', 'LockedEstimates', []
)
```

#### Return value
```python
'u32'
```
---------
### MinimumInitReward

#### Python
```python
result = substrate.query(
    'Estimates', 'MinimumInitReward', []
)
```

#### Return value
```python
'u128'
```
---------
### MinimumTicketPrice

#### Python
```python
result = substrate.query(
    'Estimates', 'MinimumTicketPrice', []
)
```

#### Return value
```python
'u128'
```
---------
### NextDataCleanUnsignedAt

#### Python
```python
result = substrate.query(
    'Estimates', 'NextDataCleanUnsignedAt', []
)
```

#### Return value
```python
'u32'
```
---------
### Participants

#### Python
```python
result = substrate.query(
    'Estimates', 'Participants', [('Bytes', ('DEVIATION', 'RANGE')), 'u64']
)
```

#### Return value
```python
[
    {
        'account': 'AccountId',
        'bsc_address': (None, 'Bytes'),
        'end': 'u32',
        'estimates': (None, 'u64'),
        'multiplier': {'Base': 'u8'},
        'range_index': (None, 'u8'),
        'reward': 'u128',
    },
]
```
---------
### PreparedEstimates

#### Python
```python
result = substrate.query(
    'Estimates', 'PreparedEstimates', [('Bytes', ('DEVIATION', 'RANGE'))]
)
```

#### Return value
```python
{
    'deviation': (None, 'u32'),
    'distribute': 'u32',
    'end': 'u32',
    'estimates_type': ('DEVIATION', 'RANGE'),
    'id': 'u64',
    'multiplier': [{'Base': 'u8'}],
    'range': (None, ['u64']),
    'start': 'u32',
    'state': (
        'InActive',
        'Active',
        'WaitingPayout',
        'Completed',
        'Unresolved',
    ),
    'symbol': 'Bytes',
    'symbol_completed_price': 'u64',
    'symbol_fraction': 'u32',
    'ticket_price': 'u128',
    'total_reward': 'u128',
}
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'Estimates', 'StorageVersion', []
)
```

#### Return value
```python
('V0', 'V1')
```
---------
### SymbolEstimatesId

#### Python
```python
result = substrate.query(
    'Estimates', 'SymbolEstimatesId', [('Bytes', ('DEVIATION', 'RANGE'))]
)
```

#### Return value
```python
'u64'
```
---------
### UnresolvedEstimates

#### Python
```python
result = substrate.query(
    'Estimates', 'UnresolvedEstimates', [('Bytes', ('DEVIATION', 'RANGE'))]
)
```

#### Return value
```python
{
    'deviation': (None, 'u32'),
    'distribute': 'u32',
    'end': 'u32',
    'estimates_type': ('DEVIATION', 'RANGE'),
    'id': 'u64',
    'multiplier': [{'Base': 'u8'}],
    'range': (None, ['u64']),
    'start': 'u32',
    'state': (
        'InActive',
        'Active',
        'WaitingPayout',
        'Completed',
        'Unresolved',
    ),
    'symbol': 'Bytes',
    'symbol_completed_price': 'u64',
    'symbol_fraction': 'u32',
    'ticket_price': 'u128',
    'total_reward': 'u128',
}
```
---------
### Winners

#### Python
```python
result = substrate.query(
    'Estimates', 'Winners', [('Bytes', ('DEVIATION', 'RANGE')), 'u64']
)
```

#### Return value
```python
[
    {
        'account': 'AccountId',
        'bsc_address': (None, 'Bytes'),
        'end': 'u32',
        'estimates': (None, 'u64'),
        'multiplier': {'Base': 'u8'},
        'range_index': (None, 'u8'),
        'reward': 'u128',
    },
]
```
---------
## Constants

---------
### MaxEndDelay
#### Value
```python
60
```
#### Python
```python
constant = substrate.get_constant('Estimates', 'MaxEndDelay')
```
---------
### MaxEstimatesPerSymbol
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Estimates', 'MaxEstimatesPerSymbol')
```
---------
### MaxQuotationDelay
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('Estimates', 'MaxQuotationDelay')
```
---------
### MaximumKeepLengthOfOldData
#### Value
```python
403200
```
#### Python
```python
constant = substrate.get_constant('Estimates', 'MaximumKeepLengthOfOldData')
```
---------
### PalletId
 The Lottery&#x27;s pallet id
#### Value
```python
'0x70792f6172657374'
```
#### Python
```python
constant = substrate.get_constant('Estimates', 'PalletId')
```
---------
### UnsignedPriority
#### Value
```python
1048576
```
#### Python
```python
constant = substrate.get_constant('Estimates', 'UnsignedPriority')
```
---------
## Errors

---------
### AccountEstimatesExist

---------
### ActiveEstimatesNotExist

---------
### AddressInvalid

---------
### AlreadyEnded

---------
### AlreadyParticipating

---------
### BadMetadata
Invalid metadata given.

---------
### EstimatesConfigInvalid

---------
### EstimatesInitDepositNotExist

---------
### EstimatesStartTooEarly

---------
### EstimatesStateError

---------
### FreeBalanceTooLow

---------
### IllegalCall

---------
### MultiplierNotExist

---------
### NotMember

---------
### PalletInactive

---------
### ParameterInvalid

---------
### PreparedEstimatesExist

---------
### PriceInvalid

---------
### SubAccountGenerateFailed

---------
### SymbolNotSupported

---------
### TooMany

---------
### TooManyEstimates

---------
### TooOften

---------
### UnableToGetPrice

---------
### UnresolvedEstimatesNotExist

---------