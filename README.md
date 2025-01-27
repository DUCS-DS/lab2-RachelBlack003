[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17817044)
# Sp25Lab2
Lab 2 for Spring 25 Data Structures

### Runtime complexity

Referring to the algorithm you implemented in the function **monotonic** in the
file **edit_me.py** and assuming that the input list has length **N**,

* the big-O worst-case complexity is the list is larger than two, decending, but the last number is acending OR it is decending all the way through, and
* the big-O best-case complexity is if the list size is two or smaller.

Referring to the code block below,
* the big-O worst-case complexity of the function **search** is if key smaller than the smallest number on the list.
  ```python
  def search(lst, key):

      assert monotonic(lst), "The list is not sorted"

      low = 0
      mid = len(lst) // 2
      high = len(lst) - 1

      while (high >= low):
          mid = (high + low) // 2
          if (lst[mid] < key):
              low = mid + 1
          elif (lst[mid] > key):
              high = mid - 1
          else:
              return mid

      return -1
  ```

Notes:
* Recall that, in Python, an **assert** statement has this form:
  ```python
  assert Boolean_expression, string
  ```
* Upon execution of an **assert** statement, **Boolean_expression** is evaluated; if it
  evaluates to **False**, execution is halted and error-message **string** is displayed.
  If **Boolean_expression** evaluates to **True**, then execution of the program continues.

#### Critique

I would not use the function **search** in real life because it only works with an acending list, otherwise lst[mid] gets further away from the desired value.
