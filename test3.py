import click

@click.command()
@click.option('-i', '--inputs', default = '0,0 1,1 2,2 1,0 2,0 3,0 0,4')
def main(inputs):
    
    if len(inputs) == 0:
        print(0)
        return

    arr = [list(map(int, in_indi.split(','))) for in_indi in inputs.split(' ')]
    print(arr)

    for idx1, ar1 in enumerate(arr):
        for idx2, ar2 in enumerate(arr[idx1 + 1:]):
            #print(ar1, ar2)
            #print(idx1, idx2 + idx1 + 1)
            dx = ar2[0] - ar1[0]
            dy = ar2[1] - ar1[1]
            if dx == 0: dxy = 'inf'
            else: dxy = dy / dx
            print(dxy)

if __name__ == "__main__":
    main()
