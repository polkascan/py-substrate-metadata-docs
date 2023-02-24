
# Inflation

---------
## Constants

---------
### InitialPeriodLength
 The length of the initial period in which the constant reward is
 minted. Once the current block exceeds this, rewards are no further
 issued.
#### Value
```python
13149000
```
#### Python
```python
constant = substrate.get_constant('Inflation', 'InitialPeriodLength')
```
---------
### InitialPeriodReward
 The amount of newly issued tokens per block during the initial
 period.
#### Value
```python
760514107536694
```
#### Python
```python
constant = substrate.get_constant('Inflation', 'InitialPeriodReward')
```
---------