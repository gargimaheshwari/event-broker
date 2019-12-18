# Notes

Language: Python (3.6)

Premise

There are two ways to do this:

1. Real time detection - A program that runs in the background at all times and checks the files at certain time intervals.
2. A program that can be run at any point to check for changes until that time.

The first solution can be easily derived from the second by adding polling. The solution here is therefore of the second type. This is also less resource-intensive.

Additionally, to compare a file to its older version, we need to save the older state separately, so that it is not affected by changes. This can be done by adding a string to a file for every file in the given list. Here, since the solution has to be restricted to the standard library, I will simply assume that the files are not too large, and store their content copies.


## Usage

Clone this repo
```
git clone https://github.com/gargimaheshwari/enlyze-application
```

To prepare the system for use of this program, add the list of files that need watching as `list_of_files.txt` to the repo folder run the `first_run.py` file.
```
python first_run.py
```
Thereafter, every time the files need to be checked, run the `program.py` file.
```
python program.py
```

# Generic Challenge

Within the following assignment, we'll be touching on the basic components of software engineering and design. 
In order to set the grounds for this, let's define some corner stones first:

* You can use any programming language for this - ok maybe Fortran isn't the way to go, but you get the concept
* The result should be made accessible via github, gitlab or similar
* You can either work on this as a private project, or share your repository with the world
* Only use the standard library of your programming language of choice

## Description
Every now and then, every programmer comes up with some implementation addressing an issue / problem, of which she is very proud of. 
We've long thought about how to structure this assignment and we believe that understanding your approach towards the same challenge 
we faced a couple of months ago, will give us the opportunity to understand how you develop software. 
Our implementation of this is in production as of today, so we're really excited to see what you come up with!

On a generic level, we'll be building is a small event broker, which can handle any type of event source and consumer. 
We can have one or multiple consumers for the same event source, but as soon as the last consumer is removed, 
the event source is removed, too. For both, event sources and consumers, it may be that they require some setup or cleanup.

To make this more concrete, let's consider the following problem: You are administrating a file server, 
where other people from your organization regularly edit files and you are responsible for reviewing those file changes. 
As it takes you at least 2 hours a day of productive work time to check for file changes manually, 
you decide that it's about time to change something. You think that a minimal requirement for a productivity enhancement 
would be a small program, which detects changes in a given list of files and logs a message to the console. 
This message should comprise the filename, the date of change and the diff, making it quick and easy for you to spot any red flags.
