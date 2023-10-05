# Python Type Annotation

## Type Annotations for Variables:

> > You can declare the type of a variable using a colon : after the variable name.
* For example, 

``` age: int = 1 means the variable age is of type int and has an initial value of 1.```
``` You can also declare a variable without initializing it, like a: int, and assign a value later.```

* If you try to assign a value of a different type to a variable, you'll get a type error.

## Common Data Types:

* You can annotate variables with common data types like int, float, bool, str, and bytes.

> > For lists and sets, you specify the type of elements inside square brackets, like list[int] or set[int].

> > For dictionaries, you specify the types of keys and values, like dict[str, float].
> > Tuples can have fixed sizes with specified element types, like tuple[int, str, float], or variable sizes with tuple[int, ...].