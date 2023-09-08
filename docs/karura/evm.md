
# EVM

---------
## Calls

---------
### call
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `EvmAddress` | 
| input | `Vec<u8>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_limit | `u32` | 
| access_list | `Vec<AccessListItem>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'call', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'gas_limit': 'u64',
    'input': 'Bytes',
    'storage_limit': 'u32',
    'target': '[u8; 20]',
    'value': 'u128',
}
)
```

---------
### create
#### Attributes
| Name | Type |
| -------- | -------- | 
| input | `Vec<u8>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_limit | `u32` | 
| access_list | `Vec<AccessListItem>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'create', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'gas_limit': 'u64',
    'input': 'Bytes',
    'storage_limit': 'u32',
    'value': 'u128',
}
)
```

---------
### create2
#### Attributes
| Name | Type |
| -------- | -------- | 
| input | `Vec<u8>` | 
| salt | `H256` | 
| value | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_limit | `u32` | 
| access_list | `Vec<AccessListItem>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'create2', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'gas_limit': 'u64',
    'input': 'Bytes',
    'salt': '[u8; 32]',
    'storage_limit': 'u32',
    'value': 'u128',
}
)
```

---------
### create_nft_contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| input | `Vec<u8>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_limit | `u32` | 
| access_list | `Vec<AccessListItem>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'create_nft_contract', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'gas_limit': 'u64',
    'input': 'Bytes',
    'storage_limit': 'u32',
    'value': 'u128',
}
)
```

---------
### create_predeploy_contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `EvmAddress` | 
| input | `Vec<u8>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_limit | `u32` | 
| access_list | `Vec<AccessListItem>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'create_predeploy_contract', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'gas_limit': 'u64',
    'input': 'Bytes',
    'storage_limit': 'u32',
    'target': '[u8; 20]',
    'value': 'u128',
}
)
```

---------
### disable_contract_development
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EVM', 'disable_contract_development', {}
)
```

---------
### enable_contract_development
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EVM', 'enable_contract_development', {}
)
```

---------
### eth_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| action | `TransactionAction` | 
| input | `Vec<u8>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_limit | `u32` | 
| access_list | `Vec<AccessListItem>` | 
| valid_until | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'eth_call', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'action': {
        'Call': '[u8; 20]',
        'Create': None,
    },
    'gas_limit': 'u64',
    'input': 'Bytes',
    'storage_limit': 'u32',
    'valid_until': 'u32',
    'value': 'u128',
}
)
```

---------
### eth_call_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| action | `TransactionAction` | 
| input | `Vec<u8>` | 
| value | `BalanceOf<T>` | 
| gas_price | `u64` | 
| gas_limit | `u64` | 
| access_list | `Vec<AccessListItem>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'eth_call_v2', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'action': {
        'Call': '[u8; 20]',
        'Create': None,
    },
    'gas_limit': 'u64',
    'gas_price': 'u64',
    'input': 'Bytes',
    'value': 'u128',
}
)
```

---------
### publish_contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'publish_contract', {'contract': '[u8; 20]'}
)
```

---------
### publish_free
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'publish_free', {'contract': '[u8; 20]'}
)
```

---------
### scheduled_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `EvmAddress` | 
| target | `EvmAddress` | 
| input | `Vec<u8>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_limit | `u32` | 
| access_list | `Vec<AccessListItem>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'scheduled_call', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'from': '[u8; 20]',
    'gas_limit': 'u64',
    'input': 'Bytes',
    'storage_limit': 'u32',
    'target': '[u8; 20]',
    'value': 'u128',
}
)
```

---------
### selfdestruct
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'selfdestruct', {'contract': '[u8; 20]'}
)
```

---------
### set_code
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `EvmAddress` | 
| code | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'set_code', {
    'code': 'Bytes',
    'contract': '[u8; 20]',
}
)
```

---------
### strict_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `EvmAddress` | 
| input | `Vec<u8>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_limit | `u32` | 
| access_list | `Vec<AccessListItem>` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'strict_call', {
    'access_list': [
        {
            'address': '[u8; 20]',
            'storage_keys': [
                '[u8; 32]',
            ],
        },
    ],
    'gas_limit': 'u64',
    'input': 'Bytes',
    'storage_limit': 'u32',
    'target': '[u8; 20]',
    'value': 'u128',
}
)
```

