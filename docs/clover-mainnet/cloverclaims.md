
# CloverClaims

---------
## Calls

---------
### burn_elastic
#### Attributes
| Name | Type |
| -------- | -------- | 
| network | `BridgeNetworks` | 
| dest | `EthereumAddress` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CloverClaims', 'burn_elastic', {
    'amount': 'u128',
    'dest': '[u8; 20]',
    'network': (
        'BSC',
        'Ethereum',
        'CloverPara',
    ),
}
)
```

---------
### claim_elastic
#### Attributes
| Name | Type |
| -------- | -------- | 
| network | `BridgeNetworks` | 
| dest | `T::AccountId` | 
| tx | `EthereumTxHash` | 
| sig | `EcdsaSignature` | 

#### Python
```python
call = substrate.compose_call(
    'CloverClaims', 'claim_elastic', {
    'dest': 'AccountId',
    'network': (
        'BSC',
        'Ethereum',
        'CloverPara',
    ),
    'sig': '[u8; 65]',
    'tx': '[u8; 32]',
}
)
```

---------
### mint_and_send_claim_elastic
bridge between two clover like chains
#### Attributes
| Name | Type |
| -------- | -------- | 
| network | `BridgeNetworks` | 
| tx | `EthereumTxHash` | 
| who | `T::AccountId` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CloverClaims', 'mint_and_send_claim_elastic', {
    'network': (
        'BSC',
        'Ethereum',
        'CloverPara',
    ),
    'tx': '[u8; 32]',
    'value': 'u128',
    'who': 'AccountId',
}
)
```

---------
### mint_claim_elastic
#### Attributes
| Name | Type |
| -------- | -------- | 
| network | `BridgeNetworks` | 
| tx | `EthereumTxHash` | 
| who | `EthereumAddress` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CloverClaims', 'mint_claim_elastic', {
    'network': (
        'BSC',
        'Ethereum',
        'CloverPara',
    ),
    'tx': '[u8; 32]',
    'value': 'u128',
    'who': '[u8; 20]',
}
)
```

---------
### set_bridge_account_elastic
update the bridge account for the target network
#### Attributes
| Name | Type |
| -------- | -------- | 
| network | `BridgeNetworks` | 
| to | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CloverClaims', 'set_bridge_account_elastic', {
    'network': (
        'BSC',
        'Ethereum',
        'CloverPara',
    ),
    'to': 'AccountId',
}
)
```

---------
### set_bridge_fee_elastic
#### Attributes
| Name | Type |
| -------- | -------- | 
| network | `BridgeNetworks` | 
| mint_fee | `BalanceOf<T>` | 
| burn_fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CloverClaims', 'set_bridge_fee_elastic', {
    'burn_fee': 'u128',
    'mint_fee': 'u128',
    'network': (
        'BSC',
        'Ethereum',
        'CloverPara',
    ),
}
)
```

---------
### set_claim_limit_elastic
#### Attributes
| Name | Type |
| -------- | -------- | 
| network | `BridgeNetworks` | 
| limit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CloverClaims', 'set_claim_limit_elastic', {
    'limit': 'u128',
    'network': (
        'BSC',
        'Ethereum',
        'CloverPara',
    ),
}
)
```

---------
## Events

---------
### BridgeAccountChanged
Bridge Account Changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### BurnFeeUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### Burned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### ClaimLimitUpdated
claim limit updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### Claimed
CLV claimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### ElasticBridgeAccountChanged
Elastic bridge account changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeNetworks` | ```('BSC', 'Ethereum', 'CloverPara')```
| None | `T::AccountId` | ```AccountId```

---------
### ElasticBurned
burned some balance and will bridge to specified network
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeNetworks` | ```('BSC', 'Ethereum', 'CloverPara')```
| None | `T::AccountId` | ```AccountId```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### ElasticClaimLimitUpdated
Elastic claim limit updated for network
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeNetworks` | ```('BSC', 'Ethereum', 'CloverPara')```
| None | `BalanceOf<T>` | ```u128```

---------
### ElasticClaimed
CLV claimed for network
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeNetworks` | ```('BSC', 'Ethereum', 'CloverPara')```
| None | `T::AccountId` | ```AccountId```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### ElasticFeeUpdated
elastic fee updated event, (network, mint fee, burn fee)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeNetworks` | ```('BSC', 'Ethereum', 'CloverPara')```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### ElasticMintSuccess
Elastic mint claim successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeNetworks` | ```('BSC', 'Ethereum', 'CloverPara')```
| None | `EthereumTxHash` | ```[u8; 32]```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### MintFeeUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### MintSuccess
Mint claims successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EthereumTxHash` | ```[u8; 32]```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### BridgeAccount

#### Python
```python
result = substrate.query(
    'CloverClaims', 'BridgeAccount', []
)
```

#### Return value
```python
(None, 'AccountId')
```
---------
### BridgeFees

#### Python
```python
result = substrate.query(
    'CloverClaims', 'BridgeFees', [('BSC', 'Ethereum', 'CloverPara')]
)
```

#### Return value
```python
('u128', 'u128')
```
---------
### BurnFee

#### Python
```python
result = substrate.query(
    'CloverClaims', 'BurnFee', []
)
```

#### Return value
```python
(None, 'u128')
```
---------
### ClaimLimit

#### Python
```python
result = substrate.query(
    'CloverClaims', 'ClaimLimit', []
)
```

#### Return value
```python
'u128'
```
---------
### Claims

#### Python
```python
result = substrate.query(
    'CloverClaims', 'Claims', ['[u8; 32]']
)
```

#### Return value
```python
(None, ('[u8; 20]', 'u128', 'bool'))
```
---------
### ElasticBridgeAccounts
 bridge account to mint bridge transactions
 it&#x27;s a good practice to configure a separate bridge account for one bridge network

#### Python
```python
result = substrate.query(
    'CloverClaims', 'ElasticBridgeAccounts', [('BSC', 'Ethereum', 'CloverPara')]
)
```

#### Return value
```python
(None, 'AccountId')
```
---------
### ElasticClaimLimits

#### Python
```python
result = substrate.query(
    'CloverClaims', 'ElasticClaimLimits', [('BSC', 'Ethereum', 'CloverPara')]
)
```

#### Return value
```python
'u128'
```
---------
### ElasticClaims
 claims that supports multiple ethereum compatible chains

#### Python
```python
result = substrate.query(
    'CloverClaims', 'ElasticClaims', [('BSC', 'Ethereum', 'CloverPara'), '[u8; 32]']
)
```

#### Return value
```python
('[u8; 20]', 'u128', 'bool')
```
---------
### MintFee

#### Python
```python
result = substrate.query(
    'CloverClaims', 'MintFee', []
)
```

#### Return value
```python
(None, 'u128')
```
---------
### PalletStorageVersion

#### Python
```python
result = substrate.query(
    'CloverClaims', 'PalletStorageVersion', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x636c76636c61696d'
```
#### Python
```python
constant = substrate.get_constant('CloverClaims', 'PalletId')
```
---------
## Errors

---------
### AlreadyClaimed

---------
### AlreadyMinted

---------
### ClaimLimitExceeded

---------
### InvalidAmount

---------
### InvalidEthereumSignature

---------
### NoPermission

---------
### SignatureNotMatch

---------
### TxNotMinted

---------