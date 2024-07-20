import click

@click.command()
@click.option('-i', '--inputs', default = '5, 2, 1, 7, 9, 2')
def main(inputs):
        
    if len(inputs) == 0:
        print(0)
        return

    arr = list(map(int, inputs.split(',')))
    print(arr)

    output = 0
    print('If I can buy and sell on same day')
    for idx, ar in enumerate(arr):
        max_val = max(arr[idx:])
        diff = max_val - ar
        print(max_val, ar, diff)
        if diff > output: output = diff
    
    print('If I can not buy and sell on same day')
    for a in range(1, len(arr)):
        max_val = max(arr[a:])
        diff = max_val - arr[a - 1]
        print(max_val, arr[a - 1], diff)
        if diff > output: output = diff

    if output < 1: output = 0
    print(output)    

if __name__ == "__main__":
    main()
