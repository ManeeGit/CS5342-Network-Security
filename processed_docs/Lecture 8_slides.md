# Lecture 8_slides


## Page 1

Properties of Random Numbers
• Randomness
• Uniformity
• distribution of bits in the sequence should be uniform 
• Independence
• no one subsequence in the sequence can be inferred from the others 
• Unpredictable
• satisfies the "next-bit test“
• given consecutive sequence of bits output (but not seed), next bit must be hard to 
predict


## Page 2

Entropy
• A measure of uncertainty
• In other words, a measure of how unpredictable the outcomes are
• High entropy = unpredictable outcomes = desirable in cryptography
• The uniform distribution has the highest entropy (every outcome equally 
likely, e.g. fair coin toss)
• Usually measured in bits (so 3 bits of entropy = uniform, random distribution 
over 8 values)
Entropy of an information source


## Page 4

True random numbers generators
• Several sources of randomness – natural sources of randomness
• decay times of radioactive materials
• electrical noise from a resistor or semiconductor
• radio channel or audible noise
• keyboard timings
• disk electrical activity
• mouse movements
• Physical unclonable function (PUF)
• Some are better than others

