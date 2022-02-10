# Write a program to generate multiplication tables from 2 to 20 and write it to the different files.Place this files in a folder.

for i in range(2,21):
    with open(f"tables/multiplication_table_of_{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:
                f.write("\n")

# Don't run this code again cz multiplication table is already generated understood mah boi, delete the tables wala folder first then run the code man. :-)