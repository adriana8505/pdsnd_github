import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to enter a city, a month, and a day to analyze. Includes checks for wrong user input.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Please type in the name of the city (chicago, new york city or washington): ').lower()
        if city=='chicago' or city=='new york city' or city=='washington':
            break
        else:
            print('This is not a valid city name. Please try again\n')


   # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Please type in the month (between january and june) or all for no month filtering: ').lower()
        if month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june' or month=='all':
            break
        else:
            print('This is not a valid month. Please try again\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Please type in the day (monday, tuesday, wednesday, thursday, friday, saturday, sunday) or all for no day filtering: ').lower()
        if day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday' or day=='all':
            break
        else:
            print('This is not a valid day. Please try again\n')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('This is the most common month: {} '.format(common_month))

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('This is the most common day of the week: {} '.format(common_day))

    # TO DO: display the most common start hour
    starthour=df['Start Time'].dt.hour
    common_starthour=starthour.mode()[0]
    print('This is the most common start hour is: {} '.format(common_starthour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startstation=df['Start Station'].mode()[0]
    print('The most commonly used start station is: {} '.format(common_startstation))

    # TO DO: display most commonly used end station
    common_endstation=df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(common_endstation))

    # TO DO: display most frequent combination of start station and end station trip
    common_combination=df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start and end station trip is: {}'.format(common_combination))

    print("\nThis took only %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltravel_time=df['Trip Duration'].sum()
    print('Total travel time is: {} '.format(totaltravel_time))


    # TO DO: display mean travel time
    meantravel_time=df['Trip Duration'].mean()
    print('Mean travel time is: {} '.format(meantravel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('Count of user types:\n {} '.format(user_type))

    # TO DO: Display counts of gender
    gender=df['Gender'].value_counts()
    print('Count of gender:\n {} '.format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth=df['Birth Year'].min()
    recent_birth=df['Birth Year'].max()
    common_birth=df['Birth Year'].mode()[0]

    print ('Earliest date of birth is: {} '.format(earliest_birth))
    print ('Most recent date of birth is: {} '.format(recent_birth))
    print ('Most common year of birth is: {} '.format(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_nobirthgender(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    print('No gender and birth date data available')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('Count of user types:\n {} '.format(user_type))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data (df):
    """Displays raw data upon request from user - 5 lines of data on each request."""
    start_time = time.time()
    i=0
    while True:
        request=input('\If you want to see raw data (5 lines each time) please enter yes. If you want to skip this option or finish enter no..\n').lower()

        if request=='yes':
           print(df.iloc[i:i+5])
           i+=5

        if request=='no':
            break
        if request!='yes' and request!='no':
            print('This is not a valid answer. Try again\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city=='chicago' or city=='new york city':
            user_stats(df)
        else:
            user_stats_nobirthgender(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
