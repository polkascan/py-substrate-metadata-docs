
# VoterList

---------
## Calls

---------
### put_in_front_of
Move the caller&\#x27;s Id directly in front of `lighter`.

The dispatch origin for this call must be _Signed_ and can only be called by the Id of
the account going in front of `lighter`.

Only works if
- both nodes are within the same bag,
- and `origin` has a greater `Score` than `lighter`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| lighter | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VoterList', 'put_in_front_of', {
    'lighter': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### rebag
Declare that some `dislocated` account has, through rewards or penalties, sufficiently
changed its score that it should properly fall into a different bag than its current
one.

Anyone can call this function about any potentially dislocated account.

Will always update the stored score of `dislocated` to the correct score, based on
`ScoreProvider`.

If `dislocated` does not exists, it returns an error.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dislocated | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VoterList', 'rebag', {
    'dislocated': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### Rebagged
Moved an account from one bag to another.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| from | `T::Score` | ```u64```
| to | `T::Score` | ```u64```

---------
### ScoreUpdated
Updated the score of some account to the given amount.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| new_score | `T::Score` | ```u64```

---------
## Storage functions

---------
### CounterForListNodes
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'VoterList', 'CounterForListNodes', []
)
```

#### Return value
```python
'u32'
```
---------
### ListBags
 A bag stored in storage.

 Stores a `Bag` struct, which stores head and tail pointers to itself.

#### Python
```python
result = substrate.query(
    'VoterList', 'ListBags', ['u64']
)
```

#### Return value
```python
{'head': (None, 'AccountId'), 'tail': (None, 'AccountId')}
```
---------
### ListNodes
 A single node, within some bag.

 Nodes store links forward and back within their respective bags.

#### Python
```python
result = substrate.query(
    'VoterList', 'ListNodes', ['AccountId']
)
```

#### Return value
```python
{
    'bag_upper': 'u64',
    'id': 'AccountId',
    'next': (None, 'AccountId'),
    'prev': (None, 'AccountId'),
    'score': 'u64',
}
```
---------
## Constants

---------
### BagThresholds
 The list of thresholds separating the various bags.

 Ids are separated into unsorted bags according to their score. This specifies the
 thresholds separating the bags. An id&#x27;s bag is the largest bag for which the id&#x27;s score
 is less than or equal to its upper threshold.

 When ids are iterated, higher bags are iterated completely before lower bags. This means
 that iteration is _semi-sorted_: ids of higher score tend to come before ids of lower
 score, but peer ids within a particular bag are sorted in insertion order.

 \# Expressing the constant

 This constant must be sorted in strictly increasing order. Duplicate items are not
 permitted.

 There is an implied upper limit of `Score::MAX`; that value does not need to be
 specified within the bag. For any two threshold lists, if one ends with
 `Score::MAX`, the other one does not, and they are otherwise equal, the two
 lists will behave identically.

 \# Calculation

 It is recommended to generate the set of thresholds in a geometric series, such that
 there exists some constant ratio such that `threshold[k + 1] == (threshold[k] *
 constant_ratio).max(threshold[k] + 1)` for all `k`.

 The helpers in the `/utils/frame/generate-bags` module can simplify this calculation.

 \# Examples

 - If `BagThresholds::get().is_empty()`, then all ids are put into the same bag, and
   iteration is strictly in insertion order.
 - If `BagThresholds::get().len() == 64`, and the thresholds are determined according to
   the procedure given above, then the constant ratio is equal to 2.
 - If `BagThresholds::get().len() == 200`, and the thresholds are determined according to
   the procedure given above, then the constant ratio is approximately equal to 1.248.
 - If the threshold list begins `[1, 2, 3, ...]`, then an id with score 0 or 1 will fall
   into bag 0, an id with score 2 will fall into bag 1, etc.

 \# Migration

 In the event that this list ever changes, a copy of the old bags list must be retained.
 With that `List::migrate` can be called, which will perform the appropriate migration.
#### Value
```python
[
    33333333,
    38184666,
    43742062,
    50108281,
    57401040,
    65755187,
    75325197,
    86288026,
    98846385,
    113232487,
    129712342,
    148590675,
    170216561,
    194989878,
    223368704,
    255877784,
    293118235,
    335778661,
    384647885,
    440629536,
    504758756,
    578221342,
    662375673,
    758777824,
    869210344,
    995715212,
    1140631598,
    1306639114,
    1496807363,
    1714652697,
    1964203240,
    2250073368,
    2577549032,
    2952685502,
    3382419332,
    3874696621,
    4438619944,
    5084616664,
    5824631742,
    6672348610,
    7643442186,
    8755868715,
    10030197794,
    11489992720,
    13162246190,
    15077879420,
    17272313899,
    19786126359,
    22665799069,
    25964579327,
    29743464044,
    34072327620,
    39031213974,
    44711816618,
    51219174136,
    58673612428,
    67212969623,
    76995144813,
    88201017720,
    101037793302,
    115742833124,
    132588044352,
    151884907519,
    173990236034,
    199312773927,
    228320753830,
    261550554952,
    299616621127,
    343222822341,
    393175469814,
    450398225296,
    515949180262,
    591040420815,
    677060440060,
    775599812382,
    888480604352,
    1017790066098,
    1165919226119,
    1335607103187,
    1529991352850,
    1752666285025,
    2007749325472,
    2299957150072,
    2634692899685,
    3018146088258,
    3457407051560,
    3960598052785,
    4537023469264,
    5197341837346,
    5953762936697,
    6820273558240,
    7812896130365,
    8949984985591,
    10252565745880,
    11744724102088,
    13454051176370,
    15412153702632,
    17655238458639,
    20224781756373,
    23168296370008,
    26540210082583,
    30402872096348,
    34827705916070,
    39896530022963,
    45703070759499,
    52354695399464,
    59974397449015,
    68703070888447,
    78702115407088,
    90156420804069,
    103277785738759,
    118308834046123,
    135527501032588,
    155252172707386,
    177847572977594,
    203731507665501,
    233382590050230,
    267349090784630,
    306259075829029,
    350832019859793,
    401892109893305,
    460383485119292,
    527387694739404,
    604143696619511,
    692070766545736,
    792794741693469,
    908178083570703,
    1040354316321961,
    1191767477182765,
    1365217308553008,
    1563911027324411,
    1791522628715580,
    2052260821186860,
    2350946848602280,
    2693103638628474,
    3085057925791037,
    3534057237519885,
    4048403906342940,
    4637608586213668,
    5312566111603995,
    6085756951128531,
    6971477980728040,
    7986106843580624,
    9148404784952770,
    10479863561632778,
    12005102840561012,
    13752325434854380,
    15753838794879048,
    18046652397130688,
    20673162077088732,
    23681933959870064,
    27128602484145260,
    31076899124450156,
    35599830833736348,
    40781029996443328,
    46716300853732512,
    53515390995440424,
    61304020674959928,
    70226207470596936,
    80446929278126800,
    92155174875271168,
    105567438465310176,
    120931722816550704,
    138532125018688464,
    158694089650123072,
    181790426491212160,
    208248204055475872,
    238556646405290848,
    273276179270092192,
    313048792736563520,
    358609912124694080,
    410801996551064960,
    470590116626953088,
    539079799334522496,
    617537470046187776,
    707413869675350912,
    810370879959114368,
    928312252892475904,
    1063418812524189696,
    1218188780021782528,
    1395483967646286592,
    1598582695797773824,
    1831240411607374592,
    2097759129958809600,
    2403066980955773440,
    2752809334727236096,
    3153453188536351744,
    3612406746388564480,
    4138156402255148032,
    4740423659834265600,
    5430344890413097984,
    6220677252688132096,
    7126034582154840064,
    8163157611837691904,
    9351223520943572992,
    10712200535224332288,
    12271254135873939456,
    14057212388066050048,
    16103098993404108800,
    18446744073709551615,
]
```
#### Python
```python
constant = substrate.get_constant('VoterList', 'BagThresholds')
```
---------
## Errors

---------
### List
A error in the list interface implementation.

---------