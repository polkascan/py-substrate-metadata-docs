
# Utility

---------
## Calls

---------
### batch
Dispatch multiple calls from the sender&\#x27;s origin.

This will execute until the first one fails and then stop.

May be called from root or a signed origin.

\# Parameters
- `calls`: The calls to be dispatched from the same origin.

\# Weight
- The sum of the weights of the `calls`.
- One event.

This will return `Ok` in all circumstances except an unsigned origin. To determine the success of the batch, an
event is deposited. If a call failed and the batch was interrupted, then the
`BatchInterrupted` event is deposited, along with the number of successful calls made
and the error of the failed call. If all were successful, then the `BatchCompleted`
event is deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch', {'calls': ['Call']}
)
```

---------
### batch_atomic
Dispatch multiple calls from the sender&\#x27;s origin.

This will execute all calls, in order, stopping at the first failure,
in which case the state changes are rolled back.
On failure, an event `BatchInterrupted(failure_idx, error)` is deposited.

May be called from root or a signed origin.

\# Parameters
- `calls`: The calls to be dispatched from the same origin.

\# Weight
- The sum of the weights of the `calls`.
- One event.

This will return `Ok` in all circumstances except an unsigned origin.
To determine the success of the batch, an event is deposited.
If any call failed, then `BatchInterrupted` is deposited.
If all were successful, then the `BatchCompleted` event is deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_atomic', {'calls': ['Call']}
)
```

---------
### batch_optimistic
Dispatch multiple calls from the sender&\#x27;s origin.

This will execute all calls, in order, irrespective of failures.
Any failures will be available in a `BatchOptimisticFailed` event.

May be called from root or a signed origin.

\# Parameters
- `calls`: The calls to be dispatched from the same origin.


\# Weight
- The sum of the weights of the `calls`.
- One event.

This will return `Ok` in all circumstances except an unsigned origin.
To determine the success of the batch, an event is deposited.
If any call failed, then `BatchOptimisticFailed` is deposited,
with a vector of event counts for each call as well as a vector
of errors.
If all were successful, then the `BatchCompleted` event is deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_optimistic', {'calls': ['Call']}
)
```

---------
### relay_tx
Relay a call for a target from an origin

Relaying in this context refers to the ability of origin to make a call on behalf of
target.

Fees are charged to origin

\# Parameters
- `target`: Account to be relayed
- `signature`: Signature from target authorizing the relay
- `call`: Call to be relayed on behalf of target

#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `T::AccountId` | 
| signature | `T::OffChainSignature` | 
| call | `UniqueCall<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'relay_tx', {
    'call': {
        'call': 'Call',
        'nonce': 'u64',
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'target': 'AccountId',
}
)
```

---------
## Events

---------
### BatchCompleted
Batch of dispatches completed fully with no error.
Includes a vector of event counts for each dispatch.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventCounts` | ```['u32']```

---------
### BatchInterrupted
Batch of dispatches did not complete fully.
Includes a vector of event counts for each dispatch and
the index of the first failing dispatch as well as the error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventCounts` | ```['u32']```
| None | `ErrorAt` | ```('u32', {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')})```

---------
### BatchOptimisticFailed
Batch of dispatches did not complete fully.
Includes a vector of event counts for each call and
a vector of any failed dispatches with their indices and associated error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventCounts` | ```['u32']```
| None | `Vec<ErrorAt>` | ```[('u32', {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')})]```

---------
## Storage functions

---------
### Nonces

#### Python
```python
result = substrate.query(
    'Utility', 'Nonces', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
## Errors

---------
### InvalidNonce
Provided nonce was invalid
If the provided nonce &lt; current nonce, the call was already executed
If the provided nonce &gt; current nonce, the call(s) before the current failed to execute

---------
### InvalidSignature
Offchain signature is invalid

---------
### TargetCddMissing
Target does not have a valid CDD

---------