# Inflate String Numbers

Inflate String Numbers is a simple Python script that increments numbers found
inside a string.

It supports both:
- Arabic integers (e.g. `2 → 3`)
- English number words, including when they appear as substrings
  (e.g. `someone → sometwo`)


## Features

- Increments Arabic integers using regular expressions
- Increments English number words (non-composite only)
- Case-insensitive matching for English words
- Substring-level replacement for English words
- Matches longer English words first to avoid partial matches


## Supported English Number Words

### Numbers 1–19

one, two, three, four, five,  
six, seven, eight, nine, ten,  
eleven, twelve, thirteen, fourteen, fifteen,  
sixteen, seventeen, eighteen, nineteen

### Tens

twenty, thirty, forty, fifty,  
sixty, seventy, eighty, ninety

**Notes**: When an English number word increments beyond the supported word range, the result is represented as a numeric string instead of an English word (e.g. `ninety → 91`).

## Example Behavior

| Input | Output |
|------|--------|
| `I have 2 apples` | `I have 3 apples` |
| `someone has one apple` | `sometwo has two apple` |
| `seventeen17` | `eighteen18` |
| `twenty` | `21` |
| `anyone has 99 problems` | `anytwo has 100 problems` |


## Usage
### Requirements

- Python 3.7 or later

You can check your Python version with:

    python3 --version


### Command-Line Arguments

Run the script by passing the input string as command-line arguments:

    python3 inflate.py someone has 2 apples

Output:

    sometwo has 3 apples


### Standard Input

You can also provide input via standard input:

    echo "I have seventeen apples" | python3 inflate.py

Output:

    I have eighteen apples

## Limitations

- Only supports Arabic integers.
  Decimal numbers (e.g. `2.5`), floating-point values, and scientific notation
  (e.g. `1e3`) are not supported.

- Integer overflow is not explicitly handled.
  Extremely large numeric values may exceed Python's practical integer limits
  in terms of memory or performance, even though Python integers are unbounded
  in theory.

- Negative numbers are not supported.
  Inputs such as `-1` or `-five` are not recognized or processed correctly.

- Only non-composite English number words are supported.
  Composite expressions such as `twenty one`, `one hundred`,
  or hyphenated forms like `twenty-one` are not parsed as a single number.

- Original capitalization is not preserved.
  For example, `One`, `ONE`, and `one` are all transformed into `two`.

- Large-scale English number units are not supported.
  Words such as `hundred`, `thousand`, `million`, and `billion` are not recognized,
  and expressions like `one hundred` or `two thousand` are not parsed.

## Use of AI Tools

AI tools were used to discuss the high-level approach to the problem, clarify reasonable assumptions about the input, narrow the scope to an initial simpler version, and identify general edge cases and limitations. 

The discussion focused on questions such as:
- How to approach the problem at a high level before implementation
- What assumptions could be made to simplify the initial solution
- How to narrow the scope to a simpler version first
- What general edge cases to be aware of
- What inputs or scenarios might be out of scope
