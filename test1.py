import click

@click.command()
@click.option('-i1', '--inputs1', default = '1, 2, 2, 3, 4, 4')
@click.option('-i2', '--inputs2', default = '3, 4, 5, 5, 6, 4')
def main(inputs1, inputs2):
    arr1 = list(map(int, inputs1.split(',')))
    arr2 = list(map(int, inputs2.split(',')))
    print(arr1)
    print(arr2)

    common = list(set(arr1).intersection(set(arr2)))
    print(common) 

if __name__ == "__main__":
    main()
