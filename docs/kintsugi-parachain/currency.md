
# Currency

---------
## Constants

---------
### GetNativeCurrencyId
 Native currency e.g. INTR/KINT
#### Value
```python
{'Token': 'KINT'}
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
{'Token': 'KSM'}
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
{'Token': 'KBTC'}
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