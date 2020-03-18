A tool to generate a list of AWS Comprehend compatible annotations. 

The outputed file can be used to train a custom entity recognizer using the "Annotations" option, as documented on this page: https://docs.aws.amazon.com/comprehend/latest/dg/cer-annotation.html

### Pre-requisites:
- Python 3

### Usage:

**Params:**

1. A list of entities to annotate
2. A document to generate annotations from
3. Entity type

`python generate_annotations.py <PATH_TO_ENTITY_LIST> <PATH_TO_TRAINING_FILE> <ENTITY_TYPE>`

`python generate_annotations.py TECH.csv CV.txt TECH`

**Usage notes:**
- The .csv files should be UTF-8 encoded.
- The entity type should match the one specified when creating a custom recognizer on AWS.

### Output:
- A .csv file in the following format: File, Line, Begin Offset, End Offset, Type
- For example: 

```
File, Line, Begin Offset, End Offset, Type
documents.txt, 0, 0, 11, ENGINEER
documents.txt, 1, 0, 5, ENGINEER
documents.txt, 3, 25, 30, ENGINEER
```
