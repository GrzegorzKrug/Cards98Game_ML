# 98 Cards Game

## Rules
Player has **98 cards** from 2 to 99 in deck.

After shufling deck, player takes 8 cards to hand.

There are **4 piles** to place cards on. 

|Info		|Left 	|Right	|
|---		|---	|---	|
|Rising		|1 		| 1		|
|Descending	|100	| 100	|

Player can play only cards from hand.

Player can play cards on rising pile only if card is higher than card on pile.

Player can play card on descending pile only if card is lower than caard on pile.

*Excepions* are cards that vary by 10. 

	Example:

	You can always play card '63' on card '73', no matter on which pile card '73' is currently placed

### Refiling Hand
* **Easy version**: Refil hand each time you play card.
* **Hard version**:	Refil hand after 2 cards was played.

### Winning Game
Win game, by playing all cards!

# To do:
- [x] My gamestyle algoritm

	*Easy version* win ratio: 4%
	
	*Harder version* win ratio: 0.5%
	
- [x] supervised approach
	- [x] collecting samples from "my gamestyle"
	- [x] trying to replicate behaviour

		*Supervised learning is failure in this case, problem is too big and too complex*
	
- [ ] reinforced approach

## Problem Complexity
Possible deck orders:
	**98! = 9.43e+153**

Number of unique starting Hands:
	**98 * 97 * .. * 91 = 6.35e+15**


## About game
I found this game in Google Play Store for android. I never won but I wanted. Now I know that my game decisions are not the best. 

