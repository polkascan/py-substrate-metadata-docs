
# Tips

---------
## Calls

---------
### close_tip
Close and payout a tip.

The dispatch origin for this call must be _Signed_.

The tip identified by `hash` must have finished its countdown period.

- `hash`: The identity of the open tip for which a tip value is declared. This is formed
  as the hash of the tuple of the original tip `reason` and the beneficiary account ID.

\# &lt;weight&gt;
- Complexity: `O(T)` where `T` is the number of tippers. decoding `Tipper` vec of length
  `T`. `T` is charged as upper bound given by `ContainsLengthBound`. The actual cost
  depends on the implementation of `T::Tippers`.
- DbReads: `Tips`, `Tippers`, `tip finder`
- DbWrites: `Reasons`, `Tips`, `Tippers`, `tip finder`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'close_tip', {'hash': '[u8; 32]'}
)
```

---------
### report_awesome
Report something `reason` that deserves a tip and claim any eventual the finder&\#x27;s fee.

The dispatch origin for this call must be _Signed_.

Payment: `TipReportDepositBase` will be reserved from the origin account, as well as
`DataDepositPerByte` for each byte in `reason`.

- `reason`: The reason for, or the thing that deserves, the tip; generally this will be
  a UTF-8-encoded URL.
- `who`: The account which should be credited for the tip.

Emits `NewTip` if successful.

\# &lt;weight&gt;
- Complexity: `O(R)` where `R` length of `reason`.
  - encoding and hashing of &\#x27;reason&\#x27;
- DbReads: `Reasons`, `Tips`
- DbWrites: `Reasons`, `Tips`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| reason | `Vec<u8>` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'report_awesome', {
    'reason': 'Bytes',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### retract_tip
Retract a prior tip-report from `report_awesome`, and cancel the process of tipping.

If successful, the original deposit will be unreserved.

The dispatch origin for this call must be _Signed_ and the tip identified by `hash`
must have been reported by the signing account through `report_awesome` (and not
through `tip_new`).

- `hash`: The identity of the open tip for which a tip value is declared. This is formed
  as the hash of the tuple of the original tip `reason` and the beneficiary account ID.

Emits `TipRetracted` if successful.

\# &lt;weight&gt;
- Complexity: `O(1)`
  - Depends on the length of `T::Hash` which is fixed.
- DbReads: `Tips`, `origin account`
- DbWrites: `Reasons`, `Tips`, `origin account`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'retract_tip', {'hash': '[u8; 32]'}
)
```

---------
### slash_tip
Remove and slash an already-open tip.

May only be called from `T::RejectOrigin`.

As a result, the finder is slashed and the deposits are lost.

Emits `TipSlashed` if successful.

\# &lt;weight&gt;
  `T` is charged as upper bound given by `ContainsLengthBound`.
  The actual cost depends on the implementation of `T::Tippers`.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'slash_tip', {'hash': '[u8; 32]'}
)
```

---------
### tip
Declare a tip value for an already-open tip.

The dispatch origin for this call must be _Signed_ and the signing account must be a
member of the `Tippers` set.

- `hash`: The identity of the open tip for which a tip value is declared. This is formed
  as the hash of the tuple of the hash of the original tip `reason` and the beneficiary
  account ID.
- `tip_value`: The amount of tip that the sender would like to give. The median tip
  value of active tippers will be given to the `who`.

Emits `TipClosing` if the threshold of tippers has been reached and the countdown period
has started.

\# &lt;weight&gt;
- Complexity: `O(T)` where `T` is the number of tippers. decoding `Tipper` vec of length
  `T`, insert tip and check closing, `T` is charged as upper bound given by
  `ContainsLengthBound`. The actual cost depends on the implementation of `T::Tippers`.

  Actually weight could be lower as it depends on how many tips are in `OpenTip` but it
  is weighted as if almost full i.e of length `T-1`.
- DbReads: `Tippers`, `Tips`
- DbWrites: `Tips`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 
| tip_value | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'tip', {
    'hash': '[u8; 32]',
    'tip_value': 'u128',
}
)
```

---------
### tip_new
Give a tip for something new; no finder&\#x27;s fee will be taken.

