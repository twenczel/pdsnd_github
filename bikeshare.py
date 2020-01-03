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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter Chicago, New York City, or Washington for the city data you want to see.\n").lower()
      
    while(True):
        if(city == 'chicago' or city == 'new york city' or city == 'washington'):
            break
        else:
            city = input('City name is incorrect, please enter again carefully: \n').lower()
                    

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nPlease provide a month name or just type \'all\' to apply no month filter. \n(all, January, February, March, April, May, June) \n> ').lower()

    while(True):
        if(month == 'January' or month == 'january' or month == 'February' or month == 'february' or month == 'March' or month == 'march' or month == 'April' or month == 'april' or month == 'May' or month == 'may' or month == 'June' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Month is incorrect, please enter again carefully: \n').lower()    
    
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nPlease provide the day of week or just type \'all\' to apply no day filter. \n(all, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) \n>').lower()

    while(True):
        
        if(day == 'Monday' or day == 'monday' or day == 'Tuesday' or day =='tuesday' or day == 'Wednesday' or day == 'wednesday' or day == 'Thursday' or day == 'thursday' or day == 'Friday' or day == 'friday' or day == 'Saturday' or day == 'saturday' or day == 'Sunday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Day is incorrect, please enter again carefully: \n').lower()
       
    
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1       

        df = df[df['Start Time'].dt.month == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Start Time'].dt.weekday_name == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('\nThe most common month:  ' + str(most_common_month))
    
    
    # TO DO: display the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('The most common day:  ' + str(most_common_day))

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour:  ' + str(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('\nThe most common start station:  ', Start_Station)
    
    
    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe most common end station:  ', End_Station)    


    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('\nThe most popular trip from start to end:  ', combination_station)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time1 = total_travel_time
    day = time1 // (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour = time1 // 3600
    time1 %= 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1
    print('\nThe total travel duration is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))
    
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    time2 = mean_travel_time
    day2 = time2 // (24 * 3600)
    time2 = time2 % (24 * 3600)
    hour2 = time2 // 3600
    time2 %= 3600
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print('\nThe average trip duration is {} hours {} minutes {} seconds'.format(hour2, minutes2, seconds2))    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    num_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    num_of_customers = df['User Type'].str.count('Customer').sum()
    print('\nThe number of subscribers:  {}\n'.format(int(num_of_subscribers)))
    print('The number of customers:  {}\n'.format(int(num_of_customers)))
       
   
    # TO DO: Display counts of gender
    if('Gender' in df):
        m_count = df['Gender'].str.count('Male').sum()
        f_count = df['Gender'].str.count('Female').sum()
        print('The number of males:  {}\n'.format(int(m_count)))
        print('The number of females:  {}\n'.format(int(f_count)))
    
            
    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        print('\n The earliest birth year:  {}\n The most recent birth year:  {}\n The most common birth year:  {}\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))  

          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: Prompt the user if they want to see 5 lines of raw data, display the data if the answer is 'yes', and continue these prompts and displays until the user says 'no'. 
def display_data(df):
    
    start_loc = 0
    end_loc = 5

    display_active = input('\nWould you like to view the raw data?  Enter \'yes\' or \'no\':\n').lower()
    while display_active.lower() not in ['yes', 'no']:
        print('Invalid response.')
        display_active = input('Please enter \'yes\' or \'no\' if you would like to view the raw data.\n').lower()
    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5
       
            end_display = input('\nDo you wish to continue? Hit the \'Enter\' key to continue or type \'no\' to stop.\n').lower()
            if end_display == 'no':
                break

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart?  Enter \'yes\' or \'no\'.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
