# DebuggingCourse

Udacity - Software Debugging

## First Course

Write a simple program of html parser.

Start by case "<a>hello</a>", expect "hello" text.

Idea : 

Using the state of string.

When string is ">", state is the `TagState`.

When string is "<", state is the `NormalState`.

TagState append the text to a string.

NormalState ignore the action.

### First Problem

When you meet the two ">" string.

ex. 

string is "<a href=">">hello</a>", expect string is `hello`, but get the string is `'hello`.
