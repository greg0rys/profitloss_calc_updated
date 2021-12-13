<h1 align="center"> Profit Loss Calculator</h1>

_*built by*_: __Greg Shenefelt__

_*version 12:13:2021*_ (most recent)

_*built using:*_ Python

---

<h3 align="center"> Usage: </h3>

+ Allows the user to run a quick estimate on the total losses for a shipment based off quick markdowns.

+ It also gives feedback on what the user should do to reduce these losses.

---

```python
# I built the interactive feel by manipulating a truthy loop

again = y;
while again:
	# run main()

	# after main() has been run -> ask if user would like to use the program again

	again = input("Would you like to go again?")

	if again == 'y':
		# make the loop iterate again
		continue
	else:
		# user entered something other than 'y' || break from the loop.
		break;
```
