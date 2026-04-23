import time
num = int(input(f"\n\033[3;32mDigite um número: \033[0m\n"))
def timer(txt):
    print(txt, end=" ", flush=True)
    time.sleep(2)
    print("  "*len(txt), end="\r", flush=True)
timer(f"\033[1mCarregando...\033[0m")
print(f"\033[1;32mTabuada do {num}:\033[0m\n")
for i in range(10):
    print(f"[{num} x {i+1} = {num * (i+1)}]") 
    time.sleep(0.05)
## kabvvfhfvjksf