---------
### transfer_maintainer
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `EvmAddress` | 
| new_maintainer | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'EVM', 'transfer_maintainer', {
    'contract': '[u8; 20]',
    'new_maintainer': '[u8; 20]',
}
)
```

---------
## Events

---------
### ContractDevelopmentDisabled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### ContractDevelopmentEnabled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### ContractPublished
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `EvmAddress` | ```[u8; 20]```

---------
### ContractSelfdestructed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `EvmAddress` | ```[u8; 20]```

---------
### ContractSetCode
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `EvmAddress` | ```[u8; 20]```

---------
### Created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `EvmAddress` | ```[u8; 20]```
| contract | `EvmAddress` | ```[u8; 20]```
| logs | `Vec<Log>` | ```[{'address': '[u8; 20]', 'topics': ['[u8; 32]'], 'data': 'Bytes'}]```
| used_gas | `u64` | ```u64```
| used_storage | `i32` | ```i32```

---------
### CreatedFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `EvmAddress` | ```[u8; 20]```
| contract | `EvmAddress` | ```[u8; 20]```
| exit_reason | `ExitReason` | ```{'Succeed': ('Stopped', 'Returned', 'Suicided'), 'Error': {'StackUnderflow': None, 'StackOverflow': None, 'InvalidJump': None, 'InvalidRange': None, 'DesignatedInvalid': None, 'CallTooDeep': None, 'CreateCollision': None, 'CreateContractLimit': None, 'OutOfOffset': None, 'OutOfGas': None, 'OutOfFund': None, 'PCUnderflow': None, 'CreateEmpty': None, 'Other': 'Str', None: None, 'InvalidCode': 'u8'}, 'Revert': ('Reverted',), 'Fatal': {'NotSupported': None, 'UnhandledInterrupt': None, 'CallErrorAsFatal': {'StackUnderflow': None, 'StackOverflow': None, 'InvalidJump': None, 'InvalidRange': None, 'DesignatedInvalid': None, 'CallTooDeep': None, 'CreateCollision': None, 'CreateContractLimit': None, 'OutOfOffset': None, 'OutOfGas': None, 'OutOfFund': None, 'PCUnderflow': None, 'CreateEmpty': None, 'Other': 'Str', None: None, 'InvalidCode': 'u8'}, 'Other': 'Str'}}```
| logs | `Vec<Log>` | ```[{'address': '[u8; 20]', 'topics': ['[u8; 32]'], 'data': 'Bytes'}]```
| used_gas | `u64` | ```u64```
| used_storage | `i32` | ```i32```

---------
### Executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `EvmAddress` | ```[u8; 20]```
| contract | `EvmAddress` | ```[u8; 20]```
| logs | `Vec<Log>` | ```[{'address': '[u8; 20]', 'topics': ['[u8; 32]'], 'data': 'Bytes'}]```
| used_gas | `u64` | ```u64```
| used_storage | `i32` | ```i32```

---------
### ExecutedFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `EvmAddress` | ```[u8; 20]```
| contract | `EvmAddress` | ```[u8; 20]```
| exit_reason | `ExitReason` | ```{'Succeed': ('Stopped', 'Returned', 'Suicided'), 'Error': {'StackUnderflow': None, 'StackOverflow': None, 'InvalidJump': None, 'InvalidRange': None, 'DesignatedInvalid': None, 'CallTooDeep': None, 'CreateCollision': None, 'CreateContractLimit': None, 'OutOfOffset': None, 'OutOfGas': None, 'OutOfFund': None, 'PCUnderflow': None, 'CreateEmpty': None, 'Other': 'Str', None: None, 'InvalidCode': 'u8'}, 'Revert': ('Reverted',), 'Fatal': {'NotSupported': None, 'UnhandledInterrupt': None, 'CallErrorAsFatal': {'StackUnderflow': None, 'StackOverflow': None, 'InvalidJump': None, 'InvalidRange': None, 'DesignatedInvalid': None, 'CallTooDeep': None, 'CreateCollision': None, 'CreateContractLimit': None, 'OutOfOffset': None, 'OutOfGas': None, 'OutOfFund': None, 'PCUnderflow': None, 'CreateEmpty': None, 'Other': 'Str', None: None, 'InvalidCode': 'u8'}, 'Other': 'Str'}}```
| output | `Vec<u8>` | ```Bytes```
| logs | `Vec<Log>` | ```[{'address': '[u8; 20]', 'topics': ['[u8; 32]'], 'data': 'Bytes'}]```
| used_gas | `u64` | ```u64```
| used_storage | `i32` | ```i32```

---------
### TransferredMaintainer
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `EvmAddress` | ```[u8; 20]```
| new_maintainer | `EvmAddress` | ```[u8; 20]```

---------
## Storage functions

---------
### AccountStorages

#### Python
```python
result = substrate.query(
    'EVM', 'AccountStorages', ['[u8; 20]', '[u8; 32]']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### Accounts

#### Python
```python
result = substrate.query(
    'EVM', 'Accounts', ['[u8; 20]']
)
```

#### Return value
```python
{
    'contract_info': (
        None,
        {
            'code_hash': '[u8; 32]',
            'maintainer': '[u8; 20]',
            'published': 'bool',
        },
    ),
    'nonce': 'u32',
}
```
---------
### ChainId

#### Python
```python
result = substrate.query(
    'EVM', 'ChainId', []
)
```

#### Return value
```python
'u64'
```
---------
### CodeInfos

#### Python
```python
result = substrate.query(
    'EVM', 'CodeInfos', ['[u8; 32]']
)
```

#### Return value
```python
{'code_size': 'u32', 'ref_count': 'u32'}
```
---------
### Codes

#### Python
```python
result = substrate.query(
    'EVM', 'Codes', ['[u8; 32]']
)
```

#### Return value
```python
'Bytes'
```
---------
### ContractStorageSizes

#### Python
```python
result = substrate.query(
    'EVM', 'ContractStorageSizes', ['[u8; 20]']
)
```

#### Return value
```python
'u32'
```
---------
### ExtrinsicOrigin

#### Python
```python
result = substrate.query(
    'EVM', 'ExtrinsicOrigin', []
)
```

#### Return value
```python
'AccountId'
```
---------
### NetworkContractIndex

#### Python
```python
result = substrate.query(
    'EVM', 'NetworkContractIndex', []
)
```

#### Return value
```python
'u64'
```
---------
### XcmOrigin

#### Python
```python
result = substrate.query(
    'EVM', 'XcmOrigin', []
)
```

#### Return value
```python
['AccountId']
```
---------
## Constants

---------
### DeveloperDeposit
#### Value
```python
50000000000000
```
#### Python
```python
constant = substrate.get_constant('EVM', 'DeveloperDeposit')
```
---------
### NetworkContractSource
#### Value
```python
'0x0000000000000000000000000000000000000000'
```
#### Python
```python
constant = substrate.get_constant('EVM', 'NetworkContractSource')
```
---------
### NewContractExtraBytes
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('EVM', 'NewContractExtraBytes')
```
---------
### PublicationFee
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('EVM', 'PublicationFee')
```
---------
### StorageDepositPerByte
#### Value
```python
100000000000000
```
#### Python
```python
constant = substrate.get_constant('EVM', 'StorageDepositPerByte')
```
---------
### TreasuryAccount
#### Value
```python
'qmmNufxeWaAVLMER2va1v4w2HbuU683c5gGtuxQG4fKTZSb'
```
#### Python
```python
constant = substrate.get_constant('EVM', 'TreasuryAccount')
```
---------
### TxFeePerGas
#### Value
```python
199999946752
```
#### Python
```python
constant = substrate.get_constant('EVM', 'TxFeePerGas')
```
---------
## Errors

---------
### AddressNotMapped

---------
### CannotKillContract

---------
### ChargeFeeFailed

---------
### ChargeStorageFailed

---------
### ContractAlreadyExisted

---------
### ContractAlreadyPublished

---------
### ContractDevelopmentAlreadyEnabled

---------
### ContractDevelopmentNotEnabled

---------
### ContractExceedsMaxCodeSize

---------
### ContractNotFound

---------
### InvalidDecimals

---------
### NoPermission

---------
### OutOfStorage

---------
### ReserveStorageFailed

---------
### StrictCallFailed

---------
### UnreserveStorageFailed

---------