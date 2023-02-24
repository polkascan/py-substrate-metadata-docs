
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
    'param': '[u8; 32]',
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
| None | `T::Parameter` | ```[u8; 32]```

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
'[u8; 32]'
```
---------