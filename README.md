This is an implementation of a dice roller. This is purpose built for the Pendragon TTRPG, but it should work in other cases.
Type quit or exit to do so.

roll formats that work:
1d20 f15 Sword (for play)
1d20 t15 Sword (for leveling)
6d6 Sword Damage
6d6*2 Sword Damage
1d20

Parts in () are optional:
1d20(_*2_) (_f/t15_) (_Sword_)
Dice(_multiplier_) (_target_) (_message_)


There are SUCCESS, FAILURE, CRITICAL, CRITICAL FAILURE results.
Only t/f are allowed target functions.
If you just roll without a target number (using  t or f) it will return a ROLL result.
Messages are available for any roll.
targets above 20 are automatically changed to 1d20+x rolls and success is treated accordingly.
![image](https://github.com/vizax/dice-roller/assets/1894549/fa789ab5-2067-4438-8999-6adcea0cf5e5)

