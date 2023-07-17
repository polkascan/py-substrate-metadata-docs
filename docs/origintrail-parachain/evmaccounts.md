
# EvmAccounts

---------
## Calls

---------
### claim_account
Claim account mapping between Substrate accounts and EVM accounts.
Ensure eth_address has not been mapped.

- `eth_address`: The address to bind to the caller&\#x27;s account
- `eth_signature`: A signature generated by the address to prove ownership
#### Attributes
| Name | Type |
| -------- | -------- | 
| eth_address | `EvmAddress` | 
| eth_signature | `Eip712Signature` | 

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
### claim_default_account
Claim account mapping between Substrate accounts and a generated EVM
address based off of those accounts.
Ensure eth_address has not been mapped
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EvmAccounts', 'claim_default_account', {}
)
```

---------
## Events

---------
### ClaimAccount
Mapping between Substrate accounts and EVM accounts
claim account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| evm_address | `EvmAddress` | ```[u8; 20]```

---------
## Storage functions

---------
### Accounts
 The Substrate Account for EvmAddresses

 Accounts: map EvmAddress =&gt; Option&lt;AccountId&gt;

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
 The EvmAddress for Substrate Accounts

 EvmAddresses: map AccountId =&gt; Option&lt;EvmAddress&gt;

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
## Constants

---------
### ChainId
 Chain ID of EVM.
#### Value
```python
2043
```
#### Python
```python
constant = substrate.get_constant('EvmAccounts', 'ChainId')
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