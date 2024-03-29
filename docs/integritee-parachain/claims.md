
# Claims

---------
## Calls

---------
### attest
See [`Pallet::attest`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| statement | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'attest', {'statement': 'Bytes'}
)
```

---------
### claim
See [`Pallet::claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `T::AccountId` | 
| ethereum_signature | `EcdsaSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'claim', {
    'dest': 'AccountId',
    'ethereum_signature': '[u8; 65]',
}
)
```

---------
### claim_attest
See [`Pallet::claim_attest`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `T::AccountId` | 
| ethereum_signature | `EcdsaSignature` | 
| statement | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'claim_attest', {
    'dest': 'AccountId',
    'ethereum_signature': '[u8; 65]',
    'statement': 'Bytes',
}
)
```

---------
### mint_claim
See [`Pallet::mint_claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `EthereumAddress` | 
| value | `BalanceOf<T>` | 
| vesting_schedule | `Option<(BalanceOf<T>, BalanceOf<T>, BlockNumberFor<T>)>` | 
| statement | `Option<StatementKind>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'mint_claim', {
    'statement': (
        None,
        ('Regular', 'Saft'),
    ),
    'value': 'u128',
    'vesting_schedule': (
        None,
        ('u128', 'u128', 'u32'),
    ),
    'who': '[u8; 20]',
}
)
```

---------
### move_claim
See [`Pallet::move_claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| old | `EthereumAddress` | 
| new | `EthereumAddress` | 
| maybe_preclaim | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'move_claim', {
    'maybe_preclaim': (
        None,
        'AccountId',
    ),
    'new': '[u8; 20]',
    'old': '[u8; 20]',
}
)
```

---------
## Events

---------
### Claimed
Someone claimed some TEERs. `[who, ethereum_address, amount]`
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
### Preclaims
 Pre-claimed Ethereum accounts, by the Account ID that they are claimed to.

#### Python
```python
result = substrate.query(
    'Claims', 'Preclaims', ['AccountId']
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### Signing
 The statement kind that must be signed, if any.

#### Python
```python
result = substrate.query(
    'Claims', 'Signing', ['[u8; 20]']
)
```

#### Return value
```python
('Regular', 'Saft')
```
---------
### Total

#### Python
```python
result = substrate.query(
    'Claims', 'Total', []
)
```

#### Return value
```python
'u128'
```
---------
### Vesting
 Vesting schedule for a claim.
 First balance is the total amount that should be held for vesting.
 Second balance is how much should be unlocked per block.
 The block number is when the vesting should start.

#### Python
```python
result = substrate.query(
    'Claims', 'Vesting', ['[u8; 20]']
)
```

#### Return value
```python
('u128', 'u128', 'u32')
```
---------
## Constants

---------
### Prefix
#### Value
```python
'Pay TEERs to the integriTEE account:'
```
#### Python
```python
constant = substrate.get_constant('Claims', 'Prefix')
```
---------
## Errors

---------
### InvalidEthereumSignature
Invalid Ethereum signature.

---------
### InvalidStatement
A needed statement was not included.

---------
### PotUnderflow
There&\#x27;s not enough in the pot to pay out some unvested amount. Generally implies a logic
error.

---------
### SenderHasNoClaim
Account ID sending transaction has no claim.

---------
### SignerHasNoClaim
Ethereum address has no claim.

---------
### VestedBalanceExists
The account already has a vested balance.

---------