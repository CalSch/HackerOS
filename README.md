# HackerOS
HackerOS is an OS for hackers (Not really)
#
I made it as a joke for my brother

# Changelog
## 0.2.3
1. Added sound
2. Gave variables names instead of index numbers.
3. Made `if` statements compare with more things.
4. Made the `math` command work with variables.
## 0.2.4
1. Removed the `!=` comparison from `if` statements.
2. `!` is the opposite of `~`.
3. If there is a `#` before the command, the first argument will be what the last command returned.
4. The first argument for `setvar` is now the value of the variable.
## 0.2.5
1. Didn't add much to `HackerOS.py`
2. Added `compiler.py` to compile `.hax` scripts into `.py`
# HaxScript Documentation
## Commands
`print`: prints a message to the user  
`pause`: waits until the user presses entry to conitue  
`askvar`: gets input and assigns it to a variable  
`printvar`: prints the value of a variable  
`math`: returns the result of a mathematical equation  
`clear`/`cls`: clears the screen  
`if`: compares 2 variables, 1 variable and a string, or 2 strings  
`cmd`: runs a command line command  
`sleep`: waits a certain amount of seconds  
`setvar`: sets a variable to a certain value  
`quit`: quits the script  
## Syntax and Examples
`print,<message>`: prints `<message>` to the screen  
`askvar,<var>`: Gets input from the user and assigns it to `<var>`  
`printvar,<var>`: prints the contents of `<var>` to the user  
`math,<num1>,<op>,<num2>`: returns `<num1> <op> <num2>`. (Ex. `math,1,/,2` returns `0.5`)  
`if,<val1>,<com>,<val2>`: compares `<val1>` and `<val2>` based on what `<op>` is.    
If the comparison is true, then `condition` is set to `True`.  
If the comparison is false, then `condition` is set to `False`.  
`cmd,<command>`: runs `<command>` in the command line  
`sleep,<sec>`: does nothing for `<sec>` seconds  
`setvar,<val>,<name>`: sets the variable named `<name>` to `<val>`  
## Extra symbols
All of theese symbols must be before the command:  
`~`: runs the command if `condition` is true  
`!`: runs the command if `condition` is false  
`#`: sets the first argument to whatever the last command returned  
`.`: does not run the command(used as a comment)  
# Using compiler(`compiler.py`)
Take your `.hax` script file and drag it into `compiler.py`, if it says `Error`, then there's a command that's not in the compiler.  
When I add a command to HaxScript, I will add it to `compiler.py`  
  
It will ask you for a file name, it will automatically add `.py` to the end.  
After it creates the compiled `.py` file, it will ask you if you want to run it, if you type an `n`, it will not run it (The capital y means it defaults to yes).  
# Other Info
## The `condition` variable
The `condition` variable is used for checking if the last if statement is true or false. You cannot directly access the variable from the HaxScript commands  
## Using one var and one string in `if` statements
You must put the variable on the first argument otherwise it will be a string.