The dispatch origin for this call must be _Signed_ and the signing account must be a
member of the `Tippers` set.

- `reason`: The reason for, or the thing that deserves, the tip; generally this will be
  a UTF-8-encoded URL.
- `who`: The account which should be credited for the tip.
- `tip_value`: The amount of tip that the sender would like to give. The median tip
  value of active tippers will be given to the `who`.

Emits `NewTip` if successful.

\# &lt;weight&gt;
- Complexity: `O(R + T)` where `R` length of `reason`, `T` is the number of tippers.
  - `O(T)`: decoding `Tipper` vec of length `T`. `T` is charged as upper bound given by
    `ContainsLengthBound`. The actual cost depends on the implementation of
    `T::Tippers`.
  - `O(R)`: hashing and encoding of reason of length `R`
- DbReads: `Tippers`, `Reasons`
- DbWrites: `Reasons`, `Tips`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| reason | `Vec<u8>` | 
| who | `AccountIdLookupOf<T>` | 
| tip_value | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'tip_new', {
    'reason': 'Bytes',
    'tip_value': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### NewTip
A new tip suggestion has been opened.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```[u8; 32]```

---------
### TipClosed
A tip suggestion has been closed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```[u8; 32]```
| who | `T::AccountId` | ```AccountId```
| payout | `BalanceOf<T, I>` | ```u128```

---------
### TipClosing
A tip suggestion has reached threshold and is closing.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```[u8; 32]```

---------
### TipRetracted
A tip suggestion has been retracted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```[u8; 32]```

---------
### TipSlashed
A tip suggestion has been slashed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```[u8; 32]```
| finder | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Reasons
 Simple preimage lookup from the reason&#x27;s hash to the original data. Again, has an
 insecure enumerable hash since the key is guaranteed to be the result of a secure hash.

#### Python
```python
result = substrate.query(
    'Tips', 'Reasons', ['[u8; 32]']
)
```

#### Return value
```python
'Bytes'
```
---------
### Tips
 TipsMap that are not yet completed. Keyed by the hash of `(reason, who)` from the value.
 This has the insecure enumerable hash function since the key itself is already
 guaranteed to be a secure hash.

#### Python
```python
result = substrate.query(
    'Tips', 'Tips', ['[u8; 32]']
)
```

#### Return value
```python
{
    'closes': (None, 'u32'),
    'deposit': 'u128',
    'finder': 'AccountId',
    'finders_fee': 'bool',
    'reason': '[u8; 32]',
    'tips': [('AccountId', 'u128')],
    'who': 'AccountId',
}
```
---------
## Constants

---------
### DataDepositPerByte
 The amount held on deposit per byte within the tip report reason or bounty description.
#### Value
```python
333333333
```
#### Python
```python
constant = substrate.get_constant('Tips', 'DataDepositPerByte')
```
---------
### MaximumReasonLength
 Maximum acceptable reason length.

 Benchmarks depend on this value, be sure to update weights file when changing this value
#### Value
```python
16384
```
#### Python
```python
constant = substrate.get_constant('Tips', 'MaximumReasonLength')
```
---------
### TipCountdown
 The period for which a tip remains open after is has achieved threshold tippers.
#### Value
```python
14400
```
#### Python
```python
constant = substrate.get_constant('Tips', 'TipCountdown')
```
---------
### TipFindersFee
 The percent of the final tip which goes to the original reporter of the tip.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Tips', 'TipFindersFee')
```
---------
### TipReportDepositBase
 The amount held on deposit for placing a tip report.
#### Value
```python
33333333300
```
#### Python
```python
constant = substrate.get_constant('Tips', 'TipReportDepositBase')
```
---------
## Errors

---------
### AlreadyKnown
The tip was already found/started.

---------
### NotFinder
The account attempting to retract the tip is not the finder of the tip.

---------
### Premature
The tip cannot be claimed/closed because it&\#x27;s still in the countdown period.

---------
### ReasonTooBig
The reason given is just too big.

---------
### StillOpen
The tip cannot be claimed/closed because there are not enough tippers yet.

---------
### UnknownTip
The tip hash is unknown.

---------