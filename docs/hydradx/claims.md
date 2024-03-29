
# Claims

---------
## Calls

---------
### claim
See [`Pallet::claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| ethereum_signature | `EcdsaSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'claim', {'ethereum_signature': '[u8; 65]'}
)
```

---------
## Events

---------
### Claim
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Claims
 Asset id storage for each shared token

#### Python
```python
result = substrate.query(
    'Claims', 'Claims', ['[u8; 20]']
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### BalanceOverflow
Value reached maximum and cannot be incremented further

---------
### InvalidEthereumSignature
Ethereum signature is not valid

---------
### NoClaimOrAlreadyClaimed
Claim is not valid

---------