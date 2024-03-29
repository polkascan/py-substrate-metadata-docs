
# EqCrowdLoanDots

---------
## Calls

---------
### allow_crowdloan_swap
#### Attributes
| Name | Type |
| -------- | -------- | 
| assets | `Vec<CrowdloanDotAsset>` | 

#### Python
```python
call = substrate.compose_call(
    'EqCrowdLoanDots', 'allow_crowdloan_swap', {
    'assets': [
        (
            'XDOT',
            'XDOT2',
            'XDOT3',
            'CDOT613',
            'CDOT714',
            'CDOT815',
        ),
    ],
}
)
```

---------
### swap_crowdloan_dots
#### Attributes
| Name | Type |
| -------- | -------- | 
| mb_who | `Option<T::AccountId>` | 
| assets | `Vec<CrowdloanDotAsset>` | 

#### Python
```python
call = substrate.compose_call(
    'EqCrowdLoanDots', 'swap_crowdloan_dots', {
    'assets': [
        (
            'XDOT',
            'XDOT2',
            'XDOT3',
            'CDOT613',
            'CDOT714',
            'CDOT815',
        ),
    ],
    'mb_who': (None, 'AccountId'),
}
)
```

---------
## Storage functions

---------
### AllowedCrowdloanDotsSwap
 Stores Crowdloan DOTs allowed to swap

#### Python
```python
result = substrate.query(
    'EqCrowdLoanDots', 'AllowedCrowdloanDotsSwap', []
)
```

#### Return value
```python
[('XDOT', 'XDOT2', 'XDOT3', 'CDOT613', 'CDOT714', 'CDOT815')]
```
---------
## Errors

---------
### CrowdloanDotSwapNotAllowed
Crowdloan DOT swap is not allowed

---------
### TransfersAreDisabled
Transfers are disabled

---------