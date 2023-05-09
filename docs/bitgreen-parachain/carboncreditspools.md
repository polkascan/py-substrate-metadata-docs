
# CarbonCreditsPools

---------
## Calls

---------
### create
Create a new CarbonCredits pool with given params

Params:
id : Id of the new pool
config : Config values for new pool
max_limit : Limit of maximum project-ids the pool can support, default to
T::MaxProjectIdLIst asset_symbol : Symbol for asset created for the pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::PoolId` | 
| admin | `T::AccountId` | 
| config | `PoolConfigOf<T>` | 
| max_limit | `Option<u32>` | 
| asset_symbol | `SymbolStringOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCreditsPools', 'create', {
    'admin': 'AccountId',
    'asset_symbol': 'Bytes',
    'config': {
        'project_id_list': (
            None,
            ['u32'],
        ),
        'registry_list': (
            None,
            [
                (
                    'Verra',
                    'GoldStandard',
                    'AmericanCarbonRegistry',
                    'ClimateActionReserve',
                ),
            ],
        ),
    },
    'id': 'u32',
    'max_limit': (None, 'u32'),
}
)
```

---------
### deposit
Deposit CarbonCredits tokens to pool with `id`

Params:
pool_id : Id of the pool to deposit into
project_id : The project_id of the CarbonCredits being deposited
amount: The amount of CarbonCredits to deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| asset_id | `T::AssetId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCreditsPools', 'deposit', {
    'amount': 'u128',
    'asset_id': 'u32',
    'pool_id': 'u32',
}
)
```

---------
### force_set_pool_storage
Force modify pool storage
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| data | `PoolOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCreditsPools', 'force_set_pool_storage', {
    'data': {
        'admin': 'AccountId',
        'config': {
            'project_id_list': (
                None,
                ['u32'],
            ),
            'registry_list': (
                None,
                [
                    (
                        'Verra',
                        'GoldStandard',
                        'AmericanCarbonRegistry',
                        'ClimateActionReserve',
                    ),
                ],
            ),
        },
        'credits': 'scale_info::331',
        'max_limit': 'u32',
    },
    'pool_id': 'u32',
}
)
```

---------
### retire
Retire Pool Tokens - A user can retire pool tokens, this will look at the available
CarbonCredits token supply in the pool and retire tokens starting from the oldest
issuance until the entire amount is retired.

Params:
pool_id : Id of the pooltokens to retire
amount: The amount of CarbonCredits to deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCreditsPools', 'retire', {'amount': 'u128', 'pool_id': 'u32'}
)
```

---------
## Events

---------
### Deposit
A new deposit was added to pool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| pool_id | `T::PoolId` | ```u32```
| asset_id | `T::AssetId` | ```u32```
| amount | `T::Balance` | ```u128```

---------
### PoolCreated
A new pool was created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| admin | `T::AccountId` | ```AccountId```
| id | `T::PoolId` | ```u32```
| config | `PoolConfigOf<T>` | ```{'registry_list': (None, [('Verra', 'GoldStandard', 'AmericanCarbonRegistry', 'ClimateActionReserve')]), 'project_id_list': (None, ['u32'])}```

---------
### Retired
Pool tokens were retired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| pool_id | `T::PoolId` | ```u32```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### PoolCredits

#### Python
```python
result = substrate.query(
    'CarbonCreditsPools', 'PoolCredits', ['u32']
)
```

#### Return value
```python
{
    'admin': 'AccountId',
    'config': {
        'project_id_list': (None, ['u32']),
        'registry_list': (
            None,
            [
                (
                    'Verra',
                    'GoldStandard',
                    'AmericanCarbonRegistry',
                    'ClimateActionReserve',
                ),
            ],
        ),
    },
    'credits': 'scale_info::331',
    'max_limit': 'u32',
}
```
---------
### Pools

#### Python
```python
result = substrate.query(
    'CarbonCreditsPools', 'Pools', ['u32']
)
```

#### Return value
```python
{
    'admin': 'AccountId',
    'config': {
        'project_id_list': (None, ['u32']),
        'registry_list': (
            None,
            [
                (
                    'Verra',
                    'GoldStandard',
                    'AmericanCarbonRegistry',
                    'ClimateActionReserve',
                ),
            ],
        ),
    },
    'credits': 'scale_info::331',
    'max_limit': 'u32',
}
```
---------
## Constants

---------
### PalletId
 The CarbonCredits-pools pallet id
#### Value
```python
'0x6269742f76637570'
```
#### Python
```python
constant = substrate.get_constant('CarbonCreditsPools', 'PalletId')
```
---------
## Errors

---------
### InvalidAmount
User entered an invalid amount

---------
### InvalidPoolId
The given PoolId does not exist

---------
### MaxLimitGreaterThanPermitted
The max limit supplied is greater than allowd

---------
### PoolIdBelowExpectedMinimum
PoolId should be above min limit

---------
### PoolIdInUse
PoolId is already being used

---------
### ProjectIdNotWhitelisted
The projectId is not whitelisted

---------
### ProjectIssuanceYearError
Cannot determine Credit issuance year

---------
### ProjectNotFound
The given project was not found

---------
### RegistryNotPermitted
The pool does not allow this registry projects

---------
### UnexpectedOverflow
Overflow happened during retire

---------