import glob
import os

def main():
    scripts = glob.glob("cards98/*.py")
    while True:
        print('\nSelect script to run:')
        for i, s in enumerate(scripts):
            print('- {}: {}'.format(i, s))
        num = int(input('Selection:'))
        if num >= 0 and num < len(scripts):
            os.system(scripts[num])
            break
        else:
            print('Incorrect selection!')
    

    input('End of execution! Bye...')
    
if __name__ == "__main__":
    main()
    
