
# SimpleDisputes

---------
## Constants

---------
### PalletId
 The pallet identifier.
#### Value
```python
'0x7a67652f73656470'
```
#### Python
```python
constant = substrate.get_constant('SimpleDisputes', 'PalletId')
```
---------
## Errors

---------
### InvalidMarketStatus
1. Any resolution must either have a `Disputed` or `Reported` market status
2. If status is `Disputed`, then at least one dispute must exist

---------
### MarketDoesNotHaveSimpleDisputesMechanism
On dispute or resolution, someone tried to pass a non-simple-disputes market type

---------