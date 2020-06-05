import time
import pandas as pd
import numpy as np

months = ['january', 'february', 'march', 'april', 'may', 'june' , "all"]

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
    while True:
        city = input("Would you like to see data for Chicago, New York city, or Washington?\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("you have enter invalid input, please try again")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? January, February, March , April, May, or June? or All \n")
        if month.lower() in months:
            break
        else:
            print("you have enter invalid input, please try again")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        
        day = input("Which day? Please type your response as an integer (e.g .. 1=Sunday) or All \n")
        try:
            if day == "all" or  (int(day) <= 7 and int(day) >=1)  :
                break
            else:
                print("you have enter invalid input, please try again")
        except:
            print("you have enter invalid input, please try again")

    print('-'*40)

    try:
        day = int(day)
    except:
        day = str(day)
        
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month , hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' , 'Saturday']
        day = days[day - 1 ]
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print("The most common month: {}".format(month))

    # TO DO: display the most common day of week
    week = df['day_of_week'].mode()[0]
    print("The  most common day of week: {}".format(week))

    # TO DO: display the most common start hour
    hour = df['hour'].mode()[0]
    print("The  most common start hour: {}".format(hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The  most commonly used start station: {}".format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The  most commonly used end station: {}".format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df['Start Station'] + " " +  df['End Station']

    print("The  most frequent combination of start station and end station trip: {}".format(start_end_station.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tota_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {}".format(tota_travel_time))
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("Average travel time: {}".format(average_travel_time ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # TO DO: Display counts of user types
    gender = df['User Type'].value_counts()
    print("counts of user types: {}".format(gender))

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print("counts of gender: {}".format(gender))



    # TO DO: Display earliest, most recent, and most common year of birth
    
    birth = df['Birth Year'].value_counts().head(1)
    

    print("most recent, and most common year of birth: {}".format(birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def read_by_chunk():
   

    while True:
        read_chunk = input('\nWould you like to view individual trip data?Type "yes" or "no".\n')
        
        if read_chunk.lower() == "yes":
            while True:
                city = input("Would you like to see data for Chicago, New York city, or Washington?\n").lower()
                if city in CITY_DATA:
                    break
                else:
                    print("you have enter invalid input, please try again") 
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
                print(chunk)
                want_more = input('\nWould you like to to see more?Type "yes" or "no".\n')
                if want_more.lower() != "yes":
                    break
        else:
            break
                

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        read_by_chunk()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
