
# EthCall

---------
## Calls

---------
### call
\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB write (event).
- Weight of derivative `call` execution + read/write + 10_000.
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
    'EthCall', 'call', {
    'call': 'Call',
    'nonce': 'u32',
    'signature': 'Bytes',
    'signer': 'AccountId',
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
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
## Constants

---------
### CallFee
 The call processing fee amount.
#### Value
```python
100000000000000000
```
#### Python
```python
constant = substrate.get_constant('EthCall', 'CallFee')
```
---------
### CallMagicNumber
 The call magic number.
#### Value
```python
592
```
#### Python
```python
constant = substrate.get_constant('EthCall', 'CallMagicNumber')
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