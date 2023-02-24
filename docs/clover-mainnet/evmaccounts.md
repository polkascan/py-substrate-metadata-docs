
# EvmAccounts

---------
## Calls

---------
### claim_account
Claim account mapping between Substrate accounts and EVM accounts.
Ensure eth_address has not been mapped.
#### Attributes
| Name | Type |
| -------- | -------- | 
| eth_address | `EvmAddress` | 
| eth_signature | `EcdsaSignature` | 

#### Python
```python
call = substrate.compose_call(
    'EvmAccounts', 'claim_account', {
    'eth_address': '[u8; 20]',
    'eth_signature': '[u8; 65]',
}
)
```

---------
## Events

---------
### ClaimAccount
Mapping between Substrate accounts and EVM accounts
claim account. \[account_id, evm_address\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `EvmAddress` | ```[u8; 20]```

---------
## Storage functions

---------
### Accounts

#### Python
```python
result = substrate.query(
    'EvmAccounts', 'Accounts', ['[u8; 20]']
)
```

#### Return value
```python
'AccountId'
```
---------
### EvmAddresses

#### Python
```python
result = substrate.query(
    'EvmAccounts', 'EvmAddresses', ['AccountId']
)
```

#### Return value
```python
'[u8; 20]'
```
---------
## Errors

---------
### AccountIdHasMapped
AccountId has mapped

---------
### BadSignature
Bad signature

---------
### EthAddressHasMapped
Eth address has mapped

---------
### InvalidSignature
Invalid signature

---------
### NonZeroRefCount
Account ref count is not zero

---------
### StillHasActiveReserved
Account still has active reserved

---------