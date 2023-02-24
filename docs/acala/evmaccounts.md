
# EvmAccounts

---------
## Calls

---------
### claim_account
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
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| evm_address | `EvmAddress` | ```[u8; 20]```

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
## Constants

---------
### ChainId
#### Value
```python
787
```
#### Python
```python
constant = substrate.get_constant('EvmAccounts', 'ChainId')
```
---------
## Errors

---------
### AccountIdHasMapped

---------
### BadSignature

---------
### EthAddressHasMapped

---------
### InvalidSignature

---------
### NonZeroRefCount

---------