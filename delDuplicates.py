import os
from PIL import Image
import imagehash

MAIN_DIR = "D:\\Datasets\\Blaetter\\Temp\\Linde"
TEST_DIR = "D:\\Datasets\\Blaetter\\Temp\\linde blatt-green"


main_filenames = []
main_hashes = []
duplicates = []

# Record hashes for original files and store them.
for file in os.listdir(MAIN_DIR):
    main_filenames.append(file)
    main_hashes.append(str(imagehash.dhash(Image.open(f"{MAIN_DIR}/{file}"))))

# find out for every file(in TEST_DIR) if file hash exists in orig hashes.
for f in os.listdir(TEST_DIR):
    if str(imagehash.dhash(Image.open(f"{TEST_DIR}/{f}"))) in main_hashes:
        for h in main_hashes:
            if h == str(imagehash.dhash(Image.open(f"{TEST_DIR}/{f}"))):
                duplicates.append([main_filenames[main_hashes.index(h)],f])

# print duplicates.
print(f"\n{len(duplicates)} DUPLICATES FOUND!")
if len(duplicates) > 0:
    print("--Original--|--Duplicate--")
    for i in range(len(duplicates)):
        print(f"{duplicates[i][0]} | {duplicates[i][1]}")

    # ask if user wants to delete duplicate files and do so if desired.
    del_in = input("\nDo you want to delete the duplicates out of the test directory?\n(y/n)")
    if del_in == "y" or "Y":
        num_deleted = 0
        for d in range(len(duplicates)):
            try:
                os.remove(f"{TEST_DIR}/{duplicates[d][1]}")
            except:
                pass
            num_deleted += 1
        print(f"{num_deleted} files removed.")

delay = input("Press Enter to exit.")
