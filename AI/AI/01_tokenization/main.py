import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There, This is Piyush"
tokens = enc.encode(text)

#  [25216, 3274, 11, 1328, 382, 398, 3403, 1776]

print("Tokens: ", tokens)

decoded = enc.decode([25216, 3274, 11, 1328, 382, 398, 3403, 1776])
print(decoded)