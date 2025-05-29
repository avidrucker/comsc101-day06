print("This is first line.")
prompt = "Enter second: "
ans = input(prompt)
print(f"\033[A\033[{len(prompt)+len(ans)}C And the third.")