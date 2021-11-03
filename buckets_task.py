bucket_5 = 0
bucket_5_max = 5
bucket_3 = 0
bucket_3_max = 3
i = 1


# Shows the initial state of both buckets
print(f'bucket 5: {bucket_5}; bucket 3: {bucket_3}')


while bucket_5 != 4 or bucket_3 != 0:
    user_input = input('Enter operation: ')
    # Fills a 5-liter bucket
    if user_input == '1':
        bucket_5 = 5

    # Fills a 3-liter bucket
    elif user_input == '2':
        bucket_3 = 3

    # Empties a 5-liter bucket
    elif user_input == '3':
        bucket_5 = 0

    # Empties a 3-liter bucket
    elif user_input == '4':
        bucket_3 = 0

    # Pours water from the 5-liter bucket to a 3-liter bucket
    elif user_input == '5':
        while bucket_3 + i <= bucket_3_max and bucket_5 - i >= 0:
            bucket_5 = bucket_5 - i
            bucket_3 = bucket_3 + i

    # Pours water from the 3-liter bucket to a 5-liter bucket
    elif user_input == '6':
        while bucket_5 + i <= bucket_5_max and bucket_3 - i >= 0:
            bucket_5 = bucket_5 + i
            bucket_3 = bucket_3 - i

    # Shows the state of our buckets after the last operation
    print(f'bucket 5: {bucket_5}; bucket 3: {bucket_3}')



