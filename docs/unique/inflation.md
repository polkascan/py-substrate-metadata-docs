
# Inflation

---------
## Calls

---------
### start_inflation
This method sets the inflation start date. Can be only called once.
Inflation start block can be backdated and will catch up. The method will create Treasury
account if it does not exist and perform the first inflation deposit.

\# Permissions

* Root

\# Arguments

* inflation_start_relay_block: The relay chain block at which inflation should start
#### Attributes
| Name | Type |
| -------- | -------- | 
| inflation_start_relay_block | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Inflation', 'start_inflation', {'inflation_start_relay_block': 'u32'}
)
```

---------
## Storage functions

---------
### BlockInflation
 Current inflation for `InflationBlockInterval` number of blocks

#### Python
```python
result = substrate.query(
    'Inflation', 'BlockInflation', []
)
```

#### Return value
```python
'u128'
```
---------
### NextInflationBlock
 Next target (relay) block when inflation will be applied

#### Python
```python
result = substrate.query(
    'Inflation', 'NextInflationBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### NextRecalculationBlock
 Next target (relay) block when inflation is recalculated

#### Python
```python
result = substrate.query(
    'Inflation', 'NextRecalculationBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### StartBlock
 Relay block when inflation has started

#### Python
```python
result = substrate.query(
    'Inflation', 'StartBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### StartingYearTotalIssuance
 starting year total issuance

#### Python
```python
result = substrate.query(
    'Inflation', 'StartingYearTotalIssuance', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### InflationBlockInterval
 Number of blocks that pass between treasury balance updates due to inflation
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Inflation', 'InflationBlockInterval')
```
---------