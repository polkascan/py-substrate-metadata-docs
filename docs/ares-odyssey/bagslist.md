
# BagsList

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
| lighter | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'BagsList', 'put_in_front_of', {'lighter': 'AccountId'}
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
| dislocated | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'BagsList', 'rebag', {'dislocated': 'AccountId'}
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
    'BagsList', 'CounterForListNodes', []
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
    'BagsList', 'ListBags', ['u64']
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
    'BagsList', 'ListNodes', ['AccountId']
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
    100000000000000,
    106282535907434,
    112959774389150,
    120056512776105,
    127599106300477,
    135615565971369,
    144135662599590,
    153191037357827,
    162815319286803,
    173044250183800,
    183915817337347,
    195470394601017,
    207750892330229,
    220802916738890,
    234674939267673,
    249418476592914,
    265088281944639,
    281742548444211,
    299443125216738,
    318255747080822,
    338250278668647,
    359500973883001,
    382086751654776,
    406091489025036,
    431604332640068,
    458720029816222,
    487539280404019,
    518169110758247,
    550723271202866,
    585322658466782,
    622095764659305,
    661179154452653,
    702717972243610,
    746866481177808,
    793788636038393,
    843658692126636,
    896661852395681,
    952994955240703,
    1012867205499736,
    1076500951379881,
    1144132510194192,
    1216013045975769,
    1292409502228280,
    1373605593276862,
    1459902857901004,
    1551621779162291,
    1649102974585730,
    1752708461114642,
    1862822999536805,
    1979855523374646,
    2104240657545975,
    2236440332435128,
    2376945499368703,
    2526277953866680,
    2684992273439945,
    2853677877130641,
    3032961214443876,
    3223508091799862,
    3426026145146232,
    3641267467913124,
    3870031404070482,
    4113167516660186,
    4371578742827277,
    4646224747067156,
    4938125485141739,
    5248364991899922,
    5578095407069235,
    5928541253969291,
    6301003987036955,
    6696866825051405,
    7117599888008300,
    7564765656719910,
    8040024775416580,
    8545142218898723,
    9081993847142344,
    9652573371700016,
    10258999759768490,
    10903525103419522,
    11588542983217942,
    12316597357287042,
    13090392008832678,
    13912800587211472,
    14786877279832732,
    15715868154526436,
    16703223214499558,
    17752609210649358,
    18867923258814856,
    20053307312537008,
    21313163545075252,
    22652170697804756,
    24075301455707600,
    25587840914485432,
    27195406207875088,
    28903967368057400,
    30719869496628636,
    32649856328471220,
    34701095276033064,
    36881204047022752,
    39198278934370992,
    41660924883519016,
    44278287448695240,
    47060086756856400,
    50016653605425536,
    53158967827883320,
    56498699069691424,
    60048250125977912,
    63820803001928304,
    67830367866937216,
    72091835084322176,
    76621030509822880,
    81434774264248528,
    86550943198537824,
    91988537283208848,
    97767750168749840,
    103910044178992000,
    110438230015967792,
    117376551472255616,
    124750775465407920,
    132588287728824640,
    140918194514440064,
    149771430684917568,
    159180874596775264,
    169181470201085280,
    179810356815193344,
    191107007047393216,
    203113373386768288,
    215874044002592672,
    229436408331885600,
    243850833070063392,
    259170849218267264,
    275453350882006752,
    292758806559399232,
    311151483703668992,
    330699687393865920,
    351476014000157824,
    373557620785735808,
    397026512446556096,
    421969845653044224,
    448480252724740928,
    476656185639923904,
    506602281657757760,
    538429751910786752,
    572256794410890176,
    608209033002485632,
    646419983893124352,
    687031551494039552,
    730194555412054016,
    776069290549944960,
    824826122395314176,
    876646119708695936,
    931721726960522368,
    990257479014182144,
    1052470760709299712,
    1118592614166106112,
    1188868596808997376,
    1263559693295730432,
    1342943284738898688,
    1427314178819094784,
    1516985704615302400,
    1612290876218400768,
    1713583629449105408,
    1821240136273157632,
    1935660201795120128,
    2057268749018809600,
    2186517396888336384,
    2323886137470138880,
    2469885118504583168,
    2625056537947004416,
    2789976657533970944,
    2965257942852572160,
    3151551337860326400,
    3349548682302620672,
    3559985281005267968,
    3783642634583792128,
    4021351341710503936,
    4273994183717548544,
    4542509402991247872,
    4827894187332742144,
    5131208373224844288,
    5453578381757959168,
    5796201401831965696,
    6160349836169256960,
    6547376026650146816,
    6958717276519173120,
    7395901188113309696,
    7860551335934872576,
    8354393296137270272,
    8879261054815360000,
    9437103818898946048,
    10029993254943105024,
    10660131182698121216,
    11329857752030707712,
    12041660133563240448,
    12798181755305525248,
    13602232119581272064,
    14456797236706498560,
    15365050714167523328,
    16330365542480556032,
    17356326621502140416,
    18446744073709551615,
]
```
#### Python
```python
constant = substrate.get_constant('BagsList', 'BagThresholds')
```
---------
## Errors

---------
### List
A error in the list interface implementation.

---------