
# ManualBridge

---------
## Calls

---------
### set_up_completed_list
#### Attributes
| Name | Type |
| -------- | -------- | 
| sender | `T::AccountId` | 
| list | `CrossChainInfoList<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ManualBridge', 'set_up_completed_list', {
    'list': [
        {
            'amount': 'u128',
            'iden': 'Bytes',
            'kind': {
                'BSC': '[u8; 20]',
                'ETH': '[u8; 20]',
            },
        },
    ],
    'sender': 'AccountId',
}
)
```

---------
### transfer_to
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain_kind | `CrossChainKind` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ManualBridge', 'transfer_to', {
    'amount': 'u128',
    'chain_kind': {
        'BSC': '[u8; 20]',
        'ETH': '[u8; 20]',
    },
}
)
```

---------
### update_minimum_balance_threshold
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ManualBridge', 'update_minimum_balance_threshold', {'amount': 'u128'}
)
```

---------
### update_stash
#### Attributes
| Name | Type |
| -------- | -------- | 
| stash | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ManualBridge', 'update_stash', {'stash': 'AccountId'}
)
```

---------
### update_waiter
#### Attributes
| Name | Type |
| -------- | -------- | 
| waiter | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ManualBridge', 'update_waiter', {'waiter': 'AccountId'}
)
```

---------
## Events

---------
### CompletedList
Completed cross-chain requests
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CrossChainInfoList<T>` | ```[{'iden': 'Bytes', 'kind': {'ETH': '[u8; 20]', 'BSC': '[u8; 20]'}, 'amount': 'u128'}]```

---------
### CrossChainRequest
Generate cross-connection requests
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| acc | `T::AccountId` | ```AccountId```
| ident | `Ident` | ```Bytes```
| kind | `CrossChainKind` | ```{'ETH': '[u8; 20]', 'BSC': '[u8; 20]'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### MinimumBalanceThresholdUpdated
When the MinimumBalanceThreshold is updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `BalanceOf<T>` | ```u128```

---------
### StashUpdated
When the waiter account is updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| acc | `T::AccountId` | ```AccountId```

---------
### WaiterUpdated
When the waiter account is updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| acc | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### MinimumBalanceThreshold

#### Python
```python
result = substrate.query(
    'ManualBridge', 'MinimumBalanceThreshold', []
)
```

#### Return value
```python
'u128'
```
---------
### PendingList

#### Python
```python
result = substrate.query(
    'ManualBridge', 'PendingList', ['AccountId']
)
```

#### Return value
```python
[
    {
        'amount': 'u128',
        'iden': 'Bytes',
        'kind': {'BSC': '[u8; 20]', 'ETH': '[u8; 20]'},
    },
]
```
---------
### StashAccout

#### Python
```python
result = substrate.query(
    'ManualBridge', 'StashAccout', []
)
```

#### Return value
```python
'AccountId'
```
---------
### WaiterAccout

#### Python
```python
result = substrate.query(
    'ManualBridge', 'WaiterAccout', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Errors

---------
### CompletedListDataCannotAllMatch
The list data to be completed must all match, otherwise the completion operation cannot be performed.

---------
### IllegalAddress


---------
### MinimumBalanceThresholdNotSet
You need to set the MinimumBalanceThreshold parameter through sudo or committee.

---------
### NoPendingList
Pending list is empty

---------
### NoPermission
No permission

---------
### StashDoesNotExists
Stash does not exist, module has not completed initialization.

---------
### StorageOverflow


---------
### TransferAmountIsTooSmall
The transfer amount must be greater than the threshold requirement.

---------
### WaiterDoesNotExists
Waiter does not exist, module has not completed initialization.

---------