
# Commitments

---------
## Calls

---------
### set_commitment
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| info | `Box<CommitmentInfo<T::MaxFields>>` | 

#### Python
```python
call = substrate.compose_call(
    'Commitments', 'set_commitment', {
    'info': {
        'fields': [
            {
                'BlakeTwo256': '[u8; 32]',
                'Keccak256': '[u8; 32]',
                'None': None,
                'Raw0': '[u8; 0]',
                'Raw1': '[u8; 1]',
                'Raw10': '[u8; 10]',
                'Raw100': '[u8; 100]',
                'Raw101': '[u8; 101]',
                'Raw102': '[u8; 102]',
                'Raw103': '[u8; 103]',
                'Raw104': '[u8; 104]',
                'Raw105': '[u8; 105]',
                'Raw106': '[u8; 106]',
                'Raw107': '[u8; 107]',
                'Raw108': '[u8; 108]',
                'Raw109': '[u8; 109]',
                'Raw11': '[u8; 11]',
                'Raw110': '[u8; 110]',
                'Raw111': '[u8; 111]',
                'Raw112': '[u8; 112]',
                'Raw113': '[u8; 113]',
                'Raw114': '[u8; 114]',
                'Raw115': '[u8; 115]',
                'Raw116': '[u8; 116]',
                'Raw117': '[u8; 117]',
                'Raw118': '[u8; 118]',
                'Raw119': '[u8; 119]',
                'Raw12': '[u8; 12]',
                'Raw120': '[u8; 120]',
                'Raw121': '[u8; 121]',
                'Raw122': '[u8; 122]',
                'Raw123': '[u8; 123]',
                'Raw124': '[u8; 124]',
                'Raw125': '[u8; 125]',
                'Raw126': '[u8; 126]',
                'Raw127': '[u8; 127]',
                'Raw128': '[u8; 128]',
                'Raw13': '[u8; 13]',
                'Raw14': '[u8; 14]',
                'Raw15': '[u8; 15]',
                'Raw16': '[u8; 16]',
                'Raw17': '[u8; 17]',
                'Raw18': '[u8; 18]',
                'Raw19': '[u8; 19]',
                'Raw2': '[u8; 2]',
                'Raw20': '[u8; 20]',
                'Raw21': '[u8; 21]',
                'Raw22': '[u8; 22]',
                'Raw23': '[u8; 23]',
                'Raw24': '[u8; 24]',
                'Raw25': '[u8; 25]',
                'Raw26': '[u8; 26]',
                'Raw27': '[u8; 27]',
                'Raw28': '[u8; 28]',
                'Raw29': '[u8; 29]',
                'Raw3': '[u8; 3]',
                'Raw30': '[u8; 30]',
                'Raw31': '[u8; 31]',
                'Raw32': '[u8; 32]',
                'Raw33': '[u8; 33]',
                'Raw34': '[u8; 34]',
                'Raw35': '[u8; 35]',
                'Raw36': '[u8; 36]',
                'Raw37': '[u8; 37]',
                'Raw38': '[u8; 38]',
                'Raw39': '[u8; 39]',
                'Raw4': '[u8; 4]',
                'Raw40': '[u8; 40]',
                'Raw41': '[u8; 41]',
                'Raw42': '[u8; 42]',
                'Raw43': '[u8; 43]',
                'Raw44': '[u8; 44]',
                'Raw45': '[u8; 45]',
                'Raw46': '[u8; 46]',
                'Raw47': '[u8; 47]',
                'Raw48': '[u8; 48]',
                'Raw49': '[u8; 49]',
                'Raw5': '[u8; 5]',
                'Raw50': '[u8; 50]',
                'Raw51': '[u8; 51]',
                'Raw52': '[u8; 52]',
                'Raw53': '[u8; 53]',
                'Raw54': '[u8; 54]',
                'Raw55': '[u8; 55]',
                'Raw56': '[u8; 56]',
                'Raw57': '[u8; 57]',
                'Raw58': '[u8; 58]',
                'Raw59': '[u8; 59]',
                'Raw6': '[u8; 6]',
                'Raw60': '[u8; 60]',
                'Raw61': '[u8; 61]',
                'Raw62': '[u8; 62]',
                'Raw63': '[u8; 63]',
                'Raw64': '[u8; 64]',
                'Raw65': '[u8; 65]',
                'Raw66': '[u8; 66]',
                'Raw67': '[u8; 67]',
                'Raw68': '[u8; 68]',
                'Raw69': '[u8; 69]',
                'Raw7': '[u8; 7]',
                'Raw70': '[u8; 70]',
                'Raw71': '[u8; 71]',
                'Raw72': '[u8; 72]',
                'Raw73': '[u8; 73]',
                'Raw74': '[u8; 74]',
                'Raw75': '[u8; 75]',
                'Raw76': '[u8; 76]',
                'Raw77': '[u8; 77]',
                'Raw78': '[u8; 78]',
                'Raw79': '[u8; 79]',
                'Raw8': '[u8; 8]',
                'Raw80': '[u8; 80]',
                'Raw81': '[u8; 81]',
                'Raw82': '[u8; 82]',
                'Raw83': '[u8; 83]',
                'Raw84': '[u8; 84]',
                'Raw85': '[u8; 85]',
                'Raw86': '[u8; 86]',
                'Raw87': '[u8; 87]',
                'Raw88': '[u8; 88]',
                'Raw89': '[u8; 89]',
                'Raw9': '[u8; 9]',
                'Raw90': '[u8; 90]',
                'Raw91': '[u8; 91]',
                'Raw92': '[u8; 92]',
                'Raw93': '[u8; 93]',
                'Raw94': '[u8; 94]',
                'Raw95': '[u8; 95]',
                'Raw96': '[u8; 96]',
                'Raw97': '[u8; 97]',
                'Raw98': '[u8; 98]',
                'Raw99': '[u8; 99]',
                'Sha256': '[u8; 32]',
                'ShaThree256': '[u8; 32]',
            },
        ],
    },
    'netuid': 'u16',
}
)
```

---------
## Events

---------
### Commitment
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| netuid | `u16` | ```u16```
| who | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### CommitmentOf
 Identity data by account

#### Python
```python
result = substrate.query(
    'Commitments', 'CommitmentOf', ['u16', 'AccountId']
)
```

#### Return value
```python
{
    'block': 'u32',
    'deposit': 'u64',
    'info': {
        'fields': [
            {
                'BlakeTwo256': '[u8; 32]',
                'Keccak256': '[u8; 32]',
                'None': None,
                'Raw0': '[u8; 0]',
                'Raw1': '[u8; 1]',
                'Raw10': '[u8; 10]',
                'Raw100': '[u8; 100]',
                'Raw101': '[u8; 101]',
                'Raw102': '[u8; 102]',
                'Raw103': '[u8; 103]',
                'Raw104': '[u8; 104]',
                'Raw105': '[u8; 105]',
                'Raw106': '[u8; 106]',
                'Raw107': '[u8; 107]',
                'Raw108': '[u8; 108]',
                'Raw109': '[u8; 109]',
                'Raw11': '[u8; 11]',
                'Raw110': '[u8; 110]',
                'Raw111': '[u8; 111]',
                'Raw112': '[u8; 112]',
                'Raw113': '[u8; 113]',
                'Raw114': '[u8; 114]',
                'Raw115': '[u8; 115]',
                'Raw116': '[u8; 116]',
                'Raw117': '[u8; 117]',
                'Raw118': '[u8; 118]',
                'Raw119': '[u8; 119]',
                'Raw12': '[u8; 12]',
                'Raw120': '[u8; 120]',
                'Raw121': '[u8; 121]',
                'Raw122': '[u8; 122]',
                'Raw123': '[u8; 123]',
                'Raw124': '[u8; 124]',
                'Raw125': '[u8; 125]',
                'Raw126': '[u8; 126]',
                'Raw127': '[u8; 127]',
                'Raw128': '[u8; 128]',
                'Raw13': '[u8; 13]',
                'Raw14': '[u8; 14]',
                'Raw15': '[u8; 15]',
                'Raw16': '[u8; 16]',
                'Raw17': '[u8; 17]',
                'Raw18': '[u8; 18]',
                'Raw19': '[u8; 19]',
                'Raw2': '[u8; 2]',
                'Raw20': '[u8; 20]',
                'Raw21': '[u8; 21]',
                'Raw22': '[u8; 22]',
                'Raw23': '[u8; 23]',
                'Raw24': '[u8; 24]',
                'Raw25': '[u8; 25]',
                'Raw26': '[u8; 26]',
                'Raw27': '[u8; 27]',
                'Raw28': '[u8; 28]',
                'Raw29': '[u8; 29]',
                'Raw3': '[u8; 3]',
                'Raw30': '[u8; 30]',
                'Raw31': '[u8; 31]',
                'Raw32': '[u8; 32]',
                'Raw33': '[u8; 33]',
                'Raw34': '[u8; 34]',
                'Raw35': '[u8; 35]',
                'Raw36': '[u8; 36]',
                'Raw37': '[u8; 37]',
                'Raw38': '[u8; 38]',
                'Raw39': '[u8; 39]',
                'Raw4': '[u8; 4]',
                'Raw40': '[u8; 40]',
                'Raw41': '[u8; 41]',
                'Raw42': '[u8; 42]',
                'Raw43': '[u8; 43]',
                'Raw44': '[u8; 44]',
                'Raw45': '[u8; 45]',
                'Raw46': '[u8; 46]',
                'Raw47': '[u8; 47]',
                'Raw48': '[u8; 48]',
                'Raw49': '[u8; 49]',
                'Raw5': '[u8; 5]',
                'Raw50': '[u8; 50]',
                'Raw51': '[u8; 51]',
                'Raw52': '[u8; 52]',
                'Raw53': '[u8; 53]',
                'Raw54': '[u8; 54]',
                'Raw55': '[u8; 55]',
                'Raw56': '[u8; 56]',
                'Raw57': '[u8; 57]',
                'Raw58': '[u8; 58]',
                'Raw59': '[u8; 59]',
                'Raw6': '[u8; 6]',
                'Raw60': '[u8; 60]',
                'Raw61': '[u8; 61]',
                'Raw62': '[u8; 62]',
                'Raw63': '[u8; 63]',
                'Raw64': '[u8; 64]',
                'Raw65': '[u8; 65]',
                'Raw66': '[u8; 66]',
                'Raw67': '[u8; 67]',
                'Raw68': '[u8; 68]',
                'Raw69': '[u8; 69]',
                'Raw7': '[u8; 7]',
                'Raw70': '[u8; 70]',
                'Raw71': '[u8; 71]',
                'Raw72': '[u8; 72]',
                'Raw73': '[u8; 73]',
                'Raw74': '[u8; 74]',
                'Raw75': '[u8; 75]',
                'Raw76': '[u8; 76]',
                'Raw77': '[u8; 77]',
                'Raw78': '[u8; 78]',
                'Raw79': '[u8; 79]',
                'Raw8': '[u8; 8]',
                'Raw80': '[u8; 80]',
                'Raw81': '[u8; 81]',
                'Raw82': '[u8; 82]',
                'Raw83': '[u8; 83]',
                'Raw84': '[u8; 84]',
                'Raw85': '[u8; 85]',
                'Raw86': '[u8; 86]',
                'Raw87': '[u8; 87]',
                'Raw88': '[u8; 88]',
                'Raw89': '[u8; 89]',
                'Raw9': '[u8; 9]',
                'Raw90': '[u8; 90]',
                'Raw91': '[u8; 91]',
                'Raw92': '[u8; 92]',
                'Raw93': '[u8; 93]',
                'Raw94': '[u8; 94]',
                'Raw95': '[u8; 95]',
                'Raw96': '[u8; 96]',
                'Raw97': '[u8; 97]',
                'Raw98': '[u8; 98]',
                'Raw99': '[u8; 99]',
                'Sha256': '[u8; 32]',
                'ShaThree256': '[u8; 32]',
            },
        ],
    },
}
```
---------
### LastCommitment

#### Python
```python
result = substrate.query(
    'Commitments', 'LastCommitment', ['u16', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### FieldDeposit
 The amount held on deposit per additional field for a registered identity.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Commitments', 'FieldDeposit')
```
---------
### InitialDeposit
 The amount held on deposit for a registered identity
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Commitments', 'InitialDeposit')
```
---------
### MaxFields
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Commitments', 'MaxFields')
```
---------
### RateLimit
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Commitments', 'RateLimit')
```
---------
## Errors

---------
### CannotCommit
Account isn&\#x27;t allow to make commitments to the chain

---------
### RateLimitExceeded
Account is trying to commit data too fast

---------
### TooManyFields
Account passed too many additional fields to their commitment

---------