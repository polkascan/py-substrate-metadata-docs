
# BridgeTransfer

---------
## Calls

---------
### set_external_balances
#### Attributes
| Name | Type |
| -------- | -------- | 
| external_balances | `bridge::BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeTransfer', 'set_external_balances', {'external_balances': 'u128'}
)
```

---------
### set_maximum_issuance
#### Attributes
| Name | Type |
| -------- | -------- | 
| maximum_issuance | `bridge::BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeTransfer', 'set_maximum_issuance', {'maximum_issuance': 'u128'}
)
```

---------
### transfer
Executes a simple currency transfer using the bridge account as the source
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| amount | `bridge::BalanceOf<T>` | 
| rid | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeTransfer', 'transfer', {
    'amount': 'u128',
    'rid': '[u8; 32]',
    'to': 'AccountId',
}
)
```

---------
### transfer_native
Transfers some amount of the native token to some recipient on a (whitelisted)
destination chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `bridge::BalanceOf<T>` | 
| recipient | `Vec<u8>` | 
| dest_id | `bridge::BridgeChainId` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeTransfer', 'transfer_native', {
    'amount': 'u128',
    'dest_id': 'u8',
    'recipient': 'Bytes',
}
)
```

---------
## Events

---------
### MaximumIssuanceChanged
MaximumIssuance was changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_value | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### BridgeBalances

#### Python
```python
result = substrate.query(
    'BridgeTransfer', 'BridgeBalances', ['[u8; 32]', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### ExternalBalances

#### Python
```python
result = substrate.query(
    'BridgeTransfer', 'ExternalBalances', []
)
```

#### Return value
```python
'u128'
```
---------
### MaximumIssuance

#### Python
```python
result = substrate.query(
    'BridgeTransfer', 'MaximumIssuance', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### DefaultMaximumIssuance
#### Value
```python
80000000000000000000
```
#### Python
```python
constant = substrate.get_constant('BridgeTransfer', 'DefaultMaximumIssuance')
```
---------
### ExternalTotalIssuance
#### Value
```python
100000000000000000000
```
#### Python
```python
constant = substrate.get_constant('BridgeTransfer', 'ExternalTotalIssuance')
```
---------
### NativeTokenResourceId
#### Value
```python
'0x00000000000000000000000000000063a7e2be78898ba83824b0c0cc8dfb6001'
```
#### Python
```python
constant = substrate.get_constant('BridgeTransfer', 'NativeTokenResourceId')
```
---------
## Errors

---------
### InvalidCommand

---------
### InvalidResourceId

---------
### OverFlow

---------
### ReachMaximumSupply

---------