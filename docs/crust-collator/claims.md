
# Claims

---------
## Calls

---------
### change_miner
See [`Pallet::change_miner`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_miner | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'change_miner', {
    'new_miner': {
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
### change_superior
See [`Pallet::change_superior`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_superior | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'change_superior', {
    'new_superior': {
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
### claim
See [`Pallet::claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `T::AccountId` | 
| tx | `EthereumTxHash` | 
| sig | `EcdsaSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'claim', {
    'dest': 'AccountId',
    'sig': '[u8; 65]',
    'tx': '[u8; 32]',
}
)
```

---------
### mint_claim
See [`Pallet::mint_claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| tx | `EthereumTxHash` | 
| who | `EthereumAddress` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'mint_claim', {
    'tx': '[u8; 32]',
    'value': 'u128',
    'who': '[u8; 20]',
}
)
```

---------
### set_claim_limit
See [`Pallet::set_claim_limit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'set_claim_limit', {'limit': 'u128'}
)
```

---------
## Events

---------
### BondEthSuccess
Ethereum address was bonded to account. [who, ethereum_address]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EthereumAddress` | ```[u8; 20]```

---------
### Claimed
Someone claimed some CRUs. [who, ethereum_address, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### InitPot
Init pot success
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### MinerChanged
Someone be the new miner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

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
### SetLimitSuccess
Set limit successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### SuperiorChanged
Someone be the new superior
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### ClaimLimit

#### Python
```python
result = substrate.query(
    'Claims', 'ClaimLimit', []
)
```

#### Return value
```python
'u128'
```
---------
### Claimed

#### Python
```python
result = substrate.query(
    'Claims', 'Claimed', ['[u8; 32]']
)
```

#### Return value
```python
'bool'
```
---------
### Claims

#### Python
```python
result = substrate.query(
    'Claims', 'Claims', ['[u8; 32]']
)
```

#### Return value
```python
('[u8; 20]', 'u128')
```
---------
### Miner

#### Python
```python
result = substrate.query(
    'Claims', 'Miner', []
)
```

#### Return value
```python
'AccountId'
```
---------
### Superior

#### Python
```python
result = substrate.query(
    'Claims', 'Superior', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### PalletId
 The claim&#x27;s module id, used for deriving its sovereign account ID.
#### Value
```python
'0x6372636c61696d73'
```
#### Python
```python
constant = substrate.get_constant('Claims', 'PalletId')
```
---------
### Prefix
 The constant used for ethereum signature.
#### Value
```python
'Pay CSMs to the Crust Shadow account:'
```
#### Python
```python
constant = substrate.get_constant('Claims', 'Prefix')
```
---------
## Errors

---------
### AlreadyBeClaimed
Ethereum tx already be claimed

---------
### AlreadyBeMint
Ethereum tx already be mint

---------
### ExceedClaimLimit
Exceed claim limitation

---------
### IllegalMiner
Miner should be the registered

---------
### IllegalSuperior
Superior not exist, should set it first

---------
### InvalidEthereumSignature
Invalid Ethereum signature.

---------
### MinerNotExist
Miner is not exist, should set it first

---------
### SignatureNotMatch
Sign not match

---------
### SignerHasNoClaim
Ethereum address has no claims.

---------