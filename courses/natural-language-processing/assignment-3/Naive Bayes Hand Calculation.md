# Naive Bayes Sentiment Classification (Hand Calculation)

Worked example transcribed from handwritten notes: a multinomial Naive Bayes classifier with Laplace (add-one) smoothing, trained on 9 short movie reviews and tested on 4 sentences.

## Training cases

Each review is followed by the key words kept from it.

**Positive (+)**

1. "The best movie I have ever seen so far in 2022" → best, ever, seen, far
2. "This may be the best batman movie ever" → best, ever
3. "They are pretty good" → pretty, good
4. "The prop and tech design is so good and fun" → prop, tech, design, good, fun
5. "Really enjoyed this movie" → really, enjoyed

**Negative (−)**

6. "It is boring and it is a bad super hero movie" → boring, bad, super, hero
7. "May be the least entertaining batman movie" → least, entertaining
8. "The batman proves to be bad and violent movie" → proves, bad, violent
9. "So boring and bleak and cynical" → boring, bleak, cynical

## Counts

|              | Positive (+) | Negative (−) |
| ------------ | ------------ | ------------ |
| Total tokens | 15           | 12           |
| Unique words | 12           | 10           |

- **Vocabulary (+):** best, ever, seen, far, pretty, good, prop, tech, design, fun, really, enjoyed
- **Vocabulary (−):** boring, bad, super, hero, least, entertaining, proves, violent, bleak, cynical
- **Total unique words (+ and −):** 12 + 10 = 22

## Priors

- P(+) = 5/9
- P(−) = 4/9

## Likelihood with Laplace smoothing

- For a word in the positive class: P(word | positive) = (count(word) + 1) / 37, since 15 + 22 = 37
- For a word in the negative class: P(word | negative) = (count(word) + 1) / 34, since 12 + 22 = 34

## Test cases

### 1. "Boring & violent" → boring, violent

|                      | Positive (+)          | Negative (−)          |
| -------------------- | --------------------- | --------------------- |
| P(boring \| class)   | (0+1)/37 = 1/37       | (2+1)/34 = 3/34       |
| P(violent \| class)  | (0+1)/37 = 1/37       | (1+1)/34 = 1/17       |
| P(sentence \| class) | 1/37 · 1/37 = 0.0007  | 3/34 · 1/17 = 0.0052  |
| P(class \| sentence) | 0.0007 · 5/9 = 0.0004 | 0.0052 · 4/9 = 0.0023 |

**Result: NEGATIVE**

### 2. "Enjoyed just watched the movie" → enjoyed, just, watched

|                      | Positive (+)             | Negative (−)              |
| -------------------- | ------------------------ | ------------------------- |
| P(enjoyed \| class)  | (1+1)/37 = 2/37          | 1/34                      |
| P(just \| class)     | 1/37                     | 1/34                      |
| P(watched \| class)  | 1/37                     | 1/34                      |
| P(sentence \| class) | 0.00004                  | 0.000025                  |
| P(class \| sentence) | 0.00004 · 5/9 = 0.000022 | 0.000025 · 4/9 = 0.000011 |

**Result: POSITIVE**

### 3. "The first half is good but I hate the ending" → good, hate

|                      | Positive (+)    | Negative (−) |
| -------------------- | --------------- | ------------ |
| P(hate \| class)     | 1/37            | 1/34         |
| P(good \| class)     | (2+1)/37 = 3/37 | 1/34         |
| P(sentence \| class) | 0.0022          | 0.0008       |
| P(class \| sentence) | 0.0012          | 0.00035      |

**Result: POSITIVE**

### 4. "Pretty good and fun movie" → pretty, good, fun

|                      | Positive (+) | Negative (−) |
| -------------------- | ------------ | ------------ |
| P(pretty \| class)   | 2/37         | 1/34         |
| P(good \| class)     | 3/37         | 1/34         |
| P(fun \| class)      | 2/37         | 1/34         |
| P(sentence \| class) | 0.00028      | 0.00002      |
| P(class \| sentence) | 0.00012      | 0.000009     |

**Result: POSITIVE**

## Answers

1. NEGATIVE
2. POSITIVE
3. POSITIVE
4. POSITIVE

> **Transcription note:** this was read from handwriting, so a few small decimals may be misread, especially in test case 4. Recomputing test 4 gives P(sentence | +) = 12/37³ ≈ 0.00024 and P(sentence | −) = 1/34³ ≈ 0.000025. The predicted class is the same either way.
