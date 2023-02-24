
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
 Kusama: to be defined, but the weights will be higher than on Rococo-Local

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
    'xcm_weight': 'u64',
}
)
```

---------
## Events

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
2223
```
#### Python
```python
constant = substrate.get_constant('XcmTransactor', 'ShellRuntimeParaId')
```
---------
## Errors

---------
### InvalidSwapIds

---------
### SwapIdsEqual

---------
### TransactFailed

---------