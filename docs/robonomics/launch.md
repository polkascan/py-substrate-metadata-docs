
# Launch

---------
## Calls

---------
### launch
Launch a robot with given parameter.
#### Attributes
| Name | Type |
| -------- | -------- | 
| robot | `T::AccountId` | 
| param | `T::Parameter` | 

#### Python
```python
call = substrate.compose_call(
    'Launch', 'launch', {
    'param': 'scale_info::9',
    'robot': 'AccountId',
}
)
```

---------
## Events

---------
### NewLaunch
Launch a robot with given parameter: sender, robot, parameter.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::Parameter` | ```scale_info::9```

---------
## Storage functions

---------
### Goal

#### Python
```python
result = substrate.query(
    'Launch', 'Goal', []
)
```

#### Return value
```python
'scale_info::9'
```
---------