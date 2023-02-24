
# Claims

---------
## Calls

---------
### claim
Make a claim to collect your EFI.

The dispatch origin for this call must be _None_.

Unsigned Validation:
A call to claim is deemed valid if the signature provided matches
the expected signed message of:

&gt; Ethereum Signed Message:
&gt; (configured prefix string)(address)

and `address` matches the `dest` account.

Parameters:
- `dest`: The destination account to payout the claim.
- `ethereum_signature`: The signature of an ethereum signed message matching the format
  described above.

&lt;weight&gt;
The weight of this call is invariant over the input parameters.
Weight includes logic to validate unsigned `claim` call.

Total Complexity: O(1)
&lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `T::AccountId` | 
| ethereum_signature | `Signature` | 

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
### mint_claim
Mint a new claim to collect EFIs.

The dispatch origin for this call must be _Root_.

Parameters:
- `who`: The Ethereum address allowed to collect this claim.
- `value`: The number of EFIs that will be claimed.

&lt;weight&gt;
The weight of this call is invariant over the input parameters.

Total Complexity: O(1)
&lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `EthereumAddress` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'mint_claim', {'value': 'u128', 'who': '[u8; 20]'}
)
```

---------
### move_claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| old | `EthereumAddress` | 
| new | `EthereumAddress` | 
| preclaim | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'move_claim', {
    'new': '[u8; 20]',
    'old': '[u8; 20]',
    'preclaim': (None, 'AccountId'),
}
)
```

---------
## Events

---------
### Claimed
Someone claimed some EFIs. `[who, ethereum_address, amount]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| ethereum_address | `EthereumAddress` | ```[u8; 20]```
| amount | `BalanceOf<T>` | ```u128```

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
## Constants

---------
### Prefix
 Prefix added to messages
#### Value
```python
'Pay EFI to the Efinity account:'
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
### SignerHasNoClaim
Ethereum address has no claim.

---------