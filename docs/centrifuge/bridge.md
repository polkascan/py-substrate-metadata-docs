
# Bridge

---------
## Calls

---------
### remark
This can be called by the chainbridge to demonstrate an arbitrary
call from a proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `<T as frame_system::Config>::Hash` | 
| r_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'remark', {
    'hash': '[u8; 32]',
    'r_id': '[u8; 32]',
}
)
```

---------
### transfer
Executes a simple currency transfer using the chainbridge account as
the source
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `<T as frame_system::Config>::AccountId` | 
| amount | `BalanceOf<T>` | 
| r_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'transfer', {
    'amount': 'u128',
    'r_id': '[u8; 32]',
    'to': 'AccountId',
}
)
```

---------
### transfer_native
Transfers some amount of the native token to some recipient on a
(whitelisted) destination chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| recipient | `Vec<u8>` | 
| dest_id | `ChainId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'transfer_native', {
    'amount': 'u128',
    'dest_id': 'u8',
    'recipient': 'Bytes',
}
)
```

---------
## Events

---------
### Remark
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as frame_system::Config>::Hash` | ```[u8; 32]```
| None | `ResourceId` | ```[u8; 32]```

---------
## Constants

---------
### BridgePalletId
 Pallet identifier.

 The module identifier may be of the form
 ```PalletId(*b&quot;c/bridge&quot;)``` (a string of eight characters) and set using the [`parameter_types`](https://substrate.dev/docs/en/knowledgebase/runtime/macros\#parameter_types)
 macro in one of the runtimes (see runtime folder).
#### Value
```python
'0x63686e6272646765'
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'BridgePalletId')
```
---------
### NativeTokenId
#### Value
```python
'0x000000000000000000000000000000330324dbcad5cd41be14952877e636a101'
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'NativeTokenId')
```
---------
### NativeTokenTransferFeeKey
 Key used to retrieve the fee that are charged when transferring
 native tokens to target chains.
#### Value
```python
'BridgeNativeTransfer'
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'NativeTokenTransferFeeKey')
```
---------
## Errors

---------
### InvalidTransfer
Invalid transfer

---------