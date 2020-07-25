#--------------------------------------------------------------------------------------------------------
# PROJECT for Programming for Data Science with Python
# July 2020 - K. Digonis

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities_filter = ['chicago','new york city', 'washington', 'all']
    while True:
        try:
            city = input('Please share a US city you are interested in:\n')
            if city.lower() not in cities_filter:
                print('There is no data for this city ...yet.\n\nPlease enter a valid city name among:\n "Chicago", "New York City", "Washington",\n or "all" if no filter is required\n')
            else:
                print('Registering city input: {}\n'.format(city))
                break
        except Exception as e:
            print('Exception occurred: {}'.format(e))

    months_filter = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Are you interested in a specific month [type: one month from January until June]\n or shall we include all available data in the analysis [type: all]?\n')
            if month.lower() not in months_filter:
                print('Please provide a valid month name or type "all" if no month filter is required\n')
            else:
                print('Registering month input: {}\n'.format(month))
                break
        except Exception as e:
            print('Exception occurred: {}'.format(e))

    days_filter = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Are you interested in a specific day [type: day name] or shall we include weeklong data in the analysis [type: all]?\n')
            if day.lower() not in days_filter:
                print('Please provide a valid day name or type "all" if no day filter is required\n')
            else:
                print('Registering day input: {}\n'.format(day))
                break
        except Exception as e:
            print('Exception occurred: {}'.format(e))
    print('-'*40)
    print('Your query: \n City: {}\n Month: {}\n Day: {}'.format(city.upper(),month.upper(),day.upper()))
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    #print(df.head())

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #print(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #print(df['month'], df['day_of_week'])

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        #print(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        # day is capitalized with .title() to match the title case used in the day_of_week column
        #print(day)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:  {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is:  {}'.format(most_common_day))

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour of day from Start Time to create new column
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is:  {}'.format(most_common_hour))

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_startstation = df['Start Station'].mode()[0]
    print('The most commonly used Start Station is:  {}\n'.format(mc_startstation))

    # TO DO: display most commonly used end station
    mc_endstation = df['End Station'].mode()[0]
    print('The most commonly used End Station is:  {}\n'.format(mc_endstation))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + '\n to station:   ' + df['End Station']
    mc_trip = df['Trip'].mode()[0]
    print('The most frequent trip is \n from station: {} \n'.format(mc_trip))

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_t = df['Trip Duration'].sum()
    print('Total travel time:  {} seconds \n which is {} minutes or {} hours\n'.format(round(total_travel_t,2), round(total_travel_t/60,1), round(total_travel_t/(60*60),1)))

    # TO DO: display mean travel time
    mean_travel_t = df['Trip Duration'].mean()
    print('Mean travel time:  {} seconds \n which is {} minutes\n'.format(round(mean_travel_t,2),round(mean_travel_t/60,1)))

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type    Count of Users')
    print(user_types)
    print('\n')
    # TO DO: Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print('Gender    Count of Users')
    else:
        genders = 'There is no Gender data available.\n'
    print(genders)
    print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        oldest = df['Birth Year'].min()
        print('\nEarliest year of birth: {}\n'.format(int(oldest)))
        youngest = df['Birth Year'].max()
        print('Most recent year of birth: {}\n'.format(int(youngest)))
        common_yob = df['Birth Year'].mode()[0]
        print('Most common year of birth: {}\n'.format(int(common_yob)))
    else:
        print('There is no Birth Year data available.\n')

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)

def displaydata(df):
    """Prompts the user if he/she wants to see raw data - 5 rows each time."""
    df = df.drop(['Trip'], axis=1)
    while True:
        try:
            permission = input('\nWould you like to see some (more) of the data? [type: "yes" or "no"]\n')
            while permission.lower() in ['yes','y','ye']:
                print(df.sample(n=5))
                break
            else:
                print('-'*40)
                break
        except Exception as e:
            print("Exception occurred: {}".format(e))



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        displaydata(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
