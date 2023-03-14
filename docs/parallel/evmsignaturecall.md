
# EVMSignatureCall

---------
## Calls

---------
### call
\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB write (event).
- Weight of derivative `call` execution + 10_000_000.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| signer | `T::AccountId` | 
| signature | `Vec<u8>` | 
| nonce | `T::Index` | 

#### Python
```python
call = substrate.compose_call(
    'EVMSignatureCall', 'call', {
    'call': 'Call',
    'nonce': 'u32',
    'signature': 'Bytes',
    'signer': 'AccountId',
}
)
```

---------
### withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetIdOf<T>` | 
| address | `H160` | 
| value | `AssetBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'EVMSignatureCall', 'withdraw', {
    'address': '[u8; 20]',
    'asset': 'u32',
    'value': 'u128',
}
)
```

---------
## Events

---------
### Executed
A call just executed. \[result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
## Constants

---------
### CallFee
 The call processing fee amount.
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('EVMSignatureCall', 'CallFee')
```
---------
### CallMagicNumber
 The call magic number.
#### Value
```python
2012
```
#### Python
```python
constant = substrate.get_constant('EVMSignatureCall', 'CallMagicNumber')
```
---------
### GetNativeCurrencyId
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('EVMSignatureCall', 'GetNativeCurrencyId')
```
---------
### VerifySignature
 Enable signature verify or not
#### Value
```python
True
```
#### Python
```python
constant = substrate.get_constant('EVMSignatureCall', 'VerifySignature')
```
---------
## Errors

---------
### BadNonce
Bad nonce parameter.

---------
### DecodeFailure
Signature decode fails.

---------
### InvalidSignature
Signature and account mismatched.

---------