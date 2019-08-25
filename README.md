# 98CardsGame

## Rules
Player has 98 cards from 2 to 99 in deck

After shufling deck, player takes 8 cards to hand.

There are 4 piles to place cards on. 

|1 	| 1		|
|100| 100	|

Player can play cards on rising pile only if card is higher than card on pile
Player can play card on decreasing pile only if card is lower than

**Excepions** are cards that vary equal by 10

*Example*: you can always play card '63' on card '73', no matter where card '73' is currently placed


### Winning Game
Win game, by playing all cards!


#### Info
I found this game in Google Play Store for android

My version of game refils hand after each card played

(Originally player plays 2 cards and then  refils his hand)

#### Problem Complexity
Possible deck orders:
98! = **9.43e+153**

Number of unique starting Hands:
98 * 97 * .. * 91 = **6.35e+15**