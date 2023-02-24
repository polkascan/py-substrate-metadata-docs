
# Currency

---------
## Constants

---------
### GetNativeCurrencyId
 Native currency e.g. INTR/KINT
#### Value
```python
{'Token': 'INTR'}
```
#### Python
```python
constant = substrate.get_constant('Currency', 'GetNativeCurrencyId')
```
---------
### GetRelayChainCurrencyId
 Relay chain currency e.g. DOT/KSM
#### Value
```python
{'Token': 'DOT'}
```
#### Python
```python
constant = substrate.get_constant('Currency', 'GetRelayChainCurrencyId')
```
---------
### GetWrappedCurrencyId
 Wrapped currency e.g. IBTC/KBTC
#### Value
```python
{'Token': 'IBTC'}
```
#### Python
```python
constant = substrate.get_constant('Currency', 'GetWrappedCurrencyId')
```
---------
## Errors

---------
### InvalidCurrency

---------
### TryIntoIntError

---------