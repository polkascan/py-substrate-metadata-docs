
# Claims

---------
## Calls

---------
### attest
Attest to a statement, needed to finalize the claims process.

WARNING: Insecure unless your chain includes `PrevalidateAttests` as a `SignedExtension`.

Unsigned Validation:
A call to attest is deemed valid if the sender has a `Preclaim` registered
and provides a `statement` which is expected for the account.

Parameters:
- `statement`: The identity of the statement which is being attested to in the signature.

&lt;weight&gt;
The weight of this call is invariant over the input parameters.
Weight includes logic to do pre-validation on `attest` call.

Total Complexity: O(1)
&lt;/weight&gt;
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
Make a claim to collect your TEERs.

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

&lt;weight&gt;
The weight of this call is invariant over the input parameters.
Weight includes logic to validate unsigned `claim` call.

Total Complexity: O(1)
&lt;/weight&gt;
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
Make a claim to collect your TEERs by signing a statement.

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

&lt;weight&gt;
The weight of this call is invariant over the input parameters.
Weight includes logic to validate unsigned `claim_attest` call.

Total Complexity: O(1)
&lt;/weight&gt;
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
Mint a new claim to collect TEERs.

The dispatch origin for this call must be _Root_.

Parameters:
- `who`: The Ethereum address allowed to collect this claim.
- `value`: The number of TEERs that will be claimed.
- `vesting_schedule`: An optional vesting schedule for these TEERs.

&lt;weight&gt;
The weight of this call is invariant over the input parameters.
We assume worst case that both vesting and statement is being inserted.

Total Complexity: O(1)
&lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `EthereumAddress` | 
| value | `BalanceOf<T>` | 
| vesting_schedule | `Option<(BalanceOf<T>, BalanceOf<T>, T::BlockNumber)>` | 
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