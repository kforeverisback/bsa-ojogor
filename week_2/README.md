# Week 2

## Goal of this week

- Learn essential data structures: List, Set, Tuples and Dictionary
  - Capture specific data from the middle, data based on condition (predicate), sort and remove duplicate etc
- Learn Python Functions
  - Call functions
  - Write functions
- Finish a quick project employing above knowledge

## Project Description

We like eating in good and exotic restaurants.
Since most of us don't have cars, we want to eat in closer restaurants. We also care about restaurant's cleanliness and other customer service aspects.

Fortunately for us, the City of Austin maintains a [restaurant dataset][Learn X in Y Minutes - Python] where they keep the restaurants address, zip code and overall inspection score.
And we can directly (and freely!) download the datbase in CSV format.

So our task is to select 10 restaunrants closest to our ZipCode and print their name, address zip code and inspection score.
Also inspection score has to be greater than 90.

> Erroneously assume numerically closer zip code means shorter distance (which is not true, see [US Zip Code Map][US Zip Code Map]).
> For example 78666 and 78662 might be numerically closer but they are not!
>
> Prioritize proximity than score

## Tools of the trade

- Visual Studio Code
- Python (conda is optional)
- Visidata packge (optional)
  - We can sort and visualize easily with this pkg

----

## References

[Learn X in Y Minutes - Python][Learn X in Y Minutes - Python]

[Automate the Boring Stuff with Python][Automate the Boring Stuff with Python]

[Python Cheatsheet][Python Cheatsheet]

[Non-Programmer's Guide to Python 3][Non-Programmer's Guide to Python 3]

[Reference Austin's Restaurant Dataset][Reference Austin's Restaurant Dataset]

[US Zip Code Map][US Zip Code Map]

----

[Learn X in Y Minutes - Python]: https://learnxinyminutes.com/docs/python/

[Automate the Boring Stuff with Python]: https://automatetheboringstuff.com/

[Python Cheatsheet]: https://www.pythoncheatsheet.org/

[Non-Programmer's Guide to Python 3]: https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3

[Reference Austin's Restaurant Dataset]: https://data.world/adamhelsinger/austin-restaurant-inspections

[US Zip Code Map]: https://www.unitedstateszipcodes.org/
