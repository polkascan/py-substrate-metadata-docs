
# XcmTransactor

---------
## Calls

---------
### send_swap_ump
Send swap instruction to the relay chain to swap the slot lease of our two parachains.
This needs to be done from within a pallet as the `XCM` origin must be the parachain
itself.

This function should really only be called once via governance, on each chain that
performs the slot swap.

Sane weight values:
 Rococo-Local as of 11.01.2022:
		* xcm_weight: 10_000_000_000
		* buy_execution_weight: 500_000_000
 Kusama as of 11.01.2022:
		* xcm_weight: 10_000_000_000
		* buy_execution_weight: 5_000_000_000

#### Attributes
| Name | Type |
| -------- | -------- | 
| self_id | `ParaId` | 
| other_id | `ParaId` | 
| xcm_weight | `XcmWeight` | 
| buy_execution_fee | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'XcmTransactor', 'send_swap_ump', {
    'buy_execution_fee': 'u128',
    'other_id': 'u32',
    'self_id': 'u32',
    'xcm_weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
## Events

---------
### SentXcm
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `XcmHash` | ```[u8; 32]```

---------
### SwapTransactSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_a | `ParaId` | ```u32```
| para_b | `ParaId` | ```u32```

---------
## Constants

---------
### IntegriteeKsmParaId
#### Value
```python
2015
```
#### Python
```python
constant = substrate.get_constant('XcmTransactor', 'IntegriteeKsmParaId')
```
---------
### ShellRuntimeParaId
#### Value
```python
2267
```
#### Python
```python
constant = substrate.get_constant('XcmTransactor', 'ShellRuntimeParaId')
```
---------
## Errors

---------
### DestinationUnsupported
The given message cannot be translated into a format that the destination can be expected
to interpret.

---------
### FeesNotMet
Fees needed to be paid in order to send the message were unavailable.

---------
### InvalidSwapIds
The swap IDs do not correspond to the runtime-configured value.

---------
### SwapIdsEqual
Swap IDs need to be different.

---------
### Transport
Destination is routable, but there is some issue with the transport mechanism. This is
considered fatal.

---------
### Unreachable
The desired destination was unreachable, generally because there is a no way of routing
to it.

---------
### Unroutable
Destination is known to be unroutable. This is considered fatal.

---------
### XcmSendError
Some XCM send error occurred.

---------