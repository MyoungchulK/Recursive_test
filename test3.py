import click

@click.command()
@click.option('-i', '--inputs', default = '0,0 1,1 2,2 1,0 2,0 3,0 0,4')
def main(inputs):
    
    if len(inputs) == 0:
        print(0)
        return

    arr = [list(map(int, in_indi.split(','))) for in_indi in inputs.split(' ')]
    print(arr)

    s_i = []
    for idx1, ar1 in enumerate(arr):
        for ar2 in arr[idx1 + 1:]:
            dx = ar2[0] - ar1[0]
            dy = ar2[1] - ar1[1]
            if dx == 0: 
                slope = 'inf'
                intercept = '-inf'
            else: 
                slope = dy / dx
                intercept = ar1[1] - slope * ar1[0]
            print(ar1, ar2, slope, intercept)
            s_i.append([slope, intercept])

    s_i_s_t = list(set(map(tuple, s_i)))
    counts = [0] * len(s_i_s_t)
    print(s_i_s_t)
    for idx, p in enumerate(s_i_s_t):
        for ar in arr:
            if p[0] == 'inf' and ar[0] == 0:
                counts[idx] += 1 
                continue
            y_test = p[0] * ar[0] + p[1]
            if y_test == ar[1]:
                counts[idx] += 1        
    print(counts)
    output = max(counts)
    print(output)

if __name__ == "__main__":
    main()
