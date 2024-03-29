
# Claims

---------
## Calls

---------
### attest
Attest to a statement, needed to finalize the claims process.

Unsigned Validation:
A call to attest is deemed valid if the sender has a `Preclaim` registered
and provides a `statement` which is expected for the account.

Parameters:
- `statement`: The identity of the statement which is being attested to in the signature.
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
Make a claim to collect your currency.

The dispatch origin for this call must be _None_.

Unsigned Validation:
A call to claim is deemed valid if the signature provided matches
the expected signed message of:

&gt; Ethereum Signed Message:
&gt; (configured prefix string)(address)

and `address` matches the `dest` account.

Parameters:
- `dest`: The destination account to payout the claim.
- `ethereum_signature`: The signature of an ethereum signed message
   matching the format described above.
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
Make a claim to collect your currency by signing a statement.

The dispatch origin for this call must be _None_.

Unsigned Validation:
A call to `claim_attest` is deemed valid if the signature provided matches
the expected signed message of:

&gt; Ethereum Signed Message:
&gt; (configured prefix string)(address)(statement)

and `address` matches the `dest` account; the `statement` must match that which is
expected according to your purchase arrangement.

Parameters:
- `dest`: The destination account to payout the claim.
- `ethereum_signature`: The signature of an ethereum signed message
   matching the format described above.
- `statement`: The identity of the statement which is being attested to in the signature.
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
Mint a new claim to collect currency

The dispatch origin for this call must be _Root_.

Parameters:
- `who`: The Ethereum address allowed to collect this claim.
- `value`: The balance that will be claimed.
- `vesting_schedule`: An optional vesting schedule for the claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `EthereumAddress` | 
| value | `T::Balance` | 
| vesting_schedule | `Option<(T::Balance, T::Balance, T::BlockNumber)>` | 
| statement | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'mint_claim', {
    'statement': 'bool',
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
Gives claims ownership from `old` to `new`
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
`AccountId` claimed `Balance` amount of currency reserved for `EthereumAddress`
\[who, ethereum_account, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EthereumAddress` | ```[u8; 20]```
| None | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Claims
 Pallet storage - stores amount to be claimed by each `EthereumAddress`

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
 Pallet storage - pre-claimed Ethereum accounts, by the Account ID that
 they are claimed to

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
 Pallet storage - stores Ethereum addresses from which additional statement
 singing is required

#### Python
```python
result = substrate.query(
    'Claims', 'Signing', ['[u8; 20]']
)
```

#### Return value
```python
'bool'
```
---------
### Total
 Pallet storage - total `Claims` amount

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
 Pallet storage - vesting schedule for a claim.
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
## Errors

---------
### InvalidEthereumSignature
Invalid Ethereum signature

---------
### InvalidReceiver
Invalid receiver

---------
### InvalidStatement
A needed statement was not included.

---------
### MethodNotAllowed
This method is not allowed in production

---------
### PotUnderflow
There&\#x27;s not enough in the pot to pay out some unvested amount. Generally
implies a logic error

---------
### SenderHasNoClaim
Account sending transaction has no claim

---------
### SignerHasNoClaim
Ethereum address has no claim

---------
### VestedBalanceExists
The account already has a vested balance

---------