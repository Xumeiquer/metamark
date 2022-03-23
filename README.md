# metamark

MetaMark is a pre-processor for Markdown documents. It allows to execute Python code inside Markdown documents and replace the code snippet by its own output.

## Usage

```shell
python3 metamark.py input.md > output.md
```

Markdown input example document.

```markdown
# Header

## List

{{eval
for i in range(6):
    print("* Line: " + str(i))
}}
```

Output document ready to use on any markdown processor.

```markdown
# Header

## List

- Line: 0
- Line: 1
- Line: 2
- Line: 3
- Line: 4
- Line: 5
```